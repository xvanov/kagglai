# Getting Started with BMDS

Welcome to BMAD Data Science! This guide will help you get up and running with scientific ML workflows.

---

## What This Module Does

BMDS provides a structured approach to data science projects:

1. **Project Initialization** — Systematic understanding before coding
2. **Hypothesis-Driven Experimentation** — Scientific rigor in ML
3. **Living Documentation** — Knowledge that compounds over time
4. **Specialized Agents** — Expert assistance at every stage

---

## Prerequisites

Before using BMDS, ensure you have:

- Python 3.9+
- Git (for version control)
- Jupyter (for notebooks, optional but recommended)

Optional but recommended:
- MLflow (`pip install mlflow`)
- DVC (`pip install dvc`)

---

## Installation

```bash
bmad install bmds
```

During installation, you'll be asked to configure:
- Output folder locations
- MLflow/DVC integration preferences
- Notebook generation settings

---

## Your First Project

### 1. Initialize the Project

Run the project initialization workflow:

```
/bmad:bmds:workflows:project-init
```

This will guide you through:

| Phase | What Happens | Output |
|-------|--------------|--------|
| Problem Statement | Define objectives, metrics, constraints | `problem-statement.md` |
| Basic EDA | Initial data exploration | `eda-report.md` |
| Deep EDA | Comprehensive analysis | Updated `eda-report.md`, notebooks |
| SOTA Research | Literature and benchmark review | `sota-synthesis.md` |
| Research Directions | Prioritize approaches | `research-directions.md` |
| Technical Spec | Plan baseline implementation | `technical-spec.md` |
| Implementation | Build working baseline | Source code, model |
| Code Review | Quality verification | `current-architecture.md` |

### 2. Run Experiment Cycles

Once your baseline is ready, iterate with experiments:

```
/bmad:bmds:workflows:experiment-cycle
```

Each cycle follows the scientific method:

1. **Hypothesis** — Formulate testable claim
2. **Design** — Plan isolated experiment
3. **Implement** — Write code
4. **Review** — Verify quality
5. **Execute** — Run and evaluate
6. **Integrate** — Merge if validated

---

## Project Structure

After initialization, your project will look like:

```
your-project/
├── _bmds/                      # Living documents
│   ├── docs/
│   ├── problem-inputs/
│   ├── current-understanding.md
│   ├── current-architecture.md
│   └── hypothesis-registry.md
│
├── src/                        # Your code
├── data/                       # Your data
├── models/                     # Model artifacts
├── experiments/                # Experiment folders
└── notebooks/                  # Jupyter notebooks
```

---

## Working with Agents

Each agent specializes in a different aspect:

### Atlas (Data Analyst)
```
/bmad:bmds:agents:data-analyst
```
Use for: EDA, data profiling, quality checks

### Owl (Researcher)
```
/bmad:bmds:agents:researcher
```
Use for: SOTA research, paper analysis, architecture proposals

### Feynman (Data Scientist)
```
/bmad:bmds:agents:data-scientist
```
Use for: Hypothesis formulation, experiment design, result evaluation

### Rex (Implementer)
```
/bmad:bmds:agents:implementer
```
Use for: Code implementation, code review, integration

---

## MLflow Integration

If MLflow is enabled, BMDS will:

- Create experiments matching your project structure
- Log metrics, parameters, and artifacts
- Track model versions in the registry

Start the MLflow UI:
```bash
mlflow ui
```

---

## DVC Integration

If DVC is enabled, BMDS will:

- Track large data files outside of git
- Version datasets alongside code
- Enable reproducible pipelines

Initialize DVC in your project:
```bash
dvc init
```

---

## Tips for Success

1. **Don't skip the understanding phase** — Rushing to code leads to wasted experiments
2. **One variable at a time** — Isolated experiments yield clear learnings
3. **Document failures** — Negative results prevent repeated mistakes
4. **Update living docs** — Your future self will thank you

---

## What's Next?

- Check out the [Agents Reference](agents.md) to meet your team
- Browse the [Workflows Reference](workflows.md) to see available processes
- See [Examples](examples.md) for real-world usage patterns

---

## Need Help?

- Review this documentation
- Check your module configuration in `_bmad/bmds/config.yaml`
- Consult the broader BMAD documentation
