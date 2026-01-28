---
name: 'step-15-complete'
description: 'Verify all artifacts and hand off to experiment-cycle'

sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
docsFolder: '{experiments_folder}/docs'
validationChecklistFile: '../data/validation-checklist.md'
---

# Step 15: Completion & Handoff

## STEP GOAL:

To verify all artifacts are complete and ready for experiment-cycle, then complete the project pickup workflow.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE THE ORCHESTRATOR, completing the workflow
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Step-Specific Rules:

- 🎯 Focus on verification and completion
- 🚫 FORBIDDEN to skip final checklist
- 💬 Provide clear handoff instructions
- 📄 Mark workflow complete

## MANDATORY SEQUENCE

### 1. Final Verification Checklist

Load {validationChecklistFile} and verify:

"**Final Verification**

Checking all artifacts against project-init end-state..."

**Documents:**
- [ ] problem-statement.md - {complete}
- [ ] eda-report.md - {complete}
- [ ] sota-synthesis.md - {complete}
- [ ] research-directions.md - {complete}
- [ ] technical-spec.md - {complete}
- [ ] current-understanding.md - {all sections complete}
- [ ] current-architecture.md - {complete}
- [ ] hypothesis-registry.md - {created with initial hypotheses}

**Implementation:**
- [ ] src/ - {organized}
- [ ] models/baselines/ - {has baseline}
- [ ] submissions/ - {has valid submission}
- [ ] Environment - {documented}

**Readiness for experiment-cycle:**
- [ ] All handoff docs complete
- [ ] Baseline performance documented
- [ ] Initial hypotheses registered
- [ ] Extension points identified

### 2. Report Verification Results

"**Verification Results:**

**PASSED:** {count}
**FAILED:** {count} - {list if any}
**WARNINGS:** {count} - {list if any}

{If all passed}
**All artifacts verified. Ready for experiment-cycle.**

{If failures}
**Some items need attention:**
{list failures and recommended actions}"

### 3. Generate Completion Summary

"**Project Pickup Complete!**

---

**Project:** {project_name}
**Brownfield Source:** {brownfield_path}
**Duration:** {start_date} to {end_date}

---

**Documents Created:**
1. problem-statement.md - Problem definition
2. eda-report.md - Data analysis and insights
3. sota-synthesis.md - State of the art review
4. research-directions.md - Prioritized approaches
5. technical-spec.md - Architecture specification
6. current-understanding.md - Living knowledge document
7. current-architecture.md - Production system spec
8. hypothesis-registry.md - Experiment tracker

---

**Baseline Performance:**
- Metric: {name} = {value}
- Model: {architecture}
- Checkpoint: {path}

---

**Top Hypotheses to Test:**
1. {H-001}: {brief description}
2. {H-002}: {brief description}
3. {H-003}: {brief description}

---

**Brownfield Value Captured:**
- {X} models analyzed
- {Y} experiments documented
- {Z} learnings preserved

---

**Next Steps:**
Run the **experiment-cycle** workflow to begin hypothesis-driven experimentation.

Command: `/bmad:bmds:workflows:experiment-cycle`

---"

### 4. Update Sidecar to Complete

Update {sidecarFile}:

```yaml
status: COMPLETE
completedDate: {date}
stepsCompleted: ['step-01-init', ..., 'step-15-complete']
```

Add final session note.

### 5. Handoff Instructions

"**Ready for Experiment-Cycle**

Your project is now set up with:
- Complete documentation suite
- Baseline model and performance
- Hypothesis registry with {X} hypotheses
- All brownfield learnings captured

**To begin experimentation:**
1. Review hypothesis-registry.md
2. Start experiment-cycle workflow
3. Test H-001 first (highest priority)

**Key files:**
- `{docsFolder}/current-understanding.md` - Updated as you learn
- `{docsFolder}/current-architecture.md` - Updated when architecture changes
- `{docsFolder}/hypothesis-registry.md` - Track all experiments

**Good luck with your experiments!**"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- All artifacts verified
- Completion summary generated
- Sidecar marked complete
- Clear handoff instructions
- User knows next steps

### ❌ SYSTEM FAILURE:
- Skipping verification
- Incomplete documentation
- Not marking complete
- No handoff instructions

**Master Rule:** Verify everything, summarize, hand off cleanly.
