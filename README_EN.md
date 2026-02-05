# **Science Copilot Loop (Centaur-AI4S)**

<div align="center">

  <a href="./README_EN.md">
    <img src="https://img.shields.io/badge/English-En-blue?style=flat-square" alt="English">
  </a>
  <a href="./README.md">
    <img src="https://img.shields.io/badge/中文-CN-red?style=flat-square" alt="Chinese">
  </a>

</div>


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

---

## **📂 Project 1: Battery Cycle Life Prediction**

**Data Source**: *Data-driven prediction of battery cycle life before capacity degradation* — Severson et al., Nature Energy, 2019

### Dataset Overview

| Item | Value |
|------|-------|
| Files | 140 JSON (one per battery) |
| Total Size | 26.03 GB |
| Avg per File | 190 MB |

### Methodology

1. **Feature Engineering**: Extract ΔQ(V) = Q₁₀₀(V) - Q₁₀(V) from discharge curves
2. **Statistical Features**: variance, min, max, mean, skewness, kurtosis, range, std (9 features)
3. **Summary Features**: temperature, resistance, charge time, capacity fade (6 features)
4. **Model**: Elastic Net Regression (α=0.1, l1_ratio=0.3)

### Results

| Metric | Value |
|--------|-------|
| MAPE | 15.15% |
| RMSE | 154.9 cycles |
| R² | 0.70 |

### Key Findings

1. `capacity_fade_100` (capacity fade in first 100 cycles) is the most important feature — aligns with engineering intuition
2. One anomalous battery: predicted 1185 cycles, actual 538 cycles — potential hidden degradation mechanism worth investigating

### Uncertainty Quantification (Gaussian Process)

| Metric | Value |
|--------|-------|
| 95% Coverage | 92.9% |
| Calibration Error | 2.1% |

---

*More projects coming soon...*
