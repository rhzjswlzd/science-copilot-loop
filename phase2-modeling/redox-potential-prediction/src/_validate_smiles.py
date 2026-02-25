"""
Construct TAQ SMILES with PARA-quinone structure.
Each quinone unit: C=O at 1,4 positions, NH2 at 2,3 positions.
Central dihydropyrazine ring. Target: C12H10N6O4, MW=302.25.
"""
from rdkit import Chem, RDLogger
from rdkit.Chem import Descriptors, rdMolDescriptors, AllChem, Draw
RDLogger.logger().setLevel(RDLogger.ERROR)

# Key difference from ortho:
#   ortho: c(=O)c(=O) — two ADJACENT C=O (1,2-quinone)
#   para:  c(=O)...c(=O) — C=O separated by one carbon (1,4-quinone)
#
# Structure description:
#   Left ring:  O=C - C(NH2) = C(NH2) - C(=O) - C - C
#               1      2        3        4       5   6
#   Center:     C5 - NH - C5' - C6' - NH - C6  (dihydropyrazine)
#   Right ring: O=C - C(NH2) = C(NH2) - C(=O) - C5' - C6'

candidates = [
    # Various para-quinone TAQ attempts
    "O=C1C(N)=C(N)C(=O)C2=C1NC1=C(N)C(=O)C(N)=C1N2",
    "O=C1C(N)=C(N)C(=O)C2C1NC1C(=O)C(N)=C(N)C(=O)C1N2",
    "O=c1c(N)c(N)c(=O)c2c1[nH]c1c(N)c(=O)c(N)c1[nH]2",
    "O=c1c(N)c(N)c(=O)c2[nH]c3c(=O)c(N)c(N)c(=O)c3[nH]c12",
    "O=C1C(N)=C(N)C(=O)C2=C1NC1=C2NC(=O)C(N)=C(N)C1=O",
    # Try different connectivity orders
    "NC1=C(N)C(=O)C2=C(C1=O)NC1=C(N)C(=O)C(N)=C1N2",
    "O=C1C(=NC2=C(N)C(=O)C(N)=C2NC3=C1N)C(N)=C3=O",
    # Based on phenazine-2,3,7,8-tetramine-1,4,6,9-tetrone
    "O=c1c(N)c(N)c(=O)c2c1[nH]c1c(=O)c(N)c(N)c(=O)c1[nH]2",
    # More systematic attempts
    "O=C1C(N)=C(N)C(=O)C2=C1[NH]C1=C(N)C(=O)C(N)=C1[NH]2",
    "O=C1C(N)=C(N)C(=O)C2=C1NC3C(=O)C(N)=C(N)C(=O)=C3N2",
    "O=C1C(N)=C(N)C(=O)c2c1[nH]c1c(=O)c(N)c(N)c(=O)c1[nH]2",
    # Start from dihydropyrazine core and build outward
    "C1(NC2=C(N)C(=O)C(N)=C2N1)=C(N)C(=O)C(N)=C",
    # Using explicit ring closures
    "O=C1C(N)=C(N)C(=O)C2C(NC3C(=O)C(N)=C(N)C3=O)=C1N2",
    # Alternative: fully aromatic form of para-quinone diaminoquinone-dihydrophenazine
    "NC1=C(N)C(=O)C2=CC3=CC(=O)C(N)=C(N)C3=NC2=C1",
]

print("Para-quinone TAQ candidates:")
print(f"Target: C12H10N6O4, MW=302.25")
print(f"Expected: 4 NH2, 2 NH (pyrazine), 4 C=O at 1,4-positions\n")

valid = []
for i, smi in enumerate(candidates):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        print(f"  v{i:2d}: PARSE FAILED | {smi}")
        continue
    f = rdMolDescriptors.CalcMolFormula(mol)
    mw = Descriptors.MolWt(mol)
    can = Chem.MolToSmiles(mol, canonical=True)
    
    # Count groups
    n_nh2 = len([a for a in mol.GetAtoms() if a.GetSymbol() == "N" and a.GetTotalNumHs() == 2])
    n_nh = len([a for a in mol.GetAtoms() if a.GetSymbol() == "N" and a.GetTotalNumHs() == 1])
    n_o = len([a for a in mol.GetAtoms() if a.GetSymbol() == "O"])
    n_rings = mol.GetRingInfo().NumRings()
    
    ok = "OK" if f == "C12H10N6O4" else "WRONG"
    print(f"  v{i:2d}: {ok:5s} | {f:15s} MW={mw:6.2f} | NH2={n_nh2} NH={n_nh} O={n_o} rings={n_rings} | {can}")
    
    if f == "C12H10N6O4":
        valid.append((i, smi, can, mol))

if valid:
    print(f"\n=== {len(valid)} VALID candidates found ===")
    
    # Draw all valid candidates
    mols_draw = []
    legends_draw = []
    for idx, orig, can, mol in valid:
        AllChem.Compute2DCoords(mol)
        mols_draw.append(mol)
        legends_draw.append(f"v{idx}\n{can[:40]}...")
    
    if len(mols_draw) == 1:
        img = Draw.MolToImage(mols_draw[0], size=(700, 700))
    else:
        img = Draw.MolsToGridImage(mols_draw, molsPerRow=2, subImgSize=(500, 500), legends=legends_draw)
    img.save("models/taq_para_candidates.png")
    print("  Saved: models/taq_para_candidates.png")
    
    print("\n  Best candidate (first valid):")
    print(f"  SMILES: {valid[0][2]}")
else:
    print("\n  ❌ No valid para-quinone TAQ found among candidates.")
    print("  Need to try more SMILES constructions.")
