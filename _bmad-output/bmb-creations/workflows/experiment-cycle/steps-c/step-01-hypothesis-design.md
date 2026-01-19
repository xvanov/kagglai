---
name: 'step-01-hypothesis-design'
description: 'Collaboratively generate hypothesis and create experiment design with the human'

nextStepFile: './step-02-design-review.md'
experimentReadmeTemplate: '../data/experiment-readme-template.md'
experimentPlanTemplate: '../data/experiment-plan-template.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
currentUnderstandingPath: '{docs_folder}/current-understanding.md'
sotaSynthesisPath: '{docs_folder}/sota-synthesis.md'
currentArchitecturePath: '{docs_folder}/current-architecture.md'
competitionRulesPath: '{docs_folder}/competition-rules.md'
experimentsFolder: '{experiments_folder}'
reviewCriteriaFile: '../data/review-criteria.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
brainstormingTask: '{project-root}/_bmad/core/tasks/brainstorming.xml'
---

# Step 1: Hypothesis & Design

## STEP GOAL:

To collaboratively identify a promising research direction, formulate a testable hypothesis, and create a complete experiment definition ready for review.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- ✅ You are a **Data Scientist** specializing in ML experimentation and hypothesis formulation
- ✅ We engage in collaborative dialogue, not command-response
- ✅ You bring expertise in experimental design, scientific methodology, and ML best practices
- ✅ The user brings domain knowledge, problem context, and experimental goals
- ✅ Together we produce rigorous, testable hypotheses

### Step-Specific Rules:

- 🎯 Focus on understanding the problem space before proposing hypotheses
- 🚫 FORBIDDEN to skip artifact review - always ground in current knowledge
- 💬 Ask 1-2 questions at a time, think about responses before probing deeper
- 🎯 Hypotheses must be falsifiable, isolated (single variable), and motivated by evidence
- 📋 All paths in experiment definition must be exact and verifiable

## EXECUTION PROTOCOLS:

- 🎯 Load and review all core documents before hypothesis generation
- 💾 Create experiment folder with readme.md and plan.md
- 📖 Register hypothesis in {hypothesisRegistryPath}
- 🚫 FORBIDDEN to proceed without complete experiment definition

## CONTEXT BOUNDARIES:

- Available: Current Understanding, SOTA Synthesis, Hypothesis Registry, Competition Rules, Current Architecture
- Focus: Identifying gaps, failure modes, or opportunities for improvement
- Limits: One hypothesis per cycle, must be testable
- Dependencies: None - this is the first step of the cycle

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load and Review Core Documents

Load and analyze the following documents to ground the conversation:

1. **Current Understanding** (`{currentUnderstandingPath}`)
   - What do we know about the data, problem, and effective approaches?
   - What are the known failure modes?
   - What open questions exist?

2. **Hypothesis Registry** (`{hypothesisRegistryPath}`)
   - What experiments have been run?
   - What worked? What didn't?
   - What's the current state of knowledge?

3. **Current Architecture** (`{currentArchitecturePath}`)
   - What's the current best system?
   - What's the baseline performance?

4. **SOTA Synthesis** (`{sotaSynthesisPath}`)
   - What techniques haven't we tried?
   - What's working for others?

5. **Competition Rules** (`{competitionRulesPath}`)
   - Any constraints we must respect?
   - Evaluation metric details?

**Present a summary:** "Based on my review of the current state..."

### 2. Identify Research Direction

Engage collaboratively with the user:

"**Let's identify a promising research direction.**

From my review, I see these opportunities:

1. **[Gap/Failure Mode]:** {description} - Potential: {why promising}
2. **[Gap/Failure Mode]:** {description} - Potential: {why promising}
3. **[Untried Technique]:** {description} - Evidence: {from SOTA}

What's your intuition? Which of these resonates, or do you have a different direction in mind?"

**Think about their response before continuing...**

### 3. Formulate Hypothesis

Once a direction is chosen, formulate a hypothesis together:

"**Let's turn this into a testable hypothesis.**

A good hypothesis is:
- **Falsifiable:** Can be proven wrong by experiment
- **Specific:** Clear expected outcome with threshold
- **Isolated:** Tests exactly one variable
- **Motivated:** Grounded in evidence

Based on our discussion, here's a draft hypothesis:

**Hypothesis:** {clear statement}
**Expected Outcome:** {quantified, e.g., '>2% improvement in CDA'}
**Rationale:** {why we believe this, linked to evidence}

Does this capture what we want to test? Should we refine it?"

### 4. Determine Experiment ID

Check `{hypothesisRegistryPath}` for the latest experiment ID and increment:

"**Assigning Experiment ID:** EXP-{XXX}"

Create the experiment folder: `{experimentsFolder}/EXP-{XXX}-{short-name}/`

### 5. Create Experiment Definition (readme.md)

Load `{experimentReadmeTemplate}` and collaboratively fill it out:

"**Let's define the experiment design.**"

Work through each section:

**Methodology:**
- "What exactly are we changing? (Independent variable)"
- "What stays constant? (Control)"
- "How will we measure success? (Dependent variable, exact metric, exact dataset)"

**Baseline:**
- "What checkpoint/config is our baseline?"
- "What's the current baseline metric?"

**Success Criteria:**
- "What threshold validates the hypothesis?"
- "What secondary metrics should we track?"

**Risks & Assumptions:**
- "What could invalidate our results?"
- "What are we assuming?"

**Create the file:** `{experimentsFolder}/EXP-{XXX}-{short-name}/readme.md`

Ensure ALL paths are exact and verifiable.

### 6. Create Implementation Plan (plan.md)

Load `{experimentPlanTemplate}` and collaboratively fill it out:

"**Now let's create the implementation plan.**"

Work through:

**Prerequisites:**
- "What files/checkpoints must exist?"
- "What's the environment setup?"

**Implementation Tasks:**
- "What specific code changes are needed?"
- "Which files will be modified?"
- "Can you walk me through the changes?"

For each task, get:
- Exact file paths
- Exact code changes (before/after)
- Verification checklist

**Execution:**
- "What's the exact training command?"
- "What's the exact evaluation command?"
- "Where will outputs be saved?"

**Create the file:** `{experimentsFolder}/EXP-{XXX}-{short-name}/plan.md`

### 7. Register Hypothesis

Add entry to `{hypothesisRegistryPath}`:

```markdown
### EXP-{XXX}: {Title}

- **Status:** PENDING
- **Dates:** {YYYY-MM}
- **Hypothesis:** {statement}
- **Baseline:** {metric} = {value} on `{dataset_path}`
- **Result:** Pending execution
- **Lesson:** To be determined
- **Details:** `experiments/EXP-{XXX}-{short-name}/`
```

### 8. Review Against Criteria

Load `{reviewCriteriaFile}` and self-check the design:

"**Let me verify the design meets review criteria...**"

Check:
- [ ] Hypothesis is falsifiable
- [ ] Single variable being tested
- [ ] Baseline clearly specified
- [ ] Success criteria defined
- [ ] All paths are exact and verifiable
- [ ] No test set leakage

If any issues, address them before proceeding.

### 9. Present Summary

"**Experiment Definition Complete!**

**EXP-{XXX}: {Title}**

- **Hypothesis:** {statement}
- **Baseline:** {metric} = {value}
- **Target:** {expected improvement}
- **Files Created:**
  - `{experimentsFolder}/EXP-{XXX}-{short-name}/readme.md`
  - `{experimentsFolder}/EXP-{XXX}-{short-name}/plan.md`
- **Registry Updated:** {hypothesisRegistryPath}

Ready for Design Review (Step 2)."

### 10. Present MENU OPTIONS

Display: **Select an Option:** [B] Brainstorming [A] Advanced Elicitation [P] Party Mode [C] Continue to Design Review

#### EXECUTION RULES:

- ALWAYS halt and wait for user input after presenting menu
- ONLY proceed to next step when user selects 'C'
- After other menu items execution, return to this menu
- User can chat or ask questions - always respond and redisplay menu

#### Menu Handling Logic:

- IF B: Execute {brainstormingTask} to generate more hypothesis ideas, then redisplay menu
- IF A: Execute {advancedElicitationTask} to stress-test the hypothesis, then redisplay menu
- IF P: Execute {partyModeWorkflow} for multi-perspective discussion, then redisplay menu
- IF C: Verify experiment folder created with readme.md and plan.md, verify registry updated, then load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Core documents reviewed and synthesized
- Research direction identified collaboratively
- Hypothesis is falsifiable, isolated, and motivated
- Experiment folder created with complete readme.md and plan.md
- All paths are exact and verifiable
- Hypothesis registered with PENDING status
- Design self-checked against review criteria
- User agrees design is ready for review

### ❌ SYSTEM FAILURE:

- Proposing hypothesis without reviewing current state
- Multiple variables being tested (not isolated)
- Vague paths or metrics (e.g., "the model" instead of exact path)
- Missing success criteria
- Skipping the self-check against review criteria
- Proceeding without user agreement

**Master Rule:** Hypotheses must be grounded in evidence and testable. Every path must be exact. Skipping steps is FORBIDDEN.
