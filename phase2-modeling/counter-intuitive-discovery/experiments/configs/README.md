# Experiment Configuration Files

This directory contains YAML configuration files for different experimental setups.

## Quick Start

1. **Baseline Experiment** (use all features):
   ```bash
   python ../run_baseline.py --config configs/baseline.yaml
   ```

2. **Blocked Experiment** (remove conventional features):
   ```bash
   python ../run_blocked.py --config configs/blocked.yaml
   ```

3. **Comparison Analysis**:
   ```bash
   python ../compare.py --baseline outputs/baseline/ --blocked outputs/blocked/
   ```

## Configuration Structure

```yaml
dataset:
  plugin: <dataset_plugin_name>      # e.g., battery_dataset
  params:
    data_path: <path>
    # ... plugin-specific parameters

feature_blocking:
  strategy: top_k | threshold        # How to select features to block
  k: <int>                           # (if top_k) Number of top features to remove
  threshold: <float>                 # (if threshold) Cumulative importance threshold

model:
  type: <model_name>                 # e.g., elastic_net, random_forest
  params:
    # ... model-specific hyperparameters

explainability:
  methods: [shap, permutation, lime] # Explainability techniques
  shap_samples: <int>                # Number of samples for SHAP
```

## Example Configs

See `baseline.yaml` and `blocked.yaml` for templates.
