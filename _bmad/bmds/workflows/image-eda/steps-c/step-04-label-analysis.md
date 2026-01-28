---
name: 'step-04-label-analysis'
description: 'Spawn Atlas (Data Analyst) to analyze label quality, class distributions, and semantic issues'

nextStepFile: './step-05-visual-patterns.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
outputScript: '{experiments_folder}/eda/03_label_analysis.py'
phaseOutputFile: '{experiments_folder}/.phase-04-output.md'
edaReportFile: '{docs_folder}/eda-report-images.md'
dataAnalystAgent: '{project-root}/_bmad/bmds/agents/data-analyst/data-analyst.agent.yaml'
---

# Step 4: Label Analysis

## STEP GOAL:

To spawn Atlas (Data Analyst agent) to analyze label quality, class distributions, imbalance, and identify labeling issues.

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
- ✅ Atlas specializes in data quality assessment
- ✅ Label quality is CRITICAL for model training - be thorough
- ✅ Sub-agent writes findings to memory file for context transfer

### Step-Specific Rules:

- 🎯 Spawn Atlas to analyze labels thoroughly
- 🚫 FORBIDDEN to perform analysis yourself - delegate to Atlas
- 💬 Provide Atlas with label format from state file
- 🤖 Sub-agent should stay under 50% context window

## EXECUTION PROTOCOLS:

- 🎯 Load state file for label format
- 💾 Atlas writes script to {outputScript}
- 📖 Atlas writes findings to {phaseOutputFile}
- 📝 Atlas updates Section 3 of {edaReportFile}

## CONTEXT BOUNDARIES:

- Basic stats complete (Phase 3)
- Label format known from initialization
- This phase is critical - garbage labels = garbage models

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load State and Prepare Context

Load {stateFile} to get:
- `image_dataset_path`
- `label_format`
- `task_type`
- `phase_outputs.phase_03`

### 2. Spawn Atlas (Data Analyst) Sub-Agent

**Launch a sub-agent with the following task:**

"You are Atlas (Data Analyst). Analyze labels for an image dataset.

**Dataset Location:** {image_dataset_path}
**Label Format:** {label_format}
**Task Type:** {task_type}

**Your Task:**
Create `{outputScript}` that analyzes:

1. **Label Format Detection:**
   - Verify label format matches expected
   - Parse all label files
   - Report parsing errors/failures

2. **Class Distribution:**
   - Count instances per class
   - Calculate class percentages
   - Visualize distribution (bar chart)

3. **Class Imbalance Assessment:**
   - Calculate imbalance ratio (majority/minority)
   - Categorize severity (none/mild/moderate/severe)
   - Recommend balancing strategies

4. **Label Coverage:**
   - Count labeled vs unlabeled images
   - Identify images with missing labels
   - Report coverage percentage

5. **Label Quality Issues:**
   - Detect potential mislabels (statistical outliers)
   - Find empty/null labels
   - Identify semantic confusion (e.g., similar class names)
   - Check for invalid bounding boxes (if detection task)
   - Check for overlapping annotations

6. **For Object Detection Tasks:**
   - Bounding box size distributions
   - Objects per image distribution
   - Small object analysis

**Script Requirements:**
- Support COCO, YOLO, Pascal VOC formats
- Output statistics to JSON
- Generate distribution visualizations
- List problematic samples for review

**After analysis, write findings to {phaseOutputFile} including:**
- Class distribution table
- Imbalance assessment
- Quality issues found with examples
- Recommendations for data cleaning

**Also update Section 3 of {edaReportFile} with the findings.**"

### 3. Verify Sub-Agent Output

After Atlas completes, verify:
- [ ] Script exists at {outputScript}
- [ ] Phase output file exists at {phaseOutputFile}
- [ ] EDA report Section 3 updated

### 4. Update State File

Update {stateFile}:
```yaml
stepsCompleted: [..., 'step-04-label-analysis']
currentPhase: 'label-analysis-complete'
phase_outputs:
  phase_04: '{phaseOutputFile}'
```

### 5. Present Summary

"**Phase 4: Label Analysis Complete**

**Class Distribution:**
{summary table from phase output}

**Imbalance:** {severity assessment}

**Quality Issues Found:**
{list of issues}

**Script:** `{outputScript}`

Ready to proceed to Phase 5: Visual Pattern Analysis?"

### 6. Present MENU OPTIONS

Display: **[C]ontinue** to Phase 5: Visual Pattern Analysis

#### Menu Handling Logic:

- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Atlas sub-agent spawned with clear requirements
- Script created with comprehensive label analysis
- Class distribution documented
- Quality issues identified
- EDA report Section 3 updated

### ❌ SYSTEM FAILURE:

- Performing analysis directly instead of delegating
- Missing class distribution analysis
- Not identifying quality issues
- State file not updated

**Master Rule:** Orchestrator delegates. Atlas analyzes. Memory files connect.
