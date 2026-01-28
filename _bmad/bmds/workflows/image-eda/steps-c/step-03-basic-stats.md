---
name: 'step-03-basic-stats'
description: 'Spawn Atlas (Data Analyst) to analyze basic image statistics - dimensions, formats, file sizes'

nextStepFile: './step-04-label-analysis.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
outputScript: '{experiments_folder}/eda/02_basic_stats.py'
phaseOutputFile: '{experiments_folder}/.phase-03-output.md'
edaReportFile: '{docs_folder}/eda-report-images.md'
dataAnalystAgent: '{project-root}/_bmad/bmds/agents/data-analyst/data-analyst.agent.yaml'
---

# Step 3: Basic Statistics

## STEP GOAL:

To spawn Atlas (Data Analyst agent) to analyze and document basic image statistics including dimensions, formats, channels, and file sizes.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ORCHESTRATOR spawning a sub-agent
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess/sub-agent unavailable, perform in main thread

### Role Reinforcement:

- ✅ You are the workflow orchestrator delegating to Atlas (Data Analyst)
- ✅ Atlas specializes in EDA and statistical analysis
- ✅ Keep orchestrator context light - delegate heavy work to sub-agent
- ✅ Sub-agent writes findings to memory file for context transfer

### Step-Specific Rules:

- 🎯 Spawn Atlas to analyze image statistics
- 🚫 FORBIDDEN to perform analysis yourself - delegate to Atlas
- 💬 Provide Atlas with data location from state file
- 🤖 Sub-agent should stay under 50% context window

## EXECUTION PROTOCOLS:

- 🎯 Load state file for data location
- 💾 Atlas writes script to {outputScript}
- 📖 Atlas writes findings to {phaseOutputFile}
- 📝 Atlas updates Section 2 of {edaReportFile}

## CONTEXT BOUNDARIES:

- Data has been acquired (Phase 2 complete or existing data-access.md)
- Atlas analyzes images without labels at this phase
- Focus on image properties only - labels come in Phase 4

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load State and Prepare Context

Load {stateFile} to get:
- `image_dataset_path`
- `phase_outputs.phase_02` (if exists)

### 2. Spawn Atlas (Data Analyst) Sub-Agent

**Launch a sub-agent with the following task:**

"You are Atlas (Data Analyst). Analyze basic statistics for an image dataset.

**Dataset Location:** {image_dataset_path}

**Your Task:**
Create `{outputScript}` that analyzes and reports:

1. **Image Dimensions:**
   - Width/height distributions (min, max, mean, std, mode)
   - Aspect ratio analysis
   - Identify dimension outliers

2. **File Formats:**
   - Format distribution (PNG, JPG, TIFF, etc.)
   - Channel counts (RGB, RGBA, Grayscale)
   - Bit depth if applicable

3. **File Sizes:**
   - Size distribution (min, max, mean, total)
   - Identify unusually large/small files

4. **Directory Structure:**
   - Map folder hierarchy
   - Count images per folder
   - Identify naming patterns

5. **Integrity Checks:**
   - Verify all files are valid images
   - Identify corrupted files
   - Check for duplicates (optional)

**Script Requirements:**
- Use PIL/Pillow for image analysis
- Progress bar for large datasets
- Output statistics to JSON for dashboard
- Generate summary visualizations (histograms)

**After analysis, write findings to {phaseOutputFile} including:**
- Key statistics summary
- Outliers and anomalies found
- Recommendations for preprocessing
- Path to generated visualizations

**Also update Section 2 of {edaReportFile} with the statistics.**"

### 3. Verify Sub-Agent Output

After Atlas completes, verify:
- [ ] Script exists at {outputScript}
- [ ] Phase output file exists at {phaseOutputFile}
- [ ] EDA report Section 2 updated

### 4. Update State File

Update {stateFile}:
```yaml
stepsCompleted: [..., 'step-03-basic-stats']
currentPhase: 'basic-stats-complete'
phase_outputs:
  phase_03: '{phaseOutputFile}'
```

### 5. Present Summary

"**Phase 3: Basic Statistics Complete**

**Key Findings:**
{summary from phase output file}

**Script:** `{outputScript}`

Ready to proceed to Phase 4: Label Analysis?"

### 6. Present MENU OPTIONS

Display: **[C]ontinue** to Phase 4: Label Analysis

#### Menu Handling Logic:

- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Atlas sub-agent spawned with clear requirements
- Script created analyzing all image properties
- Phase output file with findings
- EDA report Section 2 updated
- State file updated

### ❌ SYSTEM FAILURE:

- Performing analysis directly instead of delegating
- Missing key statistics
- Not updating EDA report
- State file not updated

**Master Rule:** Orchestrator delegates. Atlas analyzes. Memory files connect.
