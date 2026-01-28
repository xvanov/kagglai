# Discovery Patterns

**Purpose:** Guide for discovering and cataloging artifacts in brownfield codebases.

---

## What to Look For

### 1. Documentation

| Artifact | Common Locations | Indicators |
|----------|------------------|------------|
| README files | `README.md`, `docs/` | Project overview, setup instructions |
| Notebooks with markdown | `notebooks/`, `*.ipynb` | EDA narratives, experiment notes |
| Docstrings | Python files | Function/class documentation |
| Comments | Throughout code | Inline explanations, TODOs |
| Config files | `config/`, `*.yaml`, `*.json` | Settings, hyperparameters |

### 2. Data Pipelines

| Artifact | Common Locations | Indicators |
|----------|------------------|------------|
| Data loading scripts | `src/data/`, `data_loader.py` | `pd.read_csv`, `load_data` functions |
| Preprocessing code | `src/preprocessing/`, `preprocess.py` | Feature engineering, transforms |
| Data validation | `src/validate/` | Schema checks, quality assertions |
| Feature stores | `features/`, `*.parquet` | Computed features |

### 3. Models

| Artifact | Common Locations | Indicators |
|----------|------------------|------------|
| Model definitions | `src/models/`, `model.py` | Class definitions, architectures |
| Training scripts | `train.py`, `src/training/` | Training loops, optimizers |
| Checkpoints | `models/`, `checkpoints/`, `*.pkl`, `*.pt` | Saved model weights |
| Configs | `configs/`, `*.yaml` | Hyperparameters, architecture settings |

### 4. Experiments

| Artifact | Common Locations | Indicators |
|----------|------------------|------------|
| Experiment logs | `logs/`, `mlruns/`, `wandb/` | Training metrics, runs |
| Result files | `results/`, `outputs/` | Predictions, evaluations |
| Notebooks | `notebooks/experiments/` | Experiment narratives |
| Submission files | `submissions/`, `*.csv` | Past submissions |

### 5. EDA

| Artifact | Common Locations | Indicators |
|----------|------------------|------------|
| EDA notebooks | `notebooks/eda/`, `EDA.ipynb` | Visualizations, statistics |
| Plots | `figures/`, `plots/` | Saved visualizations |
| Data profiles | `data_profile.html` | Automated profiling reports |

---

## Discovery Report Structure

```markdown
## Discovery Report

**Brownfield Path:** {path}
**Scanned:** {date}

### Documentation Found
| Type | Location | Quality | Notes |
|------|----------|---------|-------|
| README | ./README.md | Good/Partial/Outdated | {notes} |

### Data Pipeline
| Component | Location | Status | Notes |
|-----------|----------|--------|-------|
| Data loader | ./src/data.py | Working/Broken/Unknown | {notes} |

### Models
| Model | Location | Status | Performance |
|-------|----------|--------|-------------|
| Baseline | ./models/v1.pkl | Trained | CV: 0.XX |

### Experiments
| Experiment | Location | Status | Result |
|------------|----------|--------|--------|
| EXP-001 | ./experiments/001/ | Complete | +X% |

### EDA
| Notebook | Location | Coverage | Findings |
|----------|----------|----------|----------|
| Basic EDA | ./notebooks/eda.ipynb | Full/Partial | {key findings} |

### Gaps Identified
- [ ] Missing: {artifact}
- [ ] Outdated: {artifact}
- [ ] Incomplete: {artifact}
```

---

## Quality Assessment Criteria

### Documentation Quality

| Rating | Criteria |
|--------|----------|
| **Good** | Clear, current, comprehensive |
| **Partial** | Exists but incomplete or unclear |
| **Outdated** | Exists but doesn't match current code |
| **Missing** | Doesn't exist |

### Code Quality

| Rating | Criteria |
|--------|----------|
| **Production** | Clean, documented, tested |
| **Experimental** | Works but messy, undocumented |
| **Prototype** | Quick hack, may not work |
| **Broken** | Errors, dependencies missing |

### Data Pipeline Status

| Rating | Criteria |
|--------|----------|
| **Working** | Runs end-to-end successfully |
| **Partial** | Some stages work |
| **Broken** | Errors prevent execution |
| **Unknown** | Not yet tested |

---

## Extraction Guidelines

### From Notebooks

1. **Narrative text** → Documentation candidates
2. **Statistical outputs** → EDA report content
3. **Visualizations** → Reference for eda-report
4. **Model experiments** → Research directions input
5. **Final code cells** → Pipeline candidates

### From Code

1. **Docstrings** → Technical spec content
2. **Config files** → Architecture documentation
3. **Training logs** → Performance baselines
4. **Comments** → Context for decisions made

### From Models

1. **Architecture** → Current architecture doc
2. **Hyperparameters** → Technical spec
3. **Performance metrics** → Baseline benchmarks
4. **Training history** → What worked/didn't

---

## Red Flags to Note

- **Hardcoded paths** - May not work in new environment
- **Missing dependencies** - requirements.txt incomplete
- **No reproducibility** - Missing seeds, versions
- **Data leakage hints** - Train/test confusion
- **Outdated libraries** - Security/compatibility risks
- **No validation strategy** - Overfitting risk
