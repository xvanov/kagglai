---
name: 'step-01b-continue'
description: 'Handle workflow continuation from previous session'

sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
workflowFile: '../workflow.md'

nextStepOptions:
  step-02-discovery: './step-02-discovery.md'
  step-03-discovery-review: './step-03-discovery-review.md'
  step-04-structure-setup: './step-04-structure-setup.md'
  step-05-problem-statement: './step-05-problem-statement.md'
  step-06-problem-review: './step-06-problem-review.md'
  step-06b-problem-fix: './step-06b-problem-fix.md'
  step-07-eda-audit: './step-07-eda-audit.md'
  step-08-eda-deep: './step-08-eda-deep.md'
  step-09-research-audit: './step-09-research-audit.md'
  step-10-research-review: './step-10-research-review.md'
  step-10b-research-fix: './step-10b-research-fix.md'
  step-11-architecture-doc: './step-11-architecture-doc.md'
  step-12-architecture-review: './step-12-architecture-review.md'
  step-12b-architecture-fix: './step-12b-architecture-fix.md'
  step-13-gap-fill: './step-13-gap-fill.md'
  step-14-baseline-verify: './step-14-baseline-verify.md'
  step-15-complete: './step-15-complete.md'
---

# Step 1b: Continue Workflow

## STEP GOAL:

To resume the project pickup workflow from where it was left off in a previous session.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ORCHESTRATOR, routing to the correct step
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the workflow orchestrator resuming a previous session
- ✅ Read the sidecar to understand current state
- ✅ Route to the correct next step
- ✅ Provide context about where we left off

### Step-Specific Rules:

- 🎯 Focus ONLY on reading state and routing
- 🚫 FORBIDDEN to re-do completed steps
- 💬 Summarize progress and next action
- 🚪 Load the correct next step file

## EXECUTION PROTOCOLS:

- 🎯 Read sidecar file for stepsCompleted
- 💾 Determine next step from completed list
- 📖 Load and execute the correct step file
- 🚫 Never skip the routing logic

## CONTEXT BOUNDARIES:

- User has run this workflow before
- Sidecar file exists with stepsCompleted array
- Need to route to the correct next step
- Artifacts from previous sessions are available

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Welcome Back

"**Welcome back to Project Pickup!**

Let me check where we left off..."

### 2. Read Sidecar State

Load {sidecarFile} and read:
- `stepsCompleted` array
- `lastStep` value
- `brownfieldPath`
- `status`

### 3. Summarize Progress

Based on stepsCompleted, summarize what's been done:

"**Project:** {projectName}
**Brownfield:** {brownfieldPath}
**Status:** {status}

**Completed Steps:**
{list each step in stepsCompleted with brief description}

**Last completed:** {lastStep}"

### 4. Determine Next Step

Based on the last completed step, determine the next step:

| Last Completed | Next Step |
|----------------|-----------|
| step-01-init | step-02-discovery |
| step-02-discovery | step-03-discovery-review |
| step-03-discovery-review | step-04-structure-setup |
| step-04-structure-setup | step-05-problem-statement |
| step-05-problem-statement | step-06-problem-review |
| step-06-problem-review | step-07-eda-audit |
| step-06b-problem-fix | step-06-problem-review |
| step-07-eda-audit | step-08-eda-deep |
| step-08-eda-deep | step-09-research-audit |
| step-09-research-audit | step-10-research-review |
| step-10-research-review | step-11-architecture-doc |
| step-10b-research-fix | step-10-research-review |
| step-11-architecture-doc | step-12-architecture-review |
| step-12-architecture-review | step-13-gap-fill |
| step-12b-architecture-fix | step-12-architecture-review |
| step-13-gap-fill | step-14-baseline-verify |
| step-14-baseline-verify | step-15-complete |
| step-15-complete | WORKFLOW COMPLETE |

**IF workflow is complete:**

"**This project pickup is already complete!**

All artifacts should be ready in `{experiments_folder}/docs/`:
- problem-statement.md
- eda-report.md
- sota-synthesis.md
- research-directions.md
- technical-spec.md
- current-understanding.md
- current-architecture.md
- hypothesis-registry.md

You can now run the **experiment-cycle** workflow to begin experimentation.

Would you like to:
**[R]estart** - Start a new project pickup (will archive current)
**[E]xit** - Exit the workflow"

→ Handle user choice accordingly.

### 5. Present Continuation Option

"**Next step:** {next_step_name}
{brief description of what this step does}

**[C]ontinue** to {next_step_name}
**[S]ummary** - Show more details about progress
**[R]estart** - Start over (will archive current progress)"

### 6. Handle User Choice

**IF C (Continue):**
- Update sidecar `lastUpdated` timestamp
- Add session note: "Resumed from {lastStep}"
- Load, read entire file, then execute the appropriate step file from {nextStepOptions}

**IF S (Summary):**
- Load and display key artifacts (current-understanding sections, etc.)
- Redisplay continuation menu

**IF R (Restart):**
- Rename current sidecar to `.project-pickup-sidecar-{timestamp}.md.bak`
- Inform user: "Previous session archived. Starting fresh..."
- Load and execute step-01-init.md

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Sidecar read correctly
- Progress summarized accurately
- Correct next step identified
- User given clear options
- Routed to correct step file

### ❌ SYSTEM FAILURE:

- Not reading sidecar properly
- Routing to wrong step
- Not handling completed workflow case
- Losing track of progress

**Master Rule:** Read the state, route correctly, never re-do completed work.
