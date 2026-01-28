---
name: project-pickup
description: "Brownfield project initialization - discover, audit, and standardize existing work to reach experiment-ready state"
web_bundle: true
installed_path: '{project-root}/_bmad/bmds/workflows/project-pickup'
---

# Project Pickup

**Goal:** Initialize a brownfield data science project by discovering existing work, auditing documentation, standardizing to BMDS format, and reaching the same experiment-ready state as a greenfield project-init workflow.

**Your Role:** In addition to your name, communication_style, and persona, you are a specialized orchestrator within the BMDS (BMAD for Data Science) framework. Each phase of this workflow invokes a specific agent role (Data Analyst, Researcher, Data Scientist, or Implementer). You bring expertise in codebase analysis, documentation standardization, and systematic project organization, while the user brings their domain knowledge and understanding of the brownfield project's history.

**Meta-Context:** This workflow is the brownfield counterpart to project-init. While project-init creates everything from scratch, project-pickup discovers what exists, extracts value from prior work, and fills gaps to reach the same end-state. Each phase runs with fresh agent context, using standardized artifacts (Current Understanding, Current Architecture, Hypothesis Registry) as connective tissue between sessions.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self-contained instruction file for a specific agent role
- **Just-In-Time Loading**: Only the current step file is in memory - never load future step files until directed
- **Sequential Enforcement**: Sequence within step files must be completed in order, no skipping or optimization allowed
- **Artifact-Based State**: Progress tracked through sidecar file and standardized documents
- **Session Isolation**: Each phase runs in a fresh session; artifacts are the handoff mechanism
- **Tri-Modal Structure**: Separate step folders for Create (steps-c/), Validate (steps-v/), and Edit (steps-e/) modes

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: If the step has a menu with Continue as an option, only proceed to next step when user selects 'C' (Continue)
5. **UPDATE ARTIFACTS**: Update sidecar and relevant documents as directed
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 💾 **ALWAYS** update sidecar file after completing each step
- 🎯 **ALWAYS** follow the exact instructions in the step file
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps
- ✅ **ALWAYS** speak output in your agent communication style with the config `{communication_language}`

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load and read full config from {project-root}/_bmad/bmds/config.yaml and resolve:

- `project_name`, `experiments_folder`, `docs_folder`
- `user_name`, `communication_language`, `document_output_language`

### 2. Mode Determination

**Check if mode was specified in the command invocation:**

- If user invoked with "pickup project" or "brownfield" or "pick up" → Set mode to **create**
- If user invoked with "validate pickup" or "-v" or "--validate" → Set mode to **validate**
- If user invoked with "edit pickup" or "-e" or "--edit" → Set mode to **edit**

**If mode is still unclear, ask user:**

"Welcome to BMDS Project Pickup! What would you like to do?

**[C]reate** - Pick up a brownfield project (discover, audit, standardize)
**[V]alidate** - Validate an existing project pickup
**[E]dit** - Modify an existing project pickup

Please select: [C]reate / [V]alidate / [E]dit"

### 3. Route to First Step

**IF mode == create:**
Load, read completely, then execute `./steps-c/step-01-init.md`

**IF mode == validate:**
Load, read completely, then execute `./steps-v/step-v-01-validate.md`

**IF mode == edit:**
Load, read completely, then execute `./steps-e/step-e-01-assess.md`

---

## PROJECT PICKUP OVERVIEW (Create Mode)

The create mode follows an 8-phase discovery and standardization process:

```
Phase 1: Initialization & Discovery
    │   └── Scan brownfield, catalog artifacts, audit docs
    ▼
Phase 2: Structure Standardization
    │   └── Create BMDS folders, organize code, setup env
    ▼
Phase 3: Problem Understanding
    │   └── Create problem-statement.md from problem-inputs/
    ▼
Phase 4: Data Understanding
    │   └── Audit existing EDA, create eda-report.md
    ▼
Phase 5: Research Understanding
    │   └── Analyze existing models, create sota-synthesis + research-directions
    ▼
Phase 6: Architecture Documentation
    │   └── Document code, create current-architecture + technical-spec
    ▼
Phase 7: Gap Fill & Baseline Verification
    │   └── Fill missing docs, create hypothesis-registry, verify baseline
    ▼
Phase 8: Verification & Handoff
        └── Same end-state as project-init, ready for experiment-cycle
```

**Human provides problem-inputs/. Agents extract value from brownfield. Artifacts connect sessions.**

---

## CORE DOCUMENTS

The workflow produces the same artifacts as project-init:

**Primary Documents (in `docs/`):**
- problem-statement.md - Project requirements, constraints, evaluation metrics
- eda-report.md - Data analysis, statistics, patterns, quality issues
- sota-synthesis.md - State of the art techniques, benchmarks, gaps
- research-directions.md - Ranked approaches for this project
- technical-spec.md - Implementation plan for baseline

**Handoff Documents (for experiment-cycle):**
- current-understanding.md - What we know about data, problem, approaches
- current-architecture.md - Production-grade system specification
- hypothesis-registry.md - Structured log of hypotheses and experiments

**Key Distinction:**
- **Problem definition** → From user-supplied `problem-inputs/` (brownfield may be different problem)
- **Reusable work** → Extracted from brownfield codebase
