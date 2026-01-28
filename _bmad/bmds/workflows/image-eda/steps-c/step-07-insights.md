---
name: 'step-07-insights'
description: 'Spawn Feynman (Data Scientist) to synthesize findings into strategic insights and update current-understanding.md'

nextStepFile: './step-08-dashboard.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
outputFile: '{experiments_folder}/eda/06_insights.md'
phaseOutputFile: '{experiments_folder}/.phase-07-output.md'
edaReportFile: '{docs_folder}/eda-report-images.md'
currentUnderstandingFile: '{docs_folder}/current-understanding.md'
dataScientistAgent: '{project-root}/_bmad/bmds/agents/data-scientist/data-scientist.agent.yaml'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 7: Insight Generation

## STEP GOAL:

To spawn Feynman (Data Scientist agent) to synthesize all EDA findings into strategic insights, update current-understanding.md Section 2, and prepare for dashboard generation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ORCHESTRATOR spawning a sub-agent
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess/sub-agent unavailable, perform in main thread

### Role Reinforcement:

- ✅ You are the workflow orchestrator delegating to Feynman (Data Scientist)
- ✅ Feynman specializes in strategic synthesis and hypothesis generation
- ✅ This is a CRITICAL phase - insights drive model selection and training
- ✅ Party Mode and Advanced Elicitation available for deeper exploration

### Step-Specific Rules:

- 🎯 Spawn Feynman to generate strategic insights
- 🚫 FORBIDDEN to generate insights yourself - delegate to Feynman
- 💬 Feynman should think like a data scientist planning experiments
- 🤖 Sub-agent should stay under 50% context window
- 📝 MUST update current-understanding.md Section 2

## EXECUTION PROTOCOLS:

- 🎯 Load all phase outputs for synthesis
- 💾 Feynman writes insights to {outputFile}
- 📖 Feynman writes summary to {phaseOutputFile}
- 📝 Feynman updates Section 6 of {edaReportFile}
- 📝 Feynman updates Section 2 of {currentUnderstandingFile}

## CONTEXT BOUNDARIES:

- All analysis phases complete (3, 4, 5, 6)
- Now need strategic synthesis, not just reporting
- Insights should guide model selection and training strategy

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load State and All Phase Outputs

Load {stateFile} and all phase outputs:
- `phase_outputs.phase_03` (basic stats)
- `phase_outputs.phase_04` (label analysis)
- `phase_outputs.phase_05` (visual patterns)
- `phase_outputs.phase_06` (data quality)

### 2. Spawn Feynman (Data Scientist) Sub-Agent

**Launch a sub-agent with the following task:**

"You are Feynman (Data Scientist). Synthesize EDA findings into strategic insights.

**All EDA Findings:**
- Basic Stats: {phase_03 summary}
- Label Analysis: {phase_04 summary}
- Visual Patterns: {phase_05 summary}
- Data Quality: {phase_06 summary}

**Your Task:**
Create `{outputFile}` with strategic insights:

1. **Critical Findings:**
   Identify the 3-5 most important discoveries:
   - What will most impact model training?
   - What must be addressed before training?
   - What opportunities exist?

   For each finding:
   - Description: What was found
   - Evidence: Statistical support
   - Implication: How this affects modeling

2. **Data Strengths:**
   - What's good about this dataset?
   - What can we leverage?
   - Competitive advantages

3. **Data Weaknesses:**
   - What challenges will we face?
   - What limitations exist?
   - Risk factors

4. **Surprising Discoveries:**
   - Unexpected patterns
   - Counter-intuitive findings
   - Things that challenge assumptions

5. **Strategic Recommendations:**
   - Data cleaning priority list
   - Augmentation strategies needed
   - Validation approach suggestions
   - Training strategy implications

6. **Open Questions:**
   - What still needs investigation?
   - What would benefit from more data?
   - Hypotheses to test

**After synthesis, update:**

1. **{phaseOutputFile}** with insights summary

2. **Section 6 of {edaReportFile}** with Key Insights

3. **Section 2 (Data) of {currentUnderstandingFile}** with:
   - Dataset overview
   - Data quality issues table
   - Data insights list
   - Reference to eda-report-images.md"

### 3. Verify Sub-Agent Output

After Feynman completes, verify:
- [ ] Insights document exists at {outputFile}
- [ ] Phase output file exists at {phaseOutputFile}
- [ ] EDA report Section 6 updated
- [ ] current-understanding.md Section 2 updated

### 4. Update State File

Update {stateFile}:
```yaml
stepsCompleted: [..., 'step-07-insights']
currentPhase: 'insights-complete'
phase_outputs:
  phase_07: '{phaseOutputFile}'
```

### 5. Present Summary

"**Phase 7: Insight Generation Complete**

**Critical Findings:**
{top 3 findings from insights}

**Key Recommendations:**
{top recommendations}

**Documents Updated:**
- `{outputFile}` - Full insights document
- `eda-report-images.md` - Section 6
- `current-understanding.md` - Section 2 (Data)

Ready to proceed to Phase 8: Dashboard Generation?"

### 6. Present MENU OPTIONS

Display:
"**Select an Option:**
**[A]** Advanced Elicitation - explore insights more deeply
**[P]** Party Mode - multi-perspective discussion on findings
**[C]** Continue to Phase 8: Dashboard Generation"

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- A and P allow deeper exploration of insights
- ONLY proceed to next step when user selects 'C'

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask}, then redisplay menu
- IF P: Execute {partyModeWorkflow}, then redisplay menu
- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Feynman sub-agent spawned with all findings
- Strategic insights generated (not just reporting)
- Critical findings with implications
- current-understanding.md Section 2 updated
- EDA report Section 6 updated

### ❌ SYSTEM FAILURE:

- Just summarizing without strategic synthesis
- Not updating current-understanding.md
- Missing implications and recommendations
- State file not updated

**Master Rule:** Orchestrator delegates. Feynman synthesizes strategically. current-understanding.md updated.
