# Workflows Reference

BMDS includes 2 core workflows for structured data science work.

---

## Project Initialization

**ID:** `bmad:bmds:workflows:project-init`

**Purpose:** Initialize a data science project with comprehensive understanding and a working baseline.

**When to Use:**
- Starting a new data science project
- Onboarding to an existing dataset
- Establishing a systematic baseline

**Modes:**
- **Create** — Full initialization from scratch
- **Validate** — Review existing setup for completeness
- **Edit** — Modify specific documents or phases

### Create Mode Steps

| Step | Phase | Agent | Output |
|------|-------|-------|--------|
| 1 | Initialize | - | Project structure, sidecar |
| 2 | Problem Statement | Atlas | `problem-statement.md` |
| 3 | Problem Statement Review | Reviewer | Validation |
| 4 | Basic EDA | Atlas | Initial `eda-report.md` |
| 5 | Deep EDA | Atlas | Complete EDA, notebooks |
| 6 | SOTA Research | Owl | `sota-synthesis.md` |
| 7 | SOTA Review | Reviewer | Validation |
| 8 | Research Directions | Owl + User | `research-directions.md` |
| 9 | Technical Spec | Rex | `technical-spec.md` |
| 10 | Technical Spec Review | Reviewer | Validation |
| 11 | Implementation | Rex | Baseline code |
| 12 | Code Review | Reviewer | Quality check |
| 13 | Complete | - | Handoff to experiment-cycle |

### Key Outputs

**Project Documents:**
- `problem-statement.md` — Requirements, constraints, metrics
- `eda-report.md` — Data analysis and insights
- `sota-synthesis.md` — State of the art techniques
- `research-directions.md` — Prioritized approaches
- `technical-spec.md` — Implementation plan

**Living Documents (for experiment-cycle):**
- `current-understanding.md` — What we know
- `current-architecture.md` — Production system
- `hypothesis-registry.md` — Experiment tracking

---

## Experiment Cycle

**ID:** `bmad:bmds:workflows:experiment-cycle`

**Purpose:** Execute hypothesis-driven experiments with scientific rigor.

**When to Use:**
- Testing a new hypothesis
- Iterating on model improvements
- Systematically exploring approaches

**Modes:**
- **Create** — Run a new experiment cycle
- **Validate** — Quality check completed experiment
- **Edit** — Modify experiment definition

### Create Mode Steps

| Step | Phase | Agent | Mode |
|------|-------|-------|------|
| 1 | Hypothesis & Design | Feynman | Collaborative |
| 2 | Design Review | Reviewer | Autonomous |
| 3 | Implementation | Rex | Autonomous |
| 4 | Code Review | Reviewer | Autonomous |
| 5 | Execution & Evaluation | Feynman | Auto → Collaborative |
| 6 | Integration | Rex | Conditional (if validated) |

### Experiment Flow

```
Step 1: Hypothesis & Design
    │
    ▼
Step 2: Design Review
    │   └── REJECTED → Return to Step 1
    ▼
Step 3: Implementation
    │
    ▼
Step 4: Code Review
    │   └── REJECTED → Return to Step 3
    ▼
Step 5: Execution & Evaluation
    │   ├── VALIDATED → Step 6
    │   ├── REJECTED → Update docs, next hypothesis
    │   └── INCONCLUSIVE → Review methodology
    ▼
Step 6: Integration (only if VALIDATED)
```

### Experiment Artifacts

Each experiment creates:
```
experiments/E-001-hypothesis-name/
├── readme.md      # Methodology, baseline, success criteria
├── plan.md        # Prerequisites, tasks, execution commands
└── results.md     # Metrics, learnings, artifacts
```

### Scientific Principles

1. **Falsifiable** — Hypotheses must be testable
2. **Isolated** — One variable per experiment
3. **Documented** — All results recorded
4. **Integrated** — Only validated changes go to production

---

## Workflow Invocation

**Start project initialization:**
```
/bmad:bmds:workflows:project-init
```

**Start experiment cycle:**
```
/bmad:bmds:workflows:experiment-cycle
```

**With specific mode:**
```
/bmad:bmds:workflows:project-init create
/bmad:bmds:workflows:experiment-cycle validate
```

---

## Workflow Architecture

Both workflows use **step-file architecture**:

- **Micro-file Design** — Each step is self-contained
- **Just-In-Time Loading** — Only current step in memory
- **Sequential Enforcement** — No skipping steps
- **Artifact-Based State** — Documents are the handoff mechanism
- **Tri-Modal Structure** — Create/Validate/Edit modes

This enables:
- Clear progress tracking
- Session isolation
- Resumable workflows
- Quality gates at each step
