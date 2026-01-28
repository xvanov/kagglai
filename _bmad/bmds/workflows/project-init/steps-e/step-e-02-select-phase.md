---
name: 'step-e-02-select-phase'
description: 'Select which document/phase to edit'

nextStepFile: './step-e-03-apply-edit.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'

# Editable documents
challengeSpecFile: '{experiments_folder}/docs/problem-statement.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
sotaSynthesisFile: '{experiments_folder}/docs/sota-synthesis.md'
researchDirectionsFile: '{experiments_folder}/docs/research-directions.md'
technicalSpecFile: '{experiments_folder}/docs/technical-spec.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
currentArchitectureFile: '{experiments_folder}/docs/current-architecture.md'
hypothesisRegistryFile: '{experiments_folder}/docs/hypothesis-registry.md'
---

# Step E-02: Select Document to Edit

## STEP GOAL:

To help the user select which document they want to edit and understand the scope and implications of that edit.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER proceed without clear user selection
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE A GUIDE helping the user make an informed choice
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are helping the user choose what to edit
- ✅ Provide enough context for an informed decision
- ✅ Clarify the scope of the selected edit
- ✅ User must explicitly confirm their choice

### Step-Specific Rules:

- 🎯 Focus on SELECTION and SCOPE DEFINITION
- 🚫 FORBIDDEN to make edits yet
- 💬 Be clear about what each option entails
- 🚪 User selection determines the apply-edit step

## EXECUTION PROTOCOLS:

- 🎯 Present document options clearly
- 💾 Record user's selection
- 📖 Clarify scope of the edit
- 🚫 FORBIDDEN to proceed without explicit selection

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Present Document Options

"**Select Document to Edit:**

**Core Documents:**
1. **[1] Problem Statement** - Project requirements, constraints, evaluation
2. **[2] EDA Report** - Data analysis, patterns, quality issues
3. **[3] SoTA Synthesis** - State of the art techniques, approaches
4. **[4] Research Directions** - Prioritized approaches, experiments
5. **[5] Technical Spec** - Implementation plan, configurations

**Handoff Documents:**
6. **[6] Current Understanding** - Problem, data, research context
7. **[7] Current Architecture** - Pipeline structure, extension points
8. **[8] Hypothesis Registry** - Hypotheses for experiment-cycle

Enter the number of the document you want to edit:"

### 2. Capture User Selection

Wait for user input (1-8).

### 3. Confirm Selection and Explain Scope

Based on selection, provide context:

**IF [1] Problem Statement:**
"**Selected: Problem Statement**

**This document contains:**
- Problem statement and task type
- Evaluation metric and formula
- Data schema and access
- Submission requirements
- Constraints (compute, data, code)
- Timeline

**Typical edits:**
- Updating constraints you missed
- Adding clarifications from forums
- Correcting metric details
- Adding timeline changes

**Cascade warning:** Changes here may affect EDA recommendations, SoTA applicability, and downstream documents."

**IF [2] EDA Report:**
"**Selected: EDA Report**

**This document contains:**
- Data overview and statistics
- Feature analysis
- Target variable analysis
- Missing data patterns
- Data quality issues
- Feature relationships
- Recommendations

**Typical edits:**
- Adding new pattern discoveries
- Updating statistics
- Adding feature engineering ideas
- Correcting analysis errors

**Cascade warning:** Changes may affect research direction priorities and technical spec."

**IF [3] SoTA Synthesis:**
"**Selected: SoTA Synthesis**

**This document contains:**
- Dominant approaches
- Key techniques
- Recent advances
- Similar projects
- Applicability assessment
- Recommendations

**Typical edits:**
- Adding new papers/techniques
- Updating recommendations
- Adding project insights
- Correcting citations

**Cascade warning:** Changes may affect research direction priorities."

**IF [4] Research Directions:**
"**Selected: Research Directions**

**This document contains:**
- Ranked research directions
- Rationale and evidence
- Dependencies
- Success criteria
- Implementation roadmap

**Typical edits:**
- Reprioritizing directions
- Adding new directions
- Updating success criteria
- Adjusting roadmap

**Cascade warning:** Changes may affect technical spec and implementation priorities."

**IF [5] Technical Spec:**
"**Selected: Technical Spec**

**This document contains:**
- Environment setup
- Data pipeline
- Model configuration
- Training strategy
- Implementation tasks

**Typical edits:**
- Changing model configuration
- Updating training parameters
- Adding missing steps
- Adjusting for constraints

**Cascade warning:** Changes may require re-implementation."

**IF [6] Current Understanding:**
"**Selected: Current Understanding (Handoff Doc)**

**This document contains:**
- Problem & Task summary
- Data summary
- Model/Research summary

**Typical edits:**
- Updating any section with new insights
- Correcting errors
- Adding missing context

**Safe to edit:** This is informational for experiment-cycle."

**IF [7] Current Architecture:**
"**Selected: Current Architecture (Handoff Doc)**

**This document contains:**
- Pipeline overview
- Key files
- Model configuration
- Baseline performance
- Extension points

**Typical edits:**
- Updating after code changes
- Adding extension guidance
- Updating performance metrics

**Safe to edit:** This is informational for experiment-cycle."

**IF [8] Hypothesis Registry:**
"**Selected: Hypothesis Registry (Handoff Doc)**

**This document contains:**
- Hypotheses to test
- Rationale
- Test approach
- Status

**Typical edits:**
- Adding new hypotheses
- Updating status
- Adding results

**Safe to edit:** This is informational for experiment-cycle."

### 4. Confirm and Record Selection

"**Confirm:** You want to edit **{document name}**?

**[Y]es** - Proceed to editing
**[N]o** - Go back to selection"

**IF Yes:**
- Record selection in memory
- Proceed to apply-edit step

**IF No:**
- Return to step 1

### 5. Hand Off to Apply Edit

"Proceeding to apply edits to **{document name}**..."

Store selection context (document path, document name) for next step.

Load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Clear options presented
- User made explicit selection
- Scope and implications explained
- Selection confirmed before proceeding

### ❌ SYSTEM FAILURE:

- Proceeding without user selection
- Not explaining implications
- Skipping confirmation
- Making edits in this step

**Master Rule:** Guide selection. Explain implications. Get explicit confirmation.
