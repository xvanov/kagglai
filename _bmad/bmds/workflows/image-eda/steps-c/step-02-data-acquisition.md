---
name: 'step-02-data-acquisition'
description: 'Spawn Rex (Implementer) to create reproducible data acquisition and sampling scripts'

nextStepFile: './step-03-basic-stats.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
outputScript: '{experiments_folder}/eda/01_data_sampling.py'
phaseOutputFile: '{experiments_folder}/.phase-02-output.md'
implementerAgent: '{project-root}/_bmad/bmds/agents/implementer/implementer.agent.yaml'
---

# Step 2: Data Acquisition

## STEP GOAL:

To spawn Rex (Implementer agent) to create reproducible data acquisition and sampling scripts that can be re-run to obtain the image dataset.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ORCHESTRATOR spawning a sub-agent
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess/sub-agent unavailable, perform in main thread

### Role Reinforcement:

- ✅ You are the workflow orchestrator delegating to Rex (Implementer)
- ✅ Rex specializes in writing clean, reproducible code
- ✅ Keep orchestrator context light - delegate heavy work to sub-agent
- ✅ Sub-agent writes findings to memory file for context transfer

### Step-Specific Rules:

- 🎯 Spawn Rex to create data acquisition script
- 🚫 FORBIDDEN to write the script yourself - delegate to Rex
- 💬 Provide Rex with clear requirements from state file
- 🤖 Sub-agent should stay under 50% context window

## EXECUTION PROTOCOLS:

- 🎯 Load state file for project configuration
- 💾 Rex writes script to {outputScript}
- 📖 Rex writes findings to {phaseOutputFile}
- 🚫 Update state file with phase completion

## CONTEXT BOUNDARIES:

- State file has: image_dataset_path, label_format, task_type
- Rex needs to create script that can sample/download data
- Script must be reproducible (can re-run later)
- Output is permanent artifact in eda/ folder

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load State and Prepare Context

Load {stateFile} to get:
- `image_dataset_path`
- `label_format`
- `task_type`
- `known_concerns`

### 2. Spawn Rex (Implementer) Sub-Agent

**Launch a sub-agent with the following task:**

"You are Rex (Implementer). Create a data acquisition script for an image dataset.

**Project Configuration:**
- Dataset Path: {image_dataset_path}
- Label Format: {label_format}
- Task Type: {task_type}
- Known Concerns: {known_concerns}

**Your Task:**
Create `{outputScript}` that:

1. **Handles Large Datasets:**
   - Implement progressive sampling (small sample first, then larger)
   - Support `--sample-size` argument (default: 100 images)
   - Support `--full` flag to get entire dataset

2. **Data Source Handling:**
   - If path is local: verify files exist, create symlinks or copy
   - If path is URL/API: implement download with progress bar
   - If path is cloud storage: implement authenticated access

3. **Sampling Strategy:**
   - Stratified sampling if labels available
   - Random sampling fallback
   - Preserve directory structure

4. **Output:**
   - Save sampled data to `{experiments_folder}/data/sampled/`
   - Create manifest file listing all sampled images
   - Log sampling statistics

5. **Reproducibility:**
   - Set random seed for reproducible sampling
   - Save sampling parameters to config file
   - Include requirements.txt with dependencies

**Code Quality:**
- Type hints on all functions
- Docstrings explaining purpose
- argparse for CLI interface
- Logging instead of print statements
- Error handling with clear messages

**After creating the script, write a summary to {phaseOutputFile} including:**
- Script location
- Key features implemented
- How to run the script
- Any limitations or notes"

### 3. Verify Sub-Agent Output

After Rex completes, verify:
- [ ] Script exists at {outputScript}
- [ ] Script is syntactically valid Python
- [ ] Phase output file exists at {phaseOutputFile}

If verification fails, ask Rex to fix issues.

### 4. Update State File

Update {stateFile}:
```yaml
stepsCompleted: ['step-01-init', 'step-02-data-acquisition']
currentPhase: 'data-acquisition-complete'
phase_outputs:
  phase_02: '{phaseOutputFile}'
```

### 5. Present Summary

"**Phase 2: Data Acquisition Complete**

**Script Created:** `{outputScript}`

**Features:**
{summary from phase output file}

**To run:**
```bash
python {outputScript} --sample-size 100  # Small sample
python {outputScript} --full              # Full dataset
```

Ready to proceed to Phase 3: Basic Statistics?"

### 6. Present MENU OPTIONS

Display: **[C]ontinue** to Phase 3: Basic Statistics

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:

- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Rex sub-agent spawned with clear requirements
- Script created at {outputScript}
- Script is reproducible and well-documented
- Phase output file created
- State file updated

### ❌ SYSTEM FAILURE:

- Writing script directly instead of delegating to Rex
- Script not reproducible
- Missing phase output file
- State file not updated

**Master Rule:** Orchestrator delegates. Rex implements. Memory files connect.
