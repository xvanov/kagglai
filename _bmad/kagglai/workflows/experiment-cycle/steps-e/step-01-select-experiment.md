---
name: 'step-01-select-experiment'
description: 'Select an existing experiment to edit from the Hypothesis Registry'

nextStepFile: './step-02-edit-definition.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
experimentsFolder: '{experiments_folder}'
---

# Step 1: Select Experiment to Edit

## STEP GOAL:

To help the user select an existing experiment from the Hypothesis Registry for editing.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Data Scientist** helping to manage experiments
- ✅ Present available experiments clearly
- ✅ Help user select the right experiment to edit

### Step-Specific Rules:

- 🎯 Load and present experiments from registry
- 💬 Allow user to select by ID or search
- 🚫 FORBIDDEN to proceed without valid selection

## MANDATORY SEQUENCE

### 1. Load Hypothesis Registry

Load `{hypothesisRegistryPath}` and extract all experiments.

### 2. Present Available Experiments

"**Welcome to Edit Mode!**

Here are your experiments:

| ID | Title | Status | Hypothesis |
|----|-------|--------|------------|
{for each experiment}
| EXP-{XXX} | {title} | {status} | {hypothesis summary} |

Which experiment would you like to edit? Enter the ID (e.g., EXP-001):"

### 3. Validate Selection

Verify the selected experiment exists and load its folder path.

Set: `{experiment_id}` = selected ID
Set: `{experiment_folder}` = `{experimentsFolder}/{experiment_id}`

### 4. Confirm Selection

"**Selected: EXP-{XXX} - {Title}**

Status: {status}
Folder: `{experiment_folder}`

What would you like to edit?
- [H] Hypothesis - Revise the hypothesis statement
- [D] Design - Modify readme.md (experimental design)
- [P] Plan - Modify plan.md (implementation instructions)

Select: [H] / [D] / [P]"

Store selection for next step.

### 5. Present MENU OPTIONS

Display: **Selection Complete - Select an Option:** [C] Continue to Edit

#### Menu Handling Logic:
- IF C: Pass experiment_id and edit_type to next step, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Registry loaded and experiments presented
- Valid experiment selected
- Edit type identified
- Ready to proceed to editing

### ❌ SYSTEM FAILURE:
- Invalid experiment ID accepted
- Not confirming selection before proceeding
