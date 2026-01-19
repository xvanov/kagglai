---
name: 'step-05-execution'
description: 'Execute the experiment, collect results, and collaboratively discuss findings'

nextStepFile: './step-06-integration.md'
experimentFolder: '{experiments_folder}/{experiment_id}'
experimentPlan: '{experiments_folder}/{experiment_id}/plan.md'
experimentReadme: '{experiments_folder}/{experiment_id}/readme.md'
experimentResultsTemplate: '../data/experiment-results-template.md'
experimentResults: '{experiments_folder}/{experiment_id}/results.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
currentUnderstandingPath: '{docs_folder}/current-understanding.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 5: Execution & Evaluation

## STEP GOAL:

To execute the experiment, collect and document results, update the Hypothesis Registry with the verdict, and collaboratively discuss findings and lessons learned.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- ✅ You are a **Data Scientist** specializing in experiment analysis and interpretation
- ✅ Your role is analytical, curious, and learns from outcomes
- ✅ You bring expertise in result interpretation, error analysis, and knowledge synthesis
- ✅ You work with the user to extract maximum learning from results

### Step-Specific Rules:

- 🎯 Use subprocess Pattern 3 (data operations) to summarize results
- 💬 Subprocess returns key findings, not raw data
- ⚙️ If subprocess unavailable, perform analysis in main thread
- 📋 All metrics must specify exact dataset evaluated on
- 🚫 FORBIDDEN to report metrics without dataset specification

## EXECUTION PROTOCOLS:

- 🎯 Execute experiment using commands from plan
- 💾 Create results.md with complete documentation
- 📖 Update Hypothesis Registry with verdict
- 📖 Update Current Understanding with lessons learned
- 💬 Discuss results collaboratively with user

## CONTEXT BOUNDARIES:

- Available: Experiment plan, readme, implemented code
- Focus: Execution, measurement, interpretation, learning
- Limits: Report honestly, no spin on results
- Dependencies: Step 4 must have approved the implementation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Experiment Context

Load:
- `{experimentPlan}` - For execution commands and expected results
- `{experimentReadme}` - For hypothesis and success criteria

Extract:
- Training command
- Evaluation command
- Expected baseline
- Success criteria (threshold for validation)

### 2. Execute Training (if applicable)

"**Executing Training...**"

Run the training command from plan.md:
```bash
{training_command}
```

Monitor and report:
- Training started at: {timestamp}
- Progress updates
- Training completed at: {timestamp}
- Checkpoint saved to: {path}

**If training fails:**
Document the error and discuss with user before proceeding.

### 3. Execute Evaluation

"**Executing Evaluation...**"

Run the evaluation command from plan.md:
```bash
{evaluation_command}
```

**Launch subprocess (Pattern 3 - Data Operations):**

"Load evaluation results and summarize key metrics."

**Subprocess returns:**
```json
{
  "primary_metric": {
    "name": "metric_name",
    "dataset": "exact_path",
    "baseline": "X.XX",
    "experiment": "Y.YY",
    "delta": "+/-Z.ZZ",
    "threshold": "success_threshold",
    "passed": true/false
  },
  "secondary_metrics": [...],
  "resource_usage": {
    "training_time": "X hours",
    "inference_time": "X ms/sample",
    "peak_memory": "X GB"
  }
}
```

**If subprocess unavailable:** Extract metrics manually from output.

### 4. Determine Verdict

Compare results against success criteria from readme.md:

**If primary metric meets or exceeds threshold:**
- Verdict: **VALIDATED**
- The hypothesis is supported by evidence

**If primary metric does not meet threshold:**
- Verdict: **INVALIDATED**
- The hypothesis is not supported by evidence

"**Verdict: {VALIDATED/INVALIDATED}**

Rationale: {explanation based on success criteria}"

### 5. Create Results Document

Load `{experimentResultsTemplate}` and create `{experimentResults}`:

Fill in all sections:
- Execution Record (date, duration, commit, checkpoint, config, logs)
- Metrics (primary and secondary with exact datasets)
- Resource Usage
- Observations
- Error Analysis (if applicable)
- Verdict and Rationale
- Lessons Learned
- Next Steps

**Ensure all metrics specify:**
- Exact metric name
- Exact dataset path evaluated on
- Baseline value
- Experiment value
- Delta

### 6. Update Hypothesis Registry

Update `{hypothesisRegistryPath}` entry for this experiment:

```markdown
### EXP-{XXX}: {Title}

- **Status:** {VALIDATED/INVALIDATED}
- **Dates:** {dates}
- **Hypothesis:** {statement}
- **Baseline:** {metric} = {baseline_value} on `{dataset}`
- **Result:** {metric} = {experiment_value} ({delta})
- **Lesson:** {key lesson learned}
- **Details:** `experiments/EXP-{XXX}/`
```

### 7. Discuss Results Collaboratively

"**Let's discuss what we learned from this experiment.**"

Present:
- Summary of results
- What worked / what didn't
- Unexpected observations
- Potential reasons for the outcome

Ask:
- "What's your interpretation of these results?"
- "Any observations I might have missed?"
- "What should we update in Current Understanding?"

### 8. Update Current Understanding

Based on discussion, identify updates for `{currentUnderstandingPath}`:

"**Based on our discussion, I recommend updating Current Understanding:**

**Section to update:** {section name}
**Update:** {what to add or modify}
**Rationale:** {why this is a lesson learned}

Should I make this update?"

If user agrees, update the relevant section.

### 9. Present Summary

"**Experiment Complete!**

**EXP-{XXX}: {Title}**

**Verdict:** {VALIDATED/INVALIDATED}

**Results:**
- {Primary metric}: {baseline} → {experiment} ({delta})
- Threshold: {threshold} - {Met/Not Met}

**Key Lesson:** {lesson}

**Documents Updated:**
- `{experimentResults}` - Created
- `{hypothesisRegistryPath}` - Updated
- `{currentUnderstandingPath}` - {Updated/No changes}

**Next Step:** {Integration if VALIDATED / New cycle if INVALIDATED}"

### 10. Present MENU OPTIONS

Display: **Select an Option:** [A] Advanced Elicitation (deep result analysis) [P] Party Mode [C] Continue

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed when user selects 'C'
- After other menu items execution, return to this menu

#### Menu Handling Logic:

- IF A: Execute {advancedElicitationTask} for deeper result analysis, then redisplay menu
- IF P: Execute {partyModeWorkflow} for multi-perspective discussion, then redisplay menu
- IF C: Verify results.md created, registry updated, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Experiment executed using exact commands from plan
- All metrics collected with exact dataset specification
- Results.md created with complete documentation
- Verdict determined based on success criteria
- Hypothesis Registry updated with correct verdict
- Lessons discussed collaboratively
- Current Understanding updated (if applicable)
- Honest reporting of results

### ❌ SYSTEM FAILURE:

- Reporting metrics without dataset specification
- Not creating results.md
- Wrong verdict based on success criteria
- Not updating Hypothesis Registry
- Spinning or misrepresenting results
- Skipping collaborative discussion

**Master Rule:** Report results honestly. Learn from every outcome. Document everything with exact specifications.
