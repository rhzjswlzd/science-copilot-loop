# 数据驱动的低估参数识别与机理验证

## 项目定位与科研价值

**本项目不是为了构建"最优预测模型"，而是为了发现被人类专家忽视的物理参数，并通过实验验证和机理研究形成闭环，实现真正的科学发现。**

### 核心理念

**传统机器学习建模往往依赖领域专家的经验选择特征**。这种方法虽然能够快速收敛到合理的预测性能，但也存在一个根本性局限：人类的经验本身可能成为探索的边界。工程师习惯性地关注那些"显而易见"的性能指标——容量、内阻、温度、循环次数等——这些指标在物理上确实与目标变量强相关，但也正因如此，基于这些指标的发现往往停留在"已知框架"内，难以突破现有认知。

**本项目提出一种"数据驱动的假说生成"策略**：通过主动屏蔽常规工程指标，迫使机器学习模型从次要特征、间接观测量或高阶交叉特征中寻找规律。这种设计的核心假设是，模型在失去"显而易见"的捷径后，可能会挖掘出被人类忽视的隐藏关联，**为后续的实验验证和机理研究提供线索**。

**为了最大化发现潜力，本项目采用渐进式特征探索策略**：

```
Level 1：人工特征（~25个）     → 受限于专家经验，但可解释性最强
Level 2：tsfresh 自动提取（700+）→ 突破特征选择的经验局限
Level 3：符号回归（无限搜索空间） → 突破特征形式的定义局限
```

其中，**tsfresh 作为当前阶段的核心特征引擎**，能够从原始时序信号中自动提取数百个统计量、频域特征、熵、非线性复杂度指标等，覆盖了远超人类直觉的特征空间。这使得"屏蔽常规指标后仍能发现有意义的模式"这一核心假设变得更加可行。

### 科研闭环

本项目是 **Science Copilot Loop** 的核心实践，连接了数据分析、实验设计和机理研究三个阶段：

```
Phase 2（本项目）：数据驱动发现
    ↓
【识别被低估的参数】
例：dQ/dV 偏度权重 > 容量衰减
    ↓
Phase 3：实验设计
    ↓
【设计针对性实验】
控制该参数，观察寿命变化
    ↓
Phase 4：机理探索
    ↓
【揭示物理机制】
为什么偏度重要？
→ 可能反映锂析出不均匀性
    ↓
【理论突破 / 新测量方法】
```

### 价值定位

**该方法的价值不仅在于预测性能的提升**，更在于"发现过程"本身。即使屏蔽常规指标后模型性能下降，那些仍能保持预测能力的非常规特征也值得深入研究——它们可能揭示了尚未被理论充分解释的物理机制，或者指向了全新的测量维度。

**具体而言**：
1. **缩小探索范围**：从数十个特征中筛选出 3-5 个"可疑线索"
2. **生成可验证假说**：机器学习权重 → 物理假设
3. **指导实验设计**：针对性实验而非盲目试错
4. **加速机理研究**：从数据触发灵感，而非仅靠直觉

---

## 认知边界与方法局限

### 三层突破与各自边界

本项目采用渐进式策略突破人类经验的局限。每一层都扩大了探索空间，但也有各自的边界：

#### Level 1：人工定义特征（当前基础）

手动提取约 25 个特征（容量、电压、dQ/dV 统计量等）。

- ✅ 能发现：dQ/dV 方差 > dQ/dV 均值（超出直觉的**排序**）
- ❌ 不能发现：time reversal asymmetry、CID complexity 等非常规统计量
- **边界**：特征池完全受限于专家经验

#### Level 2：tsfresh 自动特征提取（核心升级）

使用 [tsfresh](https://tsfresh.readthedocs.io/) 从原始时序信号中自动提取 **700+ 特征**，包括：

| 类别 | 示例特征 | 人类专家通常会想到？ |
|------|----------|---------------------|
| 基础统计量 | 均值、方差、偏度、峰度 | ✅ 会 |
| 频域特征 | FFT 系数、功率谱密度、频谱质心 | ⚠️ 偶尔 |
| 自相关特征 | 各阶 lag 的自相关系数、偏自相关 | ❌ 很少 |
| 非线性复杂度 | 近似熵、样本熵、CID complexity | ❌ 几乎不会 |
| 时间对称性 | Time reversal asymmetry statistic | ❌ 不会 |
| 分布特征 | Benford's Law 相关性、value counts | ❌ 不会 |
| 递归特征 | 递归图指标（recurrence rate, DET） | ❌ 不会 |

- ✅ 能发现：充放电曲线的近似熵与寿命的隐藏关联（人类不会主动计算的特征）
- ✅ 能发现：某个 lag 的自相关系数比容量衰减更能预测寿命
- ❌ 不能发现：`(dQ/dV 第3峰曲率)² × ln(温度梯度)` 这类全新数学形式
- **边界**：特征形式仍是预定义的数学模板，只是模板库足够大，覆盖了人类直觉之外的区域

**tsfresh 与屏蔽实验的结合**：tsfresh 提取的 700+ 特征中，绝大多数是人类专家不会主动关注的。这意味着即使不做屏蔽实验，tsfresh 本身就已经在探索"非常规特征空间"。而将 tsfresh 特征与屏蔽策略结合，可以进一步聚焦：在移除常规指标后，模型从 tsfresh 的非常规特征中选出的 top 特征，就是最值得深入研究的"反直觉线索"。

**tsfresh 的内置特征筛选**：tsfresh 提供 `select_features()` 方法，基于统计假设检验（Benjamini-Hochberg 校正）自动过滤与目标变量无显著关系的特征，将 700+ 特征缩减到几十个有统计意义的特征，避免过拟合。

#### Level 3：符号回归（未来方向）

使用符号回归（Symbolic Regression）自动搜索数学表达式，突破预定义模板的限制。

- ✅ 能发现：全新的数学形式，如 `f(x) = x₃² / (x₁ + log(x₇))`
- ✅ 能发现：多变量之间的非线性组合关系
- **边界**：搜索空间爆炸、计算成本高、结果不一定有物理意义
- **工具**：PySR、gplearn
- **策略**：不直接在原始数据上搜索，而是先用 tsfresh + 屏蔽实验缩小候选特征范围，再对 top 特征做符号回归，降低搜索复杂度

详见 [符号回归路线](#符号回归路线symbolic-regression-roadmap) 章节。

### 为什么这种渐进策略有价值？

1. **可追溯、可验证**：每一层的发现都能追溯到具体特征定义，可以查文献、做实验、指导实际
2. **渐进式探索**：从人工特征到 tsfresh 到符号回归，逐步扩大搜索空间，在可解释性和探索广度之间取得平衡
3. **层层聚焦**：每一层的输出缩小下一层的搜索范围（tsfresh 筛选 → 屏蔽实验聚焦 → 符号回归精炼）

---

## 设计思路

### 实验流程

整个实验采用对照实验设计，分为四个层次：

**特征提取（Feature Extraction）** 使用 tsfresh 从原始时序数据（充放电曲线、dQ/dV 曲线等）中自动提取 700+ 特征，并通过内置的 `select_features()` 进行统计显著性筛选，得到几十个与目标变量显著相关的候选特征。同时保留人工定义的常规工程指标，形成完整特征池。

**基线模型（Baseline Model）** 使用完整特征集（tsfresh 筛选特征 + 人工特征）建模，建立性能上限基准。通过特征重要性分析，将特征分为两类："常规工程指标"（人类专家通常优先考虑的特征）和 "tsfresh 非常规特征"（人类不太会主动关注的特征）。

**屏蔽模型（Blocked Model）** 在特征集中移除 top-K 常规工程指标后重新训练。这里的 K 值可以是固定的（如 top-5），也可以是动态的（移除累计重要性达到某一阈值的特征）。模型被迫从 tsfresh 提取的非常规特征中学习——这些特征涵盖了频域、熵、非线性复杂度等人类直觉之外的维度。

**解释与验证** 对屏蔽模型进行可解释性分析（SHAP、LIME），识别出新的关键特征。由于 tsfresh 特征具有明确的数学定义（如 `agg_autocorrelation(lag=5)` 或 `approximate_entropy(m=2, r=0.3)`），这些发现是**可追溯、可解释的**——可以回溯到具体的信号处理含义，进而通过文献调研、物理仿真或专家访谈验证其物理意义。

### 关键技术环节

| 环节 | 方法 | 目的 |
|------|------|------|
| **自动特征提取** | tsfresh `extract_features()` | 从时序信号中提取 700+ 候选特征 |
| **特征筛选** | tsfresh `select_features()` (Benjamini-Hochberg) | 过滤无关特征，保留统计显著特征 |
| **特征分组** | 人工标注 + 领域知识 | 区分"常规指标"与"非常规特征" |
| **Ablation Study** | 逐步移除特征组 | 量化常规指标的贡献，观察性能退化曲线 |
| **可解释性分析** | SHAP / LIME / Permutation Importance | 识别屏蔽后模型依赖的新特征 |
| **特征溯源** | tsfresh 特征名 → 数学定义 → 信号处理含义 | 将统计特征映射回物理可解释的概念 |
| **文献调研** | 文献数据库检索 | 判断新特征是否有理论支撑或实验依据 |
| **假说生成** | 物理推理 + 专家咨询 | 将统计关联转化为可验证的物理假说 |

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
├── feature_extraction/         # 特征提取引擎
│   ├── __init__.py
│   ├── tsfresh_extractor.py    # tsfresh 自动特征提取（700+ 特征）
│   ├── manual_features.py      # 人工定义的领域特征（兼容旧流程）
│   ├── feature_merger.py       # 合并 tsfresh + 人工特征
│   └── feature_labeler.py      # 自动/半自动标注常规 vs 非常规特征
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
├── symbolic_regression/        # 符号回归模块（Phase 2.5）
│   ├── __init__.py
│   ├── pysr_runner.py          # PySR 符号回归执行器
│   ├── expression_analyzer.py  # 表达式解析与物理解释
│   └── configs/
│       └── default.yaml        # 符号回归默认配置
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
    def get_time_series(self, df: pd.DataFrame) -> pd.DataFrame:
        """返回 tsfresh 格式的时序数据（id, time, value 列）
        用于 tsfresh 自动特征提取"""
        pass

    @abstractmethod
    def extract_manual_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """人工定义的领域特征（保留兼容性）"""
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

**tsfresh 特征提取流程**：

```python
from tsfresh import extract_features, select_features

# 1. 从原始时序数据提取 700+ 特征
ts_features = extract_features(
    timeseries_df,           # tsfresh 格式：id, time, value
    column_id="battery_id",
    column_sort="time"
)

# 2. 统计显著性筛选（Benjamini-Hochberg 校正）
relevant_features = select_features(
    ts_features,
    target,
    fdr_level=0.05           # 控制假发现率
)

# 3. 与人工特征合并，形成完整特征池
full_features = pd.concat([relevant_features, manual_features], axis=1)
```

**插件化设计的优势**：
1. **数据集切换简单**：只需修改配置文件中的 `dataset` 字段，无需改动实验代码
2. **双轨特征提取**：tsfresh 自动特征 + 人工领域特征并行，兼顾广度和领域知识
3. **特征定义可追溯**：tsfresh 特征有明确的数学定义，人工特征封装了领域知识
4. **易于扩展**：添加新数据集只需实现 5 个方法，符合开闭原则

### 实验配置示例

```yaml
# experiments/configs/blocked.yaml
dataset:
  plugin: battery_dataset          # 数据源插件名称
  params:
    data_path: /path/to/data/
    test_size: 0.2

feature_extraction:
  tsfresh:
    enabled: true                   # 启用 tsfresh 自动提取
    default_fc_parameters: "comprehensive"  # comprehensive / minimal / custom
    fdr_level: 0.05                 # select_features 的假发现率阈值
    n_jobs: 4                       # 并行计算核数
  manual:
    enabled: true                   # 同时保留人工特征
  merge_strategy: concat            # concat / tsfresh_only / manual_only

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

### Phase 2（数据分析）

1. **性能对比报告**：基线模型 vs 屏蔽模型的性能指标（MAPE、RMSE、R²）
2. **被低估的参数清单**（top-3 ~ top-5）：
   - 特征名称
   - SHAP 权重变化（屏蔽前 vs 屏蔽后）
   - 初步物理解释
3. **可视化图表**：
   - 性能退化曲线（随屏蔽特征数量变化）
   - SHAP 特征重要性对比（基线 vs 屏蔽）
   - 预测值散点图（评估屏蔽后泛化能力）
4. **可验证假说**：
   - 例："dQ/dV 偏度大 → 锂析出不均匀 → 寿命短"
   - 附文献调研证据

### Phase 3（实验验证）

设计针对性实验，控制被低估的参数，观察目标变量变化：
- 对照组：标准协议
- 实验组 A：增大该参数
- 实验组 B：减小该参数

### Phase 4（机理研究）

深入研究物理机制：
- 为什么该参数重要？
- 能否建立定量关系？
- 其他电池体系是否通用？

---

## 符号回归路线（Symbolic Regression Roadmap）

符号回归是本项目的 **Level 3 探索层**，目标是突破 tsfresh 预定义模板的限制，自动搜索全新的数学表达式。

### 为什么需要符号回归？

tsfresh 虽然提取了 700+ 特征，但每个特征都是一个**固定的数学模板**（如 `mean(x)`、`fft_coefficient(x, k=3)`）。符号回归则在**无限的数学表达式空间**中搜索，可能发现形如 `x₃² / (x₁ + log(x₇))` 的全新关系——这种关系不在任何预定义库中。

### 实施策略：tsfresh → 符号回归的流水线

符号回归的核心难题是搜索空间爆炸。本项目的策略是**用 tsfresh + 屏蔽实验的结果缩小搜索范围**，再精确搜索：

```
原始时序数据
    ↓
tsfresh 提取 700+ 特征
    ↓
屏蔽实验筛选出 top-5 非常规特征
    ↓
对 top-5 特征对应的原始子信号做符号回归
    ↓
发现新的数学表达式
    ↓
物理解释 + 实验验证
```

### 技术选型

| 工具 | 特点 | 适用场景 |
|------|------|----------|
| **PySR** | 基于遗传编程 + 模拟退火，支持自定义算子，Julia 后端速度快 | 首选工具，适合发现简洁的物理公式 |
| **gplearn** | scikit-learn 兼容的遗传编程，易集成 | 快速原型验证 |
| **神经网络 + 符号蒸馏** | 先用神经网络拟合，再用符号回归逼近 | 高维复杂关系 |

### 配置示例

```yaml
# symbolic_regression/configs/default.yaml
input:
  top_features: 5                  # 使用屏蔽实验筛选出的 top-N 特征
  source: blocked_experiment       # 从屏蔽实验结果中获取

pysr:
  niterations: 100                 # 搜索迭代次数
  binary_operators: ["+", "-", "*", "/"]
  unary_operators: ["log", "exp", "sqrt", "square"]
  maxsize: 20                      # 表达式最大复杂度
  populations: 30                  # 遗传算法种群数
  loss: "loss(prediction, target) = (prediction - target)^2"

output:
  pareto_front: true               # 输出复杂度-精度帕累托前沿
  top_expressions: 10              # 保留前 10 个候选表达式
```

### 预期产出

1. **帕累托前沿图**：表达式复杂度 vs 预测精度的权衡曲线
2. **候选公式清单**：数学表达式 + 预测性能 + 复杂度评分
3. **物理可解释性评估**：每个候选公式的量纲分析和物理意义初判

---

## 后续扩展方向

- **多数据集验证**：在电池、催化剂、材料合成等多个领域数据集上重复实验，验证方法普适性
- **实验验证闭环**：将"被低估的参数"作为新实验的设计依据，形成"发现-验证-迭代"闭环
- **因果推断**：使用因果发现算法（如 PC、GES）进一步分析新特征与目标变量的因果关系
- **交互式特征探索**：人机协同迭代，根据模型提示添加新特征

---

## 与纯机器学习方法的对比

| 维度 | 纯机器学习 | 本项目（手工特征） | 本项目（+ tsfresh） | 未来（+ 符号回归） |
|------|-----------|-------------------|---------------------|-------------------|
| **目标** | 预测性能最大化 | 发现新的研究方向 | 发现新的研究方向 | 发现新的数学关系 |
| **特征空间** | 尽可能多 | ~25 个（刻意限制） | 700+（自动扩展） | 无限（表达式搜索） |
| **人类经验依赖** | 高 | 高（特征选择受限） | 低（自动提取） | 极低（自动发现） |
| **可解释性** | 黑箱 | 高（SHAP + 物理推理） | 高（特征有数学定义） | 最高（显式公式） |
| **计算成本** | 中 | 低 | 中 | 高 |
| **科研价值** | 工程优化 | 科学发现 | 更广泛的科学发现 | 理论突破潜力 |

---

*设计理念：通过渐进式扩展特征探索空间（人工特征 → tsfresh 自动提取 → 符号回归），在可解释性和探索广度之间取得动态平衡。tsfresh 让我们突破了人类经验对特征选择的局限，符号回归则进一步突破了预定义数学模板对特征形式的局限。本项目不是终点，而是"数据驱动的假说生成器"，为后续的实验验证和机理研究提供起点。*
