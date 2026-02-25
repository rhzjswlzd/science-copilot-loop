"""
Train Chemprop D-MPNN 5 times, save ALL per-molecule test predictions
for future plot generation. Also predict target molecules.
Output: models/chemprop_5run_full.npz (numpy archive)
"""
import sys, warnings, time
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

from rdkit import Chem, RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)

import torch
from chemprop import models as chemprop_models, nn as chemprop_nn
from chemprop.data import MoleculeDatapoint, MoleculeDataset, build_dataloader
from lightning import pytorch as pl
from sklearn.model_selection import train_test_split

N_RUNS = 5
EPOCHS = 30

CHEN = {
    "TAQ":  ("Nc1c(N)c(=O)c2[nH]c3c(=O)c(N)c(N)c(=O)c3[nH]c2c1=O", 2.50),
    "TABQ": ("O=C1C(N)=C(N)C(=O)C(N)=C1N", 2.70),
    "AQ":   ("O=C1C2=CC=CC=C2C(=O)C2=CC=CC=C12", 2.30),
    "BQ":   ("O=C1C=CC(=O)C=C1", 2.80),
}

# Load data
print("Loading OMEAD data...")
df = pd.read_csv("data/OMEAD_26218.csv")
df = df.dropna(subset=["smiles", "reduction_solv"])

all_mols, all_targets = [], []
for _, row in df.iterrows():
    mol = Chem.MolFromSmiles(row["smiles"])
    if mol is not None:
        all_mols.append(mol)
        all_targets.append(row["reduction_solv"])

print(f"Valid molecules: {len(all_mols)}")

indices = list(range(len(all_mols)))
train_idx, test_idx = train_test_split(indices, test_size=0.2, random_state=42)

train_mols = [all_mols[i] for i in train_idx]
train_targets = [all_targets[i] for i in train_idx]
test_mols = [all_mols[i] for i in test_idx]
y_test = np.array([all_targets[i] for i in test_idx])

chen_names = list(CHEN.keys())
chen_mols = [Chem.MolFromSmiles(smi) for smi, _ in CHEN.values()]
chen_exp = np.array([exp for _, exp in CHEN.values()])

# Storage for all runs
test_preds_all = np.zeros((N_RUNS, len(y_test)))    # (5, 5241)
chen_preds_all = np.zeros((N_RUNS, len(chen_names)))  # (5, 4)
test_mae_all = np.zeros(N_RUNS)

for run in range(N_RUNS):
    print(f"\n{'='*50}")
    print(f"RUN {run+1}/{N_RUNS}")
    print(f"{'='*50}")
    t0 = time.time()

    train_dp = [MoleculeDatapoint(train_mols[i], y=np.array([train_targets[i]]))
                for i in range(len(train_mols))]
    train_loader = build_dataloader(MoleculeDataset(train_dp), batch_size=64,
                                     shuffle=True, num_workers=0)

    model = chemprop_models.MPNN(
        message_passing=chemprop_nn.BondMessagePassing(),
        agg=chemprop_nn.MeanAggregation(),
        predictor=chemprop_nn.RegressionFFN(),
        batch_norm=True,
    )

    trainer = pl.Trainer(
        max_epochs=EPOCHS,
        accelerator="gpu" if torch.cuda.is_available() else "cpu",
        devices=1, enable_progress_bar=True, logger=False,
        enable_checkpointing=False,
    )
    trainer.fit(model, train_loader)

    # Test set predictions
    test_dp = [MoleculeDatapoint(mol) for mol in test_mols]
    test_loader = build_dataloader(MoleculeDataset(test_dp), batch_size=256,
                                    shuffle=False, num_workers=0)
    raw = trainer.predict(model, test_loader)
    preds = np.concatenate([p.squeeze().numpy() for p in raw])
    test_preds_all[run] = preds
    test_mae_all[run] = np.mean(np.abs(y_test - preds))

    # Target molecule predictions
    chen_dp = [MoleculeDatapoint(mol) for mol in chen_mols]
    chen_loader = build_dataloader(MoleculeDataset(chen_dp),
                                    batch_size=len(chen_mols), shuffle=False, num_workers=0)
    raw_c = trainer.predict(model, chen_loader)
    chen_preds_all[run] = np.concatenate([p.squeeze().numpy() for p in raw_c]).flatten()

    elapsed = time.time() - t0
    print(f"  MAE: {test_mae_all[run]:.4f}V | Time: {elapsed:.0f}s")

# Ensemble
ensemble_preds = test_preds_all.mean(axis=0)
ensemble_mae = np.mean(np.abs(y_test - ensemble_preds))
pred_std = test_preds_all.std(axis=0)  # per-molecule uncertainty

print(f"\n{'='*60}")
print(f"DONE. Saving all data to models/chemprop_5run_full.npz")
print(f"{'='*60}")
print(f"Per-run MAEs: {[f'{m:.4f}' for m in test_mae_all]}")
print(f"Mean MAE: {test_mae_all.mean():.4f} +/- {test_mae_all.std():.4f}")
print(f"Ensemble MAE: {ensemble_mae:.4f}")
print(f"Per-molecule std: mean={pred_std.mean():.4f}, max={pred_std.max():.4f}")

# Save everything
np.savez("models/chemprop_5run_full.npz",
         y_test=y_test,
         test_preds_all=test_preds_all,   # (5, 5241)
         ensemble_preds=ensemble_preds,    # (5241,)
         pred_std=pred_std,                # (5241,)
         test_mae_all=test_mae_all,        # (5,)
         ensemble_mae=np.array([ensemble_mae]),
         chen_names=np.array(chen_names),
         chen_exp=chen_exp,                # (4,)
         chen_preds_all=chen_preds_all,    # (5, 4)
)
print("Saved: models/chemprop_5run_full.npz")
print(f"  y_test: {y_test.shape}")
print(f"  test_preds_all: {test_preds_all.shape}")
print(f"  chen_preds_all: {chen_preds_all.shape}")
