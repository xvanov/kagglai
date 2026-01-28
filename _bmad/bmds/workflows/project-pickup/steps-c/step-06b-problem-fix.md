---
name: 'step-06b-problem-fix'
description: 'Fix issues in problem statement identified during review'

returnStepFile: './step-06-problem-review.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
problemStatementFile: '{experiments_folder}/docs/problem-statement.md'
---

# Step 6b: Problem Statement Fix

## STEP GOAL:

To fix specific issues identified in the problem statement review, then return to review for re-validation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE Atlas, fixing specific issues
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are Atlas, addressing specific issues
- ✅ Fix ONLY the identified issues
- ✅ Don't expand scope beyond fixes
- ✅ Return to review when done

### Step-Specific Rules:

- 🎯 Focus ONLY on fixing identified issues
- 🚫 FORBIDDEN to add new content beyond fixes
- 💬 Confirm each fix with user
- 🔄 Return to review step when complete

## MANDATORY SEQUENCE

### 1. Load Context

Load {sidecarFile} to get the issues from review.
Load {problemStatementFile}.

"**Fixing Problem Statement Issues**

Issues to address:
{list issues from review}"

### 2. Address Each Issue

For each issue:

"**Issue {N}: {description}**
Section: {section}
Severity: {severity}

**Current text:**
{current content}

**Proposed fix:**
{proposed content}

Accept this fix? [Y]es / [M]odify / [S]kip"

Apply user-approved fixes.

### 3. Save Updated Document

Write fixed content to {problemStatementFile}.

### 4. Summary

"**Fixes Applied:**
- {issue 1}: {fixed/skipped}
- {issue 2}: {fixed/skipped}

Returning to review for re-validation..."

### 5. Return to Review

Update sidecar, then load {returnStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Each issue addressed or explicitly skipped
- User approved fixes
- Document updated
- Returned to review

### ❌ SYSTEM FAILURE:
- Auto-fixing without approval
- Adding unrelated content
- Not returning to review

**Master Rule:** Fix only what was identified, confirm each fix, return to review.
