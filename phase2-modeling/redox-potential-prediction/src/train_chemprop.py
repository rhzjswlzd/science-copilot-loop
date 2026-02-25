"""
Chemprop D-MPNN Training Script
Compare D-MPNN vs XGBoost + Morgan FP on OMEAD data
"""
import sys
import os
import json
import time
import numpy as np
import pandas as pd
from pathlib import Path

from rdkit import Chem
from rdkit import RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

# Chemprop v2 imports
from chemprop import data as chemprop_data
from chemprop import models, nn
from chemprop.data import MoleculeDatapoint, MoleculeDataset, build_dataloader
from lightning import pytorch as pl
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("=" * 60)
print("Chemprop D-MPNN vs XGBoost Comparison")
print("=" * 60)

# ---- 1. Load Data ----
DATA_PATH = Path("data/OMEAD_26218.csv")
df = pd.read_csv(DATA_PATH)
TARGET = "reduction_solv"

# Clean
df = df.dropna(subset=["smiles", TARGET])

# Parse SMILES to Mol objects and filter invalid
print("Parsing SMILES...")
mols = []
targets = []
for _, row in df.iterrows():
    mol = Chem.MolFromSmiles(row["smiles"])
    if mol is not None:
        mols.append(mol)
        targets.append(row[TARGET])

print(f"Valid molecules: {len(mols)} / {len(df)}")

# ---- 2. Split (same random_state=42 as XGBoost for fair comparison) ----
from sklearn.model_selection import train_test_split
indices = list(range(len(mols)))
train_idx, test_idx = train_test_split(indices, test_size=0.2, random_state=42)
print(f"Train: {len(train_idx)}, Test: {len(test_idx)}")

# ---- 3. Build Chemprop datasets ----
train_datapoints = [
    MoleculeDatapoint(mols[i], y=np.array([targets[i]]))
    for i in train_idx
]
test_datapoints = [
    MoleculeDatapoint(mols[i], y=np.array([targets[i]]))
    for i in test_idx
]

train_dataset = MoleculeDataset(train_datapoints)
test_dataset = MoleculeDataset(test_datapoints)

train_loader = build_dataloader(train_dataset, batch_size=64, shuffle=True, num_workers=0)
test_loader = build_dataloader(test_dataset, batch_size=64, shuffle=False, num_workers=0)

# ---- 4. Build D-MPNN model ----
mp = nn.BondMessagePassing()          # D-MPNN message passing
agg = nn.MeanAggregation()             # mean aggregation
ffn = nn.RegressionFFN()               # FFN head for regression

model = models.MPNN(
    message_passing=mp,
    agg=agg,
    predictor=ffn,
    batch_norm=True,
)

print(f"\nModel parameters: {sum(p.numel() for p in model.parameters()):,}")

# ---- 5. Train ----
print("\n=== Training D-MPNN ===")
start_time = time.time()

trainer = pl.Trainer(
    max_epochs=30,
    accelerator="gpu" if __import__("torch").cuda.is_available() else "cpu",
    devices=1,
    enable_progress_bar=True,
    logger=False,
    enable_checkpointing=False,
)

trainer.fit(model, train_loader)
train_time = time.time() - start_time
print(f"\nTraining time: {train_time:.1f}s")

# ---- 6. Evaluate ----
print("\n=== Evaluation ===")
preds = trainer.predict(model, test_loader)
y_pred = np.concatenate([p.squeeze().numpy() for p in preds])
y_test = np.array([dp.y[0] for dp in test_datapoints])

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"D-MPNN  MAE:  {mae:.4f} V")
print(f"D-MPNN  RMSE: {rmse:.4f} V")
print(f"D-MPNN  R2:   {r2:.4f}")

# ---- 7. Compare with XGBoost ----
xgb_metrics_path = Path("models/metrics.json")
if xgb_metrics_path.exists():
    xgb_metrics = json.load(open(xgb_metrics_path))
    print(f"\n{'='*60}")
    print(f"{'Metric':<12} {'XGBoost+MorganFP':>18} {'Chemprop D-MPNN':>18}")
    print(f"{'-'*12} {'-'*18} {'-'*18}")
    print(f"{'MAE (V)':<12} {xgb_metrics['test_mae']:>18.4f} {mae:>18.4f}")
    print(f"{'RMSE (V)':<12} {xgb_metrics['test_rmse']:>18.4f} {rmse:>18.4f}")
    print(f"{'R2':<12} {xgb_metrics['test_r2']:>18.4f} {r2:>18.4f}")
    print(f"{'='*60}")

    # Save comparison
    comparison = {
        "xgboost": xgb_metrics,
        "chemprop": {
            "test_mae": mae,
            "test_rmse": rmse,
            "test_r2": r2,
            "train_time_seconds": train_time,
            "epochs": 30,
            "model_params": sum(p.numel() for p in model.parameters()),
        }
    }
    with open("models/comparison.json", "w") as f:
        json.dump(comparison, f, indent=2)
    print("\nComparison saved to models/comparison.json")

print("\nDone!")
