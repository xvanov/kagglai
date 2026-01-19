---
name: project-setup
description: "Rigorous project initialization pipeline for Kaggle/ML competitions - front-loads discovery, coordinates specialized agents, produces working baseline submission"
web_bundle: true
---

# Project Setup

**Goal:** Initialize a Kaggle/ML competition project with comprehensive documentation, validated understanding, and a working baseline submission ready for experimentation.

**Your Role:** In addition to your name, communication_style, and persona, you are a workflow orchestrator coordinating specialized agents (Data Analyst, Researcher, Implementer) through a rigorous project setup process. This workflow manages session handoffs and artifact creation. You bring workflow expertise and quality standards, while the user brings their competition context and domain knowledge. Work together as equals.

**Meta-Context:** This workflow coordinates multiple agents across separate sessions using the Author/Validator pattern. Each phase runs with fresh context to maintain output quality. Standardized artifacts (challenge spec, EDA report, SoTA synthesis, etc.) serve as the connective tissue between sessions. The workflow produces handoff documents that feed directly into the experiment-cycle workflow.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self-contained instruction file for a specific agent role
- **Just-In-Time Loading**: Only the current step file is in memory - never load future step files until directed
- **Sequential Enforcement**: Sequence within step files must be completed in order, no skipping or optimization allowed
- **Artifact-Based State**: Progress tracked through sidecar file and standardized documents
- **Session Isolation**: Each step may run in a fresh session; artifacts are the handoff mechanism
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
- 💾 **ALWAYS** update sidecar file as specified in each step
- 🎯 **ALWAYS** follow the exact instructions in the step file
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps
- ✅ **ALWAYS** speak output in your agent communication style with the config `{communication_language}`

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load and read full config from {project-root}/_bmad/kagglai/config.yaml and resolve:

- `module_name`, `output_folder`, `user_name`, `communication_language`, `document_output_language`
- `experiments_folder` (typically `{project-root}/_kagglai`)

### 2. Mode Determination

**Check if mode was specified in the command invocation:**

- If user invoked with "create project" or "new project" or "setup project" → Set mode to **create**
- If user invoked with "validate project" or "review project" or "-v" or "--validate" → Set mode to **validate**
- If user invoked with "edit project" or "modify project" or "-e" or "--edit" → Set mode to **edit**

**If mode is still unclear, ask user:**

"Welcome to the Kaggle Project Setup Workflow! What would you like to do?

**[C]reate** - Initialize a new competition project (challenge spec → EDA → SoTA → research directions → technical spec → baseline implementation)
**[V]alidate** - Review an existing project setup for completeness and quality
**[E]dit** - Modify an existing project document or phase

Please select: [C]reate / [V]alidate / [E]dit"

### 3. Route to First Step

**IF mode == create:**
Load, read completely, then execute `./steps-c/step-01-init.md`

**IF mode == validate:**
Load, read completely, then execute `./steps-v/step-v-01-validate.md`

**IF mode == edit:**
Load, read completely, then execute `./steps-e/step-e-01-assess.md`

---

## WORKFLOW PHASES (Create Mode)

The create mode follows 7 phases with Author/Validator pattern:

```
Phase 1: Challenge Specification
    Data Analyst → challenge-spec.md
    │
    ▼
Phase 2: Exploratory Data Analysis
    Data Analyst → eda-report.md + current-understanding.md §2
    │
    ▼
Phase 3: State of the Art Research
    Researcher → sota-synthesis.md + current-understanding.md §3
    │
    ▼
Phase 4: Research Directions
    Researcher → research-directions.md + hypothesis-registry.md
    │
    ▼
Phase 5: Technical Specification
    Implementer → technical-spec.md
    │
    ▼
Phase 6: Implementation
    Implementer → src/ + models/ + submission
    │
    ▼
Phase 7: Code Review
    Implementer → current-architecture.md + fixes
```

**User orchestrates sessions. Artifacts connect phases.**

---

## CORE DOCUMENTS

The workflow produces these documents in `_kagglai/docs/`:

**Project-Specific Documents:**
- `challenge-spec.md` - Competition requirements, constraints, evaluation metrics
- `eda-report.md` - Data analysis, statistics, patterns, quality issues
- `sota-synthesis.md` - State of the art techniques, benchmarks, gaps
- `research-directions.md` - Ranked approaches for this competition
- `technical-spec.md` - Implementation plan for baseline

**Handoff Documents (for experiment-cycle):**
- `current-understanding.md` - What we know about data, problem, approaches
- `current-architecture.md` - Production-grade system specification
- `hypothesis-registry.md` - Structured log of hypotheses and experiments
