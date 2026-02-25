"""
Analyze OMEAD dataset: proportion of N-containing fused ring aromatics,
and statistics relevant to TAQ-like molecules.
"""
import pandas as pd
from rdkit import Chem, RDLogger
from rdkit.Chem import Descriptors, rdMolDescriptors
from collections import Counter
RDLogger.logger().setLevel(RDLogger.ERROR)

df = pd.read_csv("data/OMEAD_26218.csv")
df = df.dropna(subset=["smiles", "reduction_solv"])

total = 0
has_N = 0
has_fused_ring = 0  # >= 2 rings sharing an edge
has_N_and_fused = 0
has_N_fused_aromatic = 0  # N in aromatic fused ring system
ring_counts = Counter()
n_atom_counts = Counter()

for _, row in df.iterrows():
    mol = Chem.MolFromSmiles(row["smiles"])
    if mol is None:
        continue
    total += 1

    # Count N atoms
    n_count = sum(1 for a in mol.GetAtoms() if a.GetSymbol() == "N")
    n_atom_counts[min(n_count, 8)] += 1

    # Ring info
    ri = mol.GetRingInfo()
    num_rings = ri.NumRings()
    ring_counts[min(num_rings, 6)] += 1

    # Check for fused rings (rings sharing >= 2 atoms = sharing an edge)
    fused = False
    if num_rings >= 2:
        bond_rings = ri.BondRings()
        for i in range(len(bond_rings)):
            for j in range(i + 1, len(bond_rings)):
                shared = set(bond_rings[i]) & set(bond_rings[j])
                if len(shared) >= 1:  # sharing at least one bond = fused
                    fused = True
                    break
            if fused:
                break

    contains_N = n_count > 0

    if contains_N:
        has_N += 1
    if fused:
        has_fused_ring += 1
    if contains_N and fused:
        has_N_and_fused += 1
        # Check if N is in an aromatic ring
        n_in_aromatic = any(
            a.GetIsAromatic() for a in mol.GetAtoms()
            if a.GetSymbol() == "N"
        )
        if n_in_aromatic:
            has_N_fused_aromatic += 1

print(f"OMEAD Dataset Analysis (total valid: {total})")
print("=" * 55)
print(f"  Contains N:                    {has_N:6d}  ({has_N/total*100:.1f}%)")
print(f"  Has fused rings (>=2 rings):   {has_fused_ring:6d}  ({has_fused_ring/total*100:.1f}%)")
print(f"  N + fused rings:               {has_N_and_fused:6d}  ({has_N_and_fused/total*100:.1f}%)")
print(f"  N in aromatic fused ring:      {has_N_fused_aromatic:6d}  ({has_N_fused_aromatic/total*100:.1f}%)")
print()

print("Ring count distribution:")
for k in sorted(ring_counts.keys()):
    label = f"{k}+" if k == 6 else str(k)
    print(f"  {label} rings: {ring_counts[k]:6d}  ({ring_counts[k]/total*100:.1f}%)")

print()
print("N atom count distribution:")
for k in sorted(n_atom_counts.keys()):
    label = f"{k}+" if k == 8 else str(k)
    print(f"  {label} N atoms: {n_atom_counts[k]:6d}  ({n_atom_counts[k]/total*100:.1f}%)")

# TAQ-like: 3+ fused rings, 4+ N, 2+ O
print()
print("--- TAQ-like molecules (3+ fused rings, N>=4, O>=2) ---")
taq_like = 0
for _, row in df.iterrows():
    mol = Chem.MolFromSmiles(row["smiles"])
    if mol is None:
        continue
    n_N = sum(1 for a in mol.GetAtoms() if a.GetSymbol() == "N")
    n_O = sum(1 for a in mol.GetAtoms() if a.GetSymbol() == "O")
    n_rings = mol.GetRingInfo().NumRings()
    if n_rings >= 3 and n_N >= 4 and n_O >= 2:
        taq_like += 1

print(f"  TAQ-like count: {taq_like} / {total} ({taq_like/total*100:.2f}%)")

# Also: simple quinones (<=1 ring, only C/H/O)
print()
print("--- Simple quinones (1 ring, only C/H/O, has C=O) ---")
simple_q = 0
for _, row in df.iterrows():
    mol = Chem.MolFromSmiles(row["smiles"])
    if mol is None:
        continue
    elements = set(a.GetSymbol() for a in mol.GetAtoms())
    n_rings = mol.GetRingInfo().NumRings()
    if n_rings <= 1 and elements <= {"C", "H", "O"} and "O" in elements:
        simple_q += 1

print(f"  Simple quinone-like count: {simple_q} / {total} ({simple_q/total*100:.2f}%)")
