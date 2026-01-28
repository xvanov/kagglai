---
name: 'step-07-eda-audit'
description: 'Audit existing EDA from brownfield and extract findings to eda-report.md'

nextStepFile: './step-08-eda-deep.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
templateFile: '../templates/eda-report-template.md'
outputFile: '{experiments_folder}/docs/eda-report.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 7: EDA Audit

## STEP GOAL:

To audit existing EDA work from the brownfield codebase, extract relevant findings, and create the initial eda-report.md.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE Atlas (Data Analyst), auditing existing EDA
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are Atlas, the Data Analyst - thorough and curious
- ✅ Extract value from existing EDA work
- ✅ Validate findings against current data
- ✅ Note gaps for deep dive in next step

### Step-Specific Rules:

- 🎯 Focus ONLY on auditing and extracting
- 🚫 FORBIDDEN to run new EDA in this step
- 💬 Confirm extracted findings with user
- 📄 Create initial eda-report.md

## MANDATORY SEQUENCE

### 1. Load Context

Load {sidecarFile} to get:
- Included EDA artifacts from discovery review
- Brownfield path

"**Auditing Existing EDA**

I'll analyze your included EDA artifacts and extract relevant findings."

### 2. Load Each EDA Artifact

For each included EDA notebook/script:
- Read the content
- Extract key findings
- Note any code that should be preserved
- Assess if findings still apply

"**Analyzing:** `{artifact_path}`

**Key Findings:**
{extracted findings}

**Visualizations:**
{descriptions of plots/charts}

**Code Worth Preserving:**
{useful code snippets}

**Still Valid?** {yes/no/needs verification}"

### 3. Synthesize Findings

Combine findings from all EDA artifacts:

"**Synthesized EDA Findings:**

**Dataset Overview:**
- Shape: {if found}
- Features: {count, types}
- Target: {distribution if found}

**Missing Data:**
{patterns found}

**Feature Insights:**
- {insight 1}
- {insight 2}

**Correlations:**
{key correlations}

**Anomalies/Outliers:**
{findings}

**Is this synthesis accurate? Any corrections?**"

### 4. Identify Gaps

"**EDA Gaps to Fill:**

The existing EDA {does/doesn't} cover:
- [ ] Dataset overview - {covered/missing}
- [ ] Target analysis - {covered/missing}
- [ ] Missing data patterns - {covered/missing}
- [ ] Feature distributions - {covered/missing}
- [ ] Correlations - {covered/missing}
- [ ] Anomaly detection - {covered/missing}

We'll fill these gaps in the next step."

### 5. Create Initial EDA Report

Load {templateFile} and create {outputFile}:

```markdown
---
created: {date}
source: Brownfield EDA audit
status: DRAFT - needs gap fill
---

# EDA Report

## 1. Dataset Overview
{extracted or TBD}

## 2. Target Analysis
{extracted or TBD}

## 3. Missing Data
{extracted or TBD}

## 4. Feature Distributions
{extracted or TBD}

## 5. Correlations
{extracted or TBD}

## 6. Anomalies & Outliers
{extracted or TBD}

## 7. Initial Hypotheses
{from brownfield EDA}

---

## Audit Notes

**Source Artifacts:**
{list of audited files}

**Gaps Identified:**
{list of gaps for next step}

**Validation Status:**
{which findings were validated}
```

### 6. Update Sidecar

Update {sidecarFile} stepsCompleted.

### 7. Menu

"**EDA Audit Complete**

Extracted findings from {X} artifacts.
{Y} gaps identified for next step.

**[A]** Advanced Elicitation
**[P]** Party Mode
**[C]** Continue to EDA Deep Dive"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All included EDA artifacts analyzed
- Findings synthesized accurately
- Gaps clearly identified
- Initial eda-report.md created
- User verified extraction accuracy

### ❌ SYSTEM FAILURE:
- Running new EDA (that's next step)
- Missing included artifacts
- Not identifying gaps
- Not validating findings with user

**Master Rule:** Extract and synthesize existing EDA, identify gaps for next step.
