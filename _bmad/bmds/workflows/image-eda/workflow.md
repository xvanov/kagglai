---
name: image-eda
description: "Deep EDA workflow for image/visual data - multi-agent orchestration producing interactive Streamlit dashboard and permanent analysis scripts"
web_bundle: true
installed_path: '{project-root}/_bmad/bmds/workflows/image-eda'
---

# Image Data EDA

**Goal:** Perform comprehensive exploratory data analysis on image datasets for computer vision tasks, producing an interactive dashboard, permanent rerunnable scripts, and documented insights.

**Your Role:** In addition to your name, communication_style, and persona, you are a workflow orchestrator coordinating specialized agents (Data Analyst/Atlas, Data Scientist/Feynman, Implementer/Rex) through a rigorous image EDA process. This workflow manages agent handoffs and artifact creation. You bring workflow expertise and quality standards, while the user brings their project context and domain knowledge. Work together as equals.

**Meta-Context:** This workflow coordinates multiple agents across separate sub-agent calls using memory files for context transfer. Each phase runs with fresh context to maintain output quality (<50% context window). Standardized artifacts (scripts, insights, dashboard) serve as the connective tissue between phases. The workflow produces handoff documents that feed directly into the experiment-cycle workflow.

---

## WORKFLOW ARCHITECTURE

This uses **step-file architecture** for disciplined execution:

### Core Principles

- **Micro-file Design**: Each step is a self-contained instruction file for orchestration or agent delegation
- **Just-In-Time Loading**: Only the current step file is in memory - never load future step files until directed
- **Sequential Enforcement**: Sequence within step files must be completed in order, no skipping or optimization allowed
- **Multi-Agent Orchestration**: Spawn sub-agents for focused analysis phases, aggregate findings via memory files
- **Artifact-Based State**: Progress tracked through state file and phase output files
- **Session Isolation**: Each sub-agent runs in fresh context; memory files are the handoff mechanism
- **Tri-Modal Structure**: Separate step folders for Create (steps-c/), Validate (steps-v/), and Edit (steps-e/) modes

### Step Processing Rules

1. **READ COMPLETELY**: Always read the entire step file before taking any action
2. **FOLLOW SEQUENCE**: Execute all numbered sections in order, never deviate
3. **WAIT FOR INPUT**: If a menu is presented, halt and wait for user selection
4. **CHECK CONTINUATION**: If the step has a menu with Continue as an option, only proceed to next step when user selects 'C' (Continue)
5. **UPDATE ARTIFACTS**: Update state file and relevant documents as directed
6. **LOAD NEXT**: When directed, load, read entire file, then execute the next step file

### Critical Rules (NO EXCEPTIONS)

- 🛑 **NEVER** load multiple step files simultaneously
- 📖 **ALWAYS** read entire step file before execution
- 🚫 **NEVER** skip steps or optimize the sequence
- 💾 **ALWAYS** update state file as specified in each step
- 🎯 **ALWAYS** follow the exact instructions in the step file
- ⏸️ **ALWAYS** halt at menus and wait for user input
- 📋 **NEVER** create mental todo lists from future steps
- ✅ **ALWAYS** speak output in your agent communication style with the config `{communication_language}`
- 🤖 **SUB-AGENTS** stay under 50% context window to remain in "smart phase"

---

## INITIALIZATION SEQUENCE

### 1. Configuration Loading

Load and read full config from {project-root}/_bmad/bmds/config.yaml and resolve:

- `module_name`, `output_folder`, `user_name`, `communication_language`, `document_output_language`
- `experiments_folder` (typically `{project-root}/_bmds`)
- `current_understanding_file`, `hypothesis_registry_file`

### 2. Mode Determination

**Check if mode was specified in the command invocation:**

- If user invoked with "create" or "new" or "run eda" → Set mode to **create**
- If user invoked with "validate" or "check" or "-v" or "--validate" → Set mode to **validate**
- If user invoked with "edit" or "modify" or "re-run" or "-e" or "--edit" → Set mode to **edit**

**If mode is still unclear, ask user:**

"Welcome to the Image EDA Workflow! What would you like to do?

**[C]reate** - Run a new image EDA (data acquisition → analysis → dashboard → model selection)
**[V]alidate** - Check an existing EDA for completeness and quality
**[E]dit** - Re-run specific phases of an existing EDA

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

The create mode follows 10 phases with multi-agent orchestration:

```
Phase 1: Initialization
    Orchestrator → Check data-access.md, initialize state
    │
    ▼
Phase 2: Data Acquisition (Conditional)
    Rex (Implementer) → 01_data_sampling.py
    │
    ▼
Phase 3: Basic Statistics
    Atlas (Data Analyst) → 02_basic_stats.py
    │
    ▼
Phase 4: Label Analysis
    Atlas → 03_label_analysis.py
    │
    ▼
Phase 5: Visual Pattern Analysis
    Atlas → 04_visual_patterns.py
    │
    ▼
Phase 6: Data Quality Assessment
    Atlas → 05_data_quality.py
    │
    ▼
Phase 7: Insight Generation
    Feynman (Data Scientist) → 06_insights.md + current-understanding.md §2
    │
    ▼
Phase 8: Dashboard Generation [USER CHECKPOINT]
    Rex → dashboard/app.py
    │
    ▼
Phase 9: Model Selection
    Feynman → eda-report-images.md + current-understanding.md §3
    │
    ▼
Phase 10: Completion
    Orchestrator → Final summary and handoff
```

**Orchestrator coordinates. Sub-agents execute. Memory files connect.**

---

## CORE DOCUMENTS

The workflow produces these artifacts:

**Permanent Scripts in `{experiments_folder}/eda/`:**
- `01_data_sampling.py` - Data acquisition and sampling
- `02_basic_stats.py` - Image statistics generation
- `03_label_analysis.py` - Label quality assessment
- `04_visual_patterns.py` - Pattern analysis and visualization
- `05_data_quality.py` - Data quality filtering logic
- `06_insights.md` - Synthesized insights document
- `dashboard/app.py` - Streamlit dashboard application

**Updated Documents:**
- `current-understanding.md` - Section 2 (Data) after insights, Section 3 (Model) after model selection

**Created Documents:**
- `eda-report-images.md` - Comprehensive image EDA report

**State/Memory Files:**
- `.image-eda-state.yaml` - Workflow state tracking
- `.phase-{N}-output.md` - Phase findings for context transfer
