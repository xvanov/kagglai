---
name: 'step-01-init'
description: 'Initialize project pickup - verify inputs, detect continuation, create sidecar'

nextStepFile: './step-02-discovery.md'
continueFile: './step-01b-continue.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
experimentsFolder: '{experiments_folder}'
docsFolder: '{experiments_folder}/docs'
problemInputsFolder: '{experiments_folder}/problem-inputs'
---

# Step 1: Initialize Project Pickup

## STEP GOAL:

To initialize the brownfield project pickup by verifying required inputs exist, detecting any previous session to continue, and creating the sidecar file for state tracking.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE AN ORCHESTRATOR, setting up the workflow
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the workflow orchestrator initializing project pickup
- ✅ Verify all prerequisites before proceeding
- ✅ Detect continuation from previous sessions
- ✅ Set up state tracking for multi-session workflow

### Step-Specific Rules:

- 🎯 Focus ONLY on initialization and input verification
- 🚫 FORBIDDEN to start discovery without verifying inputs
- 💬 Clearly communicate what's needed if inputs missing
- 🚪 Route to continuation if previous session detected

## EXECUTION PROTOCOLS:

- 🎯 Check for existing sidecar (continuation detection)
- 💾 Create sidecar file to track workflow state
- 📖 Verify problem-inputs/ folder exists
- 🚫 FORBIDDEN to proceed without required inputs

## CONTEXT BOUNDARIES:

- This is the entry point for project pickup
- User may be starting fresh or continuing
- Required: problem-inputs/ folder with problem definition
- Required: Brownfield codebase path from user
- No prior context - this step establishes it

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Check for Continuation

Look for existing sidecar file at {sidecarFile}.

**IF sidecar exists AND has stepsCompleted array:**

"**Welcome back!** I found a previous project pickup session. Loading continuation..."

→ STOP here. Load, read entirely, and execute {continueFile}

**IF sidecar does not exist:**

Continue to step 2.

### 2. Welcome Message

"**Welcome to BMDS Project Pickup!**

This workflow will help you pick up an existing (brownfield) project and standardize it for the BMDS experiment workflow.

**What this workflow does:**
1. Discovers and catalogs existing work in your brownfield codebase
2. Standardizes documentation to BMDS format
3. Fills gaps to reach the same end-state as a greenfield project
4. Prepares everything for the experiment-cycle workflow

**What you'll need:**
- `problem-inputs/` folder with problem definition (description.md, rules.md, data-access.md, submission-format.md)
- Path to your brownfield codebase

Let me verify your inputs..."

### 3. Verify Problem Inputs Folder

Check if {problemInputsFolder} exists and contains required files.

**Required files:**
- description.md - Problem/competition description
- rules.md - Rules, scoring, evaluation criteria
- data-access.md - How to access the data
- submission-format.md - Submission requirements

**IF problem-inputs/ exists with required files:**

"**problem-inputs/ verified:**
- description.md
- rules.md
- data-access.md
- submission-format.md"

**IF problem-inputs/ missing or incomplete:**

"**problem-inputs/ folder is missing or incomplete.**

Please create the folder at: `{problemInputsFolder}/`

And add these files:
- `description.md` - Problem/competition description
- `rules.md` - Rules, scoring, evaluation criteria
- `data-access.md` - How to access the data
- `submission-format.md` - Submission requirements

**Note:** The brownfield project may be for a related problem, not the exact problem you're solving now. The problem-inputs/ should describe YOUR current problem.

Once created, run this workflow again."

→ HALT and wait for user to create files.

### 4. Get Brownfield Path

"**What is the path to your brownfield codebase?**

This is the existing project you want to pick up and extract value from.

Please provide the full path (e.g., `/home/user/projects/old-competition/`):"

Wait for user to provide the brownfield path.

**Verify the path exists:**
- IF path exists: Continue to step 5
- IF path doesn't exist: Ask user to verify and provide correct path

Store the brownfield path for use in subsequent steps.

### 5. Create Docs Folder

Ensure {docsFolder} exists. Create if it doesn't.

### 6. Create Sidecar File

Create {sidecarFile} with initial state:

```markdown
---
workflowType: project-pickup
projectName: '{project_name}'
brownfieldPath: '{user-provided-path}'
created: '{current_date}'
lastUpdated: '{current_date}'
lastStep: 'step-01-init'
stepsCompleted: ['step-01-init']
status: IN_PROGRESS
---

# Project Pickup Sidecar

**Project:** {project_name}
**Brownfield Source:** {brownfield_path}
**Started:** {current_date}

---

## Discovery Report

{To be filled in step-02}

---

## Session Notes

### Session 1 - {current_date}
- Workflow initialized
- Problem inputs verified
- Brownfield path: {brownfield_path}

---

## Validation Reports

{To be filled during review steps}
```

### 7. Summary and Proceed

"**Project Pickup Initialized**

**Project:** {project_name}
**Brownfield path:** {brownfield_path}
**Problem inputs:** Verified

**Sidecar created at:** {sidecarFile}

**Next step:** Discovery - I'll scan your brownfield codebase to understand what exists.

**[C]ontinue** to Discovery"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Continuation detected and routed correctly
- Problem-inputs/ verified with all required files
- Brownfield path obtained and verified
- Sidecar file created with initial state
- User informed and ready to proceed

### ❌ SYSTEM FAILURE:

- Proceeding without verifying problem-inputs/
- Not detecting existing sidecar for continuation
- Creating sidecar without brownfield path
- Not explaining what's needed when inputs missing

**Master Rule:** Verify all inputs before proceeding. Route to continuation if previous session exists.
