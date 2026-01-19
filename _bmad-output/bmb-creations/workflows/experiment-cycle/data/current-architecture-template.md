# Current Architecture

**Last Updated:** {YYYY-MM-DD}
**Performance:** {metric} = {value} on `{dataset_path}`
**Production Checkpoint:** `{exact_path}`

---

## 1. Model Architecture

### 1.1 Core Model

| Property | Value |
|----------|-------|
| Family | {e.g., YOLOv8} |
| Variant | {e.g., yolov8m} |
| Pretrained weights | `{exact_path_or_url}` |
| Final weights | `{exact_path}` |
| Config | `{exact_path}` |

### 1.2 Modifications from Base

| Modification | File | Line | Rationale | Evidence |
|--------------|------|------|-----------|----------|
| {change} | `{path}` | {XX-YY} | {why} | EXP-XXX |
| {change} | `{path}` | {XX-YY} | {why} | EXP-YYY |

---

## 2. Data Pipeline

### 2.1 Preprocessing

| Step | Implementation | Config | Parameters |
|------|---------------|--------|------------|
| Resize | `{path}:function_name` | `{config_path}` | size={value} |
| Normalize | `{path}:function_name` | `{config_path}` | mean={}, std={} |
| {other} | `{path}:function_name` | `{config_path}` | {params} |

### 2.2 Augmentations (Training)

| Augmentation | Probability | Config | Parameters | Evidence |
|--------------|-------------|--------|------------|----------|
| {name} | {X.X} | `{path}` | {params} | EXP-XXX |
| {name} | {X.X} | `{path}` | {params} | EXP-YYY |

### 2.3 Augmentations (Validation/Test)

| Augmentation | Config | Parameters |
|--------------|--------|------------|
| {name} | `{path}` | {params} |

---

## 3. Training Configuration

| Parameter | Value | Tuned | Evidence | Config Location |
|-----------|-------|-------|----------|-----------------|
| Optimizer | {name} | {Y/N} | {EXP-XXX or default} | `{path}#line` |
| Learning rate | {X.XXeY} | {Y/N} | {evidence} | `{path}#line` |
| LR schedule | {name} | {Y/N} | {evidence} | `{path}#line` |
| Batch size | {N} | {Y/N} | {evidence} | `{path}#line` |
| Epochs | {N} | {Y/N} | {evidence} | `{path}#line` |
| Loss function | {name} | {Y/N} | {evidence} | `{path}:function` |
| Early stopping | {metric}, patience={N} | {Y/N} | {evidence} | `{path}#line` |

**Full config:** `{exact_path}`

---

## 4. Post-Processing

| Step | Implementation | Parameters | Tuned | Evidence |
|------|---------------|------------|-------|----------|
| Confidence filter | `{path}:function` | threshold={X.XX} | {Y/N} | EXP-XXX |
| NMS | `{path}:function` | iou={X.XX} | {Y/N} | EXP-YYY |
| {other} | `{path}:function` | {params} | {Y/N} | {evidence} |

---

## 5. Inference

### 5.1 Single Sample

```bash
{exact command with all arguments}
```

- Input format: {description}
- Input path: `{path}`
- Output format: {description}
- Output path: `{path}`
- Expected time: {Xms}

### 5.2 Batch Inference

```bash
{exact command with all arguments}
```

- Input: `{path}`
- Output: `{path}`
- Batch size: {N}

### 5.3 Evaluation

```bash
{exact command with all arguments}
```

- Checkpoint: `{path}`
- Dataset: `{path}`
- Output metrics: `{path}`
- Expected result: {metric} = {value}

---

## 6. Validated Changes Log

| Date | EXP | Change | Impact | Commit | Files Changed |
|------|-----|--------|--------|--------|---------------|
| {date} | EXP-XXX | {description} | {+X% metric} | `{hash}` | `{paths}` |
| {date} | EXP-YYY | {description} | {+X% metric} | `{hash}` | `{paths}` |

---

## 7. Reproducibility

### 7.1 Environment

```bash
# Create environment
{exact commands to reproduce environment}
```

### 7.2 Training from Scratch

```bash
# Full training command
{exact command}
```

Expected result: {metric} = {value} ± {variance}

### 7.3 Random Seeds

| Component | Seed | Set In |
|-----------|------|--------|
| Python | {value} | `{path}#line` |
| NumPy | {value} | `{path}#line` |
| PyTorch | {value} | `{path}#line` |
| CUDA | {value} | `{path}#line` |
