---
name: 'step-06-data-quality'
description: 'Spawn Atlas (Data Analyst) to assess overall data quality and define filtering strategies'

nextStepFile: './step-07-insights.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
outputScript: '{experiments_folder}/eda/05_data_quality.py'
phaseOutputFile: '{experiments_folder}/.phase-06-output.md'
edaReportFile: '{docs_folder}/eda-report-images.md'
dataAnalystAgent: '{project-root}/_bmad/bmds/agents/data-analyst/data-analyst.agent.yaml'
---

# Step 6: Data Quality Assessment

## STEP GOAL:

To spawn Atlas (Data Analyst agent) to synthesize all findings into a comprehensive data quality assessment with filtering strategies.

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
- ✅ Atlas synthesizes all previous phase findings
- ✅ This phase produces actionable filtering strategies
- ✅ Sub-agent writes findings to memory file for context transfer

### Step-Specific Rules:

- 🎯 Spawn Atlas to create comprehensive quality assessment
- 🚫 FORBIDDEN to perform analysis yourself - delegate to Atlas
- 💬 Atlas should create filtering script with thresholds
- 🤖 Sub-agent should stay under 50% context window

## EXECUTION PROTOCOLS:

- 🎯 Load all previous phase outputs
- 💾 Atlas writes script to {outputScript}
- 📖 Atlas writes findings to {phaseOutputFile}
- 📝 Atlas updates Section 5 of {edaReportFile}

## CONTEXT BOUNDARIES:

- All analysis phases complete (3, 4, 5)
- Now synthesize into quality levels and filters
- Output should enable data cleaning for training

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load State and All Phase Outputs

Load {stateFile} and all phase outputs:
- `phase_outputs.phase_03` (basic stats)
- `phase_outputs.phase_04` (label analysis)
- `phase_outputs.phase_05` (visual patterns)

### 2. Spawn Atlas (Data Analyst) Sub-Agent

**Launch a sub-agent with the following task:**

"You are Atlas (Data Analyst). Create a comprehensive data quality assessment.

**Previous Findings:**
- Basic Stats: {phase_03 summary}
- Label Analysis: {phase_04 summary}
- Visual Patterns: {phase_05 summary}

**Your Task:**
Create `{outputScript}` that:

1. **Quality Classification:**
   Categorize every image into quality levels:

   **High Quality:**
   - Labels accurate and well-aligned
   - Image clear and representative
   - Ready for training

   **Medium Quality:**
   - Minor issues, usable with caution
   - May need augmentation to compensate

   **Low Quality (Garbage):**
   - Mislabeled or unlabeled
   - Random placement
   - Will harm model training

2. **Filtering Strategies:**
   Define and implement filters:

   **White Pixel Filter:**
   - Calculate white pixel percentage
   - Threshold (e.g., >97% = garbage)
   - Useful for architectural drawings

   **Size Filter:**
   - Remove outlier sizes
   - Enforce minimum/maximum dimensions

   **Label Filter:**
   - Remove unlabeled images
   - Remove known bad labels

   **Pattern Filter:**
   - Remove random placement examples
   - Keep only perfect/partial matches

3. **Filter Impact Analysis:**
   For each filter, calculate:
   - Images affected
   - Class distribution change
   - Recommended/not recommended

4. **Generate Filtered Datasets:**
   Create functions to:
   - Apply individual filters
   - Apply combined filters
   - Export filtered image lists

5. **Quality Report:**
   - Overall quality score
   - Quality distribution chart
   - Cleaning recommendations

**Script Requirements:**
- Configurable thresholds
- Preview mode (show what would be filtered)
- Export filtered lists (JSON/CSV)
- Generate before/after statistics

**After analysis, write findings to {phaseOutputFile} including:**
- Quality distribution (high/medium/low counts)
- Recommended filters with thresholds
- Expected dataset size after cleaning
- Data cleaning recommendations

**Also update Section 5 of {edaReportFile} with quality assessment.**"

### 3. Verify Sub-Agent Output

After Atlas completes, verify:
- [ ] Script exists at {outputScript}
- [ ] Phase output file exists at {phaseOutputFile}
- [ ] Quality classification complete
- [ ] EDA report Section 5 updated

### 4. Update State File

Update {stateFile}:
```yaml
stepsCompleted: [..., 'step-06-data-quality']
currentPhase: 'data-quality-complete'
phase_outputs:
  phase_06: '{phaseOutputFile}'
```

### 5. Present Summary

"**Phase 6: Data Quality Assessment Complete**

**Quality Distribution:**
- High Quality: {X} images ({Y}%)
- Medium Quality: {X} images ({Y}%)
- Low Quality: {X} images ({Y}%)

**Recommended Filters:**
{filter recommendations from phase output}

**Expected Clean Dataset:** {N} images ({X}% of original)

**Script:** `{outputScript}`

Ready to proceed to Phase 7: Insight Generation?"

### 6. Present MENU OPTIONS

Display: **[C]ontinue** to Phase 7: Insight Generation

#### Menu Handling Logic:

- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Atlas sub-agent spawned with all previous findings
- Quality levels defined and images classified
- Filtering strategies with thresholds
- Impact analysis for each filter
- EDA report Section 5 updated

### ❌ SYSTEM FAILURE:

- Not synthesizing previous phases
- Missing quality classification
- No actionable filtering strategies
- State file not updated

**Master Rule:** Orchestrator delegates. Atlas synthesizes. Memory files connect.
