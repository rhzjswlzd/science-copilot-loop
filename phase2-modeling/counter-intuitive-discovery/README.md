# Counter-Intuitive Feature Discovery

## 项目背景与动机

**传统机器学习建模往往依赖领域专家的经验选择特征，这种方法虽然能够快速收敛到合理的预测性能，但也存在一个根本性局限**：人类的经验本身可能成为探索的边界。工程师习惯性地关注那些"显而易见"的性能指标——容量、内阻、温度、循环次数等——这些指标在物理上确实与目标变量强相关，但也正因如此，基于这些指标的发现往往停留在"已知框架"内，难以突破现有认知。

**本项目提出一种"反直觉探索"策略**：通过主动屏蔽常规工程指标，迫使机器学习模型从次要特征、间接观测量或高阶交叉特征中寻找规律。这种设计的核心假设是，模型在失去"显而易见"的捷径后，可能会挖掘出被人类忽视的隐藏关联，从而为领域专家提供新的研究方向和物理洞察。

**该方法的价值不仅在于预测性能的提升**，更在于"发现过程"本身。即使屏蔽常规指标后模型性能下降，那些仍能保持预测能力的非常规特征也值得深入研究——它们可能揭示了尚未被理论充分解释的物理机制，或者指向了全新的测量维度。

---

## 设计思路

### 实验流程

整个实验采用对照实验设计，分为三个层次：

**基线模型（Baseline Model）** 使用完整特征集建模，包括所有常规工程指标和衍生特征。该模型的作用是建立性能上限基准，并通过特征重要性分析识别出"常规工程指标"（即人类专家通常优先考虑的特征）。

**屏蔽模型（Blocked Model）** 在特征集中移除 top-K 常规工程指标后重新训练。这里的 K 值可以是固定的（如 top-5），也可以是动态的（移除累计重要性达到某一阈值的特征）。模型被迫从剩余特征中学习，这些特征通常包括原始信号的统计量、频域特征、曲线形状描述符等。

**解释与验证** 对屏蔽模型进行可解释性分析（SHAP、LIME），识别出新的关键特征。随后通过文献调研、物理仿真或专家访谈，验证这些特征是否具有可解释的物理意义，或是否指向了未被充分研究的现象。

### 关键技术环节

| 环节 | 方法 | 目的 |
|------|------|------|
| **特征分组** | 人工标注 + 领域知识 | 区分"常规指标"与"隐藏特征" |
| **Ablation Study** | 逐步移除特征组 | 量化常规指标的贡献，观察性能退化曲线 |
| **可解释性分析** | SHAP / LIME / Permutation Importance | 识别屏蔽后模型依赖的新特征 |
| **物理验证** | 文献调研 + 专家咨询 | 判断新特征是否有理论支撑或实验依据 |

---

## 系统架构

**本项目采用模块化设计，核心原则是将数据源与建模流程解耦**，使得同一套实验框架可以无缝切换到不同的科学领域数据集（电池、材料、催化剂等）。

### 架构图

```
counter-intuitive-discovery/
│
├── data_sources/               # 数据源插件（可插拔）
│   ├── __init__.py
│   ├── base.py                 # 抽象基类（定义统一接口）
│   ├── battery_dataset.py      # 电池数据集插件
│   ├── material_dataset.py     # 材料数据集插件（示例）
│   └── custom_dataset.py       # 用户自定义数据集模板
│
├── experiments/                # 实验配置与执行
│   ├── configs/                # YAML 配置文件
│   │   ├── baseline.yaml       # 基线模型配置
│   │   └── blocked.yaml        # 屏蔽模型配置
│   ├── run_baseline.py         # 运行基线实验
│   ├── run_blocked.py          # 运行屏蔽实验
│   └── compare.py              # 对比分析脚本
│
├── models/                     # 模型定义
│   ├── __init__.py
│   ├── elastic_net.py          # Elastic Net 回归
│   ├── random_forest.py        # Random Forest
│   └── neural_net.py           # 简单神经网络（可选）
│
├── utils/                      # 工具函数
│   ├── feature_selector.py     # 特征选择与屏蔽逻辑
│   ├── explainer.py            # SHAP/LIME 包装器
│   ├── visualizer.py           # 绘图工具
│   └── metrics.py              # 评估指标（MAPE、R²等）
│
├── outputs/                    # 实验输出（自动生成）
│   ├── baseline/               # 基线模型结果
│   ├── blocked/                # 屏蔽模型结果
│   └── comparison/             # 对比分析图表
│
└── README.md                   # 本文件
```

### 数据源插件接口

**所有数据集插件必须继承 `BaseDataset` 抽象类**，并实现以下方法：

```python
class BaseDataset(ABC):
    @abstractmethod
    def load_raw_data(self) -> pd.DataFrame:
        """加载原始数据"""
        pass
    
    @abstractmethod
    def extract_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """特征工程"""
        pass
    
    @abstractmethod
    def get_target(self, df: pd.DataFrame) -> np.ndarray:
        """提取目标变量"""
        pass
    
    @abstractmethod
    def label_conventional_features(self) -> List[str]:
        """标注哪些特征是"常规工程指标"（需要屏蔽的）"""
        pass
```

**插件化设计的优势**：
1. **数据集切换简单**：只需修改配置文件中的 `dataset` 字段，无需改动实验代码
2. **特征定义可追溯**：每个数据集插件内部封装了领域知识（哪些是常规指标）
3. **易于扩展**：添加新数据集只需实现 4 个方法，符合开闭原则

### 实验配置示例

```yaml
# experiments/configs/blocked.yaml
dataset:
  plugin: battery_dataset          # 数据源插件名称
  params:
    data_path: /path/to/data/
    test_size: 0.2

feature_blocking:
  strategy: top_k                  # 屏蔽策略：top_k 或 threshold
  k: 5                              # 移除重要性排名前 5 的常规指标
  # threshold: 0.7                 # 或移除累计重要性达 70% 的特征

model:
  type: elastic_net
  params:
    alpha: 0.1
    l1_ratio: 0.3

explainability:
  methods: [shap, permutation]     # 可解释性方法
  shap_samples: 100                 # SHAP 采样数
```

---

## 预期产出

1. **对比报告**：基线模型 vs 屏蔽模型的性能指标（MAPE、RMSE、R²）
2. **特征发现清单**：屏蔽后模型依赖的非常规特征，附 SHAP 值和物理解释
3. **可视化图表**：
   - 性能退化曲线（随屏蔽特征数量变化）
   - SHAP 特征重要性对比（基线 vs 屏蔽）
   - 预测值散点图（评估屏蔽后泛化能力）
4. **物理洞察**：对新发现特征的文献调研结果或假说

---

## 后续扩展方向

- **多数据集验证**：在电池、催化剂、材料合成等多个领域数据集上重复实验，验证方法普适性
- **主动学习结合**：将"反直觉特征"作为新实验的测量维度，形成"发现-验证-迭代"闭环
- **因果推断**：使用因果发现算法（如 PC、GES）进一步分析新特征与目标变量的因果关系

---

*设计理念：通过刻意限制模型的"视野"，迫使其从非常规角度重新审视问题，从而为人类专家提供新的研究线索。*
