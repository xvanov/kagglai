---
name: 'step-05-visual-patterns'
description: 'Spawn Atlas (Data Analyst) to analyze visual patterns - good vs bad examples, placement quality'

nextStepFile: './step-06-data-quality.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
outputScript: '{experiments_folder}/eda/04_visual_patterns.py'
phaseOutputFile: '{experiments_folder}/.phase-05-output.md'
edaReportFile: '{docs_folder}/eda-report-images.md'
dataAnalystAgent: '{project-root}/_bmad/bmds/agents/data-analyst/data-analyst.agent.yaml'
---

# Step 5: Visual Pattern Analysis

## STEP GOAL:

To spawn Atlas (Data Analyst agent) to identify visual patterns including "good" vs "bad" data examples, perfect matching vs random placement, and edge cases.

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
- ✅ Atlas needs to VISUALLY inspect samples - not just statistics
- ✅ This phase identifies training data quality visually
- ✅ Sub-agent writes findings to memory file for context transfer

### Step-Specific Rules:

- 🎯 Spawn Atlas to analyze visual patterns
- 🚫 FORBIDDEN to perform analysis yourself - delegate to Atlas
- 💬 Atlas should sample and visually categorize data
- 🤖 Sub-agent should stay under 50% context window

## EXECUTION PROTOCOLS:

- 🎯 Load state file and previous phase outputs
- 💾 Atlas writes script to {outputScript}
- 📖 Atlas writes findings to {phaseOutputFile}
- 📝 Atlas updates Section 4 of {edaReportFile}

## CONTEXT BOUNDARIES:

- Label analysis complete (Phase 4)
- Now need to SEE the data, not just count it
- Identify what makes data "good" or "bad" for training

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load State and Prepare Context

Load {stateFile} to get:
- `image_dataset_path`
- `task_type`
- `phase_outputs.phase_04` (label analysis findings)

### 2. Spawn Atlas (Data Analyst) Sub-Agent

**Launch a sub-agent with the following task:**

"You are Atlas (Data Analyst). Analyze visual patterns in an image dataset.

**Dataset Location:** {image_dataset_path}
**Task Type:** {task_type}
**Label Analysis:** {summary from phase_04}

**Your Task:**
Create `{outputScript}` that identifies visual patterns:

1. **Sample Selection:**
   - Select diverse sample (100-200 images)
   - Stratified by class if possible
   - Include edge cases from label analysis

2. **Pattern Categories:**
   Define and detect these patterns:

   **Perfect Matching (Good):**
   - Labels precisely align with objects
   - Clear, unambiguous annotations
   - High-quality training examples

   **Random Placement (Bad):**
   - Labels placed arbitrarily
   - No correlation with visual content
   - Will confuse model training

   **Partial Overlap (Mixed):**
   - Labels partially cover objects
   - May be usable with adjustment

   **Edge Cases:**
   - Unusual or ambiguous examples
   - Boundary cases for classification

3. **Visual Analysis Methods:**
   - For detection: overlay bboxes, check IoU with visible objects
   - For classification: cluster similar images, check label consistency
   - For segmentation: overlay masks, check boundary accuracy

4. **Generate Visual Examples:**
   - Save example images for each category
   - Create side-by-side comparisons
   - Annotate with observations

5. **Quantify Patterns:**
   - Count images in each category
   - Calculate percentages
   - Identify systematic issues

**Script Requirements:**
- Visual output (matplotlib/PIL)
- Save categorized image lists
- Generate HTML report with examples
- Support manual review mode

**After analysis, write findings to {phaseOutputFile} including:**
- Pattern distribution (% good, bad, mixed)
- Example image paths for each category
- Systematic issues identified
- Visual inspection recommendations

**Also update Section 4 of {edaReportFile} with pattern analysis.**"

### 3. Verify Sub-Agent Output

After Atlas completes, verify:
- [ ] Script exists at {outputScript}
- [ ] Phase output file exists at {phaseOutputFile}
- [ ] Example images saved
- [ ] EDA report Section 4 updated

### 4. Update State File

Update {stateFile}:
```yaml
stepsCompleted: [..., 'step-05-visual-patterns']
currentPhase: 'visual-patterns-complete'
phase_outputs:
  phase_05: '{phaseOutputFile}'
```

### 5. Present Summary

"**Phase 5: Visual Pattern Analysis Complete**

**Pattern Distribution:**
- Good (Perfect Matching): {X}%
- Bad (Random Placement): {Y}%
- Mixed (Partial Overlap): {Z}%

**Example Images Saved:** `{experiments_folder}/eda/pattern_examples/`

**Key Observations:**
{observations from phase output}

Ready to proceed to Phase 6: Data Quality Assessment?"

### 6. Present MENU OPTIONS

Display: **[C]ontinue** to Phase 6: Data Quality Assessment

#### Menu Handling Logic:

- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Atlas sub-agent spawned with clear requirements
- Visual patterns identified and categorized
- Example images saved for review
- Pattern distribution quantified
- EDA report Section 4 updated

### ❌ SYSTEM FAILURE:

- Only statistical analysis, no visual inspection
- Not categorizing data quality
- Missing example images
- State file not updated

**Master Rule:** Orchestrator delegates. Atlas inspects visually. Memory files connect.
