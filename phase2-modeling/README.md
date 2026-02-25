# Phase 2: 仿真与设计

> Surrogate Modeling & UQ + Manual Experimentation

## 目标

利用统计学和机器学习进行预测，提供不确定性量化评估。

---

## 项目列表

### 2.1 锂电池循环寿命预测

**状态**：🚧 更新中

**数据来源**：Severson et al., Nature Energy, 2019

**详细记录**：[→ battery-lifecycle/](./battery-lifecycle/)

---

### 2.2 数据驱动的低估参数识别

**状态**：🎯 架构设计完成

**详细记录**：[→ counter-intuitive-discovery/](./counter-intuitive-discovery/)

---

### 2.3 有机分子氧化还原电位预测

**状态**：✅ 完成

**数据来源**：OMEAD — 26,218 个有机小分子 DFT 计算数据

**方法**：XGBoost + Morgan FP（MAE 0.372V）、Chemprop D-MPNN Ensemble（MAE 0.314V）

**详细记录**：[→ redox-potential-prediction/](./redox-potential-prediction/)
