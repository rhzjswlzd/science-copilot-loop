"""
data_loader.py - 加载和预处理 OMEAD 数据集
"""
import pandas as pd
import numpy as np
from pathlib import Path


DATA_DIR = Path(__file__).parent.parent / "data"
DEFAULT_CSV = DATA_DIR / "OMEAD_26218.csv"


def load_omead(csv_path: str | Path = DEFAULT_CSV) -> pd.DataFrame:
    """加载 OMEAD CSV 并进行基础清洗"""
    df = pd.read_csv(csv_path)
    print(f"原始数据: {len(df)} 行, {len(df.columns)} 列")
    
    # 确认关键列存在
    required_cols = ["smiles", "reduction_solv", "oxidation_solv"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"缺少必要列: {missing}")
    
    # 删除 SMILES 为空的行
    before = len(df)
    df = df.dropna(subset=["smiles"])
    df = df[df["smiles"].str.strip() != ""]
    print(f"删除空 SMILES: {before - len(df)} 行")
    
    # 删除目标列为空的行
    before = len(df)
    df = df.dropna(subset=["reduction_solv"])
    print(f"删除空 reduction_solv: {before - len(df)} 行")
    
    df = df.reset_index(drop=True)
    print(f"清洗后数据: {len(df)} 行")
    return df


def eda_summary(df: pd.DataFrame) -> dict:
    """数据探索摘要"""
    target_col = "reduction_solv"
    
    summary = {
        "total_rows": len(df),
        "total_cols": len(df.columns),
        "columns": list(df.columns),
        "smiles_unique": df["smiles"].nunique(),
        "target_stats": {
            "mean": df[target_col].mean(),
            "std": df[target_col].std(),
            "min": df[target_col].min(),
            "max": df[target_col].max(),
            "median": df[target_col].median(),
        },
        "redox_stable_counts": df["redox_stable"].value_counts().to_dict()
            if "redox_stable" in df.columns else {},
        "missing_values": df.isnull().sum().to_dict(),
    }
    
    print("\n=== OMEAD 数据集摘要 ===")
    print(f"总行数: {summary['total_rows']}")
    print(f"总列数: {summary['total_cols']}")
    print(f"唯一 SMILES 数: {summary['smiles_unique']}")
    print(f"\n目标变量 (reduction_solv) 统计:")
    for k, v in summary["target_stats"].items():
        print(f"  {k}: {v:.4f}")
    if summary["redox_stable_counts"]:
        print(f"\nredox_stable 分布: {summary['redox_stable_counts']}")
    
    return summary


if __name__ == "__main__":
    df = load_omead()
    eda_summary(df)
    print(f"\n前 5 行 SMILES:")
    for i, row in df.head().iterrows():
        print(f"  [{i}] {row['smiles']}  →  reduction_solv = {row['reduction_solv']:.4f} V")
