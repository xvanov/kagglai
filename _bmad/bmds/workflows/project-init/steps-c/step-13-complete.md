---
name: 'step-13-complete'
description: 'Verify all artifacts, generate summary, and hand off to experiment-cycle'

sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'

# All output documents to verify
challengeSpecFile: '{experiments_folder}/docs/problem-statement.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
sotaSynthesisFile: '{experiments_folder}/docs/sota-synthesis.md'
researchDirectionsFile: '{experiments_folder}/docs/research-directions.md'
technicalSpecFile: '{experiments_folder}/docs/technical-spec.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
currentArchitectureFile: '{experiments_folder}/docs/current-architecture.md'
hypothesisRegistryFile: '{experiments_folder}/docs/hypothesis-registry.md'

# Implementation artifacts
srcFolder: '{experiments_folder}/src'
modelsFolder: '{experiments_folder}/models'
submissionsFolder: '{experiments_folder}/submissions'
---

# Step 13: Project Setup Complete

## STEP GOAL:

To verify all project setup artifacts are complete, generate a comprehensive summary, mark the workflow as complete, and provide clear handoff instructions for the experiment-cycle workflow.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER mark complete if artifacts are missing
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: This is the final step - ensure everything is ready
- 📋 YOU ARE A WORKFLOW ORCHESTRATOR verifying completion
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are verifying the entire project setup is complete
- ✅ All handoff documents must exist for experiment-cycle
- ✅ The user should have everything they need to start experimenting
- ✅ This is a celebration moment - acknowledge the work done

### Step-Specific Rules:

- 🎯 Focus on VERIFICATION and HANDOFF
- 🚫 FORBIDDEN to create missing documents (that's earlier steps)
- 💬 Provide clear next steps for the user
- 🚪 After this, user proceeds to experiment-cycle

## EXECUTION PROTOCOLS:

- 🎯 Verify all documents exist and are complete
- 💾 Update sidecar to mark workflow complete
- 📖 Generate comprehensive summary
- 🚫 FORBIDDEN to proceed if documents missing

## CONTEXT BOUNDARIES:

- All previous steps should have created their outputs
- Handoff documents should be ready for experiment-cycle
- User has a working baseline and valid submission
- This is the transition point to experimentation

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 13: Project Setup Completion**

Let me verify all artifacts are complete and ready for the experiment-cycle workflow..."

### 2. Verify Documentation Artifacts

Check each required document exists and is non-empty:

**Primary Documents:**
| Document | Path | Status |
|----------|------|--------|
| Problem Statement | {challengeSpecFile} | {exists/missing} |
| EDA Report | {edaReportFile} | {exists/missing} |
| SoTA Synthesis | {sotaSynthesisFile} | {exists/missing} |
| Research Directions | {researchDirectionsFile} | {exists/missing} |
| Technical Spec | {technicalSpecFile} | {exists/missing} |

**Handoff Documents (for experiment-cycle):**
| Document | Path | Status |
|----------|------|--------|
| Current Understanding | {currentUnderstandingFile} | {exists/missing} |
| Current Architecture | {currentArchitectureFile} | {exists/missing} |
| Hypothesis Registry | {hypothesisRegistryFile} | {exists/missing} |

**IF ANY DOCUMENT IS MISSING:**
- Report which documents are missing
- Advise user to go back to the relevant step
- HALT - do not proceed

### 3. Verify Implementation Artifacts

Check implementation outputs:

**Code:**
- [ ] {srcFolder} exists with Python files
- [ ] train.py exists
- [ ] predict.py exists

**Models:**
- [ ] {modelsFolder}/baselines/ contains model checkpoint

**Submissions:**
- [ ] {submissionsFolder} contains baseline submission

**IF ANY ARTIFACT IS MISSING:**
- Report which artifacts are missing
- Advise user to return to step 11 (implementation)
- HALT - do not proceed

### 4. Quick Consistency Check

Verify cross-document consistency:

- [ ] Project name consistent across documents
- [ ] Metric name consistent
- [ ] Baseline performance recorded in current-architecture.md

### 5. Read Sidecar for Journey Summary

Read {sidecarFile} to understand the full journey:
- Steps completed
- Session notes (key decisions and findings)
- Validation reports

### 6. Generate Completion Summary

"**🎉 Project Setup Complete!**

---

## Summary

**Project:** {name}

**Documents Created:**
- ✅ problem-statement.md - Project requirements and constraints
- ✅ eda-report.md - Data analysis and insights
- ✅ sota-synthesis.md - State of the art techniques
- ✅ research-directions.md - Prioritized approaches
- ✅ technical-spec.md - Baseline implementation plan

**Handoff Documents (ready for experiment-cycle):**
- ✅ current-understanding.md - Problem, data, and research context
- ✅ current-architecture.md - Pipeline structure and extension points
- ✅ hypothesis-registry.md - Initial hypotheses to test

**Implementation:**
- ✅ Working baseline pipeline in `{srcFolder}/`
- ✅ Trained model in `{modelsFolder}/baselines/`
- ✅ Valid submission in `{submissionsFolder}/`

**Baseline Performance:**
- Validation {metric}: {value from current-architecture.md}

---

## Key Decisions Made

{Summarize major decisions from sidecar session notes}

---

## Research Directions Prioritized

1. **{Direction 1}** - {brief summary}
2. **{Direction 2}** - {brief summary}
3. **{Direction 3}** - {brief summary}

---

## What's Next: experiment-cycle Workflow

You now have everything needed to start the experiment-cycle workflow.

**To start experimenting:**
1. Open a new session
2. Run the experiment-cycle workflow
3. The workflow will read your handoff documents

**Handoff documents the experiment-cycle will use:**
- `current-understanding.md` - Context about the problem
- `current-architecture.md` - How to extend the code
- `hypothesis-registry.md` - What to test

**Your first hypothesis to test:**
{H-001 from hypothesis-registry.md}

---

## Workflow Statistics

- **Steps completed:** {count from sidecar}
- **Documents created:** 8
- **Lines of code:** {estimate}
- **Baseline established:** Yes

---

**Congratulations on completing project setup!**

You have a solid foundation for systematic experimentation. The baseline is working, the research directions are grounded, and the infrastructure is ready for plug-and-play experiments.

Good luck with the project! 🏆"

### 7. Update Sidecar to Complete

Update {sidecarFile}:
- Set status to 'COMPLETE'
- Set lastStep to 'step-13-complete'
- Update lastUpdated date
- Add final session note: "Project setup workflow complete. Ready for experiment-cycle."

### 8. Final State

The workflow is complete. No next step to load.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All documents verified present
- All implementation artifacts verified
- Comprehensive summary generated
- Handoff instructions clear
- Sidecar marked COMPLETE
- User has clear next steps

### ❌ SYSTEM FAILURE:

- Marking complete with missing documents
- Not verifying implementation artifacts
- Vague handoff instructions
- Not updating sidecar status
- Forgetting to celebrate the achievement

**Master Rule:** Verify everything is ready. Provide clear handoff. Celebrate the completion.
