---
name: 'step-01b-continue'
description: 'Handle workflow continuation from previous session'

sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'

# Step routing - all possible next steps
step02File: './step-02-problem-statement.md'
step03File: './step-03-problem-statement-review.md'
step03bFile: './step-03b-problem-statement-fix.md'
step04File: './step-04-eda-basic.md'
step05File: './step-05-eda-deep.md'
step06File: './step-06-sota-research.md'
step07File: './step-07-sota-review.md'
step07bFile: './step-07b-sota-fix.md'
step08File: './step-08-research-directions.md'
step09File: './step-09-technical-spec.md'
step10File: './step-10-technical-spec-review.md'
step10bFile: './step-10b-technical-spec-fix.md'
step11File: './step-11-implementation.md'
step12File: './step-12-code-review.md'
step12bFile: './step-12b-code-fix.md'
step13File: './step-13-complete.md'
---

# Step 1b: Continue Workflow

## STEP GOAL:

To resume the project setup workflow from where it was left off in a previous session, routing to the correct next step.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a workflow orchestrator helping resume work
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring workflow context, user brings their time and focus
- ✅ Together we pick up where we left off efficiently

### Step-Specific Rules:

- 🎯 Focus ONLY on reading state and routing to correct step
- 🚫 FORBIDDEN to do any work - just route
- 💬 Provide clear status summary before routing
- 🚪 This is a routing step only

## EXECUTION PROTOCOLS:

- 🎯 Read sidecar to understand current state
- 💾 Do NOT modify sidecar - just read it
- 📖 Route to the correct next step
- 🚫 FORBIDDEN to skip steps or optimize

## CONTEXT BOUNDARIES:

- User has run this workflow before
- Sidecar file exists with stepsCompleted array
- Need to determine and route to the correct next step
- Previous session notes may provide context

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Welcome Back

"**Welcome back to the BMDS Project Initialization Workflow!**

Let me check where we left off..."

### 2. Read Sidecar State

Load {sidecarFile} and extract:
- `stepsCompleted` array
- `lastStep` value
- `status` value
- Any session notes from previous sessions

### 3. Display Progress Summary

"**Project Setup Progress:**

**Steps Completed:**
[List each step from stepsCompleted with checkmark]

**Last Step:** {lastStep}
**Status:** {status}

**Session History:**
[Summarize previous session notes if any]"

### 4. Determine Next Step

Based on `lastStep`, determine the next step to execute:

| Last Step Completed | Next Step File |
|---------------------|----------------|
| step-01-init | {step02File} |
| step-02-problem-statement | {step03File} |
| step-03-problem-statement-review | {step04File} |
| step-03b-problem-statement-fix | {step04File} |
| step-04-eda-basic | {step05File} |
| step-05-eda-deep | {step06File} |
| step-06-sota-research | {step07File} |
| step-07-sota-review | {step08File} |
| step-07b-sota-fix | {step08File} |
| step-08-research-directions | {step09File} |
| step-09-technical-spec | {step10File} |
| step-10-technical-spec-review | {step11File} |
| step-10b-technical-spec-fix | {step11File} |
| step-11-implementation | {step12File} |
| step-12-code-review | {step13File} |
| step-12b-code-fix | {step13File} |
| step-13-complete | WORKFLOW COMPLETE |

### 5. Handle Special Cases

**IF status == 'COMPLETE':**
- "**This project setup is already complete!**"
- "All documents have been generated and the baseline is ready."
- "You can now use the `experiment-cycle` workflow to run experiments."
- HALT - do not proceed

**IF last step was a review step and user wants to use fix-only:**
- Ask: "The last step was a review. Would you like to:
  - **[C]ontinue** to the next phase (review was successful)
  - **[F]ix** issues using the fix-only step (review found issues)"
- Route accordingly

### 6. Confirm and Route

"**Ready to continue with: {next step name}**

**Agent needed:** {agent for that step}
**Task:** {brief description}

Proceeding..."

Load, read entire file, then execute the appropriate next step file.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Sidecar read correctly
- Progress summary displayed clearly
- Correct next step identified
- User informed of what's next
- Routed to correct step file

### ❌ SYSTEM FAILURE:

- Modifying sidecar in this step
- Wrong next step routing
- Skipping steps
- Not showing progress summary
- Proceeding without user awareness

**Master Rule:** This step ONLY reads state and routes. No work, no modifications, just navigation.
