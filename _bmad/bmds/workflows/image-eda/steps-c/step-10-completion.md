---
name: 'step-10-completion'
description: 'Complete the Image EDA workflow - verify all artifacts, summarize findings, prepare for handoff'

stateFile: '{experiments_folder}/.image-eda-state.yaml'
edaReportFile: '{docs_folder}/eda-report-images.md'
currentUnderstandingFile: '{docs_folder}/current-understanding.md'
edaFolder: '{experiments_folder}/eda'
dashboardFolder: '{experiments_folder}/eda/dashboard'
checklistFile: '../data/image-eda-checklist.md'
---

# Step 10: Completion

## STEP GOAL:

To complete the Image EDA workflow by verifying all artifacts, providing a final summary, and preparing for handoff to experiment-cycle.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE THE ORCHESTRATOR completing the workflow
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the workflow orchestrator completing the EDA
- ✅ Verify all artifacts are present and complete
- ✅ Provide comprehensive summary for user
- ✅ Prepare handoff for next workflow (experiment-cycle)

### Step-Specific Rules:

- 🎯 This is the FINAL step - no more analysis
- 🚫 FORBIDDEN to start new analysis phases
- 💬 Summarize, verify, and hand off
- 🚪 No next step - workflow complete

## EXECUTION PROTOCOLS:

- 🎯 Load checklist and verify all artifacts
- 💾 Finalize state file with completion status
- 📖 Mark EDA report as complete
- 🎁 Present final summary and handoff information

## CONTEXT BOUNDARIES:

- All phases complete (1-9)
- All documents updated
- Dashboard approved by user
- Ready for handoff to experiment-cycle

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load and Verify Checklist

Load {checklistFile} and verify each item:

**Phase Completeness:**
- [ ] Phase 2: Data Acquisition - script exists
- [ ] Phase 3: Basic Statistics - script exists
- [ ] Phase 4: Label Analysis - script exists
- [ ] Phase 5: Visual Patterns - script exists
- [ ] Phase 6: Data Quality - script exists
- [ ] Phase 7: Insights - document exists
- [ ] Phase 8: Dashboard - app exists and runs
- [ ] Phase 9: Model Selection - recommendations documented

**Document Completeness:**
- [ ] `eda-report-images.md` - all sections populated
- [ ] `current-understanding.md` - Sections 2 and 3 updated

**Artifact Inventory:**
Verify these files exist:
```
{edaFolder}/
├── 01_data_sampling.py
├── 02_basic_stats.py
├── 03_label_analysis.py
├── 04_visual_patterns.py
├── 05_data_quality.py
├── 06_insights.md
└── dashboard/
    └── app.py
```

### 2. Handle Missing Items

**IF any verification fails:**

"**Verification Issue Found:**
{description of missing item}

Would you like to:
**[F]ix** - Re-run the phase that's incomplete
**[S]kip** - Mark as incomplete and proceed anyway
**[C]ancel** - Stop completion and investigate"

Handle user choice appropriately.

**IF all verifications pass:**

Continue to Section 3.

### 3. Finalize State File

Update {stateFile}:
```yaml
stepsCompleted: ['step-01-init', 'step-02-data-acquisition', 'step-03-basic-stats',
                 'step-04-label-analysis', 'step-05-visual-patterns', 'step-06-data-quality',
                 'step-07-insights', 'step-08-dashboard', 'step-09-model-selection', 'step-10-completion']
currentPhase: 'complete'
completedDate: {current_date}
status: 'COMPLETE'
```

### 4. Finalize EDA Report

Update {edaReportFile} frontmatter:
```yaml
stepsCompleted: ['all']
lastStep: 'step-10-completion'
lastUpdated: {current_date}
status: 'COMPLETE'
```

Check all validation checkboxes in the report.

### 5. Present Final Summary

"**Image EDA Workflow Complete**

---

## Summary

**Project:** {project_name}
**Dataset:** {image_dataset_path}
**Task:** {task_type}
**Completed:** {current_date}

---

## Key Findings

**Data Overview:**
- Total Images: {count}
- Quality Distribution: {high}% high / {med}% medium / {low}% low
- Class Imbalance: {severity}

**Critical Insights:**
1. {insight 1}
2. {insight 2}
3. {insight 3}

**Recommended Model:** {top model recommendation}

---

## Artifacts Created

**Scripts (all rerunnable):**
- `{edaFolder}/01_data_sampling.py`
- `{edaFolder}/02_basic_stats.py`
- `{edaFolder}/03_label_analysis.py`
- `{edaFolder}/04_visual_patterns.py`
- `{edaFolder}/05_data_quality.py`

**Documents:**
- `{edaReportFile}` - Complete EDA report
- `{edaFolder}/06_insights.md` - Strategic insights

**Dashboard:**
- `{dashboardFolder}/app.py`
- Run: `streamlit run {dashboardFolder}/app.py`

**Updated:**
- `current-understanding.md` - Sections 2 (Data) and 3 (Model)

---

## Next Steps

The Image EDA is complete. You can now:

1. **Run the dashboard** to explore findings interactively
2. **Start experiment-cycle** to begin model training
3. **Re-run any script** to update analysis with new data
4. **Edit the EDA** using edit mode if needed

---

## Handoff to Experiment-Cycle

The following documents are ready for experiment-cycle:
- `current-understanding.md` - Updated with data and model info
- `eda-report-images.md` - Complete EDA reference
- Model recommendations with training strategy

To start experimenting:
```
/bmad:bmds:workflows:experiment-cycle
```

---

**Thank you for using the Image EDA Workflow!**"

### 6. Final Menu

Display:
"**Workflow Complete**

**[D]ashboard** - Launch the dashboard
**[R]eport** - View the EDA report
**[E]xperiment** - Start experiment-cycle
**[Q]uit** - Exit workflow

Select an option:"

#### Menu Handling Logic:

- IF D: Run `streamlit run {dashboardFolder}/app.py`
- IF R: Display {edaReportFile} content
- IF E: Suggest running `/bmad:bmds:workflows:experiment-cycle`
- IF Q: Exit with completion message
- IF Any other: Help user, redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All artifacts verified present
- State file marked complete
- EDA report finalized
- Comprehensive summary presented
- Clear handoff to experiment-cycle

### ❌ SYSTEM FAILURE:

- Missing artifacts not detected
- Incomplete summary
- State file not finalized
- No handoff information

**Master Rule:** This is the end. Verify everything. Summarize completely. Hand off clearly.
