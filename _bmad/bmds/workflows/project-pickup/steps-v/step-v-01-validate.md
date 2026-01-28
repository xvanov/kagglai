---
name: 'step-v-01-validate'
description: 'Validate project pickup completeness and quality'

sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
docsFolder: '{experiments_folder}/docs'
validationChecklistFile: '../data/validation-checklist.md'
reviewCriteriaFile: '../data/review-criteria.md'
---

# Validate Mode: Project Pickup Validation

## STEP GOAL:

To validate a completed project pickup against quality criteria and generate a validation report.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 This is a validation run - read-only
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE THE VALIDATOR, checking quality
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Step-Specific Rules:

- 🎯 Focus on validation, not fixing
- 🚫 FORBIDDEN to modify documents
- 💬 Report issues clearly with severity
- 📄 Generate validation report

## MANDATORY SEQUENCE

### 1. Load Validation Context

Load {sidecarFile} and {validationChecklistFile}.

"**Project Pickup Validation**

I'll check your project pickup against quality criteria..."

### 2. Check Document Completeness

For each required document:
- Exists?
- Has all required sections?
- Sections have content?

"**Document Completeness:**

| Document | Exists | Complete | Issues |
|----------|--------|----------|--------|
| problem-statement.md | {Y/N} | {Y/N} | {issues} |
| eda-report.md | {Y/N} | {Y/N} | {issues} |
| sota-synthesis.md | {Y/N} | {Y/N} | {issues} |
| research-directions.md | {Y/N} | {Y/N} | {issues} |
| technical-spec.md | {Y/N} | {Y/N} | {issues} |
| current-understanding.md | {Y/N} | {Y/N} | {issues} |
| current-architecture.md | {Y/N} | {Y/N} | {issues} |
| hypothesis-registry.md | {Y/N} | {Y/N} | {issues} |"

### 3. Check Document Quality

Load {reviewCriteriaFile} and check each document:

**Problem Statement:**
- [ ] Objective clear
- [ ] Metric defined
- [ ] Constraints listed

**EDA Report:**
- [ ] All sections filled
- [ ] Data-driven insights
- [ ] Hypotheses generated

**SoTA Synthesis:**
- [ ] Current approaches documented
- [ ] Gaps identified
- [ ] Sources cited

**Research Directions:**
- [ ] Priorities ranked
- [ ] Evidence provided
- [ ] First experiments suggested

**Technical Spec:**
- [ ] Architecture documented
- [ ] Commands provided
- [ ] Extension points clear

**Current Understanding:**
- [ ] All 6 sections complete
- [ ] Change log maintained

**Current Architecture:**
- [ ] All components documented
- [ ] Reproducibility info included

**Hypothesis Registry:**
- [ ] Initial hypotheses present
- [ ] Brownfield learnings captured

### 4. Check Implementation

- [ ] src/ folder organized
- [ ] models/baselines/ has model
- [ ] submissions/ has valid submission
- [ ] Environment documented

### 5. Generate Validation Report

"**Validation Report**

**Project:** {project_name}
**Validated:** {date}

---

**Summary:**
- Documents: {X}/{total} complete
- Quality checks: {Y}/{total} passed
- Implementation: {Z}/{total} verified

---

**Critical Issues (must fix):**
{list or 'None'}

**Major Issues (should fix):**
{list or 'None'}

**Minor Issues (can defer):**
{list or 'None'}

**Warnings:**
{list or 'None'}

---

**Overall Status:** {PASS / PASS WITH WARNINGS / NEEDS ATTENTION / FAIL}

---

**Recommendations:**
{specific recommendations if issues found}

---"

### 6. Offer Next Steps

"**Validation Complete**

Status: {status}

Would you like to:
**[E]dit** - Fix issues in edit mode
**[R]eport** - Save report to file
**[D]one** - Exit validation"

If E: Route to edit mode
If R: Save report to {docsFolder}/validation-report-{date}.md
If D: Exit

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All documents checked
- Quality criteria applied
- Clear report generated
- Issues categorized by severity
- Recommendations provided

### ❌ SYSTEM FAILURE:
- Modifying documents
- Skipping checks
- Unclear issue reporting
- No actionable recommendations

**Master Rule:** Validate thoroughly, report clearly, never modify.
