# **Science Copilot Loop (Centaur-AI4S)**

<div align="center">

  <a href="./README.md">
    <img src="https://img.shields.io/badge/English-En-blue?style=flat-square" alt="English">
  </a>
  <a href="./README_CN.md">
    <img src="https://img.shields.io/badge/中文-CN-red?style=flat-square" alt="Chinese">
  </a>

</div>

**Bridging the gap between AI inference and wet-lab experiments.**

A pragmatic framework accelerating scientific discovery using machine learning for prediction, small-sample data and expert knowledge.
![AI4S Practical Workflow](./images/ai4s-workflow-diagram.png)

## **📖 Introduction**

**Science-Copilot-Loop** is a practical **"Human-in-the-loop"** framework designed for AI for Science (AI4S).

Unlike the vision of fully automated "unmanned laboratories," this project is grounded in current technological realities. It advocates for a puzzle-like integration of **AI Algorithms** and **Human Experts**:

* **AI (Blue Piece)**: Handles high-dimensional data compression, generalized literature research, and probabilistic space search (Active Learning).  
* **Human (Yellow Piece)**: Handles physical intuition, captures unstructured anomalies, and ensures ethical/safety boundaries.

This is an iterative **upward spiral loop**, designed to significantly reduce reliance on traditional simulation computing through statistical and machine learning predictions, as well as small sample active learning to lower research trial and error costs.

## **🧩 Core Workflow**

The framework decomposes the scientific process into four core phases, emphasizing the interaction between AI and human experts:

| Phase | 🤖 AI Role (System/Algo) | 🧑‍🔬 Human Role (Expert/Lab) |
| :---- | :---- | :---- |
| **Phase 1: Research & Reasoning** | **Agent Reasoning** Uses LLM Agents for literature mining and logical deduction to generate initial proposals. | **Expert Knowledge** Provides domain knowledge, sets physical constraints, and defines initial hypotheses. |
| **Phase 2: Simulation & Design** | **Surrogate Modeling & UQ** Statistical machine learning prediction and provides Uncertainty Quantification (UQ). | **Manual Experimentation** Executes specific wet-lab experiments and records physical phenomena. |
| **Phase 3: Data & Review** | **Data Processing** Cleans multimodal data and performs feature extraction/dimensionality reduction. | **Review & Discussion** Reviews analysis results to capture "counter-intuitive" anomalies (Serendipity). |
| **Phase 4: Iteration & Decision** | **Active Learning** Recommends the next set of experimental parameters based on Bayesian Optimization (Acquisition Function). | **Validation & Adjustment** Validates the feasibility of AI suggestions and adjusts the final experimental queue. |

## **📂 Operation log**
1. Phase 2 operation record
New warehouse under construction
May be updated at any time
