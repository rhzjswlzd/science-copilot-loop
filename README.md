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

A pragmatic framework accelerating scientific discovery using small-sample data and expert knowledge.
![AI4S Practical Workflow](./images/workflow-diagram.png)

## **📖 Introduction**

**Science-Copilot-Loop** is a practical **"Human-in-the-loop"** framework designed for AI for Science (AI4S).

Unlike the vision of fully automated "unmanned laboratories," this project is grounded in current technological realities. It advocates for a puzzle-like integration of **AI Algorithms** and **Human Experts**:

* **AI (Blue Piece)**: Handles high-dimensional data compression, generalized literature research, and probabilistic space search (Active Learning).  
* **Human (Yellow Piece)**: Handles physical intuition, captures unstructured anomalies, and ensures ethical/safety boundaries.

This is an iterative **upward spiral loop**, designed to significantly reduce trial-and-error costs in research through **Active Learning**.

## **🧩 Core Workflow**

The framework decomposes the scientific process into four core phases, emphasizing the interaction between AI and human experts:

| Phase | 🤖 AI Role (System/Algo) | 🧑‍🔬 Human Role (Expert/Lab) |
| :---- | :---- | :---- |
| **Phase 1: Research & Reasoning** | **Agent Reasoning** Uses LLM Agents for literature mining and logical deduction to generate initial proposals. | **Expert Knowledge** Provides domain knowledge, sets physical constraints, and defines initial hypotheses. |
| **Phase 2: Simulation & Design** | **Surrogate Modeling & UQ** Runs surrogate models for rapid simulation and provides Uncertainty Quantification (UQ). | **Manual Experimentation** Executes specific wet-lab experiments and records physical phenomena. |
| **Phase 3: Data & Review** | **Data Processing** Cleans multimodal data and performs feature extraction/dimensionality reduction. | **Review & Discussion** Reviews analysis results to capture "counter-intuitive" anomalies (Serendipity). |
| **Phase 4: Iteration & Decision** | **Active Learning** Recommends the next set of experimental parameters based on Bayesian Optimization (Acquisition Function). | **Validation & Adjustment** Validates the feasibility of AI suggestions and adjusts the final experimental queue. |

## **📂 Directory Structure**

To enforce the "Practical Logic," we recommend the following standardized directory structure:

science-copilot-loop/  
├── 📂 data/  
│   ├── 📂 raw/             \# Raw Data: Human-recorded logs (Excel/Images)  
│   ├── 📂 processed/       \# Cleaned Data: AI-processed structured data (CSV/JSON)  
│   └── 📂 external/        \# External Data: References, PDFs, Benchmark data  
│  
├── 📂 models/  
│   ├── 📂 surrogates/      \# Surrogate Model Weights (e.g., Gaussian Processes)  
│   └── 📂 agents/          \# AI Agent Prompts and Configurations  
│  
├── 📂 experiments/         \# Archived Experiment Logs (by Batch/Date)  
│   ├── exp\_20240101\_v1/  
│   └── exp\_20240115\_v2/  
│  
├── 📂 src/                 \# Source Code  
│   ├── data\_loader.py      \# Data Loading & Standardization  
│   ├── active\_learning.py  \# Acquisition Functions strategy  
│   └── visualization.py    \# Visualization Tools  
│  
├── 📂 templates/           \# Protocol Templates  
│   ├── experiment\_log.xlsx \# Standard Entry Form (For Humans)  
│   └── config.yaml         \# System Config  
│  
├── 📄 README.md            \# Project Documentation (English)  
├── 📄 README\_CN.md         \# Project Documentation (Chinese)  
└── 📄 requirements.txt     \# Dependencies


## **📝 Contributing**

Contributions are welcome, especially feedback from frontline experimentalists\!

The specific content will be updated gradually based on my practical experience\
