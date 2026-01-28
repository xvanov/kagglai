---
name: 'step-12b-code-fix'
description: 'Fix-only step for code when review context was too large'

nextStepFile: './step-13-complete.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
currentArchitectureFile: '{experiments_folder}/docs/current-architecture.md'
srcFolder: '{experiments_folder}/src'
modelsFolder: '{experiments_folder}/models'
submissionsFolder: '{experiments_folder}/submissions'
---

# Step 12b: Code Fix-Only

## STEP GOAL:

To implement fixes identified in the code review report (from step 12) in a fresh context, and ensure current-architecture.md is created for experiment-cycle.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER refactor beyond identified issues
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A CODE FIXER, not a refactoring session
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are implementing fixes from a previous code review
- ✅ The review report is in the sidecar file
- ✅ Focus on fixing, not improving beyond issues
- ✅ Ensure current-architecture.md exists

### Step-Specific Rules:

- 🎯 Focus ONLY on issues from the review report
- 🚫 FORBIDDEN to do general refactoring
- 💬 Document each fix as you make it
- 🚪 Code must be ready for experiment-cycle

## EXECUTION PROTOCOLS:

- 🎯 Read review report from sidecar file
- 💾 Fix issues in priority order (Critical → Major)
- 📖 Test fixes when possible
- 🚫 FORBIDDEN to add features or refactor

## CONTEXT BOUNDARIES:

- Code review was completed in step 12 but fixes deferred
- Review report is saved in the sidecar file
- You have a fresh context to make fixes
- Only fix issues identified in the report

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 12b: Code Fix-Only**

I'm a fresh Implementer instance here to implement the fixes identified in the code review.

Loading review report from sidecar..."

### 2. Load Review Report

Read {sidecarFile} and extract the review report from the "## Validation Reports" section.

**Extract:**
- Critical Issues (bugs causing incorrect results)
- Major Issues (quality/maintainability)
- Minor Issues (optional)

### 3. Fix Critical Issues

For each Critical issue:

1. Read the issue description and location
2. Navigate to the file and line
3. Understand the bug
4. Implement the fix
5. Test if possible
6. Document: "Fixed: {issue} in {file} → {what was done}"

### 4. Fix Major Issues

For each Major issue:

1. Read the issue description
2. Locate the problem
3. Implement the fix
4. Document: "Fixed: {issue} → {what was done}"

### 5. Handle Minor Issues

For Minor issues:
- Fix them if straightforward
- Note as "Deferred" if complex

### 6. Regenerate Submission if Needed

**IF any fixes affected prediction logic:**
- Regenerate the submission file
- Verify it's still valid

### 7. Verify current-architecture.md

Check if {currentArchitectureFile} exists.

**IF it doesn't exist:**
Create it with:

```markdown
# Current Architecture

**Project:** {from sidecar}
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
| {other files} | {purposes} |

---

## 2. Model Configuration

{Fill from code inspection}

---

## 3. Baseline Performance

{Fill from training results}

---

## 4. Extension Points

{Document where to make changes}

---

## 5. Reproducibility

{Document seeds, dependencies, commands}

---

## 6. Known Issues

{Note any remaining issues or limitations}
```

**IF it exists:**
- Verify it's complete
- Update if fixes changed anything

### 8. Generate Fix Report

Create a fix report:

```markdown
## Fix Report

**Original Review:** From sidecar, step-12 validation
**Fixer:** Implementer (Fix Instance)
**Date:** {date}

### Fixes Applied
1. **{Issue from review}**
   - File: {file}
   - Fix: {what was done}
   - Tested: {yes/no}

### Submission Status
- Regenerated: {yes/no}
- Valid: {yes}

### Issues Deferred
1. **{Minor issue}**
   - Reason: {why deferred}
```

### 9. Update Sidecar

Update {sidecarFile}:
- Add 'step-12b-code-fix' to stepsCompleted
- Set lastStep to 'step-12b-code-fix'
- Update lastUpdated date
- Append fix report under the original review report
- Add session note: "Code fixes implemented"

### 10. Summary and Proceed

"**Code Fixes Complete**

**Fixes applied:** {count}
**Submission regenerated:** {yes/no}
**Issues deferred:** {count}

**Documents verified:**
- current-architecture.md (ready for experiment-cycle)

**Next step:** Project Setup Completion

**[C]ontinue** to completion"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Review report loaded from sidecar
- All Critical issues fixed
- All Major issues fixed
- Each fix documented
- Submission validity verified
- current-architecture.md verified/created
- Fix report generated

### ❌ SYSTEM FAILURE:

- Doing general refactoring
- Missing issues from the review report
- Not documenting fixes
- Not checking current-architecture.md
- Breaking the submission

**Master Rule:** Fix what was found. Ensure architecture is documented. Don't refactor.
