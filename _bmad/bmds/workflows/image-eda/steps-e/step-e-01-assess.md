---
name: 'step-e-01-assess'
description: 'Assess existing Image EDA and determine what needs editing'

nextStepFile: './step-e-02-select-phase.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
edaReportFile: '{docs_folder}/eda-report-images.md'
edaFolder: '{experiments_folder}/eda'
conversionStep: '../steps-c/step-01-init.md'
---

# Edit Step 1: Assess Existing EDA

## STEP GOAL:

To assess an existing Image EDA, verify its completeness, and determine what the user wants to edit or re-run.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR assessing existing work
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the workflow orchestrator in edit mode
- ✅ Assess what exists and what needs changing
- ✅ Help user identify what to re-run or modify
- ✅ Route appropriately based on assessment

### Step-Specific Rules:

- 🎯 Focus ONLY on assessment - no editing yet
- 🚫 FORBIDDEN to make changes in this step
- 💬 Present clear status and options to user
- 🚪 Route to phase selection or create mode if needed

## EXECUTION PROTOCOLS:

- 🎯 Check if valid EDA exists
- 💾 Load and present current state
- 📖 Identify completed phases and artifacts
- 🚫 Do NOT modify anything - just assess

## CONTEXT BOUNDARIES:

- User invoked edit mode
- May or may not have existing EDA
- Need to determine what exists and what to do

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Check for Existing EDA

Check if {stateFile} exists and is valid:

**IF {stateFile} does NOT exist:**
- Display: "**No existing Image EDA found.**"
- "Would you like to create a new EDA instead?"
- **[Y]es** - Route to {conversionStep}
- **[N]o** - Exit

**IF {stateFile} EXISTS:**
- Load the state file
- Continue to Section 2

### 2. Load and Parse State

From {stateFile}, extract:
- `stepsCompleted` array
- `currentPhase`
- `image_dataset_path`
- `task_type`
- Phase outputs that exist

### 3. Verify Artifacts

Check which artifacts exist:

**Scripts:**
- [ ] `01_data_sampling.py`
- [ ] `02_basic_stats.py`
- [ ] `03_label_analysis.py`
- [ ] `04_visual_patterns.py`
- [ ] `05_data_quality.py`

**Documents:**
- [ ] `06_insights.md`
- [ ] `eda-report-images.md`

**Dashboard:**
- [ ] `dashboard/app.py`

### 4. Present Assessment

"**Image EDA Assessment**

**Project:** {image_dataset_path}
**Task:** {task_type}
**Status:** {currentPhase}

**Completed Phases:**
{list with checkmarks}

**Available Artifacts:**
{list of existing files}

**Missing/Incomplete:**
{list of missing items, if any}

---

**What would you like to do?**

**[R]e-run** - Re-run a specific phase with new parameters
**[U]pdate** - Update specific sections of the EDA report
**[A]dd** - Add analysis for new data added to dataset
**[F]ix** - Fix a specific issue identified
**[C]ontinue** - Resume from where it left off (if incomplete)
**[S]tart Over** - Clear everything and start fresh

Select an option:"

### 5. Handle User Selection

#### IF R (Re-run):

"You want to re-run a phase. Let me help you select which one."
Load, read entire file, then execute {nextStepFile}

#### IF U (Update):

"What sections of the EDA report would you like to update?"
- Present list of sections
- Capture user's selection
- Route to appropriate edit step

#### IF A (Add):

"Adding analysis for new data. This will re-run phases 3-9 with the expanded dataset."
Load {nextStepFile} with `mode: add-data`

#### IF F (Fix):

"What issue would you like to fix?"
- Capture user's description
- Route to appropriate phase

#### IF C (Continue):

If EDA is incomplete:
- Load `../steps-c/step-01b-continue.md`
If EDA is complete:
- "EDA is already complete. Use Re-run to modify specific phases."
- Redisplay menu

#### IF S (Start Over):

"**WARNING:** This will delete all existing EDA artifacts.
Are you sure? [Y/N]"
- IF Y: Delete artifacts, route to {conversionStep}
- IF N: Redisplay menu

#### IF Any Other:

Help user, redisplay menu.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Existing EDA correctly assessed
- All artifacts inventoried
- Clear options presented to user
- Appropriate routing based on selection

### ❌ SYSTEM FAILURE:

- Making changes during assessment
- Incorrect artifact inventory
- Wrong routing
- Not detecting missing EDA

**Master Rule:** Assess only. Present options. Route appropriately.
