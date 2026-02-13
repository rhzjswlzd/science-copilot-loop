# 项目 2.1: 算法基准测试

## 📋 概述

**在统一的数据集和特征工程框架下，对比不同机器学习算法的预测性能、可解释性和计算效率，旨在为特定科学问题筛选出最适合的建模方法，同时评估算法本身对物理洞察的贡献。**

本项目采用**可插拔数据源架构**，将数据加载与模型训练解耦，使得同一套算法评估流程可以快速应用于不同领域的数据集。

---

## 📂 子项目

### 2.1.1 Severson 数据集 (2019) ✅

**数据来源**：*Data-driven prediction of battery cycle life before capacity degradation* — Severson et al., Nature Energy, 2019

**实验设计**：
- **样本**：140 颗 LFP/石墨电池
- **目标**：前 100 圈预测循环寿命
- **特征**：ΔQ(V) 差分容量曲线（9个统计特征）+ 6个汇总特征

**已测试算法**：
- **Elastic Net**：MAPE 15.15%, R² 0.70, 训练时间 ~1s

**关键发现**：
- `capacity_fade_100`（前100圈容量衰减）是最重要的预测因子
- 不确定性量化（Gaussian Process）：95% 覆盖率 92.9%
- 发现 1 颗异常电池：早期指标正常但后期突然失效

📖 **[详细文档 →](./2.1.1-severson-dataset/README.md)**

---

### 2.1.2 Multi-Stage 数据集 (2024) 🚧

**数据来源**：*A Comprehensive Multi-Stage Lithium-Ion Battery Aging Dataset* — Kim et al., Nature Scientific Data, 2024

**实验设计**：
- **样本**：147 颗 Samsung INR21700-50E 循环老化电池
- **目标**：系统化操作条件组合的寿命预测
- **特征**：5个实验条件（Tamb, SOC, DOD, Cch, Cdch）+ 早期时序特征

**计划测试算法**：
- Elastic Net（基准）
- Random Forest
- XGBoost
- LSTM（时序建模）

**状态**：🚧 数据准备中

📖 **[详细文档 →](./2.1.2-multistage-dataset/README.md)**

---

## 🎯 未来规划

| 算法类别 | 候选方法 | 预期优势 | 适用场景 |
|----------|----------|----------|----------|
| **传统机器学习** | Random Forest, XGBoost, SVM | 非线性关系建模，特征交互捕捉 | 中等规模数据，需要特征重要性排序 |
| **深度学习** | LSTM, Transformer, GRU | 时序依赖学习，端到端特征提取 | 大规模时序数据，复杂动态系统 |
| **物理信息神经网络** | PINN (Physics-Informed NN) | 融合物理约束（如能量守恒、电荷平衡） | 数据稀缺但物理规律明确的场景 |
| **概率图模型** | Bayesian Network, Gaussian Process | 因果推断，不确定性量化 | 需要理解变量间因果关系 |
| **主动学习辅助** | Bayesian Optimization, Uncertainty Sampling | 高效实验设计，减少标注成本 | 实验成本高、需迭代优化参数 |

---

## 📚 参考文献

1. Severson, K.A., et al. (2019). Data-driven prediction of battery cycle life before capacity degradation. *Nature Energy*, 4, 383–391.
2. Kim, S., et al. (2024). A Comprehensive Multi-Stage Lithium-Ion Battery Aging Dataset. *Nature Scientific Data*, 11, 1247.
