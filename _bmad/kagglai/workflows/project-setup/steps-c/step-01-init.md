---
name: 'step-01-init'
description: 'Initialize project structure, verify inputs, create sidecar for state tracking'

nextStepFile: './step-02-challenge-spec.md'
continueFile: './step-01b-continue.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
---

# Step 1: Initialize Project Setup

## STEP GOAL:

To initialize the Kaggle competition project structure, verify required inputs exist, and create the sidecar file for workflow state tracking.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a workflow orchestrator setting up project infrastructure
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring workflow expertise and standards, user brings competition context
- ✅ Together we establish a solid foundation for the competition

### Step-Specific Rules:

- 🎯 Focus ONLY on initialization - folder structure, input validation, sidecar creation
- 🚫 FORBIDDEN to start any analysis or document creation
- 💬 Be clear about what's missing if inputs are incomplete
- 🚪 This step sets up everything that follows

## EXECUTION PROTOCOLS:

- 🎯 Check for existing sidecar first (continuation detection)
- 💾 Create folder structure and sidecar file
- 📖 Verify all required inputs before proceeding
- 🚫 FORBIDDEN to proceed if required inputs missing

## CONTEXT BOUNDARIES:

- This is the FIRST step - nothing exists yet (or we're resuming)
- User should have placed challenge documents in `challenge-inputs/`
- We need to create the full project folder structure
- Sidecar file tracks workflow progress across sessions

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Check for Existing Workflow (Continuation Detection)

Check if {sidecarFile} exists:

**IF sidecar exists AND has stepsCompleted with entries:**
- STOP this step
- Display: "**Found existing project setup in progress. Loading continuation...**"
- Load, read completely, then execute {continueFile}

**IF sidecar does not exist OR is empty:**
- Continue to section 2

### 2. Welcome and Explain

"**Welcome to the Kaggle Project Setup Workflow!**

This workflow will guide you through setting up a rigorous foundation for your competition:

1. **Challenge Specification** - Extract and validate all competition requirements
2. **Exploratory Data Analysis** - Understand your data deeply
3. **State of the Art Research** - Survey techniques and approaches
4. **Research Directions** - Prioritize what to try
5. **Technical Specification** - Plan your implementation
6. **Implementation** - Build a working baseline
7. **Code Review** - Ensure quality and reproducibility

Let me set up your project structure..."

### 3. Create Folder Structure

Create the full `{experiments_folder}/` structure if it doesn't exist:

```
{experiments_folder}/
├── challenge-inputs/             # User provides these
│   └── papers/                   # Optional research papers
├── docs/                         # Generated artifacts
├── data/
│   ├── raw/                      # Original downloaded data
│   ├── processed/                # Cleaned/transformed data
│   └── splits/                   # Train/val/test splits
├── models/
│   ├── checkpoints/              # Training checkpoints
│   ├── submissions/              # Models used for submissions
│   └── baselines/                # Baseline model artifacts
├── src/                          # Implementation code
└── experiments/                  # For experiment-cycle workflow
```

Report what was created vs what already existed.

### 4. Verify Required Inputs

Check for required files in `{experiments_folder}/challenge-inputs/`:

**Required:**
- [ ] `description.md` - Competition description
- [ ] `rules.md` - Rules, scoring, evaluation criteria
- [ ] `data-access.md` - How to access the data
- [ ] `submission-format.md` - Submission requirements

**Optional:**
- [ ] `papers/` folder with research papers

**IF any required file is missing:**
- List what's missing
- Provide guidance: "Please create the missing files in `_kagglai/challenge-inputs/` with the relevant information from the competition page."
- HALT and wait for user to confirm files are ready

**IF all required files present:**
- Confirm: "All required input files found."
- Continue to section 5

### 5. Create Sidecar File

Create {sidecarFile} with initial state:

```markdown
---
workflowName: project-setup
competition: {to be filled}
created: {current date}
lastUpdated: {current date}
stepsCompleted: ['step-01-init']
lastStep: 'step-01-init'
status: IN_PROGRESS
---

# Project Setup Sidecar

## Progress Tracking

| Step | Status | Date | Notes |
|------|--------|------|-------|
| 01-init | Complete | {date} | Project structure initialized |

## Session Notes

### Session 1 - {date}
- Initialized project structure
- Verified input files present

## Validation Reports

(Validation reports will be appended here by review steps)
```

### 6. Summary and Proceed

"**Project initialized successfully!**

**Folder structure:** Created/verified at `{experiments_folder}/`
**Input files:** All required files present
**Sidecar:** Created at `{sidecarFile}`

**Next step:** Challenge Specification
- Agent: Data Analyst
- Task: Extract and synthesize challenge requirements into `challenge-spec.md`

Proceeding to challenge specification..."

### 7. Auto-Proceed to Next Step

Display: "**Proceeding to Step 02: Challenge Specification...**"

Update {sidecarFile} to mark step-01-init complete, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Continuation detection working (routes to 01b if sidecar exists)
- Full folder structure created
- All required input files verified present
- Sidecar file created with initial state
- Clear messaging about what was set up

### ❌ SYSTEM FAILURE:

- Proceeding without required input files
- Not creating sidecar file
- Not checking for continuation
- Creating analysis documents (that's later steps)
- Hardcoded paths instead of variables

**Master Rule:** This step ONLY sets up infrastructure. No analysis, no documents, no code. Just folders, validation, and sidecar.
