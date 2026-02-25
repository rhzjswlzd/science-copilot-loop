"""
Predict redox potentials for representative organic electrode molecules.
Validates model predictions against published experimental values.
"""
import sys, os, json, warnings
import numpy as np
import pandas as pd
from pathlib import Path

warnings.filterwarnings("ignore")

from rdkit import Chem, RDLogger
from rdkit.Chem import Draw, Descriptors, AllChem, rdMolDescriptors
RDLogger.logger().setLevel(RDLogger.ERROR)

# ================================================================
# STEP 1: Define validated molecules
# ================================================================
print("=" * 70)
print("STEP 1: Molecule Definitions (Pre-validated)")
print("=" * 70)

MOLECULES = {
    "TAQ": {
        "smiles": "Nc1c(N)c(=O)c2[nH]c3c(=O)c(N)c(N)c(=O)c3[nH]c2c1=O",
        "full_name": "bis-tetraaminobenzoquinone (BTABQ)",
        "target_formula": "C12H10N6O4",
        "target_mw": 302.25,
        "exp_voltage_li": 2.5,   # V vs Li+/Li (average of two platforms)
        "exp_note": "Two platforms: ~2.6V and ~2.2V vs Li+/Li",
        "source": "ACS Cent. Sci. 2024",
    },
    "TABQ": {
        "smiles": "O=C1C(N)=C(N)C(=O)C(N)=C1N",
        "full_name": "tetraamino-p-benzoquinone",
        "target_formula": "C6H8N4O2",
        "target_mw": 168.15,
        "exp_voltage_li": 2.7,
        "exp_note": "Battery-type behavior",
        "source": "Joule 2023",
    },
    "AQ": {
        "smiles": "O=C1C2=CC=CC=C2C(=O)C2=CC=CC=C12",
        "full_name": "anthraquinone",
        "target_formula": "C14H8O2",
        "target_mw": 208.21,
        "exp_voltage_li": 2.3,
        "exp_note": "Classic benchmark",
        "source": "Literature",
    },
    "BQ": {
        "smiles": "O=C1C=CC(=O)C=C1",
        "full_name": "p-benzoquinone",
        "target_formula": "C6H4O2",
        "target_mw": 108.09,
        "exp_voltage_li": 2.8,
        "exp_note": "Simplest quinone",
        "source": "Literature",
    },
    "PT": {
        "smiles": "O=c1c2ccccc2c(=O)c2cc3c(=O)c4ccccc4c(=O)c3cc12",
        "full_name": "5,7,12,14-pentacenetetrone",
        "target_formula": "C22H10O4",
        "target_mw": 338.31,
        "exp_voltage_li": 2.6,
        "exp_note": "Diffusion-controlled behavior",
        "source": "Joule 2023",
    },
}

# Validate all
for name, info in MOLECULES.items():
    mol = Chem.MolFromSmiles(info["smiles"])
    if mol is None:
        print(f"  {name}: FAILED to parse SMILES!")
        continue
    formula = rdMolDescriptors.CalcMolFormula(mol)
    mw = Descriptors.MolWt(mol)
    canonical = Chem.MolToSmiles(mol, canonical=True)
    info["mol"] = mol
    info["formula"] = formula
    info["mw"] = mw
    info["canonical"] = canonical
    
    f_match = "OK" if formula == info["target_formula"] else f"MISMATCH(got {formula})"
    print(f"  {name} ({info['full_name']})")
    print(f"    SMILES: {canonical}")
    print(f"    Formula: {formula} [{f_match}], MW: {mw:.2f}")

# ================================================================
# STEP 2: Draw 2D Structures  
# ================================================================
print("\n" + "=" * 70)
print("STEP 2: Drawing 2D Structures")
print("=" * 70)

mols_to_draw = []
legends = []
for name, info in MOLECULES.items():
    mol = info["mol"]
    AllChem.Compute2DCoords(mol)
    mols_to_draw.append(mol)
    legends.append(f"{name}\n{info['formula']}\nMW={info['mw']:.1f}")

# Grid image
img = Draw.MolsToGridImage(
    mols_to_draw,
    molsPerRow=3,
    subImgSize=(450, 400),
    legends=legends
)
struct_path = Path("models/chen_molecules_structures.png")
img.save(str(struct_path))
print(f"  Grid image saved: {struct_path}")

# Individual TAQ image (larger for inspection)
taq_mol = MOLECULES["TAQ"]["mol"]
AllChem.Compute2DCoords(taq_mol)
taq_img = Draw.MolToImage(taq_mol, size=(700, 700))
taq_path = Path("models/taq_structure.png")
taq_img.save(str(taq_path))
print(f"  TAQ individual: {taq_path}")

# ================================================================
# STEP 3: XGBoost Predictions
# ================================================================
print("\n" + "=" * 70)
print("STEP 3: XGBoost Predictions")
print("=" * 70)

sys.path.insert(0, str(Path(".").resolve()))
from src.predict import load_model, predict_single

load_model()

results = []
for name, info in MOLECULES.items():
    pred = predict_single(info["smiles"])
    pred_vacuum = pred["prediction"]
    
    if pred_vacuum is not None:
        pred_li = pred_vacuum - 1.24
        exp_li = info["exp_voltage_li"]
        deviation = pred_li - exp_li
        
        print(f"  {name:5s}: pred(vacuum)={pred_vacuum:+.4f}V -> pred(Li/Li+)={pred_li:+.4f}V | exp={exp_li}V | delta={deviation:+.4f}V")
        
        results.append({
            "Molecule": name,
            "Full_Name": info["full_name"],
            "SMILES": info["canonical"],
            "Formula": info["formula"],
            "XGB_vacuum_V": round(pred_vacuum, 4),
            "XGB_LiLi_V": round(pred_li, 4),
            "Exp_LiLi_V": exp_li,
            "XGB_delta_V": round(deviation, 4),
            "Source": info["source"],
        })
    else:
        print(f"  {name}: Prediction FAILED - {pred.get('error')}")

# ================================================================
# STEP 4: Chemprop Predictions
# ================================================================
print("\n" + "=" * 70)
print("STEP 4: Chemprop Predictions")
print("=" * 70)

chemprop_ok = False
try:
    import torch
    from chemprop import models as chemprop_models, nn as chemprop_nn
    from chemprop.data import MoleculeDatapoint, MoleculeDataset, build_dataloader
    from lightning import pytorch as pl
    from sklearn.model_selection import train_test_split
    
    print("  Chemprop available. Retraining on full OMEAD data (30 epochs)...")
    print("  (We did not save the previous model, so a quick retrain is needed)")
    
    df = pd.read_csv("data/OMEAD_26218.csv")
    df = df.dropna(subset=["smiles", "reduction_solv"])
    
    mols_train = []
    targets_train = []
    for _, row in df.iterrows():
        mol = Chem.MolFromSmiles(row["smiles"])
        if mol is not None:
            mols_train.append(mol)
            targets_train.append(row["reduction_solv"])
    
    print(f"  Training data: {len(mols_train)} molecules")
    
    train_datapoints = [
        MoleculeDatapoint(mols_train[i], y=np.array([targets_train[i]]))
        for i in range(len(mols_train))
    ]
    train_dataset = MoleculeDataset(train_datapoints)
    train_loader = build_dataloader(train_dataset, batch_size=64, shuffle=True, num_workers=0)
    
    mp = chemprop_nn.BondMessagePassing()
    agg = chemprop_nn.MeanAggregation()
    ffn = chemprop_nn.RegressionFFN()
    chemprop_model = chemprop_models.MPNN(
        message_passing=mp, agg=agg, predictor=ffn, batch_norm=True
    )
    
    trainer = pl.Trainer(
        max_epochs=30,
        accelerator="gpu" if torch.cuda.is_available() else "cpu",
        devices=1,
        enable_progress_bar=True,
        logger=False,
        enable_checkpointing=False,
    )
    
    trainer.fit(chemprop_model, train_loader)
    print("  Training complete!")
    
    # Predict target molecules
    test_mols = [info["mol"] for info in MOLECULES.values()]
    test_names = list(MOLECULES.keys())
    
    test_datapoints = [MoleculeDatapoint(mol) for mol in test_mols]
    test_dataset = MoleculeDataset(test_datapoints)
    test_loader = build_dataloader(test_dataset, batch_size=len(test_mols), shuffle=False, num_workers=0)
    
    preds_raw = trainer.predict(chemprop_model, test_loader)
    cp_preds = np.concatenate([p.squeeze().numpy() for p in preds_raw])
    
    for i, name in enumerate(test_names):
        cp_vacuum = float(cp_preds[i])
        cp_li = cp_vacuum - 1.24
        exp_li = MOLECULES[name]["exp_voltage_li"]
        cp_dev = cp_li - exp_li
        
        print(f"  {name:5s}: CP pred(vacuum)={cp_vacuum:+.4f}V -> pred(Li/Li+)={cp_li:+.4f}V | delta={cp_dev:+.4f}V")
        
        for r in results:
            if r["Molecule"] == name:
                r["CP_vacuum_V"] = round(cp_vacuum, 4)
                r["CP_LiLi_V"] = round(cp_li, 4)
                r["CP_delta_V"] = round(cp_dev, 4)
                # Ensemble
                ens_li = (r["XGB_LiLi_V"] + cp_li) / 2
                r["Ensemble_LiLi_V"] = round(ens_li, 4)
                r["Ensemble_delta_V"] = round(ens_li - exp_li, 4)
    
    chemprop_ok = True

except Exception as e:
    print(f"  Chemprop failed: {e}")
    import traceback
    traceback.print_exc()

# ================================================================
# STEP 5: Results Table
# ================================================================
print("\n" + "=" * 70)
print("STEP 5: Results Summary Table")
print("=" * 70)

df_results = pd.DataFrame(results)
print(df_results.to_string(index=False))

csv_path = Path("models/chen_prediction_results.csv")
df_results.to_csv(csv_path, index=False)
print(f"\n  Saved to: {csv_path}")

# ================================================================
# STEP 6: Parity Plot
# ================================================================
print("\n" + "=" * 70)
print("STEP 6: Parity Plot")
print("=" * 70)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12})

fig, ax = plt.subplots(1, 1, figsize=(7, 7))

exps = [r["Exp_LiLi_V"] for r in results]
preds_xgb = [r["XGB_LiLi_V"] for r in results]
names_list = [r["Molecule"] for r in results]

# XGBoost
ax.scatter(exps, preds_xgb, s=140, c="#2563EB", marker="o", zorder=5,
           label="XGBoost + Morgan FP", edgecolors="white", linewidth=1.5)

# Chemprop
if chemprop_ok:
    preds_cp = [r.get("CP_LiLi_V") for r in results]
    if all(p is not None for p in preds_cp):
        ax.scatter(exps, preds_cp, s=140, c="#DC2626", marker="^", zorder=5,
                   label="Chemprop D-MPNN", edgecolors="white", linewidth=1.5)
    
    preds_ens = [r.get("Ensemble_LiLi_V") for r in results]
    if all(p is not None for p in preds_ens):
        ax.scatter(exps, preds_ens, s=140, c="#059669", marker="s", zorder=5,
                   label="Ensemble (avg)", edgecolors="white", linewidth=1.5)

# Annotate
for i, name in enumerate(names_list):
    ax.annotate(name, (exps[i], preds_xgb[i]), textcoords="offset points",
               xytext=(12, 8), fontsize=11, fontweight="bold", color="#1E293B")

# y=x line and +/-0.5V band
all_vals = exps + preds_xgb
lo, hi = min(all_vals) - 0.5, max(all_vals) + 0.5
ax.plot([lo, hi], [lo, hi], "--", color="#94A3B8", linewidth=1.5, label="Perfect (y=x)")
ax.fill_between([lo, hi], [lo - 0.5, hi - 0.5], [lo + 0.5, hi + 0.5],
                alpha=0.08, color="#2563EB", label="+/-0.5V band")

ax.set_xlim(lo, hi)
ax.set_ylim(lo, hi)
ax.set_xlabel("Experimental Voltage (V vs Li+/Li)", fontsize=13)
ax.set_ylabel("Predicted Voltage (V vs Li+/Li)", fontsize=13)
ax.set_title("Redox Potential: Prediction vs Experiment\n(Selected Organic Electrode Molecules)", fontsize=14, fontweight="bold")
ax.legend(fontsize=10, loc="upper left")
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

plt.tight_layout()
parity_path = Path("models/chen_parity_plot.png")
fig.savefig(str(parity_path), dpi=200, bbox_inches="tight")
print(f"  Saved: {parity_path}")

# ================================================================
# STEP 7: Summary
# ================================================================
print("\n" + "=" * 70)
print("STEP 7: Deviation Analysis")
print("=" * 70)

xgb_devs = [abs(r["XGB_delta_V"]) for r in results]
print(f"  XGBoost MAE across target molecules: {np.mean(xgb_devs):.3f} V")

if chemprop_ok:
    cp_devs = [abs(r.get("CP_delta_V", 0)) for r in results]
    ens_devs = [abs(r.get("Ensemble_delta_V", 0)) for r in results]
    print(f"  Chemprop MAE across target molecules: {np.mean(cp_devs):.3f} V")
    print(f"  Ensemble MAE across target molecules: {np.mean(ens_devs):.3f} V")

print("""
Key observations:
1. Reference potential conversion (vacuum -> Li+/Li) has ~0.3V uncertainty
2. OMEAD uses acetonitrile SMD solvation; real batteries use carbonate electrolyte
3. DFT computes isolated/solution-phase molecules; TAQ is a crystalline solid
4. TAQ has two reduction platforms (2.6V, 2.2V); model gives single value
5. Deviations within 0.5V are acceptable given these systematic differences
""")

print("=" * 70)
print("DONE! Files saved:")
print(f"  - {struct_path}")
print(f"  - {taq_path}")
print(f"  - {csv_path}")
print(f"  - {parity_path}")
print("=" * 70)
