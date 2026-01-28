---
name: 'step-12-architecture-review'
description: 'Review architecture documents'

nextStepFile: './step-13-gap-fill.md'
fixStepFile: './step-12b-architecture-fix.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
archFile: '{experiments_folder}/docs/current-architecture.md'
specFile: '{experiments_folder}/docs/technical-spec.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
reviewCriteriaFile: '../data/review-criteria.md'
---

# Step 12: Architecture Review

## STEP GOAL:

To validate architecture documents and update current-understanding sections 4 and 5.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FRESH VALIDATOR
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style

### Step-Specific Rules:

- 🎯 Focus on validation
- 🚫 FORBIDDEN to auto-fix
- 📋 Update current-understanding sections 4 & 5

## MANDATORY SEQUENCE

### 1. Load and Validate Documents

Check:
- [ ] All components documented
- [ ] Paths are accurate
- [ ] Commands are runnable
- [ ] Configs are complete
- [ ] Extension points clear

Report findings.

### 2. User Decision

If issues: route to fix or accept.

### 3. Update Current Understanding Sections 4 & 5

```markdown
## 4. Training & Pipeline

### 4.1 Effective Strategies
| Strategy | Impact | Evidence | Config |
|----------|--------|----------|--------|
{from brownfield}

### 4.2 Ineffective Strategies
| Strategy | Result | Why Failed |
|----------|--------|------------|
{from brownfield}

---

## 5. Post-Processing

### 5.1 Current Pipeline
{from architecture doc}

### 5.2 Threshold Tuning
{from architecture doc}
```

### 4. Update Sidecar and Proceed

"**Architecture Review Complete**

**[C]ontinue** to Gap Fill"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Documents validated
- Current understanding sections 4 & 5 updated
- User confirmed

### ❌ SYSTEM FAILURE:
- Auto-fixing
- Skipping validation
- Not updating current-understanding

**Master Rule:** Validate, update, proceed.
