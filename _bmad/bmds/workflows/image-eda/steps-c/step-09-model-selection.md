---
name: 'step-09-model-selection'
description: 'Spawn Feynman (Data Scientist) to recommend models and update current-understanding.md Section 3'

nextStepFile: './step-10-completion.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
phaseOutputFile: '{experiments_folder}/.phase-09-output.md'
edaReportFile: '{docs_folder}/eda-report-images.md'
currentUnderstandingFile: '{docs_folder}/current-understanding.md'
dataScientistAgent: '{project-root}/_bmad/bmds/agents/data-scientist/data-scientist.agent.yaml'
---

# Step 9: Model Selection

## STEP GOAL:

To spawn Feynman (Data Scientist agent) to recommend appropriate models based on data characteristics and update current-understanding.md Section 3.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ORCHESTRATOR spawning a sub-agent
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess/sub-agent unavailable, perform in main thread
- 🌐 WEB BROWSING available for SoTA research

### Role Reinforcement:

- ✅ You are the workflow orchestrator delegating to Feynman (Data Scientist)
- ✅ Feynman specializes in model selection and experiment design
- ✅ Recommendations should be data-driven based on EDA findings
- ✅ Web browsing can be used for current SoTA research

### Step-Specific Rules:

- 🎯 Spawn Feynman to recommend models
- 🚫 FORBIDDEN to make recommendations yourself - delegate to Feynman
- 💬 Recommendations must be justified by data characteristics
- 🤖 Sub-agent should stay under 50% context window
- 📝 MUST update current-understanding.md Section 3

## EXECUTION PROTOCOLS:

- 🎯 Load all phase outputs including insights
- 💾 Feynman writes recommendations to {phaseOutputFile}
- 📝 Feynman updates Section 7 of {edaReportFile}
- 📝 Feynman updates Section 3 of {currentUnderstandingFile}
- 🌐 Optional: Use web search for current SoTA

## CONTEXT BOUNDARIES:

- All EDA complete including insights (Phases 3-7)
- Dashboard approved by user (Phase 8)
- Now need model recommendations for experiment-cycle
- This bridges EDA to experimentation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load State and All Phase Outputs

Load {stateFile} and key outputs:
- `task_type`
- `phase_outputs.phase_04` (label analysis - class count, imbalance)
- `phase_outputs.phase_06` (data quality - dataset size after cleaning)
- `phase_outputs.phase_07` (insights - key findings)

### 2. Spawn Feynman (Data Scientist) Sub-Agent

**Launch a sub-agent with the following task:**

"You are Feynman (Data Scientist). Recommend models for this computer vision task.

**Task Type:** {task_type}

**Data Characteristics:**
- Classes: {class count from phase_04}
- Imbalance: {severity from phase_04}
- Clean Dataset Size: {size from phase_06}
- Image Dimensions: {from phase_03}
- Key Challenges: {from phase_07}

**Your Task:**
Generate model recommendations:

1. **Architecture Landscape:**
   Survey relevant model families:

   **For Object Detection:**
   - One-stage: YOLO (v5/v8/v9), SSD, RetinaNet
   - Two-stage: Faster R-CNN, Mask R-CNN
   - Transformer: DETR, DINO

   **For Classification:**
   - CNN: ResNet, EfficientNet, ConvNeXt
   - Transformer: ViT, Swin Transformer
   - Hybrid approaches

   **For Segmentation:**
   - Semantic: U-Net, DeepLab, SegFormer
   - Instance: Mask R-CNN, YOLACT

2. **Model Evaluation Matrix:**
   For each relevant family, assess:
   - Suitability for this data (High/Med/Low)
   - Strengths for this task
   - Weaknesses/concerns
   - Compute requirements
   - Training data requirements

3. **Top Recommendations:**
   Rank top 3 recommended models with:
   - Why this model fits the data
   - Expected challenges
   - Suggested configuration
   - Training strategy

4. **Training Considerations:**
   Based on data characteristics:
   - Augmentation strategy (based on data quality)
   - Class balancing approach (based on imbalance)
   - Validation strategy (based on dataset size)
   - Transfer learning recommendations

5. **Expected Challenges:**
   Based on EDA findings:
   - What will be hard for any model?
   - Data-specific challenges
   - Mitigation strategies

**Optional: Use web search for current SoTA:**
- Search for recent papers/benchmarks
- Check for newer model versions
- Find relevant pretrained weights

**After analysis, update:**

1. **{phaseOutputFile}** with recommendations summary

2. **Section 7 of {edaReportFile}** with Model Recommendations

3. **Section 3 (Model) of {currentUnderstandingFile}** with:
   - Architecture landscape table
   - Current best approach (top recommendation)
   - Known failure modes (expected challenges)"

### 3. Verify Sub-Agent Output

After Feynman completes, verify:
- [ ] Phase output file exists at {phaseOutputFile}
- [ ] EDA report Section 7 updated
- [ ] current-understanding.md Section 3 updated
- [ ] At least 3 models recommended with justification

### 4. Update State File

Update {stateFile}:
```yaml
stepsCompleted: [..., 'step-09-model-selection']
currentPhase: 'model-selection-complete'
phase_outputs:
  phase_09: '{phaseOutputFile}'
```

### 5. Present Summary

"**Phase 9: Model Selection Complete**

**Top Recommended Models:**

1. **{Model 1}** - {brief rationale}
2. **{Model 2}** - {brief rationale}
3. **{Model 3}** - {brief rationale}

**Training Strategy:**
{key training recommendations}

**Documents Updated:**
- `eda-report-images.md` - Section 7 (Model Recommendations)
- `current-understanding.md` - Section 3 (Model)

Ready to complete the Image EDA workflow?"

### 6. Present MENU OPTIONS

Display: **[C]ontinue** to Phase 10: Completion

#### Menu Handling Logic:

- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Feynman sub-agent spawned with data characteristics
- Multiple models evaluated and ranked
- Recommendations justified by data findings
- Training strategy based on EDA insights
- current-understanding.md Section 3 updated

### ❌ SYSTEM FAILURE:

- Generic recommendations not tied to data
- Not updating current-understanding.md
- Missing training strategy
- State file not updated

**Master Rule:** Orchestrator delegates. Feynman recommends based on data. current-understanding.md updated.
