# BMDS: BMAD Data Science

**Scientific ML Workflows with Hypothesis-Driven Experimentation**

Rigorous data science methodology with living documentation, specialized agents, and reproducible experimentation.

---

## Overview

BMDS (BMAD Data Science) brings scientific rigor to ML/DS projects through:

- **Hypothesis-Driven Experimentation** — Every experiment has a testable hypothesis
- **Living Documentation** — Knowledge compounds across experiments
- **Specialized Agents** — Four experts: Analyst, Researcher, Scientist, Implementer
- **Clean Project Structure** — Code at project root, AI artifacts in `_bmds/`
- **MLOps Integration** — MLflow for tracking, DVC for data versioning

Born from battle-tested patterns in competitive ML, BMDS generalizes these approaches for any data science project.

---

## Installation

```bash
bmad install bmds
```

---

## Quick Start

1. **Initialize a new project:**
   ```
   /bmad:bmds:workflows:project-init
   ```
   This guides you through: Problem Statement → EDA → SOTA Research → Research Directions → Technical Spec → Baseline Implementation

2. **Run experiment cycles:**
   ```
   /bmad:bmds:workflows:experiment-cycle
   ```
   This executes: Hypothesis → Design → Implement → Review → Execute → Integrate

3. **Work with specialized agents:**
   - Atlas (Data Analyst): `/bmad:bmds:agents:data-analyst`
   - Owl (Researcher): `/bmad:bmds:agents:researcher`
   - Feynman (Data Scientist): `/bmad:bmds:agents:data-scientist`
   - Rex (Implementer): `/bmad:bmds:agents:implementer`

---

## Components

### Agents

| Agent | Name | Role |
|-------|------|------|
| 🔍 data-analyst | Atlas | EDA, data profiling, quality assessment |
| 📚 researcher | Owl | SOTA synthesis, architecture proposals |
| 🧪 data-scientist | Feynman | Hypothesis design, experiment evaluation |
| 🔧 implementer | Rex | Production code, integration, code review |

### Workflows

| Workflow | Steps | Purpose |
|----------|-------|---------|
| `project-init` | 13 | Initialize project with comprehensive understanding and baseline |
| `experiment-cycle` | 6 | Execute hypothesis-driven experiments with scientific rigor |

---

## Configuration

The module supports these configuration options (set during installation):

| Variable | Description | Default |
|----------|-------------|---------|
| `bmds_output_folder` | Living documents location | `_bmds` |
| `source_folder` | Source code location | `src` |
| `data_folder` | Data files location | `data` |
| `models_folder` | Model artifacts location | `models` |
| `experiments_folder` | Experiments location | `experiments` |
| `notebooks_folder` | Jupyter notebooks location | `notebooks` |
| `enable_mlflow` | MLflow integration | `true` |
| `enable_dvc` | DVC integration | `true` |
| `generate_eda_notebooks` | Generate notebooks during EDA | `true` |

---

## Project Structure (After Installation)

```
your-project/
├── _bmad/                      # BMAD framework
│   └── bmds/                   # This module
│
├── _bmds/                      # BMDS output (living docs)
│   ├── docs/                   # Generated documentation
│   ├── current-understanding.md
│   ├── current-architecture.md
│   └── hypothesis-registry.md
│
├── src/                        # Source code
├── data/                       # Data files
├── models/                     # Model artifacts
├── experiments/                # Experiment folders
├── notebooks/                  # Jupyter notebooks
└── outputs/                    # Predictions, reports
```

---

## Module Structure

```
bmds/
├── module.yaml                 # Module configuration
├── config.yaml                 # Runtime settings
├── README.md                   # This file
├── agents/
│   ├── data-analyst/
│   ├── researcher/
│   ├── data-scientist/
│   └── implementer/
├── workflows/
│   ├── project-init/
│   └── experiment-cycle/
└── _module-installer/
    └── installer.js
```

---

## Living Documents

BMDS maintains three core documents that evolve with your project:

1. **Current Understanding** — What you know about data, problem, and approaches
2. **Hypothesis Registry** — All experiments with status and learnings
3. **Current Architecture** — Production system specification (updated only on validated experiments)

---

## Scientific Method in Practice

```
Understand → Research → Hypothesize → Design → Implement → Review → Execute → Evaluate → Integrate
     ↑                                                                              │
     └──────────────────────── Learn and iterate ──────────────────────────────────┘
```

---

## Author

Created via BMAD Module workflow

---

## License

Part of the BMAD framework.
