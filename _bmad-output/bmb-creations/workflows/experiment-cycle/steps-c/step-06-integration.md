---
name: 'step-06-integration'
description: 'Conditional integration of validated experiment code into main codebase and architecture'

experimentFolder: '{experiments_folder}/{experiment_id}'
experimentResults: '{experiments_folder}/{experiment_id}/results.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
currentArchitecturePath: '{docs_folder}/current-architecture.md'
---

# Step 6: Integration (Conditional)

## STEP GOAL:

To integrate validated experiment code into the main codebase and update the Current Architecture document. This step only executes if the experiment was VALIDATED.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- ✅ You are an **Implementor** specializing in code integration and architecture maintenance
- ✅ Your role is careful, systematic, and production-minded
- ✅ You bring expertise in merging code, maintaining documentation, and ensuring consistency
- ✅ You only integrate validated, tested code

### Step-Specific Rules:

- 🎯 Check verdict FIRST - only proceed if VALIDATED
- 🚫 FORBIDDEN to integrate INVALIDATED experiments
- 💬 Get user confirmation before merging to main
- 📋 Update architecture document with all changes

## EXECUTION PROTOCOLS:

- 🎯 Verify experiment status is VALIDATED
- 💾 Merge code to main codebase
- 📖 Update Current Architecture document
- 📖 Promote checkpoint and config to production locations

## CONTEXT BOUNDARIES:

- Available: Experiment results, current architecture
- Focus: Clean integration, documentation update
- Limits: Only integrate if VALIDATED
- Dependencies: Step 5 must have completed with VALIDATED verdict

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Check Experiment Status

Load `{hypothesisRegistryPath}` and check the status of this experiment.

**IF status == VALIDATED:**
"**Experiment VALIDATED ✓** - Proceeding with integration."

**IF status != VALIDATED:**
"**Experiment not validated** - Status: {status}

Integration is only performed for validated experiments. This experiment cycle is complete.

**Options:**
- Start a new experiment cycle with a different hypothesis
- Return to review what we learned from this experiment"

**Present skip menu and exit.**

### 2. Load Integration Context

Load:
- `{experimentResults}` - For what changed and impact
- `{currentArchitecturePath}` - For current state

Identify:
- Files modified in experiment
- New configurations
- Checkpoint to promote
- Performance improvement achieved

### 3. Prepare Integration Plan

"**Integration Plan:**

**Code Changes to Merge:**
- `{file1}` - {change description}
- `{file2}` - {change description}

**Checkpoint to Promote:**
- From: `{experiment_checkpoint_path}`
- To: `{production_checkpoint_path}`

**Config to Promote:**
- From: `{experiment_config_path}`
- To: `{production_config_path}`

**Architecture Updates:**
- Section: {section}
- Change: {what to update}

Does this integration plan look correct?"

### 4. Execute Code Merge

"**Merging code to main codebase...**"

For each file:
1. Apply the validated changes
2. Commit with reference to experiment ID

```bash
git add {files}
git commit -m "Integrate EXP-{XXX}: {title}

- {change 1}
- {change 2}

Validated improvement: {metric} {delta}"
```

Record commit hash.

### 5. Promote Checkpoint and Config

"**Promoting artifacts to production locations...**"

1. Copy checkpoint:
   - From: `{experiment_checkpoint}`
   - To: `{production_checkpoint}`

2. Copy config:
   - From: `{experiment_config}`
   - To: `{production_config}`

### 6. Update Current Architecture

Update `{currentArchitecturePath}` with:

**Model Architecture section (if changed):**
- Update modifications table

**Training Configuration (if changed):**
- Update relevant parameters

**Post-Processing (if changed):**
- Update pipeline steps

**Validated Changes Log:**
Add new entry:
```markdown
| {date} | EXP-{XXX} | {change description} | {+X% metric} | `{commit_hash}` | `{files}` |
```

**Performance Update:**
Update the header performance metric if improved.

### 7. Update Hypothesis Registry

Update the experiment entry to reflect integration:

```markdown
### EXP-{XXX}: {Title}

- **Status:** VALIDATED ✓ INTEGRATED
- **Dates:** {dates}
- **Hypothesis:** {statement}
- **Baseline:** {metric} = {baseline}
- **Result:** {metric} = {result} ({delta})
- **Lesson:** {lesson}
- **Details:** `experiments/EXP-{XXX}/`
- **Integration:** Commit `{hash}`, {date}
```

### 8. Present Completion Summary

"**Integration Complete!**

**EXP-{XXX}: {Title}**

**Merged to Main:**
- Commit: `{commit_hash}`
- Files: {list}

**Artifacts Promoted:**
- Checkpoint: `{production_checkpoint_path}`
- Config: `{production_config_path}`

**Current Architecture Updated:**
- Performance: {old_metric} → {new_metric}
- Validated Changes Log: Entry added

**This experiment cycle is complete.**

---

**Experiment Cycle Summary:**

1. ✓ Hypothesis & Design - Created EXP-{XXX}
2. ✓ Design Review - APPROVED
3. ✓ Implementation - Completed
4. ✓ Code Review - APPROVED
5. ✓ Execution - VALIDATED
6. ✓ Integration - COMPLETE

**Ready to start a new experiment cycle when you are.**"

### 9. Present MENU OPTIONS

Display: **Cycle Complete - Select an Option:** [N] New Experiment Cycle [R] Review What We Built [D] Done

#### EXECUTION RULES:

- ALWAYS halt and wait for user input
- This is the final step of the cycle

#### Menu Handling Logic:

- IF N: "To start a new cycle, invoke the experiment-cycle workflow again with create mode."
- IF R: List all artifacts created/updated in this cycle
- IF D: "Experiment cycle complete. The validated learning has been integrated into your system."
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Verified experiment status is VALIDATED before proceeding
- Code merged cleanly to main
- Commit includes experiment reference
- Checkpoint and config promoted to production
- Current Architecture updated accurately
- Hypothesis Registry reflects integration
- Complete summary provided

### ❌ SYSTEM FAILURE:

- Integrating non-validated experiments
- Not getting user confirmation before merge
- Missing commit reference to experiment
- Not updating Current Architecture
- Not promoting artifacts to production locations
- Incomplete documentation of changes

**Master Rule:** Only integrate validated experiments. Document everything. Maintain the single source of truth.
