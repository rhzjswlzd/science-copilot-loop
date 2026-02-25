"""
train.py - 训练 XGBoost 模型预测氧化还原电位
"""
import numpy as np
import pandas as pd
import joblib
import json
from pathlib import Path
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

from src.data_loader import load_omead
from src.features import compute_features

# 路径
PROJECT_DIR = Path(__file__).parent.parent
MODEL_DIR = PROJECT_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

# 预测目标：乙腈溶剂中的还原电位 (vs. vacuum)
TARGET_COL = "reduction_solv"


def prepare_data(df: pd.DataFrame, target_col: str = TARGET_COL):
    """准备特征和目标变量"""
    print("\n=== 特征提取 ===")
    smiles_list = df["smiles"].tolist()
    y_all = df[target_col].values
    
    X, valid_mask = compute_features(smiles_list, use_fp=True, use_descriptors=True)
    
    # 筛选有效样本
    y = y_all[valid_mask]
    
    print(f"最终样本数: {len(y)}")
    print(f"目标变量范围: [{y.min():.3f}, {y.max():.3f}] V")
    
    return X, y


def train_model(X: np.ndarray, y: np.ndarray, do_cv: bool = True):
    """训练 XGBoost 回归模型"""
    
    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"\n=== 数据划分 ===")
    print(f"训练集: {len(X_train)} 样本")
    print(f"测试集: {len(X_test)} 样本")
    
    # XGBoost 模型
    model = XGBRegressor(
        n_estimators=500,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
        verbosity=0,
    )
    
    # 5-fold 交叉验证
    if do_cv:
        print(f"\n=== 5-Fold 交叉验证 ===")
        cv_mae = cross_val_score(model, X_train, y_train, cv=5,
                                  scoring="neg_mean_absolute_error", n_jobs=-1)
        cv_r2 = cross_val_score(model, X_train, y_train, cv=5,
                                 scoring="r2", n_jobs=-1)
        print(f"CV MAE:  {-cv_mae.mean():.4f} +/- {cv_mae.std():.4f}")
        print(f"CV R2:   {cv_r2.mean():.4f} +/- {cv_r2.std():.4f}")
    
    # 训练最终模型
    print(f"\n=== 训练最终模型 ===")
    model.fit(X_train, y_train)
    
    # 测试集评估
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    print(f"\n=== 测试集评估 ===")
    print(f"MAE:  {mae:.4f} V")
    print(f"RMSE: {rmse:.4f} V")
    print(f"R²:   {r2:.4f}")
    
    metrics = {
        "mae": mae,
        "rmse": rmse,
        "r2": r2,
        "train_size": len(X_train),
        "test_size": len(X_test),
        "target": TARGET_COL,
    }
    
    if do_cv:
        metrics["cv_mae_mean"] = float(-cv_mae.mean())
        metrics["cv_mae_std"] = float(cv_mae.std())
        metrics["cv_r2_mean"] = float(cv_r2.mean())
        metrics["cv_r2_std"] = float(cv_r2.std())
    
    return model, metrics, X_test, y_test, y_pred


def save_model(model, metrics: dict):
    """保存模型和指标"""
    model_path = MODEL_DIR / "xgb_redox_model.pkl"
    metrics_path = MODEL_DIR / "metrics.json"
    
    joblib.dump(model, model_path)
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
    
    print(f"\n模型已保存: {model_path}")
    print(f"指标已保存: {metrics_path}")
    return model_path


def save_plots(y_test, y_pred, metrics):
    """生成并保存评估可视化图"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 1. 预测值 vs 真实值
    ax = axes[0]
    ax.scatter(y_test, y_pred, alpha=0.3, s=10, c="#4A90D9")
    lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
    ax.plot(lims, lims, "r--", linewidth=1.5, label="y = x")
    ax.set_xlabel("True Reduction Potential (V vs. vacuum)", fontsize=12)
    ax.set_ylabel("Predicted Reduction Potential (V vs. vacuum)", fontsize=12)
    ax.set_title(f"Prediction vs Ground Truth\nMAE={metrics['mae']:.4f}V  R²={metrics['r2']:.4f}", fontsize=13)
    ax.legend()
    ax.set_aspect("equal")
    
    # 2. 残差分布
    ax = axes[1]
    residuals = y_pred - y_test
    ax.hist(residuals, bins=60, color="#4A90D9", edgecolor="white", alpha=0.8)
    ax.axvline(0, color="red", linestyle="--", linewidth=1.5)
    ax.set_xlabel("Residual (V)", fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    ax.set_title(f"Residual Distribution\nMean={residuals.mean():.4f}  Std={residuals.std():.4f}", fontsize=13)
    
    plt.tight_layout()
    plot_path = MODEL_DIR / "evaluation.png"
    plt.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"评估图已保存: {plot_path}")
    return plot_path


def main():
    # 1. 加载数据
    print("=" * 60)
    print("OMEAD 氧化还原电位预测 MVP - 模型训练")
    print("=" * 60)
    
    df = load_omead()
    
    # 2. 准备特征
    X, y = prepare_data(df)
    
    # 3. 训练模型
    model, metrics, X_test, y_test, y_pred = train_model(X, y, do_cv=True)
    
    # 4. 保存模型
    save_model(model, metrics)
    
    # 5. 保存可视化
    save_plots(y_test, y_pred, metrics)
    
    print("\n" + "=" * 60)
    print("训练完成!")
    print("=" * 60)


if __name__ == "__main__":
    main()
