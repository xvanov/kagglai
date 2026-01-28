---
name: 'step-v-01-validate'
description: 'Validate the Image EDA against quality checklist and standards'

stateFile: '{experiments_folder}/.image-eda-state.yaml'
edaReportFile: '{docs_folder}/eda-report-images.md'
currentUnderstandingFile: '{docs_folder}/current-understanding.md'
edaFolder: '{experiments_folder}/eda'
dashboardFolder: '{experiments_folder}/eda/dashboard'
checklistFile: '../data/image-eda-checklist.md'
editStepFile: '../steps-e/step-e-01-assess.md'
---

# Validate Step 1: Validate Image EDA

## STEP GOAL:

To validate the completed Image EDA against quality standards, verify all artifacts meet requirements, and ensure the EDA is ready for handoff to experiment-cycle.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE THE VALIDATOR checking quality
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the workflow orchestrator in validation mode
- ✅ Check each artifact against quality standards
- ✅ Report issues clearly with severity
- ✅ Route to edit mode if fixes needed

### Step-Specific Rules:

- 🎯 Focus ONLY on validation - no fixing here
- 🚫 FORBIDDEN to modify any artifacts
- 💬 Be specific about what passes and what fails
- 🚪 Route to edit mode for any fixes needed

## EXECUTION PROTOCOLS:

- 🎯 Load checklist and state file
- 💾 Check each artifact against checklist
- 📖 Generate validation report
- 🚫 Do NOT modify - just validate

## CONTEXT BOUNDARIES:

- User invoked validate mode
- EDA should be complete (or partially complete)
- Need to verify quality and completeness

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Validation Context

Load {stateFile} and extract:
- `stepsCompleted` array
- `currentPhase`
- `phase_outputs` dictionary

Load {checklistFile} for validation criteria.

### 2. Check EDA Completeness

**Phase Completion Check:**

| Phase | Step | Status |
|-------|------|--------|
| 1 | Init | {check stepsCompleted} |
| 2 | Data Acquisition | {check stepsCompleted} |
| 3 | Basic Statistics | {check stepsCompleted} |
| 4 | Label Analysis | {check stepsCompleted} |
| 5 | Visual Patterns | {check stepsCompleted} |
| 6 | Data Quality | {check stepsCompleted} |
| 7 | Insights | {check stepsCompleted} |
| 8 | Dashboard | {check stepsCompleted} |
| 9 | Model Selection | {check stepsCompleted} |
| 10 | Completion | {check stepsCompleted} |

**IF any phase incomplete:**
- Note which phases are missing
- Continue validation on completed phases
- Include incompleteness in final report

### 3. Validate Scripts

For each script in {edaFolder}, verify:

**01_data_sampling.py:**
- [ ] File exists
- [ ] Has docstring explaining purpose
- [ ] Configurable sample sizes
- [ ] Error handling present
- [ ] Can run standalone (python script.py)

**02_basic_stats.py:**
- [ ] File exists
- [ ] Analyzes image dimensions
- [ ] Analyzes file sizes
- [ ] Analyzes formats
- [ ] Outputs summary statistics

**03_label_analysis.py:**
- [ ] File exists
- [ ] Counts classes
- [ ] Measures imbalance
- [ ] Identifies labeling issues
- [ ] Outputs distribution data

**04_visual_patterns.py:**
- [ ] File exists
- [ ] Identifies good examples
- [ ] Identifies bad examples
- [ ] Generates visual outputs
- [ ] Documents patterns found

**05_data_quality.py:**
- [ ] File exists
- [ ] Classifies quality levels
- [ ] Generates filtering recommendations
- [ ] Outputs quality metrics

### 4. Validate Documents

**{edaReportFile}:**
- [ ] File exists
- [ ] All 7 sections populated
- [ ] Data overview complete
- [ ] Statistics match script outputs
- [ ] Insights section has strategic recommendations
- [ ] Model recommendations present

**{currentUnderstandingFile}:**
- [ ] File exists
- [ ] Section 2 (Data) updated with EDA findings
- [ ] Section 3 (Model) updated with recommendations
- [ ] Information is consistent with EDA report

**{edaFolder}/06_insights.md:**
- [ ] File exists
- [ ] Strategic insights documented
- [ ] Key findings prioritized
- [ ] Recommendations actionable

### 5. Validate Dashboard

**{dashboardFolder}/app.py:**
- [ ] File exists
- [ ] Streamlit imports present
- [ ] Data loading functional
- [ ] At least 3 visualization sections
- [ ] Interactive elements present
- [ ] Can launch without errors

**Dashboard Launch Test:**
Attempt to verify dashboard can start:
```bash
cd {dashboardFolder} && streamlit run app.py --server.headless true &
sleep 5
# Check if process started
kill %1 2>/dev/null
```

### 6. Cross-Validation Checks

**Consistency Checks:**
- [ ] Dataset size in report matches script output
- [ ] Class count consistent across documents
- [ ] Imbalance severity consistent
- [ ] Recommendations align with findings

**Traceability Checks:**
- [ ] Each insight traces to data finding
- [ ] Model recommendations justified by data
- [ ] Quality thresholds documented

### 7. Generate Validation Report

"**Image EDA Validation Report**

**Validation Date:** {current_date}
**Project:** {project_name}

---

## Summary

| Category | Pass | Fail | Warn |
|----------|------|------|------|
| Scripts | {n} | {n} | {n} |
| Documents | {n} | {n} | {n} |
| Dashboard | {n} | {n} | {n} |
| Consistency | {n} | {n} | {n} |

**Overall Status:** {PASS / PASS WITH WARNINGS / FAIL}

---

## Detailed Results

### Scripts
{detailed results for each script}

### Documents
{detailed results for each document}

### Dashboard
{detailed results for dashboard}

### Consistency
{detailed results for cross-validation}

---

## Issues Found

**Critical (must fix):**
{list of critical issues}

**Warnings (should fix):**
{list of warnings}

**Notes:**
{list of minor observations}

---

## Recommendation

{Based on results:}
- IF all pass: 'EDA is validated and ready for experiment-cycle'
- IF warnings only: 'EDA is usable but consider addressing warnings'
- IF critical issues: 'EDA requires fixes before proceeding'"

### 8. Present Results and Options

"**Validation Complete**

{summary of results}

**What would you like to do?**

**[A]ccept** - Accept EDA as validated (if no critical issues)
**[E]dit** - Go to edit mode to fix issues
**[R]e-run** - Re-run validation after manual fixes
**[D]etails** - View detailed validation report
**[Q]uit** - Exit validation mode

Select:"

### Menu Handling Logic:

#### IF A (Accept):

**IF critical issues exist:**
"Cannot accept with critical issues. Please fix issues first."
Redisplay menu.

**IF no critical issues:**
Update {stateFile}:
```yaml
validation:
  status: 'VALIDATED'
  date: {current_date}
  warnings: {count}
```

"**EDA Validated**

The Image EDA has been validated and is ready for handoff to experiment-cycle.

To start experimenting:
```
/bmad:bmds:workflows:experiment-cycle
```"

Exit validation mode.

#### IF E (Edit):

"Routing to edit mode to address issues..."
Load, read entire file, then execute {editStepFile}

#### IF R (Re-run):

"Re-running validation..."
Go back to Section 1 and repeat validation.

#### IF D (Details):

Display the full validation report from Section 7.
Then redisplay menu.

#### IF Q (Quit):

"Exiting validation mode. Issues found have NOT been addressed."
Exit.

#### IF Any Other:

Help user, redisplay menu.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All artifacts checked against standards
- Clear pass/fail/warn for each item
- Consistency verified across documents
- Actionable report generated
- Appropriate routing based on results

### ❌ SYSTEM FAILURE:

- Missing validation checks
- Accepting EDA with critical issues
- Not checking consistency
- Vague or unhelpful report

**Master Rule:** Validate thoroughly. Report clearly. Don't accept critical issues. Route to edit if fixes needed.
