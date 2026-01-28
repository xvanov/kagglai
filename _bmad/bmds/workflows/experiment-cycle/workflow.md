---
name: experiment-cycle
description: "Scientific method workflow for ML experimentation - structured hypothesis-driven experiment cycles with rigorous review and traceable learning"
web_bundle: true
installed_path: '{project-root}/_bmad/bmds/workflows/experiment-cycle'
---

# Experiment Cycle

**Goal:** Execute a complete ML experiment cycle - from hypothesis generation through validation and integration - maintaining scientific rigor with traceable, reproducible learning.

**Your Role:** In addition to your name, communication_style, and persona, you are a specialized agent within the BMDS (BMAD for Data Science) framework. Each step of this workflow invokes a specific agent role (Data Scientist, DS Reviewer, Implementor, or Code Reviewer). You bring domain expertise in ML experimentation, scientific methodology, and rigorous engineering, while the user brings their specific problem context and experimental goals. Work together as equals.

**Meta-Context:** This workflow orchestrates multiple agents across separate sessions. Each step runs with fresh context, using standardized artifacts (Hypothesis Registry, Experiment Definitions, Current Understanding, Current Architecture) as the connective tissue between sessions. The scientific method drives progress: hypothesize, design, implement, review, execute, evaluate, and integrate validated learnings.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self-contained instruction file for a specific agent role
- **Just-In-Time Loading**: Only the current step file is in memory - never load future step files until directed
- **Sequential Enforcement**: Sequence within step files must be completed in order, no skipping or optimization allowed
- **Artifact-Based State**: Progress tracked through standardized documents (Registry, Experiment folders, Understanding, Architecture)
- **Session Isolation**: Each step runs in a fresh session; artifacts are the handoff mechanism
- **Tri-Modal Structure**: Separate step folders for Create (steps-c/), Validate (steps-v/), and Edit (steps-e/) modes

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: If the step has a menu with Continue as an option, only proceed to next step when user selects 'C' (Continue)
5. **UPDATE ARTIFACTS**: Update relevant documents (Registry, Understanding, etc.) as directed
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 💾 **ALWAYS** update artifacts as specified in each step
- 🎯 **ALWAYS** follow the exact instructions in the step file
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps
- ✅ **ALWAYS** speak output in your agent communication style with the config `{communication_language}`

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load and read full config from {project-root}/_bmad/bmds/config.yaml and resolve:

- `project_name`, `output_folder`, `user_name`, `communication_language`, `document_output_language`
- `experiments_folder`, `docs_folder`

### 2. Mode Determination

**Check if mode was specified in the command invocation:**

- If user invoked with "create experiment" or "new experiment" or "run experiment cycle" → Set mode to **create**
- If user invoked with "validate experiment" or "review experiment" or "-v" or "--validate" → Set mode to **validate**
- If user invoked with "edit experiment" or "modify experiment" or "-e" or "--edit" → Set mode to **edit**

**If mode is still unclear, ask user:**

"Welcome to the BMDS Experiment Cycle! What would you like to do?

**[C]reate** - Start a new experiment cycle (hypothesis → design → implement → review → execute → integrate)
**[V]alidate** - Quality check a completed experiment (documentation, reproducibility, metrics)
**[E]dit** - Modify an existing experiment definition or revise a hypothesis

Please select: [C]reate / [V]alidate / [E]dit"

### 3. Route to First Step

**IF mode == create:**
Load, read completely, then execute `./steps-c/step-01-hypothesis-design.md`

**IF mode == validate:**
Load, read completely, then execute `./steps-v/step-01-select-experiment.md`

**IF mode == edit:**
Load, read completely, then execute `./steps-e/step-01-select-experiment.md`

---

## EXPERIMENT CYCLE OVERVIEW (Create Mode)

The create mode follows a 6-step scientific method:

```
Step 1: Hypothesis & Design (DS Agent - Collaborative)
    │
    ▼
Step 2: Design Review (DS Reviewer - Autonomous)
    │   └── If REJECTED → feedback → return to Step 1
    ▼
Step 3: Implementation (Implementor - Autonomous)
    │
    ▼
Step 4: Code Review (Code Reviewer - Autonomous)
    │   └── If REJECTED → feedback → return to Step 3
    ▼
Step 5: Execution & Evaluation (DS Agent - Auto run → Collaborative discussion)
    │
    ▼
Step 6: Integration (Implementor - Conditional, only if VALIDATED)
```

**Human initiates each cycle. Artifacts connect sessions.**

---

## CORE DOCUMENTS

The workflow operates on three central living documents:

1. **Current Understanding Document** (`docs/current-understanding.md`)
   - What we know about the data, problem, and effective approaches
   - Updated after each experiment with lessons learned

2. **Hypothesis Registry** (`docs/hypothesis-registry.md`)
   - Structured log of all hypotheses and experiments
   - Tracks status: PENDING, VALIDATED, INVALIDATED, SKIPPED

3. **Current Architecture Document** (`docs/current-architecture.md`)
   - The production-grade system specification
   - Updated only when experiments are VALIDATED

**Each experiment also produces:**
- `experiments/{exp-id}/readme.md` - Experimental design
- `experiments/{exp-id}/plan.md` - Implementation instructions
- `experiments/{exp-id}/results.md` - Experiment results
