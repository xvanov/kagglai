---
name: 'step-09-technical-spec'
description: 'Implementer authors technical specification for baseline implementation'

nextStepFile: './step-10-technical-spec-review.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
templateFile: '../templates/technical-spec-template.md'
outputFile: '{experiments_folder}/docs/technical-spec.md'
challengeSpecFile: '{experiments_folder}/docs/problem-statement.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
sotaFile: '{experiments_folder}/docs/sota-synthesis.md'
researchDirectionsFile: '{experiments_folder}/docs/research-directions.md'
---

# Step 9: Technical Specification

## STEP GOAL:

To create a detailed technical specification for the baseline implementation that translates research direction #1 into a concrete, executable plan with clear tasks, configurations, and constraints compliance.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER specify implementation details that violate constraints
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE AN IMPLEMENTER planning the work systematically
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the Implementer agent - practical and detail-oriented
- ✅ Every specification must be executable
- ✅ Constraints compliance is non-negotiable
- ✅ This plan will be implemented in the next step

### Step-Specific Rules:

- 🎯 Focus on BASELINE implementation of Direction #1
- 🚫 FORBIDDEN to over-engineer (baseline should be minimal viable)
- 💬 Be specific about commands, configurations, file structures
- 🚪 This spec must be clear enough for implementation

## EXECUTION PROTOCOLS:

- 🎯 Read all foundation documents before specifying
- 💾 Create a complete, executable technical specification
- 📖 Verify constraints compliance throughout
- 🚫 FORBIDDEN to leave ambiguous steps

## CONTEXT BOUNDARIES:

- Challenge spec defines constraints (must comply)
- EDA defines data realities (must account for)
- SoTA defines techniques (can reference)
- Research directions defines what to build (Direction #1)

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 09: Technical Specification**

I will create a detailed technical specification for the baseline implementation. This translates Research Direction #1 into an executable plan.

Loading context documents..."

### 2. Load All Foundation Documents

Read each document to gather requirements:

**From {challengeSpecFile}:**
- Evaluation metric (what we're optimizing)
- Submission format requirements
- Compute constraints (runtime, memory, GPU)
- External data/model restrictions

**From {edaReportFile}:**
- Data file locations and formats
- Feature types and preprocessing needs
- Missing data handling requirements
- Validation strategy recommendations

**From {sotaFile}:**
- Recommended model architecture
- Training strategies
- Key techniques to consider

**From {researchDirectionsFile}:**
- Direction #1 details (what to implement)
- Success criteria
- Key experiments

Summarize:

"**Implementation Context:**

**Target:** Baseline implementation of {Direction #1 name}
**Evaluation Metric:** {metric}
**Key Constraints:**
- Runtime: {limit}
- Memory: {limit}
- GPU: {requirements}
- External: {restrictions}

**Data:** {summary from EDA}
**Approach:** {from research directions}"

### 3. Load Template

Read {templateFile} to understand the target structure.

### 4. Specify Environment Setup

Document environment requirements:

**Section 2.1 - System Requirements:**
- Python version (compatible with constraints)
- GPU requirements (from constraints)
- RAM requirements (from data size analysis)
- Disk space (from data size)

**Section 2.2 - Dependencies:**
- Core libraries with versions
- Model-specific libraries
- Utility libraries

**Section 2.3 - Setup Commands:**
- Environment creation
- Dependency installation
- Verification commands

### 5. Specify Data Pipeline

Document data handling:

**Section 3.1 - Data Loading:**
- Source paths (from EDA)
- Loading approach (pandas, torch, etc.)
- Pseudocode for loading

**Section 3.2 - Data Validation:**
- File existence checks
- Schema validation
- Corruption detection

**Section 3.3 - Preprocessing Pipeline:**
- Step-by-step preprocessing (from EDA recommendations)
- Each step: input → output → implementation

**Section 3.4 - Feature Engineering (Baseline):**
- Only essential features for baseline
- Keep minimal for Direction #1

### 6. Specify Model Architecture

Document the model:

**Section 4.1 - Model Selection:**
- Model choice (from Direction #1)
- Rationale (from research directions)

**Section 4.2 - Model Configuration:**
- Hyperparameters
- Configuration code

**Section 4.3 - Training Strategy:**
- Learning rate, batch size, epochs
- Early stopping configuration
- Rationale for each choice

**Section 4.4 - Validation Strategy:**
- Split method (from EDA recommendations)
- Split ratio
- Stratification approach
- Random seed

### 7. Specify Training and Inference Pipelines

**Section 5 - Training Pipeline:**
- File structure for src/
- Training command
- Expected outputs (checkpoints, logs, metrics)

**Section 6 - Inference Pipeline:**
- Inference command
- Steps (load model, preprocess, predict, format)
- Submission generation (matching problem-statement format)

### 8. Verify Constraints Compliance

**Section 7 - Compute Constraints Compliance:**

Create checklist comparing our plan to constraints:

| Constraint | Limit | Our Implementation | Compliant |
|------------|-------|-------------------|-----------|
| Runtime | {from spec} | {our estimate} | {yes/no} |
| Memory | {from spec} | {our estimate} | {yes/no} |
| GPU | {from spec} | {our approach} | {yes/no} |
| Internet | {from spec} | {our approach} | {yes/no} |

**IF ANY CONSTRAINT IS NOT MET:**
- Note the issue
- Specify optimization approach
- Verify compliance after optimization

### 9. Document Implementation Tasks

**Section 8 - Implementation Tasks:**

Break down into executable tasks:
1. Set up environment
2. Implement data loader
3. Implement preprocessing
4. Implement model
5. Implement training loop
6. Implement inference
7. Implement submission generation
8. End-to-end test
9. Generate submission

Include dependencies and estimated effort.

### 10. Specify Testing and Risk Mitigation

**Section 9 - Testing Strategy:**
- Unit tests for each component
- Integration tests (end-to-end)
- Sanity checks (loss decreasing, valid predictions)

**Section 10 - Risk Mitigation:**
- Identified risks (from implementation analysis)
- Fallback options

### 11. Write Technical Specification

Create {outputFile} with all sections populated.

### 12. Self-Check

Verify:
- [ ] Environment setup is complete and executable
- [ ] Data pipeline handles all cases from EDA
- [ ] Model configuration matches Direction #1
- [ ] Training strategy is appropriate
- [ ] Inference mirrors training preprocessing
- [ ] Submission format matches problem-statement
- [ ] All compute constraints satisfied
- [ ] All tasks have clear implementation path
- [ ] No ambiguous steps remain

### 13. Update Sidecar

Update {sidecarFile}:
- Add 'step-09-technical-spec' to stepsCompleted
- Set lastStep to 'step-09-technical-spec'
- Update lastUpdated date
- Add session note: "Technical spec authored for baseline"

### 14. Summary and Proceed

"**Technical Specification Complete**

**Document created:** `{outputFile}`

**Baseline Plan:**
- Model: {model name}
- Training approach: {summary}
- Key configuration: {highlights}

**Tasks to implement:** {count}
**Estimated total effort:** {estimate}

**Constraints compliance:** {all met / issues noted}

**Ready for validation review.**

**[C]ontinue** to technical spec validation"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All foundation documents read and referenced
- Direction #1 translated into concrete plan
- Environment setup is executable
- Data pipeline handles EDA-identified issues
- Model configuration is justified
- Constraints compliance verified
- All tasks are unambiguous
- Clean handoff to review

### ❌ SYSTEM FAILURE:

- Not reading all foundation documents
- Over-engineering beyond baseline
- Violating compute constraints
- Ambiguous implementation steps
- Missing submission format specification
- Not accounting for EDA findings
- Template placeholders remaining

**Master Rule:** Translate Direction #1 into an executable, constraint-compliant baseline plan. Every step must be clear.
