---
stepsCompleted: ['step-01-discovery', 'step-02-classification', 'step-03-requirements', 'step-04-tools', 'step-05-plan-review', 'step-06-design', 'step-07-foundation', 'step-08-build-step-01', 'step-09-build-remaining-steps']
created: 2026-01-19
status: COMPLETE
approvedDate: 2026-01-19
completedDate: 2026-01-19
workflowName: project-setup
targetPath: _bmad/kagglai/workflows/project-setup/
---

# Workflow Creation Plan

## Discovery Notes

**User's Vision:**
A rigorous, repeatable project initialization pipeline for Kaggle/ML competitions that front-loads discovery to prevent expensive rework later. The workflow coordinates multiple specialized agents (Data Analyst, Researcher, Implementation) with an Author/Validator pattern where fresh agent instances review each artifact to catch missed details.

**Who It's For:**
Solo practitioner (the user themselves) - standardizing their own competition setup process.

**What It Produces:**
1. **Standardized documents** - Challenge spec, EDA report, SoTA summary, research directions, technical spec
2. **Working infrastructure** - Pluggable pipeline for experimentation
3. **Valid submission** - Ready to upload to competition website

**Key Insights:**

1. **Pain Point:** Tedium of repetitive setup + missing critical details (e.g., compute constraints) that cause late-stage rework

2. **Author/Validator Pattern:** Each major artifact is authored by one agent instance, then validated by a fresh instance to catch omissions

3. **Context Freshness:** Multi-session splits (especially EDA) are architectural guardrails to keep agents producing quality output - not human checkpoints

4. **Sequencing Matters:** EDA comes before SoTA research so the Researcher understands actual data characteristics before surveying techniques

5. **Researcher Capabilities:** Can use user-provided papers AND search the web independently based on challenge + EDA findings

**Workflow Phases (Revised Order):**

| Phase | Agent | Sessions | Output |
|-------|-------|----------|--------|
| 1. Challenge Spec | Data Analyst (author) → Data Analyst (validator) | 2 | challenge_spec.md |
| 2. EDA | Data Analyst | 2 (context split) | eda_report.md |
| 3. SoTA Summary | Researcher (author) → Researcher (validator) | 2 | state_of_the_art_summary.md |
| 4. Research Directions | Researcher | 1 | research_directions.md |
| 5. Technical Spec | Implementation (author) → Implementation (validator) | 2 | technical_spec.md |
| 6. Implementation | Implementation | 1+ | Working codebase + submission |
| 7. Code Review | Implementation (reviewer) | 1 | Review notes + fixes |

**End State Vision:**
- Single source of truth for challenge requirements
- Validated understanding of state-of-the-art
- Clear, ranked research directions grounded in data reality
- Minimal end-to-end working submission
- Infrastructure structured for plug-and-play experimentation

---

## Classification Decisions

**Workflow Name:** project-setup
**Target Path:** _bmad/kagglai/workflows/project-setup/

**4 Key Decisions:**
1. **Document Output:** true (produces multiple spec documents + code)
2. **Module Affiliation:** kagglai (sits alongside experiment-cycle)
3. **Session Type:** continuable (spans multiple sessions, context-fresh design)
4. **Lifecycle Support:** tri-modal (create + edit + validate)

**Structure Implications:**
- Needs `steps-c/`, `steps-e/`, `steps-v/` folders
- Needs `step-01b-continue.md` for continuation support
- Needs `stepsCompleted` tracking in output frontmatter
- Needs templates for each output document
- Will coordinate with existing kagglai agents (data-analyst, researcher, implementer)
- Precursor to experiment-cycle workflow

---

## Requirements

**Flow Structure:**
- Pattern: Linear with internal Author→Validator→Fix cycles
- Strictly sequential (each phase needs outputs from previous)
- Validation: Validator produces report → same or new instance implements fixes
- No parallelism between phases

**Phases:**
1. Challenge Spec (Author → Validator → Fix)
2. EDA (Session 1: pull data + basic stats → Session 2: deep dive patterns)
3. SoTA Summary (Author → Validator → Fix)
4. Research Directions (collaborative)
5. Technical Spec (Author → Validator → Fix)
6. Implementation (autonomous)
7. Code Review (autonomous → fixes)

**User Interaction:**
- Style: Mixed
  - Collaborative: EDA interpretation, Research Directions
  - Autonomous: Challenge Spec synthesis, SoTA synthesis, Technical Spec, Implementation, Code Review
- Decision points: Research direction prioritization, EDA pattern interpretation
- Checkpoint frequency: Between phases (artifact review)

**Inputs Required:**
- Required: Challenge definition docs in `_kagglai/challenge-inputs/`
  - description.md
  - rules.md
  - data-access.md
  - submission-format.md
- Optional: Research papers in `_kagglai/challenge-inputs/papers/`
- Agent behavior: Researcher searches web regardless of provided papers

**Folder Structure (aligned with experiment-cycle):**
```
_kagglai/
├── challenge-inputs/             # Raw materials (user provides)
│   ├── description.md
│   ├── rules.md
│   ├── data-access.md
│   ├── submission-format.md
│   └── papers/
├── docs/                         # Generated artifacts
│   ├── challenge-spec.md
│   ├── eda-report.md
│   ├── sota-synthesis.md
│   ├── research-directions.md
│   ├── technical-spec.md
│   ├── current-understanding.md  # Initialized for experiment-cycle
│   ├── current-architecture.md   # Initialized for experiment-cycle
│   └── hypothesis-registry.md    # Initialized for experiment-cycle
├── data/                         # Standard data location
│   ├── raw/                      # Original downloaded data
│   ├── processed/                # Cleaned/transformed data
│   └── splits/                   # Train/val/test splits
├── models/                       # Standard models location
│   ├── checkpoints/              # Training checkpoints
│   ├── submissions/              # Models used for submissions
│   └── baselines/                # Baseline model artifacts
├── src/                          # Implementation code
└── experiments/                  # For experiment-cycle
```

**EDA Session 1 Data Pull Responsibility:**
- Check if data exists at `_kagglai/data/raw/`
- If not present, pull/download per instructions in `challenge-inputs/data-access.md`
- Validate data integrity (checksums, expected files)
- Then proceed with basic statistics

**Handoff Documents (initialized by project-setup for experiment-cycle):**
| Document | Initialized By | Phase |
|----------|----------------|-------|
| current-architecture.md | Implementer | After implementation |
| current-understanding.md | Data Analyst + Researcher | After EDA + SoTA |
| hypothesis-registry.md | Data Analyst + Researcher | After research directions |

**Output Specifications:**
- Type: Multiple documents + code
- Format: Semi-structured (required sections + flexible fields like "Additional Notes")
- Templates needed for: challenge-spec, eda-report, sota-synthesis, research-directions, technical-spec

**Success Criteria:**
| Phase | Success Looks Like |
|-------|-------------------|
| Challenge Spec | All constraints captured, no ambiguity, validator found no omissions |
| EDA | Data fully characterized, patterns identified, quality issues documented |
| SoTA | Techniques surveyed, benchmarks noted, gaps identified |
| Research Directions | Ranked list grounded in data reality + SoTA, actionable |
| Technical Spec | Clear implementation path, all dependencies identified |
| Implementation | Valid submission generated, baseline score obtained |
| Code Review | Code clean, reproducible, pluggable for experiments |

**Overall Success:**
- Valid submission uploaded to competition
- All docs populated and consistent
- Handoff docs ready for experiment-cycle
- Infrastructure supports plug-and-play experimentation

**Instruction Style:**
- Overall: Mixed (prescriptive for execution, intent-based for creative/strategic)

| Phase | Style | Rationale |
|-------|-------|-----------|
| Challenge Spec (Author) | Prescriptive | Systematic extraction, don't miss fields |
| Challenge Spec (Validator) | Prescriptive | Checklist-based validation |
| EDA Session 1 | Prescriptive | Standard stats, consistent structure |
| EDA Session 2 | Intent-based | Creative pattern discovery |
| SoTA (Author) | Mixed | Systematic search + synthesis judgment |
| SoTA (Validator) | Prescriptive | Verify sources, check completeness |
| Research Directions | Intent-based | Strategic thinking, collaborative |
| Technical Spec | Prescriptive | Clear implementation steps |
| Implementation | Prescriptive | Execute the plan |
| Code Review | Prescriptive | Checklist-based review |

---

## Tools Configuration

**Core BMAD Tools:**
| Tool | Status | Integration Points |
|------|--------|-------------------|
| Party Mode | Included | Phase 5 (Research Directions), Phase 8 (Code Review) |
| Advanced Elicitation | Included | Phase 3 (EDA Session 2), Phase 5 (Research Directions) |
| Brainstorming | Included | Phase 5 (Research Directions) |

**LLM Features:**
| Feature | Status | Use Case |
|---------|--------|----------|
| Web-Browsing | Included | Phase 3 (EDA - external data), Phase 4 (SoTA Research) |
| File I/O | Included | Essential throughout all phases |
| Sub-Agents | Excluded | Manual orchestration with existing kagglai agents |
| Sub-Processes | Excluded | No parallelism needed |

**Memory:**
- Type: Continuable
- Tracking: `stepsCompleted`, `lastStep` in frontmatter
- Sidecar files: Included for phase tracking, validation reports, session notes

**External Integrations:**
- None required

**Orchestration Model:**
- Manual session switching between phases/agents
- Workflow provides step files with agent instructions
- Artifacts (docs) serve as handoff mechanism
- User invokes specified agent for each step

**Template Requirements:**
- Handoff docs: Use existing experiment-cycle templates
  - `current-understanding-template.md`
  - `current-architecture-template.md`
  - `hypothesis-registry-template.md`
- New templates to create:
  - `challenge-spec-template.md`
  - `eda-report-template.md`
  - `sota-synthesis-template.md`
  - `research-directions-template.md`
  - `technical-spec-template.md`

---

## Workflow Design

### Step Structure

**Create Mode (steps-c/) - 18 files:**

| Step | Name | Agent | Purpose | Menu | Outputs/Updates |
|------|------|-------|---------|------|-----------------|
| 01 | init | — | Create folder structure, check inputs, create sidecar | Auto-proceed | Folder structure, sidecar |
| 01b | continue | — | Handle workflow continuation | Auto-proceed | — |
| 02 | challenge-spec | Data Analyst | Author challenge spec from inputs | C only | challenge-spec.md |
| 03 | challenge-spec-review | Data Analyst | Validate + fix (or route to 03b) | C / F | current-understanding.md §1 |
| 03b | challenge-spec-fix | Data Analyst | Fix-only if review context too big | C only | — |
| 04 | eda-basic | Data Analyst | Pull data, basic stats | C only | eda-report.md (initial), data/raw/ |
| 05 | eda-deep | Data Analyst | Deep dive patterns, insights | A/P/C | eda-report.md (complete), current-understanding.md §2 |
| 06 | sota-research | Researcher | Survey papers + web, synthesize | C only | sota-synthesis.md |
| 07 | sota-review | Researcher | Validate + fix (or route to 07b) | C / F | current-understanding.md §3 |
| 07b | sota-fix | Researcher | Fix-only if review context too big | C only | — |
| 08 | research-directions | Researcher | Create ranked directions | A/P/C | research-directions.md, hypothesis-registry.md |
| 09 | technical-spec | Implementer | Author tech spec from all docs | C only | technical-spec.md |
| 10 | technical-spec-review | Implementer | Validate + fix (or route to 10b) | C / F | — |
| 10b | technical-spec-fix | Implementer | Fix-only if review context too big | C only | — |
| 11 | implementation | Implementer | Build baseline pipeline | C only | src/, models/, submission |
| 12 | code-review | Implementer | Review + fix (or route to 12b) | A/P/C | current-architecture.md |
| 12b | code-fix | Implementer | Fix-only if review context too big | C only | — |
| 13 | complete | — | Verify all docs, summary | — | — |

**Edit Mode (steps-e/) - 3 files:**

| Step | Name | Purpose |
|------|------|---------|
| e-01 | assess | Load workflow state, assess what needs editing |
| e-02 | select-phase | Choose which phase/document to edit |
| e-03 | apply-edit | Make edits to selected document |

**Validate Mode (steps-v/) - 1 file:**

| Step | Name | Purpose |
|------|------|---------|
| v-01 | validate | Comprehensive validation of all artifacts |

### current-understanding.md Section Mapping

| Section | Filled By | Step |
|---------|-----------|------|
| §1 Problem & Task | Challenge Spec Review | step-03 |
| §2 Data | EDA Deep | step-05 |
| §3 Model/Research | SoTA Review | step-07 |

### Data Flow

```
challenge-inputs/
       │
       ▼
[02 challenge-spec] ──► challenge-spec.md
       │
       ▼
[03 challenge-spec-review] ──► current-understanding.md §1
       │
       ▼
[04 eda-basic] ◄── data-access.md
       │
       ▼
data/raw/ + eda-report.md (initial)
       │
       ▼
[05 eda-deep] ──► eda-report.md + current-understanding.md §2
       │
       ▼
[06 sota-research] ◄── papers/ + web
       │
       ▼
sota-synthesis.md
       │
       ▼
[07 sota-review] ──► current-understanding.md §3
       │
       ▼
[08 research-directions] ──► research-directions.md + hypothesis-registry.md
       │
       ├── challenge-spec.md
       ├── eda-report.md
       ├── sota-synthesis.md
       ▼
[09 technical-spec] ──► technical-spec.md
       │
       ▼
[11 implementation] ──► src/ + models/ + submission
       │
       ▼
[12 code-review] ──► current-architecture.md
       │
       ▼
[13 complete] ──► Ready for experiment-cycle
```

### File Structure

```
_bmad/kagglai/workflows/project-setup/
├── workflow.md                          # Entry point with mode routing
├── data/                                # Shared standards and templates
│   ├── challenge-spec-template.md
│   ├── eda-report-template.md
│   ├── sota-synthesis-template.md
│   ├── research-directions-template.md
│   ├── technical-spec-template.md
│   ├── validation-checklist.md
│   └── review-criteria.md
├── steps-c/                             # Create mode (18 files)
│   ├── step-01-init.md
│   ├── step-01b-continue.md
│   ├── step-02-challenge-spec.md
│   ├── step-03-challenge-spec-review.md
│   ├── step-03b-challenge-spec-fix.md
│   ├── step-04-eda-basic.md
│   ├── step-05-eda-deep.md
│   ├── step-06-sota-research.md
│   ├── step-07-sota-review.md
│   ├── step-07b-sota-fix.md
│   ├── step-08-research-directions.md
│   ├── step-09-technical-spec.md
│   ├── step-10-technical-spec-review.md
│   ├── step-10b-technical-spec-fix.md
│   ├── step-11-implementation.md
│   ├── step-12-code-review.md
│   ├── step-12b-code-fix.md
│   └── step-13-complete.md
├── steps-e/                             # Edit mode (3 files)
│   ├── step-e-01-assess.md
│   ├── step-e-02-select-phase.md
│   └── step-e-03-apply-edit.md
└── steps-v/                             # Validate mode (1 file)
    └── step-v-01-validate.md
```

### Agent Role Mapping

| Agent | Steps | Communication Style |
|-------|-------|---------------------|
| Data Analyst | 02, 03, 03b, 04, 05 | Precise, data-driven, highlights uncertainties |
| Researcher | 06, 07, 07b, 08 | Academic, thorough, cites sources |
| Implementer | 09, 10, 10b, 11, 12, 12b | Direct, practical, focuses on working code |

### Interaction Patterns

| Pattern | Steps | Description |
|---------|-------|-------------|
| Auto-proceed | 01, 01b | Setup steps, no user choice needed |
| C only | 02, 03b, 04, 06, 07b, 09, 10b, 11, 12b | Autonomous work, continue when done |
| C / F | 03, 07, 10, 12 | Review steps with fix-only escape hatch |
| A/P/C | 05, 08, 12 | Collaborative steps with creative tools |

### Validation and Error Handling

| Scenario | Handling |
|----------|----------|
| Missing challenge-inputs/ | Init step errors with clear guidance |
| Data pull fails | eda-basic retries or asks for manual intervention |
| Validation finds issues | Review step fixes or routes to fix-only step |
| Context too big | User exits, invokes fix-only step with validation report |
| Implementation fails | Code review identifies issues, fix step addresses |

### Continuation Support

- **Sidecar file:** `_kagglai/docs/.project-setup-sidecar.md`
- **Tracking:** `stepsCompleted` array, `lastStep`, `lastUpdated`
- **Resume:** step-01b-continue reads sidecar, routes to appropriate step

### Workflow Chaining

| Position | Workflow | Handoff |
|----------|----------|---------|
| Before | None | User provides challenge-inputs/ |
| After | experiment-cycle | current-understanding, current-architecture, hypothesis-registry |

---

## Foundation Build Complete

**Created:**
- Folder structure at: `_bmad/kagglai/workflows/project-setup/`
  - `steps-c/` (create mode)
  - `steps-e/` (edit mode)
  - `steps-v/` (validate mode)
  - `data/` (shared standards)
  - `templates/` (document templates)
- `workflow.md` - Main entry point with tri-modal routing

**Templates Created:**
| Template | Location |
|----------|----------|
| challenge-spec-template.md | templates/ |
| eda-report-template.md | templates/ |
| sota-synthesis-template.md | templates/ |
| research-directions-template.md | templates/ |
| technical-spec-template.md | templates/ |

**Data Files Created:**
| File | Purpose |
|------|---------|
| validation-checklist.md | Comprehensive validation criteria |
| review-criteria.md | Standards for Author/Validator reviews |

**Configuration:**
- Workflow name: project-setup
- Continuable: yes
- Document output: yes (multiple)
- Mode: tri-modal (create + edit + validate)

**Next Steps:**
- Step 8: Build step-01-init.md (and step-01b-continue.md)
- Step 9+: Build remaining steps (repeatable for each step)

---

## Step 01 Build Complete

**Created:**
- `steps-c/step-01-init.md` - Initialize project structure, verify inputs, create sidecar
- `steps-c/step-01b-continue.md` - Handle workflow continuation from previous session

**Step Configuration:**
- Type: Continuable (with continuation detection)
- Input Discovery: No (user provides challenge-inputs directly)
- Menu: Auto-proceed (no user choice needed after init)
- Next Step: step-02-challenge-spec

**Step 01 Features:**
- Creates full `_kagglai/` folder structure if not exists
- Verifies required input files in `challenge-inputs/`
- Creates sidecar file for state tracking
- Routes to step-01b-continue if existing workflow detected

**Step 01b Features:**
- Reads sidecar to determine progress
- Displays progress summary
- Routes to correct next step based on last completed step
- Handles special cases (complete workflow, review steps)

**Remaining Steps to Build:**
| Mode | Count | Steps |
|------|-------|-------|
| Create | 16 | 02, 03, 03b, 04, 05, 06, 07, 07b, 08, 09, 10, 10b, 11, 12, 12b, 13 |
| Edit | 3 | e-01, e-02, e-03 |
| Validate | 1 | v-01 |
| **Total** | **20** | |

---

## All Steps Build Complete

**All 22 step files have been created successfully!**

### Create Mode Steps (18 files)

| File | Purpose |
|------|---------|
| step-01-init.md | Initialize project structure, verify inputs, create sidecar |
| step-01b-continue.md | Handle workflow continuation from previous session |
| step-02-challenge-spec.md | Data Analyst authors challenge spec from inputs |
| step-03-challenge-spec-review.md | Fresh Data Analyst validates + fixes (or routes to 03b) |
| step-03b-challenge-spec-fix.md | Fix-only step for challenge spec |
| step-04-eda-basic.md | Data Analyst pulls data, generates basic statistics |
| step-05-eda-deep.md | Data Analyst deep-dive patterns, insights (collaborative) |
| step-06-sota-research.md | Researcher surveys papers + web, synthesizes |
| step-07-sota-review.md | Fresh Researcher validates + fixes (or routes to 07b) |
| step-07b-sota-fix.md | Fix-only step for SoTA synthesis |
| step-08-research-directions.md | Researcher creates ranked directions (collaborative) |
| step-09-technical-spec.md | Implementer authors tech spec from all docs |
| step-10-technical-spec-review.md | Fresh Implementer validates + fixes (or routes to 10b) |
| step-10b-technical-spec-fix.md | Fix-only step for technical spec |
| step-11-implementation.md | Implementer builds baseline pipeline |
| step-12-code-review.md | Fresh Implementer reviews code (or routes to 12b) |
| step-12b-code-fix.md | Fix-only step for code |
| step-13-complete.md | Verify all docs, generate summary, handoff to experiment-cycle |

### Edit Mode Steps (3 files)

| File | Purpose |
|------|---------|
| step-e-01-assess.md | Load workflow state, assess what needs editing |
| step-e-02-select-phase.md | Choose which phase/document to edit |
| step-e-03-apply-edit.md | Make edits to selected document |

### Validate Mode Step (1 file)

| File | Purpose |
|------|---------|
| step-v-01-validate.md | Comprehensive validation of all artifacts |

---

## Workflow Creation Summary

**Total Files Created:** 30+

### Workflow Structure
```
_bmad/kagglai/workflows/project-setup/
├── workflow.md                    # Entry point with tri-modal routing
├── templates/                     # 5 document templates
│   ├── challenge-spec-template.md
│   ├── eda-report-template.md
│   ├── sota-synthesis-template.md
│   ├── research-directions-template.md
│   └── technical-spec-template.md
├── data/                          # 2 shared data files
│   ├── validation-checklist.md
│   └── review-criteria.md
├── steps-c/                       # 18 create mode steps
├── steps-e/                       # 3 edit mode steps
└── steps-v/                       # 1 validate mode step
```

### Key Features Implemented
- **Tri-modal operation:** Create, Edit, Validate modes
- **Author/Validator pattern:** Fresh instances review each artifact
- **Fix-only escape hatch:** Handle large context situations
- **Continuation support:** Resume from any point via sidecar file
- **Handoff documents:** Initialize experiment-cycle workflow docs
- **Collaborative tools:** Party Mode, Advanced Elicitation, Brainstorming where appropriate

### Workflow Flow
1. **Init** → Verify inputs, create folder structure
2. **Challenge Spec** → Author → Review/Fix
3. **EDA** → Basic stats → Deep dive (2 sessions for context freshness)
4. **SoTA** → Research → Review/Fix
5. **Research Directions** → Collaborative prioritization
6. **Technical Spec** → Author → Review/Fix
7. **Implementation** → Build baseline
8. **Code Review** → Review/Fix
9. **Complete** → Verify all, handoff to experiment-cycle

**STATUS: WORKFLOW CREATION COMPLETE**
