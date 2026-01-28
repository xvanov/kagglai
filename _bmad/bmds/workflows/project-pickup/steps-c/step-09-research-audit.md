---
name: 'step-09-research-audit'
description: 'Analyze existing models and approaches, create sota-synthesis and research-directions'

nextStepFile: './step-10-research-review.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
sotaTemplateFile: '../templates/sota-synthesis-template.md'
researchTemplateFile: '../templates/research-directions-template.md'
sotaOutputFile: '{experiments_folder}/docs/sota-synthesis.md'
researchOutputFile: '{experiments_folder}/docs/research-directions.md'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 9: Research Audit

## STEP GOAL:

To analyze existing models and approaches from the brownfield, research current state-of-the-art, and create sota-synthesis.md and research-directions.md.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE Owl (Researcher), the research specialist
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are Owl, the Researcher - methodical, thorough, evidence-based
- ✅ Extract learnings from brownfield experiments
- ✅ Research current SoTA for the problem type
- ✅ Synthesize what worked, what didn't, what to try

### Step-Specific Rules:

- 🎯 Focus on models, architectures, and approaches
- 🚫 FORBIDDEN to implement - just research and document
- 💬 Use web search for current SoTA
- 📄 Create both sota-synthesis and research-directions

## MANDATORY SEQUENCE

### 1. Load Brownfield Model Context

Load {sidecarFile} to get included model artifacts.

"**Research Audit**

I'll analyze your existing models and research current state-of-the-art approaches."

### 2. Analyze Existing Models

For each included model artifact:

"**Analyzing:** `{model_path}`

**Architecture:** {type/name}
**Configuration:** {key hyperparameters}
**Performance:** {metrics if available}
**Training:** {epochs, batch size, etc. if available}
**What worked:** {positive findings}
**What didn't:** {negative findings}
**Lessons:** {key learnings}"

### 3. Synthesize Brownfield Learnings

"**Learnings from Brownfield:**

**Approaches Tried:**
| Approach | Performance | Verdict | Notes |
|----------|-------------|---------|-------|
{rows}

**Key Insights:**
- {insight 1}
- {insight 2}

**What to Preserve:**
- {successful approach 1}

**What to Avoid:**
- {failed approach 1}"

### 4. Research Current SoTA

Use web search to research:
- Best approaches for this problem type
- Recent competition winners
- SOTA benchmarks and techniques
- Relevant papers

"**Current State-of-the-Art:**

**Top Approaches:**
1. {approach 1} - {why effective}
2. {approach 2} - {why effective}

**Recent Developments:**
- {development 1}
- {development 2}

**Benchmark Performance:**
- {benchmark} = {score} using {method}

**Sources:**
- {source 1}
- {source 2}"

### 5. Create SoTA Synthesis

Load {sotaTemplateFile} and create {sotaOutputFile}:

```markdown
---
created: {date}
source: Brownfield audit + web research
---

# State-of-the-Art Synthesis

## Problem Type
{classification/regression/etc.}

## Current SoTA
{summary of best approaches}

## Brownfield Approaches
{what was tried, results}

## Architecture Comparison
| Architecture | Strengths | Weaknesses | Performance |
|--------------|-----------|------------|-------------|
{rows}

## Key Techniques
{effective techniques for this problem}

## Gaps vs SoTA
{where brownfield falls short}

## Opportunities
{unexplored approaches worth trying}

## References
{papers, competitions, sources}
```

### 6. Create Research Directions

Load {researchTemplateFile} and create {researchOutputFile}:

```markdown
---
created: {date}
---

# Research Directions

## Priority Rankings

### Priority 1: High Confidence
{approaches with strong evidence}

### Priority 2: Medium Confidence
{approaches worth exploring}

### Priority 3: Experimental
{novel/risky approaches}

## Direction Details

### Direction 1: {name}
- **Approach:** {description}
- **Evidence:** {why this might work}
- **Effort:** {low/medium/high}
- **Expected Impact:** {potential improvement}
- **First Experiment:** {suggested test}

### Direction 2: {name}
...

## Not Recommended
{approaches to avoid and why}

## Resource Requirements
{compute, data, time estimates}
```

### 7. Update Sidecar

Update stepsCompleted.

### 8. Menu

"**Research Audit Complete**

- Analyzed {X} brownfield models
- Researched current SoTA
- Created sota-synthesis.md
- Created research-directions.md with {Y} directions

**[A]** Advanced Elicitation
**[P]** Party Mode
**[C]** Continue to Research Review"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Brownfield models analyzed
- SoTA researched
- Both documents created
- Clear direction priorities
- Evidence-based recommendations

### ❌ SYSTEM FAILURE:
- Skipping brownfield analysis
- No web research for current SoTA
- Missing either document
- Recommendations without evidence

**Master Rule:** Combine brownfield learnings with current SoTA to chart research directions.
