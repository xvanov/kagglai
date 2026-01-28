---
name: 'step-03b-problem-statement-fix'
description: 'Fix-only step for problem statement when review context was too large'

nextStepFile: './step-04-eda-basic.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
specFile: '{experiments_folder}/docs/problem-statement.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'

# Input files if re-verification needed
descriptionFile: '{experiments_folder}/problem-inputs/description.md'
rulesFile: '{experiments_folder}/problem-inputs/rules.md'
dataAccessFile: '{experiments_folder}/problem-inputs/data-access.md'
submissionFile: '{experiments_folder}/problem-inputs/submission-format.md'
---

# Step 3b: Problem Statementification Fix-Only

## STEP GOAL:

To implement fixes identified in the review report (from step 03) in a fresh context. This step exists because the review step may have consumed too much context to effectively implement fixes.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate new content - only fix identified issues
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FIXER, not a re-reviewer
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are implementing fixes from a previous review
- ✅ The review report is in the sidecar file
- ✅ Focus on fixing, not re-reviewing
- ✅ Verify each fix after making it

### Step-Specific Rules:

- 🎯 Focus ONLY on issues from the review report
- 🚫 FORBIDDEN to do a full re-review (that wastes context)
- 💬 Document each fix as you make it
- 🚪 This step gets the spec to an approvable state

## EXECUTION PROTOCOLS:

- 🎯 Read review report from sidecar file
- 💾 Fix issues in priority order (Critical → Major)
- 📖 Verify fix against source documents when needed
- 🚫 FORBIDDEN to add new issues - just fix what was found

## CONTEXT BOUNDARIES:

- Review was completed in step 03 but fixes deferred
- Review report is saved in the sidecar file
- You have a fresh context to make fixes
- Only fix issues identified in the report

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 03b: Problem Statementification Fix-Only**

I'm a fresh instance here to implement the fixes identified in the review report.

Loading review report from sidecar..."

### 2. Load Review Report

Read {sidecarFile} and extract the review report from the "## Validation Reports" section.

**Extract:**
- Critical Issues list
- Major Issues list
- Minor Issues list (optional - may skip if only doing critical/major)

### 3. Read Current Spec

Read {specFile} to understand current state.

### 4. Fix Critical Issues

For each Critical issue:

1. Read the issue description
2. Locate the problem in the spec
3. If verification needed, read the relevant source document
4. Make the fix
5. Document: "Fixed: {issue} → {what was done}"

**Example:**
```
Fixed: Missing metric formula → Added "MAE = (1/n) * Σ|y_i - ŷ_i|" from rules.md line 47
```

### 5. Fix Major Issues

For each Major issue:

1. Read the issue description
2. Locate the problem in the spec
3. If verification needed, read the relevant source document
4. Make the fix
5. Document: "Fixed: {issue} → {what was done}"

### 6. Handle Minor Issues

For Minor issues, choose one:
- Fix them if straightforward
- Note them as "Deferred - can address later"

### 7. Verify current-understanding.md Section 1

Check if {currentUnderstandingFile} Section 1 exists and is properly populated.

**IF Section 1 is missing or incomplete:**
- Populate it from the (now fixed) problem-statement.md:

```markdown
## 1. Problem & Task

### 1.1 Task Definition
- **Type:** {from spec}
- **Objective:** {from spec}
- **Primary Metric:** {from spec}

### 1.2 Key Constraints
- **Compute:** {from spec}
- **External Data:** {from spec}
- **Timeline:** {key dates}

### 1.3 Success Criteria
- {What constitutes a good score}
- {Key requirements to meet}
```

### 8. Generate Fix Report

Create a fix report:

```markdown
## Fix Report

**Original Review:** From sidecar, step-03 validation
**Fixer:** Data Analyst (Fix Instance)
**Date:** {date}

### Fixes Applied
1. **{Issue from review}**
   - Fix: {what was done}
   - Verified: yes

### Issues Deferred
1. **{Minor issue}**
   - Reason: {why deferred}
```

### 9. Update Sidecar

Update {sidecarFile}:
- Add 'step-03b-problem-statement-fix' to stepsCompleted
- Set lastStep to 'step-03b-problem-statement-fix'
- Update lastUpdated date
- Append fix report under the original review report
- Add session note: "Challenge spec fixes implemented"

### 10. Summary and Proceed

"**Problem Statementification Fixes Complete**

**Fixes applied:** {count}
**Issues deferred:** {count}

**Documents updated:**
- problem-statement.md (fixes applied)
- current-understanding.md (Section 1 verified)

**Next step:** EDA Basic - Pull data and generate basic statistics

**[C]ontinue** to EDA basic analysis"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Review report loaded from sidecar
- All Critical issues fixed
- All Major issues fixed
- Each fix documented
- current-understanding.md Section 1 verified
- Fix report generated

### ❌ SYSTEM FAILURE:

- Starting a new review instead of fixing
- Missing issues from the review report
- Not documenting fixes
- Skipping verification of fixes
- Not checking current-understanding.md

**Master Rule:** Fix what was found. Document what you fixed. Don't re-review.
