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

一套利用机器学习预测，小样本数据学习，结合人类判断，加速科学发现的闭环工作流。

## **📖 项目简介 (Introduction)**

**Science-Copilot-Loop** 是一个专为科学发现（AI4S）设计的\*\*"人机协同"（Human-in-the-loop）\*\*实操框架。

不同于追求完全自动化的"无人实验室"愿景，本项目立足于当下的技术现实，主张 **AI 算法与人类专家** 像拼图一样紧密咬合：

* **AI (蓝色拼图)**：负责高维数据压缩、广义文献调研、概率空间搜索（主动学习）。  
* **Human (黄色拼图)**：负责物理直觉判断、非结构化异常捕捉、实验伦理与安全边界把控。

这是一个不断迭代的**螺旋上升闭环**，旨在通过统计学和机器学习预测来减少对传统模拟计算的依赖，以及小样本主动学习来降低科研试错成本。

## **🧩 核心架构 (Core Workflow)**

本框架将科研过程拆解为四个核心阶段，强调 AI 与人类专家的交互与互补：

| 阶段 (Phase) | 🤖 AI Role (系统/算法) | 🧑‍🔬 Human Role (专家/实验) |
| :---- | :---- | :---- |
| **Phase 1: 调研与推理** | **Agent Reasoning** 利用 LLM Agent 进行文献挖掘与逻辑推理，生成初步方案。 | **Expert Knowledge** 提供领域知识、设定物理约束与初始假设。 |
| **Phase 2: 仿真与设计** | **Surrogate Modeling & UQ** 统计性机器学习预测，并提供不确定性量化评估。 | **Manual Experimentation** 执行具体的湿实验（Wet-lab），记录物理现象。 |
| **Phase 3: 数据与审阅** | **Data Processing** 清洗多模态数据，进行特征提取与降维分析。 | **Review & Discussion** 审阅分析结果，捕捉“反常识”的异常点。 |
| **Phase 4: 迭代与决策** | **Active Learning** 基于贝叶斯优化推荐下一组实验参数。 | **Validation & Adjustment** 审查 AI 建议的可行性，调整最终实验队列。 |

## **📂 操作记录 **
1. Phase2操作记录
新仓库建立中
随时可能更新
