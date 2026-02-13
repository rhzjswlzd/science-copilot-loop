# **Science Copilot Loop (Centaur-AI4S)**

<div align="center">

  <a href="./README_EN.md">
    <img src="https://img.shields.io/badge/English-En-blue?style=flat-square" alt="English">
  </a>
  <a href="./README.md">
    <img src="https://img.shields.io/badge/中文-CN-red?style=flat-square" alt="Chinese">
  </a>

</div>

一套利用机器学习预测、小样本数据学习，结合人类判断，加速科学发现的闭环工作流。

![AI4S Practical Workflow](./images/ai4s-workflow-diagram.png)

## 📖 项目简介

**Science-Copilot-Loop** 是一个专为科学发现（AI4S）设计的"人机协同"（Human-in-the-loop）实操框架。

不同于追求完全自动化的"无人实验室"愿景，本项目立足于当下的技术现实，主张 **AI 算法与人类专家** 像拼图一样紧密咬合：

* **AI (蓝色拼图)**：负责高维数据压缩、广义文献调研、概率空间搜索（主动学习）。  
* **Human (黄色拼图)**：负责物理直觉判断、非结构化异常捕捉、实验伦理与安全边界把控。

---

## 🧩 核心架构

本框架将科研过程拆解为四个核心阶段，强调 AI 与人类专家的交互与互补：

| 阶段 | 🤖 AI Role | 🧑‍🔬 Human Role | 实操记录 |
| :---- | :---- | :---- | :---- |
| **Phase 1: 调研与推理** | Agent Reasoning（文献挖掘与逻辑推理） | Expert Knowledge（领域知识与初始假设） | [→ 查看](#-phase-1-调研与推理) |
| **Phase 2: 仿真与设计** | Surrogate Modeling & UQ（机器学习预测与不确定性量化） | Manual Experimentation（湿实验执行） | [→ 查看](#-phase-2-仿真与设计) |
| **Phase 3: 数据与审阅** | Data Processing（数据清洗与特征提取） | Review & Discussion（异常点捕捉） | [→ 查看](#-phase-3-数据与审阅) |
| **Phase 4: 迭代与决策** | Active Learning（贝叶斯优化推荐实验参数） | Validation & Adjustment（可行性审查） | [→ 查看](#-phase-4-迭代与决策) |

---

## 📂 仓库结构

```
science-copilot-loop/
├── README.md                    # 中文说明（本文件）
├── README_EN.md                 # English version
├── images/                      # 图片资源
│   └── ai4s-workflow-diagram.png
│
├── phase1-research/             # 阶段1：调研与推理
│   ├── README.md                # 阶段说明与实操记录
│   ├── multi-paper-analysis/    # 多论文综合分析
│   │   └── ...
│   └── literature-tools/        # 文献处理工具笔记
│       └── ...
│
├── phase2-modeling/                    # 阶段2：仿真与设计
│   ├── README.md                       # 阶段说明与实操记录
│   ├── battery-lifecycle/              # 电池寿命预测项目
│   │   └── ...
│   ├── counter-intuitive-discovery/    # 反直觉特征发现
│   │   ├── data_sources/               # 可插拔数据源模块
│   │   ├── experiments/                # 实验配置与执行
│   │   ├── models/                     # 模型定义
│   │   └── utils/                      # 工具函数
│   └── ...
│
├── phase3-data/                 # 阶段3：数据与审阅
│   ├── README.md                # 阶段说明与实操记录
│   └── ...
│
└── phase4-iteration/            # 阶段4：迭代与决策
    ├── README.md                # 阶段说明与实操记录
    └── ...
```

---

# 📘 Phase 1: 调研与推理

> **目标**：利用 AI Agent 进行文献挖掘与逻辑推理，结合专家知识生成初步方案

## 实操记录

### 项目 1.1：多论文综合分析系统

**背景**：单篇论文信噪比较低，需要将多篇论文放在一起进行跨论文综合分析。

**设计思路**：

| 方案 | 描述 | 优缺点 |
|------|------|--------|
| A. 长上下文直灌 | 全部论文喂给长上下文模型 | 简单但成本高，难追溯 |
| B. 分层摘要+综合 | 先结构化摘要，再主题聚类 | 可控可追溯，推荐✅ |
| C. 知识图谱+RAG | 提取三元组构建图谱 | 结构化但实现复杂 |

**工具选型**：

| 工具 | Stars | 用途 |
|------|-------|------|
| [MinerU](https://github.com/opendatalab/MinerU) | 53.8k | PDF → Markdown/JSON，专为 AI4S 设计 |
| [Marker](https://github.com/datalab-to/marker) | 31.5k | 高速高精度 PDF 转换 |
| [GROBID](https://github.com/grobidOrg/grobid) | 4.6k | 学术论文结构化提取 |

**状态**：📋 设计中

**详细记录**：[→ phase1-research/multi-paper-analysis/](./phase1-research/multi-paper-analysis/)

---

# 🔬 Phase 2: 仿真与设计

> **目标**：利用统计学和机器学习进行预测，提供不确定性量化评估

**在科学研究中，机器学习模型通常被视为"黑盒预测器"**，其价值局限于提供数值结果。然而，模型的真正潜力不仅在于预测本身，更在于其学习过程中揭示的特征依赖关系——这些关系可能指向被人类忽视的物理机制或测量维度。本阶段的两个项目从**算法选择**和**特征选择**两个正交维度出发，系统性地探索机器学习辅助科学发现的路径。

## 实操记录

### 项目 2.1：算法基准测试（Algorithm Benchmarking）

**该项目在统一的数据集和特征工程框架下，对比不同机器学习算法的预测性能、可解释性和计算效率**，旨在为特定科学问题筛选出最适合的建模方法，同时评估算法本身对物理洞察的贡献。

**设计思路**：

本项目采用**可插拔数据源架构**（与项目 2.2 共享），将数据加载与模型训练解耦，使得同一套算法评估流程可以快速应用于不同领域的数据集。核心实验流程包括：(1) 在统一特征集上训练多种算法；(2) 对比预测性能（MAPE、R²）与计算开销；(3) 通过可解释性分析（SHAP、特征重要性）评估算法对物理洞察的贡献；(4) 使用不确定性量化（UQ）识别模型难以解释的异常样本。

**当前进展**：**锂电池循环寿命预测**

- **数据来源**：*Data-driven prediction of battery cycle life before capacity degradation* — Severson et al., Nature Energy, 2019
- **数据集规模**：140 颗电池，26.03 GB
- **特征工程**：提取 ΔQ(V) = Q₁₀₀(V) - Q₁₀(V) 差分容量曲线，计算 9 个统计特征 + 6 个汇总特征（温度、内阻、充电时长等）

**已测试算法**：

| 算法 | MAPE | R² | 训练时间 | 可解释性 | 关键发现 |
|------|------|-----|----------|----------|----------|
| **Elastic Net** | 15.15% | 0.70 | ~1s | ✅ 线性权重 | `capacity_fade_100` 最重要，符合工程直觉 |

**模型方程示例**（Elastic Net）：
```
log(寿命) = 6.49 - 0.097×capacity_fade_100 + 0.077×dQ_minimum - 0.073×dQ_std + ...
```

**不确定性量化**（Gaussian Process）：95% Coverage = 92.9%，发现一颗异常电池（预测 1185 圈，实际 538 圈）→ 潜在未知衰减机理

**未来规划**：

| 算法类别 | 候选方法 | 预期优势 | 适用场景 |
|----------|----------|----------|----------|
| **传统机器学习** | Random Forest, XGBoost, SVM | 非线性关系建模，特征交互捕捉 | 中等规模数据，需要特征重要性排序 |
| **深度学习** | LSTM, Transformer, GRU | 时序依赖学习，端到端特征提取 | 大规模时序数据，复杂动态系统 |
| **物理信息神经网络** | PINN (Physics-Informed NN) | 融合物理约束（如能量守恒、电荷平衡） | 数据稀缺但物理规律明确的场景 |
| **概率图模型** | Bayesian Network, Gaussian Process | 因果推断，不确定性量化 | 需要理解变量间因果关系 |
| **主动学习辅助** | Bayesian Optimization, Uncertainty Sampling | 高效实验设计，减少标注成本 | 实验成本高、需迭代优化参数 |

**架构设计**：

所有算法实验共享相同的数据源接口（`BaseDataset`），并通过统一的评估脚本输出标准化报告。算法模块遵循 scikit-learn 接口（`fit` / `predict`），便于快速集成新方法。

**状态**：✅ Elastic Net 基准完成，🎯 其他算法待实现

**详细记录**：[→ phase2-modeling/battery-lifecycle/](./phase2-modeling/battery-lifecycle/)

---

### 项目 2.2：数据驱动的低估参数识别与机理验证

**本项目不是为了构建"最优预测模型"，而是为了发现被人类专家忽视的物理参数，并通过实验验证和机理研究形成闭环，实现真正的科学发现。**

**核心理念**：传统机器学习建模往往依赖领域专家的经验选择特征（如容量、内阻、温度等），这种方法虽然高效，但也将探索空间限制在"已知框架"内。通过刻意移除这些常规指标，模型被迫从次要特征、间接观测量或高阶交叉特征中学习，**为后续的实验验证和机理研究提供线索**。

**科研闭环**（Science Copilot Loop）：

```
Phase 2（数据驱动发现）
    ↓
识别被低估的参数
    ↓
Phase 3（实验设计）
    ↓
设计针对性实验
    ↓
Phase 4（机理探索）
    ↓
揭示物理机制
    ↓
理论突破 / 新测量方法
```

**设计思路**：

| 阶段 | 方法 | 产出 |
|------|------|------|
| **基线模型** | 完整特征（包括常规工程指标） | 识别"常规特征"，建立性能基准 |
| **屏蔽模型** | 移除 top-K 常规指标后的剩余特征 | 发现被低估的参数（3-5个候选） |
| **假说生成** | SHAP 分析 + 文献调研 | 可验证的物理假说 |
| **实验验证** | 针对性实验（Phase 3） | 验证假说，控制参数观察目标变化 |
| **机理研究** | 深入分析（Phase 4） | 揭示物理本质，理论突破 |

**价值定位**：
- ✅ 缩小探索范围（数十个特征 → 3-5个线索）
- ✅ 生成可验证假说（机器学习权重 → 物理假设）
- ✅ 指导实验设计（针对性实验而非盲目试错）
- ✅ 加速机理研究（数据触发灵感）

**认知边界**：本项目仍受限于人类定义的特征空间（25个统计特征），但在现有框架内能够发现"被低估的维度"，为后续突破提供起点。

**状态**：🎯 架构设计完成，待数据集实现

**详细记录**：[→ phase2-modeling/counter-intuitive-discovery/](./phase2-modeling/counter-intuitive-discovery/)

---

# 📊 Phase 3: 数据与审阅

> **目标**：清洗多模态数据，进行特征提取与降维分析，审阅结果捕捉异常

## 实操记录

*暂无项目，待补充...*

---

# 🔄 Phase 4: 迭代与决策

> **目标**：基于贝叶斯优化推荐下一组实验参数，人工审查可行性

## 实操记录

*暂无项目，待补充...*

---

## 📚 参考资料

- [MinerU - PDF 提取工具](https://github.com/opendatalab/MinerU)
- [Severson et al., Nature Energy, 2019](https://www.nature.com/articles/s41560-019-0356-8)
- [BEEP - 电池数据处理工具](https://github.com/TRI-AMDD/beep)

---

## 📝 License

MIT License - 自由使用、修改和分享

---

*Created with curiosity 🦊*
