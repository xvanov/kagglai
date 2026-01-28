---
name: 'step-01b-continue'
description: 'Handle workflow continuation from previous session - route to appropriate phase'

stateFile: '{experiments_folder}/.image-eda-state.yaml'
outputFile: '{docs_folder}/eda-report-images.md'

# Step routing map
step02File: './step-02-data-acquisition.md'
step03File: './step-03-basic-stats.md'
step04File: './step-04-label-analysis.md'
step05File: './step-05-visual-patterns.md'
step06File: './step-06-data-quality.md'
step07File: './step-07-insights.md'
step08File: './step-08-dashboard.md'
step09File: './step-09-model-selection.md'
step10File: './step-10-completion.md'
---

# Step 1b: Continue Image EDA Workflow

## STEP GOAL:

To resume the Image EDA workflow from where it was left off in a previous session, routing to the correct next phase.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the workflow orchestrator resuming a previous session
- ✅ Read the state file to understand progress
- ✅ Route to the correct next phase
- ✅ Give user option to restart or re-run specific phases

### Step-Specific Rules:

- 🎯 Focus ONLY on reading state and routing
- 🚫 FORBIDDEN to perform analysis - just route
- 💬 Summarize progress and offer options
- 🚪 This step determines where to continue

## EXECUTION PROTOCOLS:

- 🎯 Load state file and determine last completed step
- 💾 Present progress summary to user
- 📖 Offer continuation options
- 🚫 Do NOT modify state - just read and route

## CONTEXT BOUNDARIES:

- User has run this workflow before
- State file exists with stepsCompleted array
- Need to route to the correct next phase
- May offer to re-run phases if user wants

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome Back

"**Welcome back to the Image EDA Workflow!**

Let me check where we left off..."

### 2. Load State File

Load and parse {stateFile}:
- Read `stepsCompleted` array
- Read `currentPhase`
- Read project configuration (dataset path, label format, etc.)
- Read any phase outputs that exist

### 3. Determine Progress

**Map stepsCompleted to phases:**

| Steps Completed | Current Phase | Next Phase |
|-----------------|---------------|------------|
| step-01-init | Initialization | Phase 2 or 3 |
| step-02-data-acquisition | Data Acquisition | Phase 3 |
| step-03-basic-stats | Basic Statistics | Phase 4 |
| step-04-label-analysis | Label Analysis | Phase 5 |
| step-05-visual-patterns | Visual Patterns | Phase 6 |
| step-06-data-quality | Data Quality | Phase 7 |
| step-07-insights | Insights | Phase 8 |
| step-08-dashboard | Dashboard | Phase 9 |
| step-09-model-selection | Model Selection | Phase 10 |

Identify:
- `last_completed_step`
- `next_step_to_run`
- `phases_with_outputs` (which phases have memory files)

### 4. Present Progress Summary

"**Workflow Progress Summary**

**Project:** {image_dataset_path}
**Task:** {task_type}
**Label Format:** {label_format}

**Completed Phases:**
{list of completed phases with checkmarks}

**Next Phase:** {next phase name and description}

**Phase Outputs Available:**
{list of phases with memory files that can be reviewed}

---

**Options:**

**[C]ontinue** - Proceed to {next phase name}
**[R]eview** - Review output from a completed phase
**[E]dit** - Re-run a specific phase (will switch to edit mode)
**[S]tart Over** - Reset and start fresh (WARNING: clears progress)

What would you like to do?"

### 5. Handle User Selection

#### IF C (Continue):

Determine next step file based on `last_completed_step`:

| Last Completed | Load This File |
|----------------|----------------|
| step-01-init (skip_data_acquisition=false) | {step02File} |
| step-01-init (skip_data_acquisition=true) | {step03File} |
| step-02-data-acquisition | {step03File} |
| step-03-basic-stats | {step04File} |
| step-04-label-analysis | {step05File} |
| step-05-visual-patterns | {step06File} |
| step-06-data-quality | {step07File} |
| step-07-insights | {step08File} |
| step-08-dashboard | {step09File} |
| step-09-model-selection | {step10File} |

Display: "Continuing to {next phase name}..."
Load, read entire file, then execute the appropriate step file.

#### IF R (Review):

"Which phase output would you like to review?
{numbered list of phases with outputs}

Enter phase number:"

Display the requested phase output file content.
After review, return to menu in Section 4.

#### IF E (Edit):

"Switching to edit mode...

To re-run a specific phase, the edit workflow will help you select and modify."

Load `../steps-e/step-e-01-assess.md` to enter edit mode.

#### IF S (Start Over):

"**WARNING:** This will clear all progress and phase outputs.

Are you sure you want to start over? [Y/N]"

IF Y:
- Delete {stateFile}
- Clear phase output files
- Display: "Progress cleared. Starting fresh..."
- Load `./step-01-init.md`

IF N:
- Return to menu in Section 4

#### IF Any Other:

Help user understand options, then redisplay menu from Section 4.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- State file loaded and parsed correctly
- Progress summary accurate
- User given clear continuation options
- Correct routing to next phase
- Review and edit options work correctly

### ❌ SYSTEM FAILURE:

- Wrong phase identification
- Routing to incorrect step file
- Losing user progress
- Not offering review/edit options
- Starting over without confirmation

**Master Rule:** This step ONLY reads state and routes. No analysis. No modifications unless explicitly requested.
