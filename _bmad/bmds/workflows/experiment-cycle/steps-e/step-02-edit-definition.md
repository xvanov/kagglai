---
name: 'step-02-edit-definition'
description: 'Edit the selected experiment definition (hypothesis, readme, or plan)'

experimentFolder: '{experiments_folder}/experiments/{experiment_id}'
experimentReadme: '{experiments_folder}/experiments/{experiment_id}/readme.md'
experimentPlan: '{experiments_folder}/experiments/{experiment_id}/plan.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
reviewCriteriaFile: '../data/review-criteria.md'
---

# Step 2: Edit Experiment Definition

## STEP GOAL:

To collaboratively edit the selected aspect of the experiment definition while maintaining document integrity and validity.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a **Data Scientist** helping to refine experiments
- ✅ Maintain document structure while making edits
- ✅ Ensure edits don't invalidate other parts of the design

### Step-Specific Rules:

- 🎯 Edit only what the user wants to change
- 🚫 FORBIDDEN to break document structure
- 💬 Verify changes against review criteria
- 📋 Update Hypothesis Registry if hypothesis changed

## MANDATORY SEQUENCE

### 1. Load Current State

Based on edit_type from previous step:

**If H (Hypothesis):**
Load `{hypothesisRegistryPath}` entry for this experiment.

**If D (Design):**
Load `{experimentReadme}`.

**If P (Plan):**
Load `{experimentPlan}`.

### 2. Present Current Content

"**Current {Hypothesis/Design/Plan}:**

{Display the current content}

What would you like to change?"

### 3. Collaborate on Edits

Work with user to make changes:

- Discuss what needs to change
- Propose edits
- Get confirmation
- Apply changes

### 4. Validate Edits

Load `{reviewCriteriaFile}` and verify edits don't violate criteria:

- Hypothesis still falsifiable, specific, isolated, motivated?
- Paths still valid?
- Success criteria still clear?
- No multi-variable testing introduced?

"**Validation Check:**
- ✓/✗ {criterion 1}
- ✓/✗ {criterion 2}
..."

### 5. Save Changes

Save the edited document.

**If hypothesis was edited:**
Update `{hypothesisRegistryPath}` with new hypothesis statement.

### 6. Present Summary

"**Edit Complete!**

**EXP-{XXX}: {Title}**

**Changes Made:**
- {change 1}
- {change 2}

**Validation:** All criteria still pass ✓

**Note:** If you made significant changes, consider running through Design Review again to ensure the experiment is still sound."

### 7. Present MENU OPTIONS

Display: **Edit Complete - Select an Option:** [E] Edit More [R] Run Design Review [D] Done

#### Menu Handling Logic:
- IF E: Return to step 1 to select another experiment or edit type
- IF R: Recommend running create mode step-02 for design review
- IF D: "Edit complete. Your experiment definition has been updated."
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Current state loaded and presented
- Edits made collaboratively
- Changes validated against criteria
- Documents updated correctly
- Registry updated if hypothesis changed

### ❌ SYSTEM FAILURE:
- Breaking document structure
- Not validating edits
- Not updating registry when hypothesis changes
