# Examples & Use Cases

Practical examples for using BMDS in real data science projects.

---

## Example 1: Starting a New Classification Project

### Scenario
You have a dataset and need to build a classifier.

### Workflow

**1. Initialize the project:**
```
/bmad:bmds:workflows:project-init
```

**2. During Problem Statement phase, define:**
- Objective: Binary/multiclass classification
- Primary metric: F1, AUC, accuracy
- Constraints: Inference time, model size
- Success criteria: Minimum acceptable performance

**3. During EDA, Atlas will:**
- Analyze class distribution (imbalance?)
- Check feature distributions by class
- Identify missing data patterns
- Generate correlation analysis
- Create EDA notebook

**4. During SOTA Research, Owl will:**
- Find relevant papers for your domain
- Identify benchmark datasets
- Compare model architectures
- Propose baseline and advanced approaches

**5. Build baseline and iterate with experiment-cycle.**

---

## Example 2: Improving an Existing Model

### Scenario
You have a working model but want to improve it systematically.

### Workflow

**1. Start experiment cycle:**
```
/bmad:bmds:workflows:experiment-cycle
```

**2. Formulate hypothesis with Feynman:**
```
Hypothesis: Adding feature X will improve F1 by 2%
Rationale: Feature X captures temporal patterns not in current features
```

**3. Design isolated experiment:**
- Variable under test: Feature X inclusion
- Baseline: Current model without feature X
- Treatment: Model with feature X
- Success threshold: F1 improvement ≥ 2%

**4. Implement, review, execute.**

**5. Evaluate results:**
- If VALIDATED: Integrate into production architecture
- If REJECTED: Document learnings, try next hypothesis

---

## Example 3: Research-Driven Exploration

### Scenario
You're exploring a new problem domain and need to understand SOTA.

### Workflow

**1. Invoke Owl directly:**
```
/bmad:bmds:agents:researcher
```

**2. Request research synthesis:**
```
SR (Search Research): "time series forecasting for energy consumption"
```

**3. Owl will provide:**
- Recent papers and techniques
- Benchmark datasets (electricity, M4, etc.)
- Model comparisons (N-BEATS, Temporal Fusion Transformer, etc.)
- Recommended architecture with citations

**4. Request architecture proposal:**
```
PA (Propose Architecture)
```

**5. Use findings to inform project-init or experiment-cycle.**

---

## Common Scenarios

### "I need to understand my data quickly"

```
/bmad:bmds:agents:data-analyst
ED (EDA)
```
Atlas will run comprehensive EDA and generate a report.

### "I want to track all my experiments"

Use the experiment-cycle workflow. Every experiment is:
- Registered in `hypothesis-registry.md`
- Documented in `experiments/E-XXX/`
- Tracked with status (PENDING, VALIDATED, REJECTED)

### "I need to document what we know"

```
/bmad:bmds:agents:data-scientist
SS (Show Status)
```
Feynman will summarize current understanding, active experiments, and learnings.

### "I need production-quality code"

```
/bmad:bmds:agents:implementer
CR (Code Review)
```
Rex will review code against coding standards and flag issues.

---

## Tips & Tricks

### 1. Start with Understanding
Don't rush to model building. The project-init workflow front-loads discovery for a reason — understanding prevents wasted experiments.

### 2. One Variable at a Time
When running experiments, change only ONE thing. Multi-variable experiments make it impossible to know what worked.

### 3. Document Failures
Use `/bmad:bmds:agents:data-scientist UD` to update documents even after failed experiments. Knowing what doesn't work is valuable.

### 4. Use Notebooks for Exploration
Enable `generate_eda_notebooks` to get interactive notebooks during EDA. Great for ad-hoc exploration.

### 5. Track Everything with MLflow
If MLflow is enabled, all experiments are tracked. Run `mlflow ui` to visualize progress.

---

## Troubleshooting

### "Workflow seems stuck"

Check the sidecar file (`.project-sidecar.md` or similar) to see current step. You can resume from where you left off.

### "Agent doesn't understand my request"

Use explicit menu triggers (ED, SR, NH, etc.) instead of free-form requests.

### "Living documents are out of date"

Use `UU` (Update Understanding) with Atlas or `UD` (Update Documents) with Feynman to manually update.

### "MLflow not tracking"

Ensure MLflow is installed (`pip install mlflow`) and `enable_mlflow: true` in config.yaml.

### "DVC not working"

Initialize DVC first: `dvc init`. Then ensure `enable_dvc: true` in config.yaml.

---

## Sample Hypothesis Registry Entry

```markdown
## H-003: Gradient Boosting Ensemble

**Statement:** Combining XGBoost, LightGBM, and CatBoost with averaging will improve F1 by 3% over single best model.

**Status:** VALIDATED

**Experiment:** E-003

**Results:**
- Single best (LightGBM): F1 = 0.847
- Ensemble: F1 = 0.872
- Improvement: +2.9%

**Learnings:**
- Ensemble reduces variance significantly
- Averaging works better than stacking for this dataset
- Diminishing returns beyond 3 models

**Integration:** Merged to production architecture on 2026-01-15
```

---

## Getting More Help

- Review the [Getting Started](getting-started.md) guide
- Check [Agents Reference](agents.md) for available commands
- See [Workflows Reference](workflows.md) for detailed step information
- Consult the broader BMAD documentation
