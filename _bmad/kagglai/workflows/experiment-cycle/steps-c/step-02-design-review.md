---
name: 'step-02-design-review'
description: 'Autonomous review of experiment design against scientific methodology criteria'

nextStepFile: './step-03-implementation.md'
redesignStepFile: './step-01-hypothesis-design.md'
reviewCriteriaFile: '../data/review-criteria.md'
experimentFolder: '{experiments_folder}/{experiment_id}'
experimentReadme: '{experiments_folder}/{experiment_id}/readme.md'
hypothesisRegistryPath: '{docs_folder}/hypothesis-registry.md'
---

# Step 2: Design Review

## STEP GOAL:

To autonomously validate the experiment design (readme.md) against scientific methodology criteria, ensuring the hypothesis is testable, isolated, and properly documented before implementation begins.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FACILITATOR, not a content generator
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If any instruction references a subprocess, subagent, or tool you do not have access to, you MUST still achieve the outcome in your main context thread

### Role Reinforcement:

- ✅ You are a **DS Reviewer** specializing in scientific methodology and experimental design
- ✅ Your role is to be critical, thorough, and constructive
- ✅ You bring expertise in experimental isolation, statistical validity, and reproducibility
- ✅ You are adversarial but fair - find real issues, not nitpicks

### Step-Specific Rules:

- 🎯 Use subprocess Pattern 2 (deep analysis) for methodology review
- 💬 Subprocess returns structured findings, not full content
- ⚙️ If subprocess unavailable, perform analysis in main thread
- 🚫 FORBIDDEN to pass designs with multiple variables being tested
- 🚫 FORBIDDEN to pass designs with missing paths or vague metrics

## EXECUTION PROTOCOLS:

- 🎯 Load review criteria and experiment design
- 💾 Document review findings
- 📖 Update Hypothesis Registry status based on outcome
- 🚫 This is a gatekeeper step - enforce quality rigorously

## CONTEXT BOUNDARIES:

- Available: Experiment readme.md, Review criteria
- Focus: Methodology soundness, experimental isolation, documentation completeness
- Limits: Review only, do not modify the design
- Dependencies: Step 1 must have created experiment folder with readme.md

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Load Review Criteria

Load `{reviewCriteriaFile}` to understand the pass/fail criteria for design review.

Key criteria to evaluate:
- Hypothesis Quality (falsifiable, specific, isolated, motivated)
- Methodology Soundness (controlled, isolated changes, measurable, reproducible)
- Documentation Completeness (paths exist, dataset specified, success criteria, references)
- Anti-Pattern Prevention (no multi-variable, no test leakage, no scope creep)

### 2. Load Experiment Design

Load `{experimentReadme}` and analyze deeply.

**Launch subprocess (Pattern 2 - Deep Analysis):**

"Analyze the experiment design readme.md for methodology soundness. Return structured findings."

**Subprocess returns:**
```json
{
  "experiment_id": "EXP-XXX",
  "hypothesis_quality": {
    "falsifiable": true/false,
    "specific": true/false,
    "isolated": true/false,
    "motivated": true/false,
    "issues": ["list of issues"]
  },
  "methodology_soundness": {
    "controlled": true/false,
    "isolated_changes": true/false,
    "measurable": true/false,
    "reproducible": true/false,
    "issues": ["list of issues"]
  },
  "documentation_completeness": {
    "paths_valid": true/false,
    "dataset_specified": true/false,
    "success_criteria": true/false,
    "references": true/false,
    "issues": ["list of issues"]
  },
  "anti_patterns": {
    "multi_variable": true/false,
    "test_leakage": true/false,
    "scope_creep": true/false,
    "issues": ["list of issues"]
  },
  "verdict": "PASS" or "FAIL",
  "critical_issues": ["list"],
  "recommendations": ["list"]
}
```

**If subprocess unavailable:** Perform the same analysis in main thread.

### 3. Evaluate Against Criteria

For each category, check all criteria:

**Hypothesis Quality:**
- [ ] Falsifiable - Can be proven wrong by experiment
- [ ] Specific - Clear expected outcome with threshold
- [ ] Isolated - Tests exactly one variable
- [ ] Motivated - Grounded in evidence

**Methodology Soundness:**
- [ ] Controlled - Baseline clearly defined with exact paths
- [ ] Isolated changes - Only independent variable changes
- [ ] Measurable - Primary metric specified with evaluation method
- [ ] Reproducible - All paths, seeds, commands specified

**Documentation Completeness:**
- [ ] Paths exist - All referenced files are valid
- [ ] Dataset specified - Exact dataset for evaluation
- [ ] Success criteria - Clear threshold for validation
- [ ] References - Links to Understanding, SOTA, Architecture

**Anti-Pattern Prevention:**
- [ ] No multi-variable testing
- [ ] No test set leakage
- [ ] No scope creep

### 4. Make Verdict

**IF all criteria pass:**
- Verdict: **APPROVED**
- Update `{hypothesisRegistryPath}`: Status → APPROVED_FOR_IMPLEMENTATION

**IF any critical criteria fail:**
- Verdict: **REJECTED**
- Update `{hypothesisRegistryPath}`: Status → NEEDS_REVISION
- Generate detailed feedback

### 5. Present Review Results

**If APPROVED:**

"**Design Review: APPROVED ✓**

**EXP-{XXX}: {Title}**

All criteria passed:
- ✓ Hypothesis is falsifiable, specific, isolated, and motivated
- ✓ Methodology is sound with proper controls
- ✓ Documentation is complete with valid paths
- ✓ No anti-patterns detected

**Ready for Implementation (Step 3).**"

**If REJECTED:**

"**Design Review: REJECTED ✗**

**EXP-{XXX}: {Title}**

### Issues Found

{For each issue}:
1. **[Category]:** {Specific issue}
   - Location: {Where in readme.md}
   - Fix: {What needs to change}

### Required Changes

Before resubmission:
- [ ] {Change 1}
- [ ] {Change 2}

### Guidance

{Additional context to help with redesign}

**Action Required:** Return to Step 1 to address these issues."

### 6. Present MENU OPTIONS

**If APPROVED:**

Display: **Design Review Passed - Select an Option:** [C] Continue to Implementation

#### Menu Handling Logic (APPROVED):
- IF C: Load, read entire file, then execute {nextStepFile}
- IF Any other: Help user, then redisplay menu

**If REJECTED:**

Display: **Design Review Failed - Select an Option:** [R] Return to Hypothesis & Design

#### Menu Handling Logic (REJECTED):
- IF R: Load, read entire file, then execute {redesignStepFile}
- IF Any other: Help user, then redisplay menu

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Review criteria loaded and applied rigorously
- All criteria evaluated systematically
- Subprocess used for deep analysis (or fallback applied)
- Clear verdict with justification
- Hypothesis Registry updated with correct status
- Detailed feedback provided if rejected
- Correct routing based on verdict

### ❌ SYSTEM FAILURE:

- Passing designs with multiple variables
- Passing designs with missing/vague paths
- Not providing actionable feedback on rejection
- Not updating Hypothesis Registry
- Routing to wrong step based on verdict

**Master Rule:** This is a quality gate. Be rigorous but fair. Enforce criteria without exception.
