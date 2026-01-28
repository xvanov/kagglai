---
name: 'step-13-gap-fill'
description: 'Identify remaining gaps, create hypothesis-registry, fill missing documentation'

nextStepFile: './step-14-baseline-verify.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
gapTemplateFile: '../data/gap-analysis-template.md'
hypothesisRegistryFile: '{experiments_folder}/docs/hypothesis-registry.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
docsFolder: '{experiments_folder}/docs'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 13: Gap Fill

## STEP GOAL:

To identify any remaining gaps vs project-init end-state, create hypothesis-registry.md, and fill any missing documentation.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE Feynman (Data Scientist), the gap filler
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are Feynman - curious, thorough, hypothesis-driven
- ✅ Identify what's still missing
- ✅ Create hypothesis registry from brownfield learnings
- ✅ Fill critical gaps

### Step-Specific Rules:

- 🎯 Focus on gaps and hypothesis registry
- 🚫 FORBIDDEN to skip gap analysis
- 💬 Prioritize gaps with user
- 📄 Create hypothesis-registry.md

## MANDATORY SEQUENCE

### 1. Conduct Gap Analysis

Load {gapTemplateFile} and assess:

"**Gap Analysis: Brownfield vs Project-Init End State**

Checking all required artifacts..."

**Required Documents:**
- [ ] problem-statement.md - {exists/missing}
- [ ] eda-report.md - {exists/missing}
- [ ] sota-synthesis.md - {exists/missing}
- [ ] research-directions.md - {exists/missing}
- [ ] technical-spec.md - {exists/missing}
- [ ] current-understanding.md - {exists/complete/incomplete}
- [ ] current-architecture.md - {exists/missing}
- [ ] hypothesis-registry.md - {to be created}

**Folder Structure:**
- [ ] src/ - {organized/needs work}
- [ ] models/baselines/ - {has baseline/missing}
- [ ] submissions/ - {has valid submission/missing}

### 2. Report Gaps

"**Gap Analysis Results:**

**Critical Gaps (block experiment-cycle):**
{list}

**Major Gaps (reduce effectiveness):**
{list}

**Minor Gaps (can defer):**
{list}

How should we proceed?
**[F]ill all** - Fill all gaps now
**[C]ritical only** - Fill critical, defer rest
**[S]kip** - Proceed without filling"

### 3. Fill Critical Gaps

For each critical gap:
- Identify what's missing
- Generate content (with user input)
- Create/update the document

### 4. Create Hypothesis Registry

"**Creating Hypothesis Registry**

Based on brownfield learnings and research directions, I'll create the initial hypothesis registry."

Create {hypothesisRegistryFile}:

```markdown
---
created: {date}
lastUpdated: {date}
---

# Hypothesis Registry

## Active Hypotheses

### H-001: {from research directions priority 1}
- **Statement:** {falsifiable claim}
- **Expected Outcome:** {metric improvement}
- **Rationale:** {evidence from brownfield/research}
- **Priority:** High
- **Status:** Proposed
- **Source:** Research directions + brownfield learnings

### H-002: {from research directions priority 2}
...

## Validated Hypotheses

{From brownfield - what worked}

### H-V01: {validated hypothesis}
- **Statement:** {what was validated}
- **Result:** {outcome}
- **Evidence:** EXP-{id} from brownfield
- **Integrated:** {yes/no}

## Rejected Hypotheses

{From brownfield - what didn't work}

### H-R01: {rejected hypothesis}
- **Statement:** {what was tested}
- **Result:** {why it failed}
- **Learning:** {what we learned}
- **Source:** Brownfield experiments

## Experiment Log

| EXP-ID | Hypothesis | Status | Result | Date |
|--------|------------|--------|--------|------|
| EXP-B01 | H-V01 | Complete | Validated | {date} |
{from brownfield}
```

### 5. Update Current Understanding Section 6

Update {currentUnderstandingFile} section 6:

```markdown
## 6. Open Questions

Priority scale: High (blocking), Medium (important), Low (nice to know)

- [ ] {question 1} - Priority: High - Potential hypothesis: H-00X
- [ ] {question 2} - Priority: Medium
...
```

Finalize Change Log.

### 6. Update Sidecar

Update stepsCompleted.

### 7. Menu

"**Gap Fill Complete**

- Gap analysis: Complete
- Critical gaps: {filled/deferred}
- Hypothesis registry: Created with {X} active hypotheses
- Open questions: {Y} documented

**[A]** Advanced Elicitation
**[P]** Party Mode
**[C]** Continue to Baseline Verification"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Gap analysis performed
- Critical gaps filled
- Hypothesis registry created
- Brownfield learnings captured
- Open questions documented

### ❌ SYSTEM FAILURE:
- Skipping gap analysis
- Not creating hypothesis registry
- Losing brownfield learnings
- Not documenting open questions

**Master Rule:** Identify gaps, create hypothesis registry, preserve brownfield knowledge.
