---
name: 'step-01-select-experiment'
description: 'Select a completed experiment to validate from the Hypothesis Registry'

nextStepFile: './step-02-quality-check.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
experimentsFolder: '{experiments_folder}'
---

# Step 1: Select Experiment to Validate

## STEP GOAL:

To help the user select a completed experiment from the Hypothesis Registry for quality validation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Quality Auditor** for experiments
- ✅ Present completed experiments for validation
- ✅ Focus on experiments that have results

### Step-Specific Rules:

- 🎯 Filter to show only completed experiments (VALIDATED/INVALIDATED)
- 💬 Allow user to select by ID
- 🚫 FORBIDDEN to validate experiments still in progress

## MANDATORY SEQUENCE

### 1. Load Hypothesis Registry

Load `{hypothesisRegistryPath}` and filter to completed experiments.

### 2. Present Completed Experiments

"**Welcome to Validate Mode!**

Here are your completed experiments:

| ID | Title | Status | Result |
|----|-------|--------|--------|
{for each completed experiment}
| EXP-{XXX} | {title} | {VALIDATED/INVALIDATED} | {result summary} |

Which experiment would you like to validate? Enter the ID (e.g., EXP-001):

**Note:** Validation checks documentation completeness, reproducibility, and traceability."

### 3. Validate Selection

Verify the selected experiment:
- Exists in registry
- Has VALIDATED or INVALIDATED status (i.e., has been executed)

Set: `{experiment_id}` = selected ID
Set: `{experiment_folder}` = `{experimentsFolder}/{experiment_id}`

### 4. Confirm Selection

"**Selected: EXP-{XXX} - {Title}**

Status: {status}
Result: {result}
Folder: `{experiment_folder}`

Ready to run quality validation?"

### 5. Present MENU OPTIONS

Display: **Selection Complete - Select an Option:** [C] Continue to Quality Check

#### Menu Handling Logic:
- IF C: Pass experiment_id to next step, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Registry loaded and completed experiments presented
- Valid completed experiment selected
- Ready to proceed to quality check

### ❌ SYSTEM FAILURE:
- Allowing validation of incomplete experiments
- Invalid experiment ID accepted
