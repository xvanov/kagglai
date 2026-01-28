---
name: 'step-06-problem-review'
description: 'Review problem statement and initialize current-understanding section 1'

nextStepFile: './step-07-eda-audit.md'
fixStepFile: './step-06b-problem-fix.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
problemStatementFile: '{experiments_folder}/docs/problem-statement.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
currentUnderstandingTemplate: '{project-root}/_bmad/bmds/workflows/experiment-cycle/data/current-understanding-template.md'
reviewCriteriaFile: '../data/review-criteria.md'
---

# Step 6: Problem Statement Review

## STEP GOAL:

To validate the problem statement with fresh eyes and initialize section 1 of current-understanding.md (Problem & Task).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FRESH VALIDATOR - pretend you didn't write this
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a fresh reviewer, not the author
- ✅ Look for gaps, inconsistencies, ambiguities
- ✅ Validate against review criteria
- ✅ User confirms if issues need fixing

### Step-Specific Rules:

- 🎯 Focus ONLY on validation and current-understanding init
- 🚫 FORBIDDEN to auto-fix - route to fix step if needed
- 💬 Present findings clearly
- 📋 Initialize current-understanding section 1

## MANDATORY SEQUENCE

### 1. Load Documents

Load {problemStatementFile} completely.
Load {reviewCriteriaFile} for validation criteria.

"**Reviewing Problem Statement**

I'm reviewing with fresh eyes to catch any issues..."

### 2. Validate Against Criteria

Check each criterion from review-criteria.md:

**Completeness:**
- [ ] Objective clearly stated
- [ ] Evaluation metric defined with formula
- [ ] All constraints documented
- [ ] Data description complete
- [ ] Submission requirements clear

**Clarity:**
- [ ] No ambiguous language
- [ ] Technical terms defined
- [ ] Examples where helpful

**Accuracy:**
- [ ] Metric formula correct
- [ ] Constraint interpretation correct
- [ ] Timeline accurate

**Consistency:**
- [ ] No contradictions
- [ ] Aligned with rules.md source

### 3. Report Findings

"**Review Findings:**

**Passed:**
- {criteria that passed}

**Issues Found:**
| Issue | Section | Severity | Description |
|-------|---------|----------|-------------|
{any issues}

**Severity Guide:**
- Critical: Blocks progress
- Major: Should fix before EDA
- Minor: Can fix later"

### 4. User Decision

"**Review Complete**

{IF no issues}
Problem statement is validated. Ready to proceed.

{IF issues found}
Found {X} issues ({critical}, {major}, {minor}).

How would you like to proceed?
**[F]ix** - Route to fix step (recommended if Critical/Major)
**[A]ccept** - Accept as-is, note issues for later
**[C]ontinue** - Continue with validated document"

**IF user chooses F:** Load {fixStepFile}
**IF user chooses A or C:** Continue to step 5

### 5. Initialize Current Understanding

Load {currentUnderstandingTemplate} and create {currentUnderstandingFile} with Section 1:

```markdown
---
lastUpdated: {date}
updatedBy: step-06-problem-review
---

# Current Understanding

## 1. Problem & Task

### 1.1 Objective
- Competition/task: {from problem-statement}
- Goal: {what we're optimizing}
- Source: `docs/problem-statement.md`

### 1.2 Evaluation Metric
- **Metric:** {name}
- **Formula:** {formula}
- **Implementation:** {path if exists, else TBD}
- **Gotchas:** {known edge cases}

### 1.3 Constraints & Rules
- {constraint 1} - Source: `docs/problem-statement.md`
- {constraint 2}
- **Forbidden:** {explicit prohibitions}

---

## 2. Data
{To be filled in EDA steps}

---

## 3. Model
{To be filled in research steps}

---

## 4. Training & Pipeline
{To be filled in architecture steps}

---

## 5. Post-Processing
{To be filled in architecture steps}

---

## 6. Open Questions
- [ ] {any open questions from problem statement}

---

## Change Log
| Date | Source | Section Updated | Summary |
|------|--------|-----------------|---------|
| {date} | step-06-problem-review | 1. Problem & Task | Initial creation |
```

### 6. Update Sidecar

Update {sidecarFile}:
- Add to stepsCompleted
- Note review status

### 7. Proceed

"**Problem Review Complete**

- Problem statement: {VALIDATED/ACCEPTED}
- Current understanding: Section 1 initialized

**[C]ontinue** to EDA Audit"

Load {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Validation performed against criteria
- Issues clearly reported
- User decision on issues
- Current-understanding initialized
- Section 1 populated correctly

### ❌ SYSTEM FAILURE:

- Auto-fixing without user input
- Skipping validation criteria
- Not initializing current-understanding
- Missing issue severity ratings

**Master Rule:** Validate thoroughly, report clearly, let user decide on fixes.
