---
name: 'step-e-01-assess'
description: 'Assess current workflow state and determine what needs editing'

nextStepFile: './step-e-02-select-phase.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'

# Documents to assess
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
sotaSynthesisFile: '{experiments_folder}/docs/sota-synthesis.md'
researchDirectionsFile: '{experiments_folder}/docs/research-directions.md'
technicalSpecFile: '{experiments_folder}/docs/technical-spec.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
currentArchitectureFile: '{experiments_folder}/docs/current-architecture.md'
hypothesisRegistryFile: '{experiments_folder}/docs/hypothesis-registry.md'
---

# Step E-01: Assess Current State

## STEP GOAL:

To assess the current state of all project setup artifacts and help the user understand what can be edited and what the implications might be.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER make edits in this step - assessment only
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step, ensure entire file is read
- 📋 YOU ARE AN ASSESSOR helping the user understand their options
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are assessing the state to inform editing decisions
- ✅ Help user understand document dependencies
- ✅ Flag potential cascade effects of edits
- ✅ Guide user to the right document to edit

### Step-Specific Rules:

- 🎯 Focus on ASSESSMENT and GUIDANCE
- 🚫 FORBIDDEN to make any edits
- 💬 Be clear about what exists and what's editable
- 🚪 This step informs the selection step

## EXECUTION PROTOCOLS:

- 🎯 Check which documents exist
- 💾 Assess document completeness
- 📖 Explain dependencies between documents
- 🚫 FORBIDDEN to edit anything

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Announce Edit Mode

"**Edit Mode: Assessment**

I'll assess your current project setup artifacts to help you determine what needs editing.

Scanning documents..."

### 2. Check Document Inventory

Check each document and note its status:

**Core Documents:**
| Document | Exists | Last Updated |
|----------|--------|--------------|
| challenge-spec.md | {yes/no} | {date} |
| eda-report.md | {yes/no} | {date} |
| sota-synthesis.md | {yes/no} | {date} |
| research-directions.md | {yes/no} | {date} |
| technical-spec.md | {yes/no} | {date} |

**Handoff Documents:**
| Document | Exists | Last Updated |
|----------|--------|--------------|
| current-understanding.md | {yes/no} | {date} |
| current-architecture.md | {yes/no} | {date} |
| hypothesis-registry.md | {yes/no} | {date} |

### 3. Explain Document Dependencies

"**Document Dependencies:**

Understanding dependencies helps you know what might need updating if you change something:

```
challenge-spec.md
      ↓
eda-report.md ←──────────┐
      ↓                   │
sota-synthesis.md         │
      ↓                   │
research-directions.md ───┤
      ↓                   │
technical-spec.md ────────┘
      ↓
implementation (code)
```

**Cascade Effects:**
- Editing **challenge-spec** may affect: EDA recommendations, SoTA applicability, all downstream docs
- Editing **EDA** may affect: Research directions, technical spec
- Editing **SoTA** may affect: Research directions, technical spec
- Editing **research-directions** may affect: Technical spec, implementation
- Editing **technical-spec** may affect: Implementation only (if not yet done)
- Editing **handoff docs** is generally safe (informational)"

### 4. Read Sidecar for Context

Read {sidecarFile} to understand:
- What steps have been completed
- Any notes about issues or decisions
- Current workflow status

### 5. Provide Assessment Summary

"**Assessment Summary:**

**Workflow Status:** {from sidecar}

**Editable Documents:**
{List documents that exist and can be edited}

**Editing Considerations:**
- If you edit early documents (challenge-spec, EDA), consider whether downstream documents need updates
- If the workflow is COMPLETE, edits won't re-run later steps automatically
- Handoff documents (current-understanding, current-architecture, hypothesis-registry) can be edited freely

**Common Edit Scenarios:**
1. **Competition details changed** → Edit challenge-spec
2. **New data insights** → Edit eda-report
3. **Found new techniques** → Edit sota-synthesis
4. **Want to reprioritize** → Edit research-directions
5. **Implementation changes** → Edit technical-spec
6. **Update for experiments** → Edit handoff docs

**What would you like to edit?**

**[C]ontinue** to document selection"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All documents checked for existence
- Dependencies explained clearly
- Sidecar context provided
- User understands their options
- Clean handoff to selection step

### ❌ SYSTEM FAILURE:

- Making edits in this step
- Not explaining dependencies
- Skipping sidecar context
- Confusing the user about options

**Master Rule:** Assess and inform. Don't edit. Guide the user to the right choice.
