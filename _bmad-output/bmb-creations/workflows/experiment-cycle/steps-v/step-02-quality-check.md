---
name: 'step-02-quality-check'
description: 'Comprehensive quality validation of a completed experiment'

experimentFolder: '{experiments_folder}/{experiment_id}'
experimentReadme: '{experiments_folder}/{experiment_id}/readme.md'
experimentPlan: '{experiments_folder}/{experiment_id}/plan.md'
experimentResults: '{experiments_folder}/{experiment_id}/results.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
currentUnderstandingPath: '{docs_folder}/current-understanding.md'
currentArchitecturePath: '{docs_folder}/current-architecture.md'
reviewCriteriaFile: '../data/review-criteria.md'
---

# Step 2: Quality Check

## STEP GOAL:

To perform a comprehensive quality validation of a completed experiment, checking documentation completeness, reproducibility, and traceability.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess unavailable, perform in main thread

### Role Reinforcement:

- ✅ You are a **Quality Auditor** ensuring experiment rigor
- ✅ Check all aspects of documentation and reproducibility
- ✅ Be thorough but fair

### Step-Specific Rules:

- 🎯 Use subprocess Pattern 4 (parallel) for multiple independent checks
- 💬 Each subprocess returns findings for its category
- 📋 Generate a validation report

## MANDATORY SEQUENCE

### 1. Load Experiment Documents

Load all experiment documents:
- `{experimentReadme}` - Design
- `{experimentPlan}` - Implementation plan
- `{experimentResults}` - Results

Load `{reviewCriteriaFile}` for validation criteria.

### 2. Run Parallel Quality Checks

**Launch subprocesses in parallel (Pattern 4):**

**Subprocess 1: Documentation Completeness**
Check:
- [ ] readme.md fully populated (all sections filled)
- [ ] plan.md fully populated (all tasks, checklists)
- [ ] results.md fully populated (metrics, verdict, lessons)
- [ ] All paths in documents are valid

**Subprocess 2: Reproducibility**
Check:
- [ ] Checkpoint saved to documented path
- [ ] Config saved to documented path
- [ ] Training command documented and looks executable
- [ ] Evaluation command documented and looks executable
- [ ] Seeds documented

**Subprocess 3: Traceability**
Check:
- [ ] Git commit recorded in results.md
- [ ] Current Understanding updated (if lessons learned)
- [ ] Current Architecture updated (if VALIDATED)
- [ ] Hypothesis Registry status matches results

**Subprocess 4: Metrics Integrity**
Check:
- [ ] Metrics evaluated on correct dataset (not test for tuning)
- [ ] Baseline and experiment metrics from same evaluation
- [ ] Delta calculation correct
- [ ] Verdict matches success criteria

**If subprocess unavailable:** Perform checks sequentially in main thread.

### 3. Aggregate Findings

Collect results from all checks:

```json
{
  "documentation": {"passed": X, "failed": Y, "issues": [...]},
  "reproducibility": {"passed": X, "failed": Y, "issues": [...]},
  "traceability": {"passed": X, "failed": Y, "issues": [...]},
  "metrics_integrity": {"passed": X, "failed": Y, "issues": [...]}
}
```

### 4. Generate Validation Report

"**Quality Validation Report: EXP-{XXX}**

## Documentation Completeness
- ✓/✗ readme.md complete
- ✓/✗ plan.md complete
- ✓/✗ results.md complete
- ✓/✗ All paths valid

{Issues if any}

## Reproducibility
- ✓/✗ Checkpoint exists at documented path
- ✓/✗ Config exists at documented path
- ✓/✗ Training command documented
- ✓/✗ Evaluation command documented
- ✓/✗ Seeds documented

{Issues if any}

## Traceability
- ✓/✗ Git commit recorded
- ✓/✗ Current Understanding updated
- ✓/✗ Current Architecture updated (if applicable)
- ✓/✗ Registry status correct

{Issues if any}

## Metrics Integrity
- ✓/✗ Correct dataset for evaluation
- ✓/✗ Consistent baseline/experiment evaluation
- ✓/✗ Delta calculation correct
- ✓/✗ Verdict matches criteria

{Issues if any}

---

**Overall Score:** {passed}/{total} checks passed

**Verdict:** {QUALITY_PASS / QUALITY_CONCERNS / QUALITY_FAIL}"

### 5. Provide Recommendations

**If issues found:**

"**Recommendations:**

{For each issue}:
1. **{Category}:** {Issue}
   - Location: {where}
   - Fix: {how to fix}

Would you like to address any of these issues now?"

**If all passed:**

"**Excellent!** This experiment meets all quality standards.

- Documentation is complete and accurate
- Experiment is reproducible
- Full traceability maintained
- Metrics are valid

This is a well-documented, rigorous experiment."

### 6. Present MENU OPTIONS

Display: **Validation Complete - Select an Option:** [F] Fix Issues [V] Validate Another [D] Done

#### Menu Handling Logic:
- IF F: List issues and offer to help fix (may involve editing documents)
- IF V: Return to step-01 to select another experiment
- IF D: "Validation complete."
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All experiment documents loaded
- All quality checks performed (parallel or sequential)
- Comprehensive report generated
- Clear verdict provided
- Actionable recommendations for issues

### ❌ SYSTEM FAILURE:
- Missing quality check categories
- Not checking all criteria
- Vague or non-actionable findings
- Not providing recommendations for issues
