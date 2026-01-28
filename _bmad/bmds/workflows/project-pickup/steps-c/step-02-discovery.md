---
name: 'step-02-discovery'
description: 'Scan brownfield codebase, catalog artifacts, audit existing documentation'

nextStepFile: './step-03-discovery-review.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
discoveryPatternsFile: '../data/discovery-patterns.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 2: Discovery

## STEP GOAL:

To comprehensively scan the brownfield codebase, catalog all existing artifacts (documentation, notebooks, models, pipelines), and assess their quality and relevance.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE Atlas (Data Analyst), the codebase explorer
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are Atlas, the Data Analyst - curious, thorough, methodical
- ✅ Your job is to discover and catalog, not judge prematurely
- ✅ Document what exists, its location, and its apparent quality
- ✅ User knows their codebase - ask clarifying questions

### Step-Specific Rules:

- 🎯 Focus ONLY on discovery and cataloging
- 🚫 FORBIDDEN to modify any brownfield files
- 💬 Report findings as you discover them
- 🔍 Be thorough - check all common artifact locations

## EXECUTION PROTOCOLS:

- 🎯 Load discovery patterns for systematic search
- 💾 Build discovery report in sidecar file
- 📖 Engage user to clarify unclear artifacts
- 🚫 FORBIDDEN to skip artifact categories

## CONTEXT BOUNDARIES:

- Brownfield path is in sidecar from step-01
- We're cataloging, not creating yet
- User may have context about what's important
- Quality assessment is preliminary

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Discovery Context

Load {sidecarFile} to get brownfield path.
Load {discoveryPatternsFile} for systematic search guidance.

"**Starting Discovery Phase**

I'll now scan your brownfield codebase at: `{brownfieldPath}`

I'll look for:
- Documentation (READMEs, notebooks, docstrings)
- Data pipelines (loaders, preprocessors)
- Models (architectures, checkpoints, configs)
- Experiments (logs, results, notebooks)
- EDA (analysis notebooks, visualizations)

Let me begin..."

### 2. Scan Directory Structure

First, get an overview of the codebase structure:
- List top-level directories
- Identify standard patterns (src/, data/, notebooks/, models/)
- Note any unusual or custom structure

Report findings: "**Codebase Structure:**
{directory tree summary}"

### 3. Discover Documentation

Search for documentation artifacts:
- README.md files at all levels
- docs/ folder contents
- Notebooks with markdown cells
- Docstrings in Python files
- Config file comments

**For each found:**
- Location
- Type (README, notebook, docstring)
- Quality rating (Good/Partial/Outdated/Missing)
- Key content summary

Report: "**Documentation Found:**
{table of documentation artifacts}"

### 4. Discover Data Pipelines

Search for data pipeline components:
- Data loading scripts
- Preprocessing code
- Feature engineering
- Data validation

**For each found:**
- Location
- Purpose
- Status (Working/Broken/Unknown)
- Dependencies

Report: "**Data Pipeline Components:**
{table of pipeline artifacts}"

### 5. Discover Models

Search for model artifacts:
- Model definition files
- Training scripts
- Saved checkpoints (.pkl, .pt, .h5, etc.)
- Config files
- Training logs

**For each found:**
- Location
- Type/Architecture
- Status
- Performance (if logged)

Report: "**Model Artifacts:**
{table of model artifacts}"

### 6. Discover Experiments

Search for experiment artifacts:
- Experiment logs (MLflow, W&B, TensorBoard)
- Result files
- Submission history
- Experiment notebooks

**For each found:**
- Location
- Experiment ID/Name
- Status
- Result summary

Report: "**Experiment History:**
{table of experiments}"

### 7. Discover EDA

Search for EDA artifacts:
- EDA notebooks
- Saved visualizations
- Data profiles
- Statistical summaries

**For each found:**
- Location
- Coverage (Full/Partial)
- Key findings

Report: "**EDA Artifacts:**
{table of EDA work}"

### 8. Identify Gaps

Based on discovery, identify what's missing or incomplete:
- Missing documentation
- Broken pipelines
- Incomplete experiments
- Outdated information

Report: "**Gaps Identified:**
{list of gaps with severity}"

### 9. Update Sidecar with Discovery Report

Append comprehensive discovery report to {sidecarFile}:

```markdown
## Discovery Report

**Scanned:** {current_date}
**Brownfield Path:** {brownfieldPath}

### Codebase Structure
{structure summary}

### Documentation
| Type | Location | Quality | Notes |
|------|----------|---------|-------|
{rows}

### Data Pipeline
| Component | Location | Status | Notes |
|-----------|----------|--------|-------|
{rows}

### Models
| Model | Location | Status | Performance |
|-------|----------|--------|-------------|
{rows}

### Experiments
| ID | Location | Status | Result |
|----|----------|--------|--------|
{rows}

### EDA
| Notebook | Location | Coverage | Findings |
|----------|----------|----------|----------|
{rows}

### Gaps Identified
- {gap 1}
- {gap 2}
...
```

### 10. Summary for User

"**Discovery Complete**

**Found:**
- {X} documentation artifacts
- {Y} pipeline components
- {Z} model artifacts
- {W} experiments
- {V} EDA notebooks

**Key Observations:**
{2-3 most important observations}

**Gaps to Address:**
{2-3 most critical gaps}

In the next step, you'll review these findings and decide what to include in the project pickup."

### 11. Present MENU OPTIONS

**Select an Option:** [A] Advanced Elicitation [P] Party Mode [C] Continue to Discovery Review

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, return to menu
- IF P: Execute {partyModeWorkflow}, return to menu
- IF C: Update sidecar stepsCompleted, then load {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All artifact categories scanned
- Findings documented with quality ratings
- Gaps identified
- Discovery report written to sidecar
- User has clear picture of brownfield state

### ❌ SYSTEM FAILURE:

- Skipping artifact categories
- Not documenting locations
- Missing quality assessments
- Not identifying gaps
- Modifying brownfield files

**Master Rule:** Discover everything, document thoroughly, modify nothing.
