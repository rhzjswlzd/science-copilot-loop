"""
features.py - 从 SMILES 提取分子特征
"""
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem, Descriptors, rdMolDescriptors
from rdkit import RDLogger

# 抑制 RDKit 警告
RDLogger.logger().setLevel(RDLogger.ERROR)


def smiles_to_mol(smiles: str):
    """将 SMILES 转换为 RDKit 分子对象"""
    try:
        mol = Chem.MolFromSmiles(smiles)
        return mol
    except Exception:
        return None


def mol_to_morgan_fp(mol, radius: int = 2, n_bits: int = 2048) -> np.ndarray | None:
    """从 RDKit 分子对象生成 Morgan Fingerprint"""
    if mol is None:
        return None
    try:
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=n_bits)
        return np.array(fp, dtype=np.int8)
    except Exception:
        return None


def mol_to_descriptors(mol) -> dict | None:
    """从 RDKit 分子对象提取物化描述符"""
    if mol is None:
        return None
    try:
        return {
            "MolWt": Descriptors.MolWt(mol),
            "LogP": Descriptors.MolLogP(mol),
            "TPSA": Descriptors.TPSA(mol),
            "NumHDonors": Descriptors.NumHDonors(mol),
            "NumHAcceptors": Descriptors.NumHAcceptors(mol),
            "NumRotatableBonds": Descriptors.NumRotatableBonds(mol),
            "NumAromaticRings": rdMolDescriptors.CalcNumAromaticRings(mol),
            "NumHeavyAtoms": Descriptors.HeavyAtomCount(mol),
            "RingCount": Descriptors.RingCount(mol),
            "FractionCSP3": Descriptors.FractionCSP3(mol),
        }
    except Exception:
        return None


def compute_features(
    smiles_list: list[str],
    use_fp: bool = True,
    use_descriptors: bool = True,
    fp_radius: int = 2,
    fp_n_bits: int = 2048,
) -> tuple[np.ndarray, list[bool]]:
    """
    批量计算特征矩阵
    
    Returns:
        features: (n_valid, n_features) 特征矩阵
        valid_mask: 长度为 n_total 的布尔列表，标记每个 SMILES 是否有效
    """
    all_features = []
    valid_mask = []
    
    for i, smi in enumerate(smiles_list):
        mol = smiles_to_mol(smi)
        if mol is None:
            valid_mask.append(False)
            continue
        
        parts = []
        
        if use_fp:
            fp = mol_to_morgan_fp(mol, fp_radius, fp_n_bits)
            if fp is None:
                valid_mask.append(False)
                continue
            parts.append(fp)
        
        if use_descriptors:
            desc = mol_to_descriptors(mol)
            if desc is None:
                valid_mask.append(False)
                continue
            parts.append(np.array(list(desc.values()), dtype=np.float64))
        
        all_features.append(np.concatenate(parts))
        valid_mask.append(True)
        
        if (i + 1) % 5000 == 0:
            print(f"  已处理 {i+1}/{len(smiles_list)} 个分子...")
    
    features = np.array(all_features, dtype=np.float64) if all_features else np.array([])
    
    n_valid = sum(valid_mask)
    n_total = len(smiles_list)
    print(f"特征提取完成: {n_valid}/{n_total} 个有效 ({n_valid/n_total*100:.1f}%)")
    
    if use_fp and use_descriptors:
        print(f"特征维度: {fp_n_bits} (Morgan FP) + 10 (描述符) = {features.shape[1] if len(features) > 0 else 0}")
    elif use_fp:
        print(f"特征维度: {fp_n_bits} (Morgan FP)")
    else:
        print(f"特征维度: 10 (描述符)")
    
    return features, valid_mask


def get_descriptor_names() -> list[str]:
    """返回描述符列名"""
    return [
        "MolWt", "LogP", "TPSA", "NumHDonors", "NumHAcceptors",
        "NumRotatableBonds", "NumAromaticRings", "NumHeavyAtoms",
        "RingCount", "FractionCSP3",
    ]


def get_feature_names(use_fp: bool = True, use_descriptors: bool = True, fp_n_bits: int = 2048) -> list[str]:
    """返回完整特征列名"""
    names = []
    if use_fp:
        names.extend([f"MorganFP_{i}" for i in range(fp_n_bits)])
    if use_descriptors:
        names.extend(get_descriptor_names())
    return names


if __name__ == "__main__":
    # 快速测试
    test_smiles = [
        "O=C1C=CC(=O)C=C1",       # 苯醌
        "c1ccc2c(c1)cc1ccc3cccc4ccc2c1c34",  # 芘
        "CCC(C#N)CC",              # OMEAD 中的分子
        "INVALID_SMILES",          # 无效 SMILES
    ]
    features, mask = compute_features(test_smiles)
    print(f"\n有效分子: {sum(mask)}/{len(mask)}")
    print(f"特征矩阵维度: {features.shape}")
