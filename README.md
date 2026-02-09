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

**在科学研究中，机器学习模型通常被视为"黑盒预测器"**，其价值局限于提供数值结果。然而，模型的真正潜力不仅在于预测本身，更在于其学习过程中揭示的特征依赖关系——这些关系可能指向被人类忽视的物理机制或测量维度。本阶段的两个项目分别从"正向验证"和"反向探索"两个角度，展示如何通过机器学习辅助科学发现。

## 实操记录

### 项目 2.1：锂电池循环寿命预测

**该项目验证了机器学习在传统特征工程框架下的预测能力**，同时通过不确定性量化识别出模型难以解释的异常样本，为后续深入研究提供线索。

**数据来源**：*Data-driven prediction of battery cycle life before capacity degradation* — Severson et al., Nature Energy, 2019

**数据集规模**：

| 项目 | 数值 |
|------|------|
| 文件数 | 140 个 JSON（140颗电池） |
| 总大小 | 26.03 GB |

**方法概要**：

1. 特征工程：提取 ΔQ(V) = Q₁₀₀(V) - Q₁₀(V) 差分容量曲线
2. 统计特征：9 个（variance, min, max, mean, skewness, kurtosis, range, std, abs_mean）
3. 汇总特征：6 个（温度、内阻、充电时长、容量衰减等）
4. 模型：Elastic Net 回归（α=0.1, l1_ratio=0.3）

**结果**：

| 指标 | 值 |
|------|-----|
| MAPE | 15.15% |
| RMSE | 154.9 cycles |
| R² | 0.70 |

**模型方程**：
```
log(寿命) = 6.49 - 0.097×capacity_fade_100 + 0.077×dQ_minimum - 0.073×dQ_std + ...
```

**不确定性量化（GP）**：95% Coverage = 92.9%

**关键发现**：
1. `capacity_fade_100` 是最重要特征，符合工程直觉
2. 发现一颗异常电池：预测 1185 圈，实际 538 圈 → 潜在未知衰减机理

**状态**：🚧 更新中

**详细记录**：[→ phase2-modeling/battery-lifecycle/](./phase2-modeling/battery-lifecycle/)

---

### 项目 2.2：反直觉特征发现（Counter-Intuitive Feature Discovery）

**与传统建模相反，该项目通过主动屏蔽"显而易见"的工程指标，迫使模型从非常规特征中寻找规律**，旨在发现被人类经验框架忽视的隐藏关联。

**核心动机**：传统机器学习建模往往依赖领域专家的经验选择特征（如容量、内阻、温度等），这种方法虽然高效，但也将探索空间限制在"已知框架"内。通过刻意移除这些常规指标，模型被迫从次要特征、间接观测量或高阶交叉特征中学习，可能揭示出尚未被理论充分解释的物理机制。

**设计思路**：

| 实验类型 | 特征集 | 目的 |
|----------|--------|------|
| **基线模型** | 完整特征（包括常规工程指标） | 建立性能上限，识别"常规特征" |
| **屏蔽模型** | 移除 top-K 常规指标后的剩余特征 | 发现非常规预测路径 |
| **解释验证** | SHAP/LIME 分析 + 文献调研 | 判断新特征是否有物理意义 |

**技术架构**：

该项目采用**可插拔数据源设计**，将数据加载、特征工程和领域知识（"哪些是常规指标"）封装为独立模块。所有数据集插件遵循统一接口（`BaseDataset`），使得同一套实验框架可以无缝应用于不同科学领域（电池、材料、催化剂等）。

**预期产出**：
1. 性能对比报告（基线 vs 屏蔽）
2. 非常规特征清单及其物理解释
3. 可视化：特征重要性对比、性能退化曲线

**应用场景**：
- 探索新的测量维度或实验参数
- 挑战现有理论框架的完备性
- 为主动学习提供"下一步实验"的设计灵感

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
