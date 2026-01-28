---
name: 'step-e-03-apply-edit'
description: 'Apply the configured edits by re-running selected phases'

stateFile: '{experiments_folder}/.image-eda-state.yaml'
step02File: '../steps-c/step-02-data-acquisition.md'
step03File: '../steps-c/step-03-basic-stats.md'
step04File: '../steps-c/step-04-label-analysis.md'
step05File: '../steps-c/step-05-visual-patterns.md'
step06File: '../steps-c/step-06-data-quality.md'
step07File: '../steps-c/step-07-insights.md'
step08File: '../steps-c/step-08-dashboard.md'
step09File: '../steps-c/step-09-model-selection.md'
---

# Edit Step 3: Apply Edits

## STEP GOAL:

To apply the configured edits by routing to and executing the appropriate create-mode phase steps.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ORCHESTRATOR applying edits
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the workflow orchestrator in edit mode
- ✅ Route to appropriate create-mode steps
- ✅ Create-mode steps do the actual work
- ✅ Track edit progress through state file

### Step-Specific Rules:

- 🎯 Route to correct phase step based on configuration
- 🚫 FORBIDDEN to duplicate create-mode logic here
- 💬 Reuse create-mode steps with edit context
- 🚪 Return to edit mode after completion

## EXECUTION PROTOCOLS:

- 🎯 Load re-run configuration from state
- 💾 Route to starting phase
- 📖 Phases will execute in sequence
- 🚫 After completion, offer to continue or exit

## CONTEXT BOUNDARIES:

- Re-run plan configured in previous step
- Use create-mode steps for execution
- Modifications stored in state file
- Downstream phases auto-triggered

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Re-run Configuration

Load {stateFile} and extract:
- `editMode.startPhase`
- `editMode.modifications`
- `editMode.phasesToRerun`

### 2. Announce Edit Execution

"**Applying Edits**

Starting Phase: {startPhase}
Modifications: {modifications or 'None'}
Phases to Re-run: {phasesToRerun}

Beginning re-execution..."

### 3. Route to Starting Phase

Map starting phase to step file:

| Phase | Step File |
|-------|-----------|
| 2 | {step02File} |
| 3 | {step03File} |
| 4 | {step04File} |
| 5 | {step05File} |
| 6 | {step06File} |
| 7 | {step07File} |
| 8 | {step08File} |
| 9 | {step09File} |

**Before routing:**

Update state to indicate edit mode is active:
```yaml
editMode:
  active: true
  startPhase: {N}
  modifications: {modifications}
```

**Route:**

Load, read entire file, then execute the appropriate step file.

**Note:** The create-mode steps will:
1. Execute their phase with any modifications
2. Update state and documents
3. Proceed to next phase automatically
4. Continue through all downstream phases
5. Return to completion (step-10)

### 4. Post-Completion Handling

**After all phases complete (at step-10):**

Step-10 will detect edit mode and offer:

"**Edit Complete**

All selected phases have been re-run.

**Changes Made:**
{summary of what was re-executed}

**Would you like to:**
**[V]alidate** - Run validation on the updated EDA
**[E]dit More** - Make additional edits
**[D]one** - Exit edit mode

Select:"

#### Menu Handling:

- IF V: Route to `../steps-v/step-v-01-validate.md`
- IF E: Route to `./step-e-01-assess.md`
- IF D: Clear editMode from state, exit

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Configuration correctly loaded
- Routed to correct starting phase
- Create-mode steps executed successfully
- Edit mode properly tracked in state
- Clean completion handling

### ❌ SYSTEM FAILURE:

- Wrong phase routing
- Duplicating create-mode logic
- Losing edit context
- Not completing downstream phases

**Master Rule:** Route to create-mode steps. Let them do the work. Track edit context in state.
