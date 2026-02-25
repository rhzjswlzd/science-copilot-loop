"""
predict.py - 推理接口：SMILES → 氧化还原电位预测
"""
import numpy as np
import joblib
from pathlib import Path
from rdkit import Chem

from src.features import smiles_to_mol, mol_to_morgan_fp, mol_to_descriptors

MODEL_DIR = Path(__file__).parent.parent / "models"
MODEL_PATH = MODEL_DIR / "xgb_redox_model.pkl"

_model = None


def load_model():
    """加载训练好的模型（单例）"""
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"模型文件不存在: {MODEL_PATH}\n请先运行 python -m src.train 训练模型。"
            )
        _model = joblib.load(MODEL_PATH)
        print(f"模型已加载: {MODEL_PATH}")
    return _model


def predict_single(smiles: str) -> dict:
    """
    预测单个分子的氧化还原电位
    
    Args:
        smiles: 分子的 SMILES 字符串
    
    Returns:
        dict with keys: smiles, canonical_smiles, prediction, unit, error
    """
    result = {
        "smiles": smiles,
        "canonical_smiles": None,
        "prediction": None,
        "unit": "V (vs. vacuum, acetonitrile)",
        "error": None,
    }
    
    # 1. 验证 SMILES
    mol = smiles_to_mol(smiles)
    if mol is None:
        result["error"] = f"无法解析 SMILES: '{smiles}'"
        return result
    
    result["canonical_smiles"] = Chem.MolToSmiles(mol, canonical=True)
    
    # 2. 提取特征
    fp = mol_to_morgan_fp(mol, radius=2, n_bits=2048)
    desc = mol_to_descriptors(mol)
    
    if fp is None or desc is None:
        result["error"] = "特征提取失败"
        return result
    
    features = np.concatenate([fp, np.array(list(desc.values()))])
    features = features.reshape(1, -1)
    
    # 3. 预测
    model = load_model()
    prediction = model.predict(features)[0]
    result["prediction"] = float(prediction)
    
    return result


def predict_batch(smiles_list: list[str]) -> list[dict]:
    """批量预测"""
    return [predict_single(s) for s in smiles_list]


if __name__ == "__main__":
    # 测试
    test_cases = [
        "O=C1C=CC(=O)C=C1",        # 苯醌
        "CCC(C#N)CC",               # 来自 OMEAD 的分子
        "c1ccccc1",                  # 苯
        "CC(=O)O",                   # 乙酸
    ]
    
    print("=== 单分子预测测试 ===\n")
    for smi in test_cases:
        r = predict_single(smi)
        if r["error"]:
            print(f"  {smi} → 错误: {r['error']}")
        else:
            print(f"  {smi}")
            print(f"    Canonical: {r['canonical_smiles']}")
            print(f"    Prediction: {r['prediction']:.4f} {r['unit']}")
            print()
