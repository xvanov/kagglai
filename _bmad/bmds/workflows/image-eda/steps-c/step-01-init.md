---
name: 'step-01-init'
description: 'Initialize Image EDA workflow - check for existing data access, set up state tracking, and route to appropriate phase'

nextStepFile: './step-02-data-acquisition.md'
skipToStepFile: './step-03-basic-stats.md'
continueFile: './step-01b-continue.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
dataAccessFile: '{experiments_folder}/problem-inputs/data-access.md'
edaFolder: '{experiments_folder}/eda'
outputFile: '{docs_folder}/eda-report-images.md'
templateFile: '../data/eda-report-images-template.md'
---

# Step 1: Initialize Image EDA

## STEP GOAL:

To initialize the Image EDA workflow by checking for existing data access configuration, setting up state tracking, and routing to the appropriate starting phase.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- ✅ You are the workflow orchestrator coordinating specialized agents
- ✅ This step sets up everything - state tracking, folder structure, initial routing
- ✅ You bring workflow expertise; user brings project context and domain knowledge
- ✅ Keep this step lightweight - heavy lifting happens in sub-agent phases

### Step-Specific Rules:

- 🎯 Focus ONLY on initialization - do not perform any analysis yet
- 🚫 FORBIDDEN to start EDA analysis - that's for subsequent phases
- 💬 Check existing artifacts, set up state, route correctly
- 🚪 This step determines the starting point for the workflow

## EXECUTION PROTOCOLS:

- 🎯 Check for continuation first (existing state file with progress)
- 💾 Create state file and EDA folder structure
- 📖 Determine if data acquisition is needed or can be skipped
- 🚫 Do NOT spawn sub-agents yet - just set up and route

## CONTEXT BOUNDARIES:

- This is the FIRST step - no prior context from this workflow
- May have artifacts from project-init (data-access.md, problem-statement.md)
- Focus: Initialization and routing only
- Dependencies: bmds config must be loaded

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Check for Existing Workflow (Continuation Detection)

Check if {stateFile} exists:

**IF {stateFile} EXISTS and contains `stepsCompleted` with entries:**
- This workflow was started previously
- Display: "**Existing Image EDA workflow detected.** Loading continuation handler..."
- STOP HERE and load {continueFile}

**IF {stateFile} does NOT exist or is empty:**
- This is a fresh start
- Continue to Section 2

### 2. Welcome and Gather Context

"**Welcome to the Image EDA Workflow!**

This workflow will perform comprehensive exploratory data analysis on your image dataset, producing:
- Permanent, rerunnable analysis scripts
- An interactive Streamlit dashboard
- Insights documented in current-understanding.md
- Model recommendations

**Before we begin, I need to understand your project:**

1. What is the **image dataset location** (path to images)?
2. What is the **label format** (COCO, YOLO, Pascal VOC, custom, or unknown)?
3. What is the **task type** (object detection, classification, segmentation, etc.)?
4. Any **known data quality concerns** you're already aware of?"

Wait for user response and capture:
- `image_dataset_path`
- `label_format`
- `task_type`
- `known_concerns` (optional)

### 3. Check for Existing Data Access

Check if {dataAccessFile} exists:

**IF {dataAccessFile} EXISTS:**
- Read it to understand existing data acquisition setup
- Display: "Found existing data access configuration from project-init."
- Set `skip_data_acquisition: true`

**IF {dataAccessFile} does NOT exist:**
- Display: "No existing data access configuration found. We'll create data acquisition scripts in Phase 2."
- Set `skip_data_acquisition: false`

### 4. Create EDA Folder Structure

Create the folder structure for permanent artifacts:

```
{edaFolder}/
├── 01_data_sampling.py      # (Phase 2 - if needed)
├── 02_basic_stats.py        # (Phase 3)
├── 03_label_analysis.py     # (Phase 4)
├── 04_visual_patterns.py    # (Phase 5)
├── 05_data_quality.py       # (Phase 6)
├── 06_insights.md           # (Phase 7)
└── dashboard/               # (Phase 8)
    └── app.py
```

Create {edaFolder} if it doesn't exist.

### 5. Initialize State File

Create {stateFile} with initial state:

```yaml
# Image EDA Workflow State
created: {current_date}
lastUpdated: {current_date}
stepsCompleted: ['step-01-init']
currentPhase: 'initialization'

# Project Configuration
image_dataset_path: '{user_provided_path}'
label_format: '{user_provided_format}'
task_type: '{user_provided_task}'
known_concerns: '{user_provided_concerns}'

# Routing
skip_data_acquisition: {true/false}

# Phase Outputs (populated as workflow progresses)
phase_outputs:
  phase_02: null
  phase_03: null
  phase_04: null
  phase_05: null
  phase_06: null
  phase_07: null
  phase_08: null
  phase_09: null
```

### 6. Initialize Output Document

Create {outputFile} from {templateFile}:
- Copy template to output location
- Fill in frontmatter with project details
- Set `stepsCompleted: ['step-01-init']`

### 7. Present Summary and Route

"**Initialization Complete**

**Project Configuration:**
- Dataset: `{image_dataset_path}`
- Label Format: {label_format}
- Task: {task_type}
- Known Concerns: {known_concerns or 'None specified'}

**Artifacts Created:**
- State file: `{stateFile}`
- EDA folder: `{edaFolder}/`
- Report initialized: `{outputFile}`

**Next Phase:** {Phase 2: Data Acquisition OR Phase 3: Basic Statistics (if data access exists)}

Ready to proceed?"

### 8. Present MENU OPTIONS

**IF skip_data_acquisition is TRUE:**

Display: "**[C]ontinue** to Phase 3: Basic Statistics (data acquisition already configured)"

**IF skip_data_acquisition is FALSE:**

Display: "**[C]ontinue** to Phase 2: Data Acquisition"

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:

- IF C AND skip_data_acquisition is TRUE: Load, read entire file, then execute {skipToStepFile}
- IF C AND skip_data_acquisition is FALSE: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Continuation detection performed correctly
- User context gathered (dataset path, label format, task type)
- Existing data-access.md checked
- EDA folder structure created
- State file initialized with correct configuration
- Output document created from template
- Correct routing determined (Phase 2 vs Phase 3)

### ❌ SYSTEM FAILURE:

- Skipping continuation check
- Not gathering user context
- Starting analysis without initialization
- Wrong routing based on data-access.md existence
- Not creating state file or EDA folder

**Master Rule:** This step ONLY initializes and routes. No analysis. No sub-agents. Just setup.
