# Current Architecture Document Template

This template defines the structure for the Current Architecture Document - the single source of truth for the production system.

---

## Document Structure

```markdown
# Current Architecture

Last Updated: [DATE]
Last Validated Experiment: [EXPERIMENT-ID]
Production Metric: [METRIC VALUE]

---

## 1. Model Architecture

### Base Model
- Model Type: [e.g., XGBoost, ResNet50, BERT]
- Framework: [PyTorch/TensorFlow/scikit-learn/etc.]
- Pretrained Weights: [source/version if applicable]

### Architecture Modifications
- [List any modifications from base]
- [Custom layers, heads, etc.]

### Model Configuration
```yaml
[Key hyperparameters and config]
```

---

## 2. Training Pipeline

### Data Loading
- Dataset: [path/source]
- Loader: [DataLoader config]
- Batch Size: [value]
- Workers: [value]

### Training Configuration
- Optimizer: [type + params]
- Scheduler: [type + params]
- Loss Function: [type]
- Epochs: [value]
- Early Stopping: [criteria]

### Augmentations
- [List all augmentations with parameters]

---

## 3. Data Preprocessing

### Input Format
- Shape: [H, W, C] or [seq_len, features] or [rows, cols]
- Dtype: [float32, etc.]
- Normalization: [mean, std] or [min, max]

### Preprocessing Steps
1. [Step 1]
2. [Step 2]
3. [Step N]

### Feature Engineering
- [Engineered features and rationale]

### Validation Preprocessing
- [Any differences from training]

---

## 4. Postprocessing

### Model Output Format
- Shape: [output dimensions]
- Type: [logits/probabilities/regression values]

### Postprocessing Steps
1. [Step 1: e.g., threshold application]
2. [Step 2: e.g., calibration]
3. [Step N: e.g., format conversion]

### Ensemble (if applicable)
- Models: [list]
- Strategy: [averaging/voting/stacking]

---

## 5. Evaluation

### Primary Metric
- Metric: [e.g., RMSE, F1, AUC]
- Current Value: [value]
- Validation Split: [description]

### Secondary Metrics
- [Metric 1]: [value]
- [Metric 2]: [value]

### Evaluation Protocol
- [Cross-validation strategy]
- [Test-time augmentation if used]

---

## 6. Inference Pipeline

### Input Requirements
- [Format, size, preprocessing]

### Inference Steps
1. [Load model]
2. [Preprocess input]
3. [Run inference]
4. [Postprocess output]

### Output Format
- [Structure of predictions]

### Performance
- Inference Time: [ms per sample]
- Memory Usage: [GB]
- Hardware: [GPU/CPU specs]

---

## 7. Dependencies

### Core Dependencies
```
[package versions]
```

### Environment
- Python: [version]
- CUDA: [version if applicable]
- OS: [target OS]

---

## 8. Known Limitations

- [Limitation 1]
- [Limitation 2]

## 9. Change History

| Date | Experiment | Change | Impact |
|------|------------|--------|--------|
| [DATE] | [EXP-ID] | [Description] | [+/- metric] |
```

---

## Update Protocol

When updating this document:

1. **Only update after validated experiments**
2. **Include experiment ID that validated the change**
3. **Update the metric values**
4. **Add entry to change history**
5. **Review for consistency across sections**
