---
name: 'step-14-baseline-verify'
description: 'Verify baseline model produces valid submission'

nextStepFile: './step-15-complete.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
submissionsFolder: '{experiments_folder}/submissions'
modelsFolder: '{experiments_folder}/models/baselines'
currentArchFile: '{experiments_folder}/docs/current-architecture.md'
---

# Step 14: Baseline Verification

## STEP GOAL:

To verify that the existing baseline model can produce a valid submission file.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE Rex (Implementer), the verification specialist
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are Rex - direct, verify everything works
- ✅ Test the actual pipeline
- ✅ Document any issues
- ✅ Ensure reproducibility

### Step-Specific Rules:

- 🎯 Focus on verification, not improvement
- 🚫 FORBIDDEN to modify the baseline
- 💬 Report issues clearly
- 📄 Document verification results

## MANDATORY SEQUENCE

### 1. Load Architecture

Load {currentArchFile} to get inference commands.

"**Baseline Verification**

I'll verify your baseline can produce a valid submission."

### 2. Check Baseline Model Exists

Check {modelsFolder}:

"**Baseline Model Check:**
- Location: {modelsFolder}
- Model file: {exists/missing}
- Config: {exists/missing}
- Weights: {valid/invalid/missing}"

If missing:
"**No baseline model found.**

Options:
**[T]rain** - Run training to create baseline
**[S]kip** - Skip verification (will need baseline for experiment-cycle)
**[P]rovide** - Specify path to existing model"

### 3. Run Inference (If Model Exists)

"**Running baseline inference on validation set...**"

Execute inference command from architecture doc.

Report:
- Success/failure
- Any errors
- Time taken
- Output format

### 4. Validate Submission Format

Check submission against problem-statement requirements:

"**Submission Validation:**
- File created: {yes/no}
- Format: {csv/json/etc.} - {correct/incorrect}
- Columns: {list} - {all present/missing: X}
- Rows: {count} - {matches expected/mismatch}
- Values: {valid range/issues found}"

### 5. Calculate Baseline Score (If Possible)

If local evaluation is possible:

"**Baseline Performance:**
- Metric: {name}
- Score: {value}
- On: validation set

This establishes your baseline to improve upon."

### 6. Document Verification Results

Update sidecar and {currentArchFile}:

```markdown
## Baseline Verification

**Date:** {date}
**Model:** {path}
**Status:** {VERIFIED/FAILED/SKIPPED}

**Inference Test:**
- Command: `{command}`
- Result: {success/failure}
- Time: {duration}

**Submission Validation:**
- Format: {VALID/INVALID}
- Issues: {if any}

**Performance:**
- Metric: {name} = {value}
- Dataset: validation set
```

### 7. Summary and Proceed

"**Baseline Verification Complete**

**Status:** {VERIFIED/ISSUES FOUND/SKIPPED}
**Baseline Score:** {value or N/A}
**Submission:** {valid/needs fixes}

{If issues}
Note: Issues found but can proceed. These should be addressed early in experiment-cycle.

**[C]ontinue** to Completion"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Baseline model located
- Inference tested
- Submission validated
- Score documented
- Issues clearly reported

### ❌ SYSTEM FAILURE:
- Skipping verification silently
- Not testing actual inference
- Not validating submission format
- Modifying the baseline

**Master Rule:** Verify everything works, document results, don't modify.
