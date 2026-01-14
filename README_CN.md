# **Science Copilot Loop (Centaur-AI4S)**

<div align="center">

  <a href="./README.md">
    <img src="https://img.shields.io/badge/English-En-blue?style=flat-square" alt="English">
  </a>
  <a href="./README_CN.md">
    <img src="https://img.shields.io/badge/中文-CN-red?style=flat-square" alt="Chinese">
  </a>

</div>

**跨越 AI 推理与湿实验的鸿沟。**

一套利用小样本数据和专家知识，务实加速科学发现的闭环工作流。

## **📖 项目简介 (Introduction)**

**Science-Copilot-Loop** 是一个专为科学发现（AI for Science）设计的\*\*"人机协同"（Human-in-the-loop）\*\*实操框架。

不同于追求完全自动化的"无人实验室"愿景，本项目立足于当下的技术现实，主张 **AI 算法与人类专家** 像拼图一样紧密咬合：

* **AI (蓝色拼图)**：负责高维数据压缩、广义文献调研、概率空间搜索（主动学习）。  
* **Human (黄色拼图)**：负责物理直觉判断、非结构化异常捕捉、实验伦理与安全边界把控。

这是一个不断迭代的**螺旋上升闭环**，旨在通过小样本主动学习（Active Learning）显著降低科研试错成本。

## **🧩 核心架构 (Core Workflow)**

本框架将科研过程拆解为四个核心阶段，强调 AI 与人类专家的交互与互补：

| 阶段 (Phase) | 🤖 AI Role (系统/算法) | 🧑‍🔬 Human Role (专家/实验) |
| :---- | :---- | :---- |
| **Phase 1: 调研与推理** | **Agent Reasoning** 利用 LLM Agent 进行文献挖掘与逻辑推理，生成初步方案。 | **Expert Knowledge** 提供领域知识（Domain Knowledge）、设定物理约束与初始假设。 |
| **Phase 2: 仿真与设计** | **Surrogate Modeling & UQ** 运行代理模型进行快速仿真，并提供不确定性量化（UQ）评估。 | **Manual Experimentation** 执行具体的湿实验（Wet-lab），记录物理现象。 |
| **Phase 3: 数据与审阅** | **Data Processing** 清洗多模态数据，进行特征提取与降维分析。 | **Review & Discussion** 审阅分析结果，捕捉“反常识”的异常点（Serendipity）。 |
| **Phase 4: 迭代与决策** | **Active Learning** 基于贝叶斯优化推荐下一组实验参数（Acquisition Function）。 | **Validation & Adjustment** 审查 AI 建议的可行性，调整最终实验队列。 |

## **📂 项目结构 (Directory Structure)**

为了贯彻“实操逻辑”，本项目建议采用以下标准化的目录结构，以规范数据流转：

science-copilot-loop/  
├── 📂 data/  
│   ├── 📂 raw/             \# 原始数据：存放人类记录的实验日志 (Excel/Images/Logs)  
│   ├── 📂 processed/       \# 清洗数据：AI 处理后的结构化数据 (CSV/JSON/Parquet)  
│   └── 📂 external/        \# 外部数据：参考文献 PDF、外部数据库导出的基准数据  
│  
├── 📂 models/  
│   ├── 📂 surrogates/      \# 代理模型权重 (e.g., Gaussian Processes, GNNs)  
│   └── 📂 agents/          \# AI Agent 的提示词工程 (Prompts) 与配置  
│  
├── 📂 experiments/         \# 实验记录归档 (按批次或日期命名)  
│   ├── exp\_20240101\_v1/  
│   └── exp\_20240115\_v2/  
│  
├── 📂 src/                 \# 核心源代码  
│   ├── data\_loader.py      \# 数据加载与标准化接口  
│   ├── active\_learning.py  \# 主动学习策略 (Acquisition Functions)  
│   └── visualization.py    \# 结果可视化工具  
│  
├── 📂 templates/           \# 人机交互协议模版  
│   ├── experiment\_log.xlsx \# 标准实验录入表 (供人类填写)  
│   └── config.yaml         \# 系统配置文件  
│  
├── 📄 README.md            \# 项目文档 (English)  
├── 📄 README\_CN.md         \# 项目文档 (Chinese)  
└── 📄 requirements.txt     \# 依赖库列表


## **📝 贡献指南 (Contributing)**

本项目欢迎任何形式的贡献，特别是来自一线实验人员的反馈！

具体内容会根据我的实践情况陆续更新
