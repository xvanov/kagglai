---
name: 'step-v-01-validate'
description: 'Comprehensive validation of all project setup artifacts'

sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
validationChecklistFile: '../data/validation-checklist.md'

# All documents to validate
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
sotaSynthesisFile: '{experiments_folder}/docs/sota-synthesis.md'
researchDirectionsFile: '{experiments_folder}/docs/research-directions.md'
technicalSpecFile: '{experiments_folder}/docs/technical-spec.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
currentArchitectureFile: '{experiments_folder}/docs/current-architecture.md'
hypothesisRegistryFile: '{experiments_folder}/docs/hypothesis-registry.md'

# Implementation artifacts
srcFolder: '{experiments_folder}/src'
modelsFolder: '{experiments_folder}/models'
submissionsFolder: '{experiments_folder}/submissions'
---

# Step V-01: Comprehensive Validation

## STEP GOAL:

To perform a comprehensive validation of all project setup artifacts, checking completeness, consistency, and readiness for the experiment-cycle workflow.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER skip any validation check
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: This is a thorough validation - be systematic
- 📋 YOU ARE A VALIDATOR checking everything
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are performing comprehensive quality assurance
- ✅ Check each document against its validation criteria
- ✅ Check cross-document consistency
- ✅ Provide actionable feedback on issues

### Step-Specific Rules:

- 🎯 Focus on THOROUGH VALIDATION
- 🚫 FORBIDDEN to fix issues (just report them)
- 💬 Be specific about issues found
- 🚪 This is a quality gate for experiment-cycle

## EXECUTION PROTOCOLS:

- 🎯 Load validation criteria
- 💾 Check each document systematically
- 📖 Check cross-document consistency
- 🚫 FORBIDDEN to make edits - report only

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Announce Validation

"**Comprehensive Validation**

I will validate all project setup artifacts against quality criteria and check for consistency.

Loading validation criteria..."

### 2. Load Validation Criteria

Read {validationChecklistFile} to understand validation standards.

### 3. Validate Challenge Specification

Check {challengeSpecFile}:

**Completeness:**
- [ ] Problem statement clear and unambiguous
- [ ] Task type correctly identified
- [ ] Evaluation metric fully specified with formula
- [ ] All data files documented with schemas
- [ ] Submission format requirements complete
- [ ] All constraints captured (compute, code, legal)
- [ ] Timeline accurate and complete
- [ ] Source documents referenced

**Accuracy:**
- [ ] Metric formula looks correct
- [ ] Constraints are specific numbers, not vague
- [ ] Submission format is precise

**Issues found:** {list or "None"}

### 4. Validate EDA Report

Check {edaReportFile}:

**Completeness:**
- [ ] All data files analyzed
- [ ] Feature types correctly identified
- [ ] Target distribution analyzed
- [ ] Missing data patterns documented
- [ ] Data quality issues catalogued
- [ ] Feature relationships explored
- [ ] Train-test consistency checked
- [ ] Recommendations provided

**Quality:**
- [ ] Statistics look reasonable
- [ ] Patterns have evidence
- [ ] Recommendations are actionable

**Issues found:** {list or "None"}

### 5. Validate SoTA Synthesis

Check {sotaSynthesisFile}:

**Completeness:**
- [ ] All major architecture families covered
- [ ] Recent advances included (last 2 years)
- [ ] Similar competitions analyzed
- [ ] Applicability to this competition assessed
- [ ] All sources properly cited

**Quality:**
- [ ] Recommendations grounded in evidence
- [ ] Trade-offs acknowledged
- [ ] Relevance to this competition clear

**Issues found:** {list or "None"}

### 6. Validate Research Directions

Check {researchDirectionsFile}:

**Completeness:**
- [ ] All directions grounded in spec, EDA, or SoTA
- [ ] Priorities clearly justified
- [ ] Difficulty assessments provided
- [ ] Dependencies mapped
- [ ] Success criteria defined
- [ ] Excluded directions documented

**Quality:**
- [ ] Success criteria measurable
- [ ] Difficulty assessments realistic
- [ ] Implementation roadmap practical

**Issues found:** {list or "None"}

### 7. Validate Technical Specification

Check {technicalSpecFile}:

**Completeness:**
- [ ] Environment setup documented
- [ ] Data pipeline specified
- [ ] Model configuration documented
- [ ] Training strategy defined
- [ ] Inference pipeline documented
- [ ] Submission format handled
- [ ] All tasks listed

**Feasibility:**
- [ ] Compute constraints satisfied
- [ ] Dependencies clear
- [ ] Risks identified

**Issues found:** {list or "None"}

### 8. Validate Handoff Documents

Check handoff documents for experiment-cycle:

**current-understanding.md:**
- [ ] Section 1 (Problem & Task) complete
- [ ] Section 2 (Data) complete
- [ ] Section 3 (Model/Research) complete

**current-architecture.md:**
- [ ] Architecture documented
- [ ] Extension points clear
- [ ] Performance baseline recorded

**hypothesis-registry.md:**
- [ ] Initial hypotheses present
- [ ] Format is correct

**Issues found:** {list or "None"}

### 9. Validate Implementation Artifacts

Check implementation:

**Code:**
- [ ] src/ folder exists
- [ ] train.py exists
- [ ] predict.py exists

**Models:**
- [ ] models/baselines/ has checkpoint

**Submissions:**
- [ ] submissions/ has baseline submission

**Issues found:** {list or "None"}

### 10. Cross-Document Consistency

Check consistency across documents:

**Competition name:**
- [ ] Same in all documents

**Evaluation metric:**
- [ ] Same name and formula across docs

**Constraints:**
- [ ] Same values in challenge-spec and technical-spec

**Research direction #1:**
- [ ] Matches what technical-spec implements

**Data characteristics:**
- [ ] EDA findings reflected in technical spec decisions

**Issues found:** {list or "None"}

### 11. Generate Validation Report

"**Validation Report**

**Date:** {date}

---

## Document Validation Results

| Document | Completeness | Quality | Issues |
|----------|--------------|---------|--------|
| challenge-spec.md | {✓/△/✗} | {✓/△/✗} | {count} |
| eda-report.md | {✓/△/✗} | {✓/△/✗} | {count} |
| sota-synthesis.md | {✓/△/✗} | {✓/△/✗} | {count} |
| research-directions.md | {✓/△/✗} | {✓/△/✗} | {count} |
| technical-spec.md | {✓/△/✗} | {✓/△/✗} | {count} |
| current-understanding.md | {✓/△/✗} | {✓/△/✗} | {count} |
| current-architecture.md | {✓/△/✗} | {✓/△/✗} | {count} |
| hypothesis-registry.md | {✓/△/✗} | {✓/△/✗} | {count} |

**Legend:** ✓ = Pass, △ = Minor Issues, ✗ = Major Issues

---

## Implementation Artifacts

| Artifact | Status |
|----------|--------|
| src/ code | {present/missing} |
| Model checkpoint | {present/missing} |
| Baseline submission | {present/missing} |

---

## Cross-Document Consistency

{✓/✗} Competition name consistent
{✓/✗} Evaluation metric consistent
{✓/✗} Constraints consistent
{✓/✗} Direction #1 matches implementation

---

## Issues Summary

**Critical Issues:** {count}
{List critical issues}

**Major Issues:** {count}
{List major issues}

**Minor Issues:** {count}
{List or summarize minor issues}

---

## Overall Assessment

**Status:** {READY / NEEDS WORK / CRITICAL ISSUES}

{Assessment paragraph}

---

## Recommendations

{If issues exist, list recommended actions}

---

## Next Steps

**If READY:**
- Proceed to experiment-cycle workflow
- Handoff documents are validated

**If NEEDS WORK:**
- Use [E]dit mode to address issues
- Re-run validation after fixes

**If CRITICAL ISSUES:**
- Address critical issues first
- May need to re-run create mode steps"

### 12. Update Sidecar

Add validation record to sidecar:

```markdown
### Validation - {date}
- **Result:** {READY/NEEDS WORK/CRITICAL}
- **Issues:** {count}
- **Recommendation:** {summary}
```

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All documents checked systematically
- All validation criteria applied
- Cross-document consistency verified
- Clear report generated
- Issues categorized by severity
- Actionable recommendations provided

### ❌ SYSTEM FAILURE:

- Skipping documents
- Vague issue descriptions
- Not checking consistency
- Making edits (validation only)
- Missing critical issues

**Master Rule:** Check everything. Report clearly. Don't fix - just report.
