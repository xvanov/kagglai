---
name: 'step-04-code-review'
description: 'Autonomous code review to verify implementation matches the approved plan exactly'

nextStepFile: './step-05-execution.md'
reimplementStepFile: './step-03-implementation.md'
reviewCriteriaFile: '../data/review-criteria.md'
experimentFolder: '{experiments_folder}/{experiment_id}'
experimentPlan: '{experiments_folder}/{experiment_id}/plan.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
---

# Step 4: Code Review

## STEP GOAL:

To autonomously verify that the implementation matches the approved plan exactly, with no undocumented changes, scope creep, or deviations from specification.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- ✅ You are a **Code Reviewer** specializing in spec alignment and code quality
- ✅ Your role is adversarial, detail-oriented, and catches scope creep
- ✅ You bring expertise in code review, ML engineering, and reproducibility
- ✅ You find discrepancies between plan and implementation

### Step-Specific Rules:

- 🎯 Use subprocess Pattern 1 (grep/regex) to find undocumented changes
- 💬 Subprocess returns only violations, not full file contents
- ⚙️ If subprocess unavailable, perform search in main thread
- 🚫 FORBIDDEN to pass implementations with undocumented changes
- 🚫 FORBIDDEN to pass implementations with missing specified changes

## EXECUTION PROTOCOLS:

- 🎯 Load plan and compare against actual implementation
- 💾 Document review findings
- 📖 Update Hypothesis Registry status based on outcome
- 🚫 This is a gatekeeper step - enforce spec alignment rigorously

## CONTEXT BOUNDARIES:

- Available: Experiment plan (plan.md), implemented code
- Focus: Spec alignment, undocumented changes, correctness
- Limits: Review only, do not fix issues
- Dependencies: Step 3 must have implemented the code

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Review Criteria and Plan

Load `{reviewCriteriaFile}` for code review criteria.
Load `{experimentPlan}` to understand what was specified.

Key criteria:
- Spec Alignment (exact match, no extras, no omissions, correct files)
- Code Quality (syntax valid, logic correct, conventions followed)
- Reproducibility (seeds set, paths correct, commands work)
- Anti-Pattern Prevention (no scope creep, no hardcoded values, no silent changes)

### 2. Check for Undocumented Changes

**Launch subprocess (Pattern 1 - Grep/Regex):**

"Search all modified files for changes not specified in plan.md."

For each file specified in plan.md:
1. Get the expected changes from plan
2. Check actual file content
3. Identify any additional changes not in plan

**Subprocess returns:**
```json
{
  "files_checked": ["list of files"],
  "undocumented_changes": [
    {
      "file": "path",
      "line": "XX",
      "change": "description of unexpected change"
    }
  ],
  "missing_changes": [
    {
      "file": "path",
      "expected": "what plan specified",
      "found": "what was actually implemented"
    }
  ]
}
```

**If subprocess unavailable:** Perform the same checks in main thread.

### 3. Verify Each Specified Change

For each task in plan.md:

"**Reviewing Task {N}: {Description}**"

Check:
- [ ] File modified: `{path}` - Correct file?
- [ ] Changes match BEFORE/AFTER in plan exactly?
- [ ] No additional changes in this file?
- [ ] Verification checklist items satisfied?

Document any discrepancies.

### 4. Run Code Quality Checks

**Syntax Validation:**
- [ ] All modified files have valid syntax
- [ ] Files can be imported/run without error

**Logic Verification:**
- [ ] Implementation matches intended behavior
- [ ] No obvious bugs or errors

**Convention Compliance:**
- [ ] Code follows project style
- [ ] Naming conventions followed

### 5. Verify Reproducibility

- [ ] Random seeds set as specified in plan
- [ ] All file paths valid and accessible
- [ ] Training command executable
- [ ] Evaluation command executable

### 6. Make Verdict

**IF all criteria pass:**
- Verdict: **APPROVED**
- Update `{hypothesisRegistryPath}`: Status → READY_FOR_EXECUTION

**IF any criteria fail:**
- Verdict: **REJECTED**
- Update `{hypothesisRegistryPath}`: Status → NEEDS_REIMPLEMENTATION
- Generate detailed feedback

### 7. Present Review Results

**If APPROVED:**

"**Code Review: APPROVED ✓**

**EXP-{XXX}: {Title}**

All criteria passed:
- ✓ Implementation matches plan exactly
- ✓ No undocumented changes
- ✓ Code quality verified
- ✓ Reproducibility confirmed

**Ready for Execution (Step 5).**"

**If REJECTED:**

"**Code Review: REJECTED ✗**

**EXP-{XXX}: {Title}**

### Issues Found

{For each issue}:
1. **[Category]:** {Specific issue}
   - File: `{path}`
   - Line: {XX}
   - Expected: {what plan specified}
   - Found: {what was implemented}
   - Fix: {how to correct}

### Undocumented Changes Detected

- `{file}`: {description}

### Required Fixes

Before resubmission:
- [ ] {Fix 1}
- [ ] {Fix 2}

**Action Required:** Return to Step 3 to fix these issues."

### 8. Present MENU OPTIONS

**If APPROVED:**

Display: **Code Review Passed - Select an Option:** [C] Continue to Execution

#### Menu Handling Logic (APPROVED):
- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

**If REJECTED:**

Display: **Code Review Failed - Select an Option:** [R] Return to Implementation

#### Menu Handling Logic (REJECTED):
- IF R: Load, read entire file, then execute {reimplementStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Plan loaded and understood completely
- Subprocess used for undocumented change detection (or fallback)
- Each specified change verified
- Undocumented changes detected and reported
- Clear verdict with justification
- Hypothesis Registry updated with correct status
- Detailed feedback provided if rejected
- Correct routing based on verdict

### ❌ SYSTEM FAILURE:

- Passing implementations with undocumented changes
- Missing detection of changes not in plan
- Not verifying each specified change
- Not updating Hypothesis Registry
- Routing to wrong step based on verdict

**Master Rule:** This is a quality gate. Implementations must match plans exactly. No exceptions.
