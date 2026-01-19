---
name: 'step-12-code-review'
description: 'Fresh Implementer reviews code quality, reproducibility, and correctness'

nextStepFile: './step-13-complete.md'
fixOnlyFile: './step-12b-code-fix.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
techSpecFile: '{experiments_folder}/docs/technical-spec.md'
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
currentArchitectureFile: '{experiments_folder}/docs/current-architecture.md'
srcFolder: '{experiments_folder}/src'
modelsFolder: '{experiments_folder}/models'
submissionsFolder: '{experiments_folder}/submissions'
reviewCriteriaFile: '../data/review-criteria.md'
validationChecklistFile: '../data/validation-checklist.md'

# Advanced tools
partyModeEnabled: true
---

# Step 12: Code Review

## STEP GOAL:

To review the implemented code for quality, reproducibility, and correctness, implement fixes, and create the current-architecture.md document for the experiment-cycle workflow. This uses the Author/Validator pattern - you are a FRESH instance reviewing another's work.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER approve code that produces invalid submissions
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A CODE REVIEWER, skeptical and thorough
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a FRESH Implementer instance - critical of the code
- ✅ Check reproducibility (can it run from clean state?)
- ✅ Verify correctness (does it do what the spec says?)
- ✅ Assess quality (is it maintainable for experiments?)

### Step-Specific Rules:

- 🎯 Focus on REPRODUCIBILITY, CORRECTNESS, and QUALITY
- 🚫 FORBIDDEN to approve code with obvious bugs
- 💬 Be specific about issues - file, line, problem
- 🚪 Code must be ready for experiment-cycle

## EXECUTION PROTOCOLS:

- 🎯 Read code with critical eye
- 💾 Verify against technical spec
- 📖 Test reproducibility where possible
- 🚫 FORBIDDEN to assume code is correct

## CONTEXT BOUNDARIES:

- Code was implemented by a previous Implementer instance
- Technical spec defines what it should do
- Challenge spec defines submission format requirements
- Review criteria provide the standards

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 12: Code Review**

I am a fresh Implementer instance reviewing the baseline code. I will assess reproducibility, correctness, and code quality.

Beginning systematic review..."

### 2. Load Review Standards

Read {reviewCriteriaFile} for the "Code Review" section.
Read {validationChecklistFile} for the "Implementation Validation" checklist.

### 3. Load Specifications

Read {techSpecFile} to understand what was supposed to be built.
Read {challengeSpecFile} Section 4 to verify submission format.

### 4. Survey the Codebase

List and understand the code structure in {srcFolder}:

```
src/
├── config.py
├── data/
│   ├── loader.py
│   └── preprocess.py
├── models/
│   └── {model}.py
├── train.py
├── predict.py
└── utils/
    └── submission.py
```

"**Code Structure:**
{list files found}

Reviewing each component..."

### 5. Review Each Component

For each file, assess:

**Correctness:**
- Does it match the spec?
- Any obvious logic bugs?
- Edge cases handled?

**Quality:**
- Code readable?
- Functions documented?
- Consistent style?

**Reproducibility:**
- Random seeds set?
- Dependencies clear?
- Paths not hardcoded?

Document issues found:
```markdown
### {filename}
- **Issue:** {description}
- **Location:** {line or function}
- **Severity:** {Critical/Major/Minor}
- **Fix:** {recommendation}
```

### 6. Verify Reproducibility

Test if the pipeline can run from a clean state:

**Check:**
- [ ] Dependencies listed (requirements.txt or similar)
- [ ] Random seeds set for reproducibility
- [ ] No hardcoded absolute paths
- [ ] Instructions complete (README or comments)
- [ ] Works from clean environment

**Test if possible:**
```bash
# Try running training
python {srcFolder}/train.py --config configs/baseline.yaml
```

### 7. Verify Submission Correctness

Check the generated submission:

**Load submission file from {submissionsFolder}:**
- [ ] Format matches challenge-spec requirements
- [ ] Column names correct
- [ ] Row count matches test set
- [ ] Values in valid range
- [ ] No NaN or invalid values

### 8. Apply Validation Checklist

Work through the Implementation Validation checklist:

**Functionality:**
- [ ] Environment sets up correctly
- [ ] Data loads without errors
- [ ] Model trains successfully
- [ ] Inference runs correctly
- [ ] Submission generates properly

**Quality:**
- [ ] Code follows standards
- [ ] Functions documented
- [ ] Error handling present
- [ ] Logging implemented

**Reproducibility:**
- [ ] Random seeds set
- [ ] Dependencies pinned
- [ ] Instructions complete
- [ ] Works from clean state

**Submission:**
- [ ] Format matches requirements
- [ ] Row count correct
- [ ] Values in valid range
- [ ] File size acceptable

### 9. Generate Review Report

Create a review report:

```markdown
## Code Review Report

**Codebase:** {srcFolder}
**Reviewer:** Implementer (Reviewer Instance)
**Date:** {date}

### Summary
{1-2 sentence overall assessment}

### Critical Issues (Must Fix)
{Bugs that cause incorrect results or crashes}

### Major Issues (Should Fix)
{Quality issues affecting maintainability}

### Minor Issues (Can Fix Later)
{Style and documentation improvements}

### Verification Results
- Reproducibility: {passed/issues}
- Correctness: {passed/issues}
- Quality: {passed/issues}
- Submission: {valid/issues}

### Recommendation
{APPROVE / APPROVE WITH FIXES / REJECT}
```

### 10. Implement Fixes (or Route to Fix-Only)

**IF no Critical or Major issues:**
- Report: "**Review passed with minor or no issues.**"
- Proceed to Section 11

**IF Critical or Major issues exist:**
- Assess the scope of fixes needed

**IF fixes are straightforward:**
- Make the fixes directly
- Document each fix made
- Proceed to Section 11

**IF fixes are extensive:**
- Append the review report to {sidecarFile}
- Display: "**Review found issues requiring extensive fixes.**"
- Present options:
  - **[C]ontinue** - I will implement all fixes now
  - **[F]ix-only** - Route to fix-only step
- If user selects [F], load and execute {fixOnlyFile}

### 11. Create current-architecture.md

Create {currentArchitectureFile} for experiment-cycle:

```markdown
# Current Architecture

**Competition:** {competition_name}
**Created:** {date}
**Last Updated:** {date}

---

## 1. Pipeline Overview

### 1.1 Data Flow
```
data/raw/ → loader → preprocess → model → submission
```

### 1.2 Key Files
| File | Purpose |
|------|---------|
| src/train.py | Training entry point |
| src/predict.py | Inference entry point |
| src/config.py | Configuration management |
| src/data/loader.py | Data loading |
| src/data/preprocess.py | Preprocessing |
| src/models/{model}.py | Model definition |

---

## 2. Model Configuration

### 2.1 Current Model
- **Type:** {model type}
- **Key Hyperparameters:** {from training}

### 2.2 Training Configuration
- **Batch Size:** {value}
- **Learning Rate:** {value}
- **Epochs:** {value}
- **Validation Split:** {method}

---

## 3. Baseline Performance

### 3.1 Metrics
- **Validation {metric}:** {value}
- **Training {metric}:** {value}

### 3.2 Submission
- **File:** submissions/baseline_submission.csv
- **Leaderboard Score:** {if known, else "Not submitted"}

---

## 4. Extension Points

### 4.1 Where to Add Features
- Feature engineering: `src/data/preprocess.py`
- Model modifications: `src/models/`
- Training changes: `src/train.py`

### 4.2 Configuration
- All hyperparameters in: `configs/baseline.yaml`
- Easy to create new configs for experiments

---

## 5. Reproducibility

### 5.1 Random Seeds
- Set in: {location}
- Value: {seed}

### 5.2 Dependencies
- Listed in: requirements.txt
- Python version: {version}

### 5.3 Run Commands
```bash
# Training
python src/train.py --config configs/baseline.yaml

# Inference
python src/predict.py --model models/baselines/{name}.pkl
```

---

## 6. Known Issues and Limitations

- {Any known issues}
- {Limitations of current approach}
```

### 12. Update Sidecar

Update {sidecarFile}:
- Add 'step-12-code-review' to stepsCompleted
- Set lastStep to 'step-12-code-review'
- Update lastUpdated date
- Add session note: "Code review complete, architecture documented"
- Append review report if not already added

### 13. Summary and Proceed

"**Code Review Complete**

**Review outcome:** {APPROVED / APPROVED WITH FIXES}

**Verification:**
- Reproducibility: {status}
- Correctness: {status}
- Quality: {status}
- Submission validity: {status}

**Fixes applied:** {count}

**Documents created:**
- current-architecture.md (ready for experiment-cycle)

**Next step:** Project Setup Completion

**Select an option:**
- **[A]dvanced Elicitation** - Discuss any code concerns
- **[P]arty Mode** - Multi-agent review discussion
- **[C]ontinue** - Proceed to completion"

Wait for user selection.

**IF [A]:** Use advanced elicitation
**IF [P]:** Initiate party mode
**IF [C]:** Load, read entire file, then execute {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Code reviewed thoroughly
- Reproducibility verified
- Submission format validated
- Review report generated
- Fixes implemented (or routed)
- current-architecture.md created
- Ready for experiment-cycle

### ❌ SYSTEM FAILURE:

- Approving code with bugs
- Not checking submission format
- Skipping reproducibility check
- Vague issue descriptions
- Not creating current-architecture.md

**Master Rule:** Code must be reproducible, correct, and produce valid submissions. Document the architecture for experiment-cycle.
