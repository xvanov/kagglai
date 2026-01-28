---
name: 'step-e-02-select-phase'
description: 'Select which phase to re-run and configure modifications'

nextStepFile: './step-e-03-apply-edit.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
---

# Edit Step 2: Select Phase to Re-run

## STEP GOAL:

To help the user select which phase(s) to re-run and configure any modifications to the analysis parameters.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR helping user configure edits
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the workflow orchestrator in edit mode
- ✅ Help user select and configure phase re-runs
- ✅ Understand dependencies between phases
- ✅ Prepare clear instructions for re-execution

### Step-Specific Rules:

- 🎯 Focus on selection and configuration
- 🚫 FORBIDDEN to execute phases here - that's next step
- 💬 Explain phase dependencies clearly
- 🚪 Prepare re-run configuration

## EXECUTION PROTOCOLS:

- 🎯 Present phases and their dependencies
- 💾 Capture user's selection
- 📖 Configure any parameter changes
- 🚫 Do NOT execute yet - just configure

## CONTEXT BOUNDARIES:

- User wants to re-run specific phase(s)
- Need to understand phase dependencies
- Downstream phases may need re-running too

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Present Phase Selection

"**Select Phase(s) to Re-run**

| # | Phase | Description | Depends On |
|---|-------|-------------|------------|
| 2 | Data Acquisition | Sampling scripts | - |
| 3 | Basic Statistics | Image stats | Phase 2 |
| 4 | Label Analysis | Label quality | Phase 3 |
| 5 | Visual Patterns | Good/bad examples | Phase 4 |
| 6 | Data Quality | Filtering strategies | Phase 5 |
| 7 | Insights | Strategic synthesis | Phases 3-6 |
| 8 | Dashboard | Streamlit app | Phase 7 |
| 9 | Model Selection | Recommendations | Phase 7 |

**Note:** Re-running a phase will invalidate downstream phases.

Which phase would you like to re-run? (Enter number 2-9):"

### 2. Capture Selection and Calculate Dependencies

When user selects a phase:

**Calculate downstream phases that need re-running:**

| If Re-running | Also Re-run |
|---------------|-------------|
| Phase 2 | 3, 4, 5, 6, 7, 8, 9 |
| Phase 3 | 4, 5, 6, 7, 8, 9 |
| Phase 4 | 5, 6, 7, 8, 9 |
| Phase 5 | 6, 7, 8, 9 |
| Phase 6 | 7, 8, 9 |
| Phase 7 | 8, 9 |
| Phase 8 | 9 |
| Phase 9 | - |

Present impact:

"**Re-running Phase {N}: {name}**

This will also require re-running:
{list of downstream phases}

Total phases to re-run: {count}

Continue with this selection? [Y/N]"

### 3. Configure Modifications

"**Configure Phase {N} Modifications**

Would you like to change any parameters for this phase?

**Current Configuration:**
{show current parameters from state file}

**Options:**
**[K]eep** - Keep current parameters
**[M]odify** - Change parameters

Select:"

#### IF M (Modify):

Present phase-specific configuration options:

**For Phase 2 (Data Acquisition):**
- Sample size
- Sampling strategy
- Data source

**For Phases 3-6 (Analysis):**
- Filtering thresholds
- Analysis depth
- Specific focus areas

**For Phase 7 (Insights):**
- Focus areas
- Depth of analysis

**For Phase 8 (Dashboard):**
- Features to add/remove
- Layout changes

**For Phase 9 (Model Selection):**
- Model families to consider
- Constraints

Capture modifications.

### 4. Confirm Re-run Plan

"**Re-run Plan:**

**Starting Phase:** {N} - {name}
**Modifications:** {list or 'None'}
**Phases to Re-run:** {list}

**This will:**
- Re-execute the selected phase with modifications
- Re-run all dependent downstream phases
- Update the EDA report and current-understanding.md

Ready to proceed? [Y/N]"

### 5. Save Configuration and Route

**IF Y:**

Update {stateFile} with re-run configuration:
```yaml
editMode:
  startPhase: {N}
  modifications: {user's modifications}
  phasesToRerun: [list]
```

Display: "Configuration saved. Proceeding to apply edits..."
Load, read entire file, then execute {nextStepFile}

**IF N:**

"Would you like to select a different phase or exit edit mode?

**[S]elect** - Select different phase
**[E]xit** - Exit edit mode"

Handle accordingly.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Phase dependencies correctly calculated
- User informed of downstream impact
- Modifications captured clearly
- Re-run plan confirmed

### ❌ SYSTEM FAILURE:

- Incorrect dependency calculation
- Not informing user of downstream impact
- Missing modification capture
- Executing phases in this step

**Master Rule:** Select and configure only. Explain dependencies. Don't execute yet.
