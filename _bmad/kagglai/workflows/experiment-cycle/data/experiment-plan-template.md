# Implementation Plan: EXP-XXX

## Quick Reference

| Item | Value |
|------|-------|
| Experiment ID | EXP-XXX |
| Hypothesis | {one-line summary} |
| Primary Metric | {metric} on `{dataset_path}` |
| Baseline | {exact value} from `{checkpoint_path}` |
| Target | {expected improvement} |

## Prerequisites

### Required Artifacts

- [ ] Baseline checkpoint exists: `{exact_path}`
- [ ] Config file exists: `{exact_path}`
- [ ] Evaluation data exists: `{exact_path}`
- [ ] Dependencies installed: `{requirements.txt or list}`

### Environment

- Python version: {exact}
- CUDA version: {exact}
- Key library versions:
  - {library}: {version}
  - {library}: {version}

## Implementation Tasks

### Task 1: {Description}

**Implements:** {Which part of methodology}
**Files to modify:**
- `{exact_path}` - {what changes}

**Changes:**
```python
# BEFORE (line XX-YY in {file}):
{exact code being replaced}

# AFTER:
{exact new code}
```

**Verification:**
- [ ] Change isolated - no other modifications
- [ ] Syntax valid - file runs without error
- [ ] Logic matches experiment design

### Task 2: {Description}

**Implements:** {Which part of methodology}
**Files to modify:**
- `{exact_path}` - {what changes}

**Changes:**
```python
# BEFORE (line XX-YY in {file}):
{exact code being replaced}

# AFTER:
{exact new code}
```

**Verification:**
- [ ] Change isolated - no other modifications
- [ ] Syntax valid - file runs without error
- [ ] Logic matches experiment design

## Pre-Execution Checklist

### Code Quality

- [ ] All changes match experiment design EXACTLY
- [ ] No undocumented changes introduced
- [ ] No scope creep (features not in design)
- [ ] Code follows project conventions

### Reproducibility

- [ ] Random seeds set: `{exact value}`
- [ ] Baseline reproducible: Run `{command}`, expect `{exact metric}`
- [ ] Checkpoint will be saved with experiment ID
- [ ] Config logged with experiment

### Data Integrity

- [ ] Training data: `{exact_path}` ({N} samples)
- [ ] Validation data: `{exact_path}` ({N} samples)
- [ ] Test data: `{exact_path}` ({N} samples) - DO NOT USE until final eval
- [ ] No data leakage between splits

### Anti-Pattern Prevention

- [ ] NOT using test set for hyperparameter tuning
- [ ] NOT introducing multiple changes (isolate hypothesis)
- [ ] NOT skipping validation step
- [ ] NOT modifying evaluation script

## Execution

### Training Command

```bash
{exact command with all arguments}
```

- Expected runtime: {estimate}
- Expected GPU memory: {estimate}
- Output checkpoint: `{exact_path}`
- Logs: `{exact_path}`

### Evaluation Command

```bash
{exact command with all arguments}
```

- Input checkpoint: `{exact_path}`
- Evaluation data: `{exact_path}`
- Output metrics: `{exact_path}`

## Post-Execution Checklist

- [ ] Training completed without error
- [ ] Checkpoint saved to correct location: `{path}`
- [ ] Metrics logged to correct location: `{path}`
- [ ] Ready for results documentation in `results.md`
