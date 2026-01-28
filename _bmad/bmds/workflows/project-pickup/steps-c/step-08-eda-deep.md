---
name: 'step-08-eda-deep'
description: 'Fill EDA gaps with fresh analysis and update current-understanding section 2'

nextStepFile: './step-09-research-audit.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
notebooksFolder: '{experiments_folder}/notebooks/exploration'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 8: EDA Deep Dive

## STEP GOAL:

To fill gaps identified in EDA audit with fresh analysis and update current-understanding.md section 2 (Data).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE Atlas (Data Analyst), conducting fresh EDA
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are Atlas - curious and thorough
- ✅ Focus on gaps identified in audit
- ✅ Validate and update existing findings
- ✅ Generate actionable insights

### Step-Specific Rules:

- 🎯 Focus on filling identified gaps
- 🚫 FORBIDDEN to redo work that's already complete
- 💬 Present findings for user confirmation
- 📊 Create/update EDA notebooks as needed

## MANDATORY SEQUENCE

### 1. Load Gap List

Load {edaReportFile} to get gaps from audit.

"**Filling EDA Gaps**

Gaps to address:
{list from audit}

I'll conduct fresh analysis for each gap."

### 2. For Each Gap - Conduct Analysis

**Gap: Dataset Overview (if missing)**
- Load data
- Report shape, memory, dtypes
- Basic statistics

**Gap: Target Analysis (if missing)**
- Distribution of target variable
- Class balance (if classification)
- Target statistics

**Gap: Missing Data (if missing)**
- Missing value counts per feature
- Missing patterns
- Potential impact

**Gap: Feature Distributions (if missing)**
- Numeric feature statistics
- Categorical value counts
- Outlier identification

**Gap: Correlations (if missing)**
- Feature-target correlations
- Feature-feature correlations
- Multicollinearity check

**Gap: Anomalies (if missing)**
- Outlier detection
- Data quality issues
- Inconsistencies

Present each analysis result and get user confirmation.

### 3. Update EDA Report

Update {edaReportFile} with gap-filled content:

"**Updating EDA Report:**

- Dataset Overview: {updated}
- Target Analysis: {updated}
- Missing Data: {updated}
- Feature Distributions: {updated}
- Correlations: {updated}
- Anomalies: {updated}

Status changed from DRAFT to COMPLETE."

### 4. Generate Hypotheses

Based on complete EDA:

"**Data-Driven Hypotheses:**

From this analysis, I propose these initial hypotheses:

1. {hypothesis based on finding 1}
2. {hypothesis based on finding 2}
3. {hypothesis based on finding 3}

These will be registered in the hypothesis-registry in a later step."

### 5. Update Current Understanding Section 2

Load {currentUnderstandingFile} and update section 2:

```markdown
## 2. Data

### 2.1 Dataset Overview
| Split | Path | Samples | Class Distribution |
|-------|------|---------|-------------------|
| Train | `{path}` | {N} | {distribution} |
| Val | `{path}` | {N} | {distribution} |
| Test | `{path}` | {N} | DO NOT USE until final |

### 2.2 Data Quality Issues
| Issue | Severity | Affected Samples | Mitigation |
|-------|----------|------------------|------------|
| {issue} | {severity} | {count} | {approach} |

### 2.3 Data Insights
- {insight 1} - Discovered: EDA audit + deep dive
- {insight 2} - Source: `{path}`
```

Add to Change Log.

### 6. Save EDA Notebook (Optional)

If new analysis was conducted:

"**Save analysis as notebook?**

I can save this analysis to `{notebooksFolder}/eda-pickup-{date}.ipynb`

**[Y]es** - Save notebook
**[N]o** - Skip (findings already in report)"

### 7. Update Sidecar

Update stepsCompleted.

### 8. Menu

"**EDA Deep Dive Complete**

- All gaps filled
- EDA report: COMPLETE
- Current understanding: Section 2 updated
- {X} hypotheses identified

**[A]** Advanced Elicitation
**[P]** Party Mode
**[C]** Continue to Research Audit"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All gaps filled with fresh analysis
- EDA report complete
- Current understanding section 2 updated
- Hypotheses generated
- User confirmed findings

### ❌ SYSTEM FAILURE:
- Skipping identified gaps
- Not updating current-understanding
- Redoing already-complete sections
- Not generating hypotheses

**Master Rule:** Fill gaps, update documents, generate hypotheses from data insights.
