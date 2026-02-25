"""
Train Chemprop D-MPNN 5 times independently, predict target molecules,
report mean ± std for each molecule + test set MAE comparison.
"""
import sys, warnings, time
import numpy as np
import pandas as pd
from pathlib import Path

warnings.filterwarnings("ignore")

from rdkit import Chem, RDLogger
from rdkit.Chem import Descriptors, rdMolDescriptors
RDLogger.logger().setLevel(RDLogger.ERROR)

import torch
from chemprop import models as chemprop_models, nn as chemprop_nn
from chemprop.data import MoleculeDatapoint, MoleculeDataset, build_dataloader
from lightning import pytorch as pl
from sklearn.model_selection import train_test_split

N_RUNS = 5
EPOCHS = 30

# === Target molecules ===
CHEN_MOLECULES = {
    "TAQ":  ("Nc1c(N)c(=O)c2[nH]c3c(=O)c(N)c(N)c(=O)c3[nH]c2c1=O", 2.50),
    "TABQ": ("O=C1C(N)=C(N)C(=O)C(N)=C1N", 2.70),
    "AQ":   ("O=C1C2=CC=CC=C2C(=O)C2=CC=CC=C12", 2.30),
    "BQ":   ("O=C1C=CC(=O)C=C1", 2.80),
}

# === Load and prepare data ===
print("Loading OMEAD data...")
df = pd.read_csv("data/OMEAD_26218.csv")
df = df.dropna(subset=["smiles", "reduction_solv"])

all_mols = []
all_targets = []
for _, row in df.iterrows():
    mol = Chem.MolFromSmiles(row["smiles"])
    if mol is not None:
        all_mols.append(mol)
        all_targets.append(row["reduction_solv"])

print(f"Valid molecules: {len(all_mols)}")

# Fixed train/test split (same as XGBoost)
indices = list(range(len(all_mols)))
train_idx, test_idx = train_test_split(indices, test_size=0.2, random_state=42)

train_mols = [all_mols[i] for i in train_idx]
train_targets = [all_targets[i] for i in train_idx]
test_mols = [all_mols[i] for i in test_idx]
test_targets = np.array([all_targets[i] for i in test_idx])

# Target molecules
chen_mols = [Chem.MolFromSmiles(smi) for smi, _ in CHEN_MOLECULES.values()]
chen_names = list(CHEN_MOLECULES.keys())

# === Run 5 independent trainings ===
all_test_preds = []
all_chen_preds = []
all_test_mae = []

for run in range(N_RUNS):
    print(f"\n{'='*50}")
    print(f"RUN {run+1}/{N_RUNS}")
    print(f"{'='*50}")
    
    t0 = time.time()
    
    # Build fresh dataloaders
    train_datapoints = [
        MoleculeDatapoint(train_mols[i], y=np.array([train_targets[i]]))
        for i in range(len(train_mols))
    ]
    train_dataset = MoleculeDataset(train_datapoints)
    train_loader = build_dataloader(train_dataset, batch_size=64, shuffle=True, num_workers=0)
    
    # Fresh model with new random seed
    mp = chemprop_nn.BondMessagePassing()
    agg = chemprop_nn.MeanAggregation()
    ffn = chemprop_nn.RegressionFFN()
    model = chemprop_models.MPNN(
        message_passing=mp, agg=agg, predictor=ffn, batch_norm=True
    )
    
    trainer = pl.Trainer(
        max_epochs=EPOCHS,
        accelerator="gpu" if torch.cuda.is_available() else "cpu",
        devices=1,
        enable_progress_bar=True,
        logger=False,
        enable_checkpointing=False,
    )
    
    trainer.fit(model, train_loader)
    
    # Predict test set
    test_datapoints = [MoleculeDatapoint(mol) for mol in test_mols]
    test_dataset = MoleculeDataset(test_datapoints)
    test_loader = build_dataloader(test_dataset, batch_size=256, shuffle=False, num_workers=0)
    
    test_preds_raw = trainer.predict(model, test_loader)
    test_preds = np.concatenate([p.squeeze().numpy() for p in test_preds_raw])
    test_mae = np.mean(np.abs(test_targets - test_preds))
    all_test_preds.append(test_preds)
    all_test_mae.append(test_mae)
    
    # Predict target molecules
    chen_datapoints = [MoleculeDatapoint(mol) for mol in chen_mols]
    chen_dataset = MoleculeDataset(chen_datapoints)
    chen_loader = build_dataloader(chen_dataset, batch_size=len(chen_mols), shuffle=False, num_workers=0)
    
    chen_preds_raw = trainer.predict(model, chen_loader)
    chen_preds = np.concatenate([p.squeeze().numpy() for p in chen_preds_raw]).flatten()
    all_chen_preds.append(chen_preds)
    
    elapsed = time.time() - t0
    print(f"  Test MAE: {test_mae:.4f} V | Time: {elapsed:.1f}s")
    for i, name in enumerate(chen_names):
        li_val = chen_preds[i] - 1.24
        print(f"  {name}: {chen_preds[i]:.4f}V (vacuum) = {li_val:.4f}V (Li+/Li)")

# === Summary ===
print("\n" + "=" * 70)
print("SUMMARY: 5-Run Chemprop Results")
print("=" * 70)

all_chen_preds = np.array(all_chen_preds)  # shape: (5, 4)
all_test_mae = np.array(all_test_mae)

print(f"\nTest Set MAE across 5 runs: {all_test_mae.mean():.4f} +/- {all_test_mae.std():.4f} V")
print(f"  Individual: {', '.join(f'{m:.4f}' for m in all_test_mae)}")

print(f"\nTarget Molecule Predictions (vs vacuum, mean +/- std):")
print(f"{'Molecule':>8s} | {'Mean(vac)':>10s} | {'Std':>6s} | {'Mean(Li)':>10s} | {'Exp(Li)':>8s} | {'Delta':>8s}")
print("-" * 70)

for i, name in enumerate(chen_names):
    vac_mean = all_chen_preds[:, i].mean()
    vac_std = all_chen_preds[:, i].std()
    li_mean = vac_mean - 1.24
    exp_li = CHEN_MOLECULES[name][1]
    delta = li_mean - exp_li
    print(f"{name:>8s} | {vac_mean:>9.4f}V | {vac_std:>5.3f} | {li_mean:>9.4f}V | {exp_li:>7.2f}V | {delta:>+7.4f}V")

# Ensemble prediction (mean of 5 runs)
ensemble_chen = all_chen_preds.mean(axis=0)
ensemble_test = np.mean(all_test_preds, axis=0)
ensemble_test_mae = np.mean(np.abs(test_targets - ensemble_test))

print(f"\nEnsemble (5-run average) Test MAE: {ensemble_test_mae:.4f} V")
print(f"  vs single-run average: {all_test_mae.mean():.4f} V")
print(f"  Ensemble is {'better' if ensemble_test_mae < all_test_mae.mean() else 'worse'} by {abs(ensemble_test_mae - all_test_mae.mean()):.4f} V")

# Save results
results = {
    "test_mae_per_run": all_test_mae.tolist(),
    "test_mae_mean": float(all_test_mae.mean()),
    "test_mae_std": float(all_test_mae.std()),
    "ensemble_test_mae": float(ensemble_test_mae),
}
for i, name in enumerate(chen_names):
    results[f"{name}_vacuum_per_run"] = all_chen_preds[:, i].tolist()
    results[f"{name}_vacuum_mean"] = float(all_chen_preds[:, i].mean())
    results[f"{name}_vacuum_std"] = float(all_chen_preds[:, i].std())

import json
with open("models/chemprop_5run_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("\nResults saved to: models/chemprop_5run_results.json")
