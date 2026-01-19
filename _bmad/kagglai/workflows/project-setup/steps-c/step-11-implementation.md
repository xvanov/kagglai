---
name: 'step-11-implementation'
description: 'Implementer builds the baseline pipeline per technical specification'

nextStepFile: './step-12-code-review.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
techSpecFile: '{experiments_folder}/docs/technical-spec.md'
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
srcFolder: '{experiments_folder}/src'
modelsFolder: '{experiments_folder}/models'
submissionsFolder: '{experiments_folder}/submissions'
dataRawFolder: '{experiments_folder}/data/raw'
---

# Step 11: Implementation

## STEP GOAL:

To implement the baseline pipeline exactly as specified in the technical specification, producing working code, trained model, and valid submission file. Execute the plan, don't redesign it.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER deviate from the technical specification without user approval
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE AN IMPLEMENTER executing the plan
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the Implementer agent - execute the plan faithfully
- ✅ The technical spec is your blueprint - follow it
- ✅ Communicate blockers, don't silently work around them
- ✅ Generate working code that produces a valid submission

### Step-Specific Rules:

- 🎯 Focus on IMPLEMENTING the spec, not improving it
- 🚫 FORBIDDEN to add features beyond the spec
- 💬 Report progress as you complete each task
- 🚪 Success = valid submission file generated

## EXECUTION PROTOCOLS:

- 🎯 Follow the technical spec task by task
- 💾 Write code to {srcFolder}
- 📖 Test as you go - don't batch up debugging
- 🚫 FORBIDDEN to skip spec steps or add unplanned features

## CONTEXT BOUNDARIES:

- Technical spec defines exactly what to build
- Challenge spec defines submission format (authoritative)
- Data is in data/raw/ (verified in step 04)
- This step produces: src/, models/, and submission file

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 11: Implementation**

I will implement the baseline pipeline exactly as specified in the technical specification.

Loading specification..."

### 2. Load Technical Specification

Read {techSpecFile} completely.

Extract:
- Section 2: Environment setup commands
- Section 3: Data pipeline specification
- Section 4: Model configuration
- Section 5: Training pipeline structure
- Section 6: Inference pipeline
- Section 8: Task breakdown (checklist to follow)

"**Implementation Plan:**

Tasks to complete:
1. {task 1}
2. {task 2}
...
{N}. {task N}

Beginning implementation..."

### 3. Task 1: Set Up Environment

Follow Section 2.3 (Environment Setup Commands):

```bash
# Execute setup commands from spec
{commands}
```

**Verify:**
- [ ] Environment created
- [ ] Dependencies installed
- [ ] Installation verified

Report: "**Task 1 Complete:** Environment set up successfully."

### 4. Task 2: Implement Data Loader

Create data loading module per Section 3.1:

```
{srcFolder}/data/loader.py
```

**Implement:**
- Load function for each data file
- Path handling
- Basic validation

**Test:** Load train and test data, verify shapes.

Report: "**Task 2 Complete:** Data loader implemented and tested."

### 5. Task 3: Implement Preprocessing

Create preprocessing module per Section 3.3:

```
{srcFolder}/data/preprocess.py
```

**Implement:**
- Each preprocessing step from the spec
- Handle missing data per spec
- Feature engineering per spec

**Test:** Run preprocessing on sample data, verify output.

Report: "**Task 3 Complete:** Preprocessing pipeline implemented."

### 6. Task 4: Implement Model

Create model module per Section 4:

```
{srcFolder}/models/{model_name}.py
```

**Implement:**
- Model class/function per spec configuration
- Hyperparameters as specified
- Training interface

**Test:** Instantiate model, verify it accepts expected input shape.

Report: "**Task 4 Complete:** Model implemented."

### 7. Task 5: Implement Training Loop

Create training script per Section 5:

```
{srcFolder}/train.py
```

**Implement:**
- Data loading and preprocessing
- Training loop per spec
- Validation strategy per spec
- Checkpoint saving
- Logging

**Test:** Run training for 1 epoch, verify no errors.

Report: "**Task 5 Complete:** Training loop implemented."

### 8. Task 6: Implement Inference

Create inference script per Section 6:

```
{srcFolder}/predict.py
```

**Implement:**
- Model loading
- Test data preprocessing (same as training)
- Prediction generation

**Test:** Run inference on sample data, verify output format.

Report: "**Task 6 Complete:** Inference pipeline implemented."

### 9. Task 7: Implement Submission Generation

Create submission module per Section 6.3:

```
{srcFolder}/utils/submission.py
```

**Read {challengeSpecFile} Section 4 for authoritative format:**
- File format
- Column names
- Value formatting

**Implement:**
- Submission file generation matching exact format

**Test:** Generate sample submission, verify format.

Report: "**Task 7 Complete:** Submission generator implemented."

### 10. Task 8: End-to-End Test

Run the full pipeline on actual data:

1. Load data
2. Preprocess
3. Train model (full training per spec)
4. Save checkpoint
5. Run inference on test set
6. Generate submission

**Monitor:**
- Training loss decreasing
- Validation metric improving
- No errors or crashes

Report: "**Task 8 Complete:** End-to-end pipeline tested."

### 11. Task 9: Generate Final Submission

Generate the submission file:

```bash
python {srcFolder}/predict.py --model {modelsFolder}/baselines/{model_name}.pkl
```

**Verify submission:**
- [ ] Correct file format (CSV/etc.)
- [ ] Correct column names
- [ ] Correct number of rows (matches test set)
- [ ] Values in valid range
- [ ] File size acceptable

**Save to:** `{submissionsFolder}/baseline_submission.csv`

Report: "**Task 9 Complete:** Submission file generated."

### 12. Record Baseline Performance

Document the baseline results:

- Training metric: {value}
- Validation metric: {value}
- Submission file: `{submissionsFolder}/baseline_submission.csv`

**Note:** If competition allows, consider uploading to get actual leaderboard score.

### 13. Update Sidecar

Update {sidecarFile}:
- Add 'step-11-implementation' to stepsCompleted
- Set lastStep to 'step-11-implementation'
- Update lastUpdated date
- Add session note: "Baseline implemented - {validation metric} on validation set"
- Note submission file location

### 14. Summary and Proceed

"**Implementation Complete**

**Code created:**
- `{srcFolder}/` - Full pipeline implementation
- `{srcFolder}/train.py` - Training entry point
- `{srcFolder}/predict.py` - Inference entry point

**Artifacts:**
- Model checkpoint: `{modelsFolder}/baselines/{name}.pkl`
- Submission file: `{submissionsFolder}/baseline_submission.csv`

**Baseline Performance:**
- Validation {metric}: {value}

**Next step:** Code Review
- Agent: Implementer (fresh instance)
- Task: Review code quality, reproducibility, and correctness

**[C]ontinue** to code review"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## HANDLING BLOCKERS

**IF a task fails:**

1. Identify the specific error
2. Check if it's a spec issue vs implementation bug
3. **IF spec issue:** Report to user, propose fix, wait for approval
4. **IF implementation bug:** Debug and retry
5. Document the issue and resolution

**IF data issues arise:**
- Refer to EDA report for guidance
- Don't invent solutions - ask if unclear

**IF training doesn't converge:**
- Check hyperparameters match spec
- Report to user with training curves
- Don't silently change hyperparameters

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All tasks completed per specification
- Code is organized per spec structure
- Model trains without errors
- Validation metric is reasonable
- Valid submission file generated
- All artifacts in correct locations

### ❌ SYSTEM FAILURE:

- Deviating from spec without approval
- Adding features beyond spec
- Silently working around issues
- Generating invalid submission format
- Not testing components as you go
- Leaving code that doesn't run

**Master Rule:** Execute the plan faithfully. Communicate blockers. Generate a valid submission.
