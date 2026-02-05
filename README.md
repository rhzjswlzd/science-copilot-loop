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
├── phase2-modeling/             # 阶段2：仿真与设计
│   ├── README.md                # 阶段说明与实操记录
│   ├── battery-lifecycle/       # 电池寿命预测项目
│   │   └── ...
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

## 实操记录

### 项目 2.1：锂电池循环寿命预测

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
