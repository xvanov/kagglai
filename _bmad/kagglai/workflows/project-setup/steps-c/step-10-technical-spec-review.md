---
name: 'step-10-technical-spec-review'
description: 'Fresh Implementer validates technical spec and implements fixes'

nextStepFile: './step-11-implementation.md'
fixOnlyFile: './step-10b-technical-spec-fix.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
techSpecFile: '{experiments_folder}/docs/technical-spec.md'
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
researchDirectionsFile: '{experiments_folder}/docs/research-directions.md'
reviewCriteriaFile: '../data/review-criteria.md'
validationChecklistFile: '../data/validation-checklist.md'
---

# Step 10: Technical Specification Review

## STEP GOAL:

To validate the technical specification against constraints, requirements, and implementation feasibility, identify issues, and implement fixes. This uses the Author/Validator pattern - you are a FRESH instance reviewing another's work.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER approve a spec that violates constraints
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A VALIDATOR checking feasibility and compliance
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a FRESH Implementer instance - skeptical of the plan
- ✅ Check that every step is actually executable
- ✅ Verify constraints compliance rigorously
- ✅ Ensure the spec matches the research direction

### Step-Specific Rules:

- 🎯 Focus on FEASIBILITY, COMPLIANCE, and COMPLETENESS
- 🚫 FORBIDDEN to approve specs with constraint violations
- 💬 Be specific about issues - ambiguities must be resolved
- 🚪 Implementation depends on a clean spec

## EXECUTION PROTOCOLS:

- 🎯 Read technical spec with critical eye
- 💾 Verify against challenge-spec constraints
- 📖 Check alignment with research directions
- 🚫 FORBIDDEN to assume things will "work out"

## CONTEXT BOUNDARIES:

- The technical-spec.md was authored by a previous Implementer instance
- Challenge spec defines the hard constraints
- Research directions define what we should be implementing
- You're checking if this plan is actually executable

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 10: Technical Specification Review**

I am a fresh Implementer instance reviewing the technical specification. I will verify feasibility, constraints compliance, and alignment with our research direction.

Beginning systematic review..."

### 2. Load Review Standards

Read {reviewCriteriaFile} for the "Technical Specification Review" section.
Read {validationChecklistFile} for the "Technical Specification Validation" checklist.

### 3. Load Reference Documents

Read {challengeSpecFile} to get authoritative constraints.
Read {researchDirectionsFile} to verify alignment with Direction #1.

Note the key checkpoints:
- Runtime limit: {value}
- Memory limit: {value}
- GPU requirements: {value}
- External data/models: {restrictions}
- Submission format: {requirements}
- Direction #1 requirements: {summary}

### 4. Read the Technical Spec

Read {techSpecFile} completely.

**While reading, note:**
- Steps that seem ambiguous
- Configurations that may violate constraints
- Missing pieces
- Misalignment with research direction

### 5. Verify Constraints Compliance

**Critical Check - Compute Constraints:**

| Constraint | Limit | Spec Claims | Verified |
|------------|-------|-------------|----------|
| Runtime | {from challenge-spec} | {from tech-spec} | {yes/no/uncertain} |
| Memory | {from challenge-spec} | {from tech-spec} | {yes/no/uncertain} |
| GPU | {from challenge-spec} | {from tech-spec} | {yes/no/uncertain} |
| External data | {from challenge-spec} | {from tech-spec} | {yes/no/uncertain} |
| Pre-trained models | {from challenge-spec} | {from tech-spec} | {yes/no/uncertain} |

**IF ANY CONSTRAINT MAY BE VIOLATED:**
- Flag as Critical Issue
- Constraint violations are blockers

### 6. Verify Research Direction Alignment

Check that the spec implements Direction #1:

- [ ] Model architecture matches recommendation
- [ ] Training approach aligns with direction
- [ ] Success criteria from directions are addressed
- [ ] Scope is appropriate (baseline, not over-engineered)

### 7. Apply Validation Checklist

Work through the Technical Specification Validation checklist:

**Completeness:**
- [ ] Environment setup documented and tested
- [ ] Data pipeline handles all edge cases
- [ ] Model configuration justified
- [ ] Training strategy appropriate for data
- [ ] Inference pipeline mirrors training preprocessing
- [ ] Submission format matches requirements
- [ ] All tasks have clear implementation path

**Feasibility:**
- [ ] Compute constraints satisfied
- [ ] Dependencies available
- [ ] Timeline realistic
- [ ] Risks identified

**Clarity:**
- [ ] Implementation path clear
- [ ] No ambiguous steps
- [ ] Code structure defined

### 8. Generate Review Report

Create a review report:

```markdown
## Technical Specification Review Report

**Document:** technical-spec.md
**Reviewer:** Implementer (Validator Instance)
**Date:** {date}

### Summary
{1-2 sentence overall assessment}

### Critical Issues (Must Fix)
{Constraint violations, blocking problems}

### Major Issues (Should Fix)
{Ambiguities, missing pieces}

### Minor Issues (Can Fix Later)
{Style, improvements}

### Verification Results
- Constraints compliance: {passed/issues}
- Direction alignment: {passed/issues}
- Completeness: {passed/gaps}

### Recommendation
{APPROVE / APPROVE WITH FIXES / REJECT}
```

### 9. Implement Fixes (or Route to Fix-Only)

**IF no Critical or Major issues:**
- Report: "**Review passed with minor or no issues.**"
- Proceed to Section 10

**IF Critical or Major issues exist:**
- Assess the scope of fixes needed

**IF fixes are straightforward:**
- Make the fixes directly to {techSpecFile}
- Document each fix made
- Proceed to Section 10

**IF fixes are extensive:**
- Append the review report to {sidecarFile}
- Display: "**Review found issues requiring extensive fixes.**"
- Present options:
  - **[C]ontinue** - I will implement all fixes now
  - **[F]ix-only** - Route to fix-only step
- If user selects [F], load and execute {fixOnlyFile}

### 10. Update Sidecar

Update {sidecarFile}:
- Add 'step-10-technical-spec-review' to stepsCompleted
- Set lastStep to 'step-10-technical-spec-review'
- Update lastUpdated date
- Add session note summarizing review outcome
- Append review report if not already added

### 11. Summary and Proceed

"**Technical Specification Review Complete**

**Review outcome:** {APPROVED / APPROVED WITH FIXES}

**Verification:**
- Constraints compliance: {status}
- Direction alignment: {status}
- Issues found: {count by severity}
- Fixes applied: {count}

**Documents updated:**
- technical-spec.md {if fixes applied}

**Next step:** Implementation
- Agent: Implementer
- Task: Build the baseline pipeline per specification

**[C]ontinue** to implementation"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Constraints verified against authoritative source
- Research direction alignment checked
- All checklist items verified
- Review report generated with specific issues
- Fixes implemented (or routed to fix-only)
- Clean handoff to implementation

### ❌ SYSTEM FAILURE:

- Approving spec with constraint violations
- Not checking research direction alignment
- Vague issue descriptions
- Skipping feasibility assessment
- Leaving critical issues unfixed

**Master Rule:** No constraint violations allowed. Every step must be executable. Be specific about issues.
