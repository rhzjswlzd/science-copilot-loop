# Counter-Intuitive Feature Discovery - Utilities

This directory contains shared utility functions for:

- **Feature selection & blocking** (`feature_selector.py`)
- **Model explainability** (`explainer.py`) - SHAP, LIME, permutation importance
- **Visualization** (`visualizer.py`) - Performance curves, SHAP plots, comparison charts
- **Evaluation metrics** (`metrics.py`) - MAPE, RMSE, R², custom domain metrics

## Usage Example

```python
from utils.feature_selector import FeatureBlocker
from utils.explainer import SHAPExplainer
from utils.visualizer import plot_feature_importance_comparison

# Block conventional features
blocker = FeatureBlocker(strategy='top_k', k=5)
X_blocked, blocked_features = blocker.fit_transform(X, y, conventional_features)

# Explain model
explainer = SHAPExplainer(model)
shap_values = explainer.explain(X_blocked)

# Visualize
plot_feature_importance_comparison(
    baseline_importance, 
    blocked_importance,
    save_path='outputs/comparison.png'
)
```

See individual module docstrings for detailed API documentation.
