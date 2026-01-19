---
name: 'step-08-research-directions'
description: 'Researcher creates ranked research directions in collaboration with user'

nextStepFile: './step-09-technical-spec.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
templateFile: '../templates/research-directions-template.md'
outputFile: '{experiments_folder}/docs/research-directions.md'
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
sotaFile: '{experiments_folder}/docs/sota-synthesis.md'
hypothesisRegistryFile: '{experiments_folder}/docs/hypothesis-registry.md'

# Advanced tools
advancedElicitationEnabled: true
partyModeEnabled: true
brainstormingEnabled: true
---

# Step 8: Research Directions

## STEP GOAL:

To collaboratively develop prioritized research directions that synthesize challenge requirements, data insights, and state of the art knowledge into a strategic roadmap for the competition. This is a creative, strategic step requiring user engagement.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER finalize directions without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A STRATEGIC ADVISOR collaborating on research priorities
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the Researcher agent doing strategic planning
- ✅ Every direction must be GROUNDED in evidence (spec, EDA, SoTA)
- ✅ This is COLLABORATIVE - user priorities matter
- ✅ Prioritization involves judgment - discuss trade-offs

### Step-Specific Rules:

- 🎯 Focus on ACTIONABLE directions with clear success criteria
- 🚫 FORBIDDEN to propose unsupported directions
- 💬 Actively seek user input on priorities and trade-offs
- 🚪 This document guides all subsequent work

## EXECUTION PROTOCOLS:

- 🎯 Synthesize all prior documents (spec, EDA, SoTA)
- 💾 Generate candidate directions with evidence
- 📖 Collaborate with user to rank and refine
- 🚫 FORBIDDEN to make priority decisions alone

## CONTEXT BOUNDARIES:

- Challenge spec defines what we're optimizing for
- EDA reveals data realities and opportunities
- SoTA provides technique options and evidence
- User has context, preferences, and constraints you don't see

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 08: Research Directions**

This is a strategic planning step where we'll develop prioritized research directions together. Every direction will be grounded in what we've learned from the challenge spec, EDA, and state of the art research.

Let me load our accumulated knowledge..."

### 2. Load and Synthesize Context

Read all three foundation documents:
- {challengeSpecFile} - Constraints and objectives
- {edaReportFile} - Data characteristics and opportunities
- {sotaFile} - Techniques and what works

Synthesize a summary:

"**Strategic Context:**

**What We're Optimizing:** {metric} ({direction better})

**Key Constraints:**
- {constraint 1}
- {constraint 2}
- {constraint 3}

**Data Realities:**
- {key EDA finding 1}
- {key EDA finding 2}
- {data quality consideration}

**Promising Techniques (from SoTA):**
- {technique 1} - {relevance}
- {technique 2} - {relevance}
- {technique 3} - {relevance}

Does this summary capture the key strategic factors? Anything to add?"

Wait for user input.

### 3. Brainstorm Candidate Directions

Generate candidate research directions:

"Let me brainstorm potential directions based on our analysis..."

**For each candidate direction, note:**
- Name and brief description
- Supporting evidence (from spec, EDA, or SoTA)
- Expected difficulty
- Potential upside

Present the candidates:

"**Candidate Directions:**

1. **{Direction A}** - {1-sentence description}
   - Evidence: {from spec/EDA/SoTA}
   - Difficulty: {L/M/H}

2. **{Direction B}** - {1-sentence description}
   - Evidence: {from spec/EDA/SoTA}
   - Difficulty: {L/M/H}

3. **{Direction C}** - {1-sentence description}
   - Evidence: {from spec/EDA/SoTA}
   - Difficulty: {L/M/H}

4. **{Direction D}** - {1-sentence description}
   - Evidence: {from spec/EDA/SoTA}
   - Difficulty: {L/M/H}

5. **{Direction E}** - {1-sentence description}
   - Evidence: {from spec/EDA/SoTA}
   - Difficulty: {L/M/H}

What are your thoughts? Any directions to add or remove? Any early preferences?"

Wait for user input.

### 4. Discuss Trade-offs and Priorities

Engage in prioritization discussion:

"Let's discuss how to prioritize these directions.

**Trade-off Considerations:**

- **Quick wins vs. long-term gains:** {Direction X} is quick but limited upside. {Direction Y} is harder but higher potential.

- **Constraint compatibility:** {Direction Z} pushes against {constraint}, while {Direction W} is comfortably within limits.

- **Dependencies:** {Direction A} needs to come before {Direction B} because...

**My initial ranking suggestion:**
1. {Direction} - {rationale}
2. {Direction} - {rationale}
3. {Direction} - {rationale}
4. {Direction} - {rationale}
5. {Direction} - {rationale}

What's your reaction to this ranking? What factors are most important to you?"

Wait for user input. Iterate as needed.

### 5. Finalize Directions with User

Once ranking is discussed, confirm:

"**Confirmed Research Directions (in priority order):**

1. **{Direction 1}** - {brief description}
2. **{Direction 2}** - {brief description}
3. **{Direction 3}** - {brief description}
4. **{Direction 4}** - {brief description}
5. **{Direction 5}** - {brief description}

**Excluded:** {directions not pursuing and why}

Is this our final ranking?"

Wait for user confirmation before proceeding.

### 6. Load Template and Document

Read {templateFile} to understand the target structure.

For each confirmed direction (Priority 1-5), populate:
- Detailed description
- Why promising (grounded evidence)
- Alignment with evaluation metric
- Expected difficulty and timeline
- Dependencies
- Key experiments to run
- Measurable success criteria

Also populate:
- Strategic overview and key success factors
- Direction comparison matrix
- Dependency graph
- Excluded directions with rationale
- Implementation roadmap (phased)
- Grounding evidence table (from spec, EDA, SoTA)
- Uncertainty areas and pivot triggers

### 7. Write Research Directions Document

Create {outputFile} with all content.

### 8. Initialize Hypothesis Registry

Create {hypothesisRegistryFile} with initial entries:

```markdown
# Hypothesis Registry

**Competition:** {competition_name}
**Created:** {date}
**Last Updated:** {date}

---

## Registry Format

Each hypothesis follows this structure:
- **ID:** H-{number}
- **Hypothesis:** {statement}
- **Rationale:** {why we believe this}
- **Test:** {how to test it}
- **Status:** {PENDING/TESTING/VALIDATED/INVALIDATED}
- **Result:** {outcome when tested}

---

## Hypotheses from Project Setup

### H-001: {from Direction 1}
- **Hypothesis:** {testable statement}
- **Rationale:** {from research directions}
- **Test:** {first experiment}
- **Status:** PENDING

### H-002: {from Direction 2}
- **Hypothesis:** {testable statement}
- **Rationale:** {from research directions}
- **Test:** {first experiment}
- **Status:** PENDING

### H-003: {from Direction 3}
- **Hypothesis:** {testable statement}
- **Rationale:** {from research directions}
- **Test:** {first experiment}
- **Status:** PENDING

{Continue for remaining directions}

---

## Registry Notes

Initial hypotheses derived from project-setup research directions.
These will be tested during the experiment-cycle workflow.
```

### 9. Update Sidecar

Update {sidecarFile}:
- Add 'step-08-research-directions' to stepsCompleted
- Set lastStep to 'step-08-research-directions'
- Update lastUpdated date
- Add session note: "Research directions finalized - {count} directions prioritized"
- Note the priority 1 direction

### 10. Summary and Proceed

"**Research Directions Complete**

**Documents created:**
- `{outputFile}` - {count} prioritized research directions
- `{hypothesisRegistryFile}` - Initial hypotheses for experiment-cycle

**Priority 1 Direction:** {name}
**Implementation Approach:** {brief summary}

**Next step:** Technical Specification
- Agent: Implementer
- Task: Plan the baseline implementation for Direction 1

**Select an option:**
- **[A]dvanced Elicitation** - Explore any directions more deeply
- **[P]arty Mode** - Multi-agent discussion of research strategy
- **[C]ontinue** - Proceed to technical specification"

Wait for user selection.

**IF [A]:** Use advanced elicitation techniques
**IF [P]:** Initiate party mode for multi-perspective discussion
**IF [C]:** Load, read entire file, then execute {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All three foundation documents synthesized
- Multiple candidate directions generated
- User engaged in prioritization discussion
- Final ranking confirmed by user
- Every direction grounded in evidence
- Success criteria are measurable
- Dependencies mapped
- Hypothesis registry initialized

### ❌ SYSTEM FAILURE:

- Making priority decisions without user input
- Proposing unsupported directions
- Skipping trade-off discussion
- Not grounding directions in evidence
- Vague success criteria
- Missing dependency analysis
- Forgetting to initialize hypothesis registry

**Master Rule:** This is COLLABORATIVE strategy. Every direction must be grounded. User confirms the final ranking.
