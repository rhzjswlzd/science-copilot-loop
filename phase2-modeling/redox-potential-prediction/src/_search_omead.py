"""Search OMEAD for BQ and AQ, compare DFT values with model predictions."""
import pandas as pd
from rdkit import Chem, RDLogger
RDLogger.logger().setLevel(RDLogger.ERROR)
import sys
sys.path.insert(0, ".")
from src.predict import load_model, predict_single

df = pd.read_csv("data/OMEAD_26218.csv")
df["canonical"] = df["smiles"].apply(
    lambda s: Chem.MolToSmiles(Chem.MolFromSmiles(s)) if Chem.MolFromSmiles(s) else None
)

targets = {
    "BQ": "O=C1C=CC(=O)C=C1",
    "AQ": "O=C1c2ccccc2C(=O)c2ccccc21",
}

load_model()

print("=" * 60)
print("OMEAD Dataset Search + Model Prediction Comparison")
print("=" * 60)

for name, smi in targets.items():
    can = Chem.MolToSmiles(Chem.MolFromSmiles(smi))
    matches = df[df["canonical"] == can]

    print(f"\n{name}:")
    print(f"  Canonical SMILES: {can}")
    print(f"  Found in OMEAD: {len(matches)} match(es)")

    if len(matches) > 0:
        for _, row in matches.iterrows():
            print(f"  Dataset original SMILES: {row['smiles']}")
            print(f"  reduction_solv (DFT, vs vacuum): {row['reduction_solv']:.4f} V")
            cols_to_check = ["oxidation_solv", "reduction_gas", "oxidation_gas"]
            for col in cols_to_check:
                if col in row and pd.notna(row.get(col)):
                    print(f"  {col}: {row[col]:.4f} V")
    else:
        print("  NOT in dataset!")

    pred = predict_single(smi)
    print(f"  XGBoost prediction (vs vacuum): {pred['prediction']:.4f} V")

    if len(matches) > 0:
        dft_val = matches.iloc[0]["reduction_solv"]
        model_val = pred["prediction"]
        print(f"  >>> Model error (pred - DFT): {model_val - dft_val:+.4f} V")
