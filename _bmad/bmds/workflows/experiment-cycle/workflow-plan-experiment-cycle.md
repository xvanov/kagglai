---
stepsCompleted: ['step-01-discovery', 'step-02-classification', 'step-03-requirements', 'step-04-tools', 'step-05-plan-review', 'step-06-design', 'step-07-foundation', 'step-08-build-step-01', 'step-09-build-all-remaining']
created: 2026-01-17
status: BUILD_COMPLETE
approvedDate: 2026-01-18
completedDate: 2026-01-18
---

# Workflow Creation Plan

## Classification Decisions

**Workflow Name:** experiment-cycle
**Target Path:** _bmad/bmds/workflows/experiment-cycle/

**4 Key Decisions:**
1. **Document Output:** true (produces Hypothesis Registry, Experiment Definition, Current Understanding, Current Architecture; Implementor produces code)
2. **Module Affiliation:** BMDS (new module - BMAD for Data Science)
3. **Session Type:** single-session per step (inner loops for review rejection handled by workflow logic)
4. **Lifecycle Support:** tri-modal (Create + Edit + Validate)

**Structure Implications:**
- Needs `steps-c/`, `steps-e/`, `steps-v/` directories
- Each step is a fresh session, artifacts are connective tissue
- Inner loops: Design↔Review, Code↔CodeReview iterate until passing
- Outer loop is human-initiated
- No continuation logic needed within steps (single-session each)

---

## Discovery Notes

**User's Vision:**
A scientific method workflow for ML experimentation within BMDS - the BMAD-style agentic methodology for data science. The core is a repeating experiment cycle that maintains rigor while allowing rapid iteration. Each step runs in a fresh session due to context window limits, with standardized artifacts serving as the connective tissue between sessions.

**Who It's For:**
Data scientists / ML practitioners working on ML projects or similar ML projects, using the BMDS agent team.

**What It Produces:**
- Updated Hypothesis Registry entries
- Experiment Definition documents
- Updated Current Understanding Document
- Updated Current Architecture Document (when experiments pass)
- Integrated codebase changes (when experiments pass)

**Key Insights:**

1. **Context limits drive session boundaries** - Each step needs fresh context, artifacts are the handoff mechanism

2. **Human-initiated outer loop** - Human triggers each major experiment cycle, decides when to continue

3. **Automatic inner loops** - Design↔Review and Code↔CodeReview iterate automatically until passing

4. **Six distinct session types:**
   - DS: Research direction + hypothesis + experiment design
   - DS Review: Validate design (may reject → inner loop)
   - Implementor: Write code from Experiment Definition
   - Code Review: Validate code (may reject → inner loop)
   - DS: Run experiment, log results, update docs
   - Implementor: Integrate to main (only if hypothesis passes)

5. **Artifact flow:**
   - Reads: Current Understanding, Hypothesis Registry, Current Architecture
   - Writes: Experiment Definition, updated Registry, updated Understanding, (conditionally) updated Architecture + codebase

6. **Loop termination:** Experiment validates or invalidates hypothesis → update docs → human decides next cycle

---

## Requirements

**Flow Structure:**
- Pattern: Repeating loop with inner loops
- Phases:
  1. DS: Research Direction + Hypothesis + Experiment Design
  2. DS Review: Validate design (→ loop to 1 if rejected)
  3. Implementor: Write code
  4. Code Review: Validate code (→ loop to 3 if rejected)
  5. DS: Run & Evaluate, log results, update docs
  6. (Conditional) Implementor: Integrate to main + update Architecture
  7. Human decides: next cycle?
- Estimated steps: 6 step files (with inner loop logic in steps 2 and 4)

**User Interaction:**
- Style: Mixed
  - Step 1 (Hypothesis + Design): Collaborative with human
  - Steps 2-4: Autonomous (agent validates/implements)
  - Step 5 (Results): Autonomous run → Collaborative discussion
  - Step 6 (Integrate): Autonomous
- Decision points: Human initiates each cycle, reviews results
- Checkpoint frequency: After experiment results, before next cycle

**Inputs Required:**
- Required:
  - Current Understanding Document (`docs/current-understanding.md`)
  - Hypothesis Registry (`docs/hypothesis-registry.md`)
  - Current Architecture Document (`docs/current-architecture.md`)
  - SOTA Synthesis Document (`docs/sota-synthesis.md`)
  - Problem Statement Document (`docs/problem-statement.md`)
  - Codebase
- Optional: None identified
- Prerequisites: Initial EDA and research phases completed

**Output Specifications:**
- Type: Multiple documents + code
- Format: Structured (all documents follow rigorous templates)
- Documents produced/updated:
  - Hypothesis Registry (semi-structured, standard entry format)
  - Experiment Definition folder:
    - `experiments/{exp-id}-{name}/readme.md` (experimental design)
    - `experiments/{exp-id}-{name}/plan.md` (implementation instructions)
    - `experiments/{exp-id}-{name}/results.md` (experiment results)
  - Current Understanding Document (structured sections)
  - Current Architecture Document (structured sections)
- Code: Implemented experiment code, integrated to main if validated
- Key template requirements:
  - Exact paths for all models, data, configs, scripts
  - Explicit dataset specification for all metrics (train/val/test)
  - Reproducibility information (seeds, commits, commands)
  - Anti-pattern prevention checklists
  - Full traceability (commits, evidence, sources)

**Success Criteria:**
- Hypothesis clearly validated or invalidated (no ambiguous results)
- All artifacts properly updated (Registry, Understanding, Architecture if applicable)
- Code properly integrated (if validated)
- Lessons captured for future cycles
- Experiment data captured and saved for reproducibility
- Documentation complete enough to reproduce later

**Instruction Style:**
- Overall: Mixed
- Creative steps (hypothesis generation, research direction): Intent-based
- Rigorous steps (checklists, validation, code review): Prescriptive
- Notes: Inner loops (review rejection) should be prescriptive with clear pass/fail criteria

---

## Tools Configuration

**Core BMAD Tools:**
- **Party Mode:** Included - Phase 1 (hypothesis brainstorming with multiple AI perspectives)
- **Advanced Elicitation:** Included - Phase 1 (stress-test hypothesis) + Phase 5 (deep result analysis)
- **Brainstorming:** Included - Phase 1 (candidate hypothesis generation)

**LLM Features:**
- **Web-Browsing:** Excluded - SOTA Synthesis doc provides sufficient research context
- **File I/O:** Included - Essential for all artifact operations (read/write all documents)
- **Sub-Agents:** Excluded - Each session is focused enough, no need for delegation within sessions
- **Sub-Processes:** Included - For running multiple experiments in parallel

**Memory:**
- Type: Single-session per step, artifacts are memory
- Core state documents:
  - Current Understanding Document (evolving knowledge base)
  - Hypothesis Registry (experiment tracking)
  - Current Architecture Document (production system state)
- These link to individual experiment folders for detailed context
- No additional session-to-session memory needed within steps

**External Integrations:**
- None for now - file-based artifacts are sufficient
- Future consideration: Git integration, experiment tracking (W&B/MLflow)

**Installation Requirements:**
- None - all selected tools are built-in or file-based

---

## Workflow Design

### Architecture Overview

**Type:** Single orchestration workflow with step files as agent invocation specifications
**Session Model:** Each step runs as a separate session with fresh context
**Connective Tissue:** Artifacts (documents) serve as handoff between sessions
**Continuation:** Not needed within steps (single-session each)

### Step Structure (Create Mode - `steps-c/`)

| Step | File | Agent | Type | Interaction | Menu | Inner Loop |
|------|------|-------|------|-------------|------|------------|
| 1 | `step-01-hypothesis-design.md` | DS Agent | Middle (Standard) | Collaborative | A/P/C | No |
| 2 | `step-02-design-review.md` | DS Review | Branch | Autonomous | Auto/Loop | → Step 1 |
| 3 | `step-03-implementation.md` | Implementor | Middle (Simple) | Autonomous | C only | No |
| 4 | `step-04-code-review.md` | Code Review | Branch | Autonomous | Auto/Loop | → Step 3 |
| 5 | `step-05-execution.md` | DS Agent | Middle (Standard) | Auto→Collab | A/P/C | No |
| 6 | `step-06-integration.md` | Implementor | Final (Conditional) | Autonomous | Auto | VALIDATED only |

### Step Details

**Step 1: Hypothesis & Design**
- Agent: Data Scientist
- Inputs: Current Understanding, SOTA Synthesis, Hypothesis Registry, Competition Rules, Current Architecture
- Outputs: `experiments/{exp-id}/readme.md`, `experiments/{exp-id}/plan.md`
- Updates: Hypothesis Registry (new entry, status: PENDING)
- Tools: Brainstorming, Party Mode, Advanced Elicitation available

**Step 2: Design Review**
- Agent: DS Reviewer
- Inputs: `experiments/{exp-id}/readme.md`
- Outputs: APPROVED or REJECTED + feedback
- Subprocess: Pattern 2 (deep analysis of methodology soundness)
- Branch Logic: PASS → Step 3, FAIL → feedback for Step 1 redesign

**Step 3: Implementation**
- Agent: Implementor
- Inputs: `experiments/{exp-id}/plan.md`
- Outputs: Experiment code in specified locations
- Instruction Style: Prescriptive (follow plan.md exactly)

**Step 4: Code Review**
- Agent: Code Reviewer (Implementor role)
- Inputs: `experiments/{exp-id}/plan.md`, implemented code
- Outputs: APPROVED or REJECTED + feedback
- Subprocess: Pattern 1 (grep for undocumented changes)
- Branch Logic: PASS → Step 5, FAIL → feedback for Step 3 reimplementation

**Step 5: Execution & Evaluation**
- Agent: Data Scientist
- Inputs: `experiments/{exp-id}/`, implemented code
- Outputs: `experiments/{exp-id}/results.md`
- Updates: Hypothesis Registry (VALIDATED/INVALIDATED), Current Understanding
- Subprocess: Pattern 3 (load results, summarize findings)
- Tools: Advanced Elicitation available for deep result analysis

**Step 6: Integration (Conditional)**
- Agent: Implementor
- Condition: Only if Hypothesis Registry status == VALIDATED
- Inputs: Validated code, Current Architecture
- Outputs: Merged code to main codebase
- Updates: Current Architecture Document

### Edit Mode (`steps-e/`)

**Purpose:** Edit existing experiment definitions or revise hypotheses

| Step | File | Purpose |
|------|------|---------|
| 1 | `step-01-select-experiment.md` | Select experiment to edit from Registry |
| 2 | `step-02-edit-definition.md` | Modify readme.md, plan.md, or hypothesis |

### Validate Mode (`steps-v/`)

**Purpose:** Quality check completed experiments

| Step | File | Purpose |
|------|------|---------|
| 1 | `step-01-select-experiment.md` | Select experiment to validate from Registry |
| 2 | `step-02-quality-check.md` | Check documentation, reproducibility, metrics |

**Subprocess:** Pattern 4 (parallel checks for documentation, reproducibility, metrics)

### Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CORE DOCUMENTS                               │
│  Current Understanding ◄──┬──► Hypothesis Registry ◄──┬──► Current  │
│                           │                           │   Architecture│
└───────────────────────────┼───────────────────────────┼─────────────┘
                            │                           │
┌───────────────────────────▼───────────────────────────▼─────────────┐
│  Step 1: Hypothesis & Design (DS Agent - Collaborative)              │
│  ├── Reads: All core docs + SOTA + Competition Rules                 │
│  └── Writes: experiments/{exp-id}/readme.md, plan.md                 │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│  Step 2: Design Review (DS Review - Autonomous)                      │
│  ├── Reads: readme.md                                                │
│  └── Outputs: APPROVED ──► Step 3  OR  REJECTED ──► Back to Step 1   │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ (if APPROVED)
┌─────────────────────────────▼───────────────────────────────────────┐
│  Step 3: Implementation (Implementor - Autonomous)                   │
│  ├── Reads: plan.md                                                  │
│  └── Writes: Experiment code                                         │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│  Step 4: Code Review (Code Reviewer - Autonomous)                    │
│  ├── Reads: plan.md + code                                           │
│  └── Outputs: APPROVED ──► Step 5  OR  REJECTED ──► Back to Step 3   │
└─────────────────────────────┬───────────────────────────────────────┘
                              │ (if APPROVED)
┌─────────────────────────────▼───────────────────────────────────────┐
│  Step 5: Execution & Evaluation (DS Agent - Auto→Collaborative)      │
│  ├── Runs: Experiment                                                │
│  ├── Writes: results.md                                              │
│  └── Updates: Hypothesis Registry, Current Understanding             │
└─────────────────────────────┬───────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────┐
│  Step 6: Integration (Implementor - Conditional)                     │
│  ├── Condition: Only if VALIDATED                                    │
│  ├── Merges: Code to main codebase                                   │
│  └── Updates: Current Architecture                                   │
└─────────────────────────────────────────────────────────────────────┘
```

### File Structure

```
_bmad/bmds/workflows/experiment-cycle/
├── workflow.md
├── data/
│   ├── hypothesis-registry-template.md
│   ├── experiment-readme-template.md
│   ├── experiment-plan-template.md
│   ├── experiment-results-template.md
│   ├── current-understanding-template.md
│   ├── current-architecture-template.md
│   └── review-criteria.md
├── steps-c/
│   ├── step-01-hypothesis-design.md
│   ├── step-02-design-review.md
│   ├── step-03-implementation.md
│   ├── step-04-code-review.md
│   ├── step-05-execution.md
│   └── step-06-integration.md
├── steps-e/
│   ├── step-01-select-experiment.md
│   └── step-02-edit-definition.md
└── steps-v/
    ├── step-01-select-experiment.md
    └── step-02-quality-check.md
```

### Agent Roles & Personas

| Agent | Expertise | Tone | Instruction Style |
|-------|-----------|------|-------------------|
| Data Scientist | ML experimentation, hypothesis formulation, experimental design | Collaborative, curious, rigorous | Intent-based |
| DS Reviewer | Scientific methodology, experimental isolation, statistical validity | Critical, thorough, constructive | Prescriptive |
| Implementor | Code implementation, ML engineering, best practices | Precise, disciplined, follows spec exactly | Prescriptive |
| Code Reviewer | Code quality, spec alignment, correctness | Adversarial, detail-oriented | Prescriptive |

### Subprocess Optimization

| Step | Pattern | Application |
|------|---------|-------------|
| Step 2 | Pattern 2 (Deep Analysis) | Analyze readme.md for methodology soundness |
| Step 4 | Pattern 1 (Grep/Regex) | Search code for undocumented changes |
| Step 5 | Pattern 3 (Data Operations) | Load results, summarize key findings |
| Validate | Pattern 4 (Parallel) | Parallel checks for documentation, reproducibility, metrics |

### Inner Loop & Conditional Logic

**Step 2 (Design Review):**
```
IF review passes:
    └── Proceed to Step 3
ELSE:
    ├── Document issues in feedback file
    ├── Update experiment status: NEEDS_REVISION
    └── Human initiates new Step 1 session with feedback
```

**Step 4 (Code Review):**
```
IF review passes:
    └── Proceed to Step 5
ELSE:
    ├── Document issues in feedback file
    ├── Update experiment status: NEEDS_REIMPLEMENTATION
    └── Human initiates new Step 3 session with feedback
```

**Step 6 (Integration):**
```
IF Hypothesis Registry status == VALIDATED:
    └── Execute integration
ELSE:
    └── Skip integration, cycle complete
```

---

## Foundation Build Complete

**Created:**
- Folder structure at: `_bmad-output/bmb-creations/workflows/experiment-cycle/`
- `workflow.md` - Main orchestration with tri-modal routing
- `data/hypothesis-registry-template.md`
- `data/experiment-readme-template.md`
- `data/experiment-plan-template.md`
- `data/experiment-results-template.md`
- `data/current-understanding-template.md`
- `data/current-architecture-template.md`
- `data/review-criteria.md`
- `steps-c/` folder (empty, ready for step files)
- `steps-e/` folder (empty, ready for step files)
- `steps-v/` folder (empty, ready for step files)

**Configuration:**
- Workflow name: experiment-cycle
- Continuable: No (single-session per step, artifacts are handoff)
- Document output: Yes (7 structured templates)
- Mode: Tri-modal (Create + Edit + Validate)

**Next Steps:**
- Step 8: Build step-01-hypothesis-design.md (Create mode)
- Step 9+: Build remaining step files

---

## Step 01 Build Complete

**Created:**
- `steps-c/step-01-hypothesis-design.md`

**Step Configuration:**
- Type: Non-continuable (single-session, artifact handoff)
- Input Discovery: No (documents expected to exist)
- Menu: B/A/P/C (Brainstorming, Advanced Elicitation, Party Mode, Continue)
- Agent Role: Data Scientist (collaborative hypothesis formulation)
- Next Step: step-02-design-review.md

**Key Features:**
- Loads and reviews all 5 core documents before hypothesis generation
- Collaborative research direction identification
- Rigorous hypothesis formulation (falsifiable, isolated, motivated)
- Creates experiment folder with readme.md and plan.md
- Self-checks against review criteria before proceeding
- All paths must be exact and verifiable

---

## All Remaining Steps Build Complete

### Create Mode Steps (steps-c/)

**Step 02: Design Review**
- File: `steps-c/step-02-design-review.md`
- Agent: DS Reviewer
- Type: Branch step (APPROVED → Step 3, REJECTED → feedback for Step 1)
- Subprocess: Pattern 2 (deep analysis of methodology soundness)
- Key Features:
  - Loads review criteria and experiment readme
  - Uses subprocess for deep methodology analysis
  - Provides structured feedback on rejection
  - Updates Registry status to NEEDS_REVISION if rejected

**Step 03: Implementation**
- File: `steps-c/step-03-implementation.md`
- Agent: Implementor
- Type: Autonomous (C-only menu)
- Key Features:
  - Follows plan.md exactly, no undocumented changes
  - Runs all checklists from plan before completion
  - Commits with experiment ID reference

**Step 04: Code Review**
- File: `steps-c/step-04-code-review.md`
- Agent: Code Reviewer
- Type: Branch step (APPROVED → Step 5, REJECTED → feedback for Step 3)
- Subprocess: Pattern 1 (grep/regex for undocumented changes)
- Key Features:
  - Compares implemented code against plan.md spec
  - Detects undocumented changes (files, parameters, etc.)
  - Updates Registry status to NEEDS_REIMPLEMENTATION if rejected

**Step 05: Execution & Evaluation**
- File: `steps-c/step-05-execution.md`
- Agent: Data Scientist
- Type: Autonomous → Collaborative result discussion
- Subprocess: Pattern 3 (load and summarize results)
- Key Features:
  - Runs experiment with documented commands
  - Creates results.md with metrics, verdicts, lessons
  - Updates Registry (VALIDATED/INVALIDATED)
  - Updates Current Understanding with lessons learned
  - Advanced Elicitation available for deep result analysis

**Step 06: Integration (Conditional)**
- File: `steps-c/step-06-integration.md`
- Agent: Implementor
- Type: Conditional (only executes if VALIDATED)
- Key Features:
  - Checks Registry status first
  - Merges code to main with experiment ID reference
  - Promotes checkpoint and config to production locations
  - Updates Current Architecture with validated changes
  - Complete cycle summary provided

### Edit Mode Steps (steps-e/)

**Step 01: Select Experiment**
- File: `steps-e/step-01-select-experiment.md`
- Purpose: Load Registry and present experiments for editing
- Key Features:
  - Shows all experiments with ID, title, status
  - User selects by ID
  - Offers edit type: Hypothesis/Design/Plan

**Step 02: Edit Definition**
- File: `steps-e/step-02-edit-definition.md`
- Purpose: Collaboratively edit selected aspect of experiment
- Key Features:
  - Loads current state based on edit type
  - Collaborative editing with user
  - Validates edits against review criteria
  - Updates Registry if hypothesis changed

### Validate Mode Steps (steps-v/)

**Step 01: Select Experiment**
- File: `steps-v/step-01-select-experiment.md`
- Purpose: Select completed experiment for quality validation
- Key Features:
  - Filters to show only VALIDATED/INVALIDATED experiments
  - User selects by ID

**Step 02: Quality Check**
- File: `steps-v/step-02-quality-check.md`
- Purpose: Comprehensive quality validation
- Subprocess: Pattern 4 (parallel checks)
- Key Features:
  - Documentation Completeness check
  - Reproducibility check (paths, seeds, commands)
  - Traceability check (commits, Registry, docs)
  - Metrics Integrity check (datasets, calculations, verdicts)
  - Aggregated validation report with PASS/CONCERNS/FAIL verdict
  - Actionable recommendations for issues

---

## Build Summary

**Total Files Created:** 17

**workflow.md** - Main orchestration with tri-modal routing

**Data Templates (7):**
- hypothesis-registry-template.md
- experiment-readme-template.md
- experiment-plan-template.md
- experiment-results-template.md
- current-understanding-template.md
- current-architecture-template.md
- review-criteria.md

**Create Mode Steps (6):**
- step-01-hypothesis-design.md
- step-02-design-review.md
- step-03-implementation.md
- step-04-code-review.md
- step-05-execution.md
- step-06-integration.md

**Edit Mode Steps (2):**
- step-01-select-experiment.md
- step-02-edit-definition.md

**Validate Mode Steps (2):**
- step-01-select-experiment.md
- step-02-quality-check.md

**Workflow Status:** BUILD_COMPLETE
