---
name: 'step-03-problem-statement-review'
description: 'Fresh Data Analyst validates problem statement and implements fixes'

nextStepFile: './step-04-eda-basic.md'
fixOnlyFile: './step-03b-problem-statement-fix.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
specFile: '{experiments_folder}/docs/problem-statement.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
reviewCriteriaFile: '../data/review-criteria.md'
validationChecklistFile: '../data/validation-checklist.md'

# Input files for verification
descriptionFile: '{experiments_folder}/problem-inputs/description.md'
rulesFile: '{experiments_folder}/problem-inputs/rules.md'
dataAccessFile: '{experiments_folder}/problem-inputs/data-access.md'
submissionFile: '{experiments_folder}/problem-inputs/submission-format.md'
---

# Step 3: Problem Statementification Review

## STEP GOAL:

To validate the problem statementification against source documents and quality criteria, identify issues, implement fixes, and initialize Section 1 of current-understanding.md. This step uses the Author/Validator pattern - you are a FRESH instance reviewing another's work.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER assume the authored document is correct
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A VALIDATOR, skeptical and thorough
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a FRESH Data Analyst instance - no memory of authoring
- ✅ Assume errors exist until proven otherwise
- ✅ Verify every claim against source documents
- ✅ Your job is to catch what the author missed

### Step-Specific Rules:

- 🎯 Focus on VALIDATION first, then FIXES
- 🚫 FORBIDDEN to approve without thorough checking
- 💬 Be specific about issues - location, problem, fix
- 🚪 Must produce a review report regardless of outcome

## EXECUTION PROTOCOLS:

- 🎯 Read problem-statement.md with skeptical eye
- 💾 Verify claims against original source documents
- 📖 Apply review criteria systematically
- 🚫 FORBIDDEN to just skim - check every section

## CONTEXT BOUNDARIES:

- The problem-statement.md was authored by a previous instance
- You have access to all original input documents for verification
- Review criteria provide the validation standards
- You may fix issues directly OR route to fix-only step if context is large

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 03: Problem Statementification Review**

I am a fresh Data Analyst instance reviewing the problem statementification. I will validate every claim against source documents and identify any issues.

Beginning systematic review..."

### 2. Load Review Standards

Read {reviewCriteriaFile} for the "Problem Statementification Review" section.
Read {validationChecklistFile} for the "Problem Statementification Validation" checklist.

### 3. Read the Problem Statement

Read {specFile} completely.

**While reading, note:**
- Claims that seem unverified
- Sections that seem incomplete
- Inconsistencies within the document
- Template placeholders remaining

### 4. Verify Against Source Documents

For each major claim in the spec, verify against the original:

**Read and cross-check:**
1. {descriptionFile} - Verify problem statement, task type, objective
2. {rulesFile} - Verify metric formula, constraints, timeline
3. {dataAccessFile} - Verify data access instructions, file details
4. {submissionFile} - Verify submission format, limits

**For each section, check:**
- [ ] Facts match source documents exactly
- [ ] No information was invented
- [ ] Gaps are properly marked (not filled with assumptions)
- [ ] Cross-references are accurate

### 5. Apply Validation Checklist

Work through each item in the Problem Statementification Validation checklist:

**Completeness:**
- [ ] Problem statement is clear and unambiguous
- [ ] Task type correctly identified
- [ ] Evaluation metric fully specified with formula
- [ ] All data files documented with schemas
- [ ] Submission format requirements complete
- [ ] All constraints captured (compute, code, legal)
- [ ] Timeline accurate and complete
- [ ] Source documents referenced

**Accuracy:**
- [ ] Metric formula matches official documentation
- [ ] Data schemas verified against actual files
- [ ] Submission format tested with example
- [ ] Constraints cross-checked with rules

**Consistency:**
- [ ] No contradictory information
- [ ] Terminology consistent throughout
- [ ] References accurate

### 6. Generate Review Report

Create a review report with this structure:

```markdown
## Problem Statementification Review Report

**Document:** problem-statement.md
**Reviewer:** Data Analyst (Validator Instance)
**Date:** {date}

### Summary
{1-2 sentence overall assessment}

### Critical Issues (Must Fix)
{List any blocking issues}

### Major Issues (Should Fix)
{List significant gaps or inaccuracies}

### Minor Issues (Can Fix Later)
{List small improvements}

### Verification Results
- [x] {Checks that passed}
- [ ] {Checks that failed}

### Recommendation
{APPROVE / APPROVE WITH FIXES / REJECT}
```

### 7. Implement Fixes (or Route to Fix-Only)

**IF no Critical or Major issues:**
- Report: "**Review passed with minor or no issues.**"
- Proceed to Section 8

**IF Critical or Major issues exist:**
- Assess the scope of fixes needed

**IF fixes are straightforward (can complete in this session):**
- Make the fixes directly to {specFile}
- Document each fix made
- Proceed to Section 8

**IF fixes are extensive (context getting large):**
- Append the review report to {sidecarFile} under "## Validation Reports"
- Display: "**Review found issues requiring extensive fixes.**"
- Display: "The review report has been saved to the sidecar file."
- Present options:
  - **[C]ontinue** - I will implement all fixes now
  - **[F]ix-only** - Route to fix-only step (recommended if context is large)
- If user selects [F], load and execute {fixOnlyFile}

### 8. Initialize current-understanding.md Section 1

Create or update {currentUnderstandingFile} with Section 1 (Problem & Task):

```markdown
# Current Understanding

**Project:** {from spec}
**Last Updated:** {date}

---

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

---

## 2. Data
{To be filled by EDA phase}

---

## 3. Model/Research
{To be filled by SoTA phase}
```

### 9. Update Sidecar

Update {sidecarFile}:
- Add 'step-03-problem-statement-review' to stepsCompleted
- Set lastStep to 'step-03-problem-statement-review'
- Update lastUpdated date
- Add session note summarizing review outcome
- Append review report under "## Validation Reports" if not already added

### 10. Summary and Proceed

"**Problem Statementification Review Complete**

**Review outcome:** {APPROVED / APPROVED WITH FIXES}

**Issues found:** {count by severity}
**Fixes applied:** {count}

**Documents updated:**
- problem-statement.md {if fixes applied}
- current-understanding.md (Section 1 initialized)

**Next step:** EDA Basic - Pull data and generate basic statistics

**[C]ontinue** to EDA basic analysis"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Every claim verified against source documents
- Review report generated with specific issues
- Fixes implemented (or routed to fix-only)
- current-understanding.md Section 1 populated
- Clear handoff to EDA step

### ❌ SYSTEM FAILURE:

- Approving without thorough verification
- Vague issue descriptions ("some things seem off")
- Not checking against all source documents
- Skipping the review criteria/checklist
- Not initializing current-understanding.md
- Leaving critical issues unfixed

**Master Rule:** Assume errors exist. Verify everything. Be specific about issues. Fix what you find.
