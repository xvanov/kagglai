---
name: 'step-10b-technical-spec-fix'
description: 'Fix-only step for technical spec when review context was too large'

nextStepFile: './step-11-implementation.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
techSpecFile: '{experiments_folder}/docs/technical-spec.md'
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
---

# Step 10b: Technical Specification Fix-Only

## STEP GOAL:

To implement fixes identified in the review report (from step 10) in a fresh context. This step exists because the review step may have consumed too much context to effectively implement fixes.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate new specifications - only fix identified issues
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FIXER, not a re-reviewer
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are implementing fixes from a previous review
- ✅ The review report is in the sidecar file
- ✅ Focus on fixing, not re-reviewing
- ✅ Constraint fixes are highest priority

### Step-Specific Rules:

- 🎯 Focus ONLY on issues from the review report
- 🚫 FORBIDDEN to do a full re-review
- 💬 Document each fix as you make it
- 🚪 Implementation cannot proceed with constraint violations

## EXECUTION PROTOCOLS:

- 🎯 Read review report from sidecar file
- 💾 Fix issues in priority order (Critical → Major)
- 📖 For constraint issues, verify against challenge-spec
- 🚫 FORBIDDEN to add new content beyond fixes

## CONTEXT BOUNDARIES:

- Review was completed in step 10 but fixes deferred
- Review report is saved in the sidecar file
- You have a fresh context to make fixes
- Only fix issues identified in the report

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 10b: Technical Specification Fix-Only**

I'm a fresh Implementer instance here to implement the fixes identified in the review report.

Loading review report from sidecar..."

### 2. Load Review Report

Read {sidecarFile} and extract the review report from the "## Validation Reports" section.

**Extract:**
- Critical Issues (must fix - especially constraint violations)
- Major Issues (should fix)
- Minor Issues (optional)

### 3. Load Authoritative Constraints

If any issues involve constraints, read {challengeSpecFile} Section 5 (Constraints) to get exact values.

### 4. Read Current Spec

Read {techSpecFile} to understand current state.

### 5. Fix Critical Issues

For each Critical issue (especially constraint violations):

1. Read the issue description
2. Locate the problem in the spec
3. If constraint-related, verify the correct limit
4. Make the fix
5. Document: "Fixed: {issue} → {what was done}"

**Constraint Fix Examples:**
- "Fixed: Runtime over limit → Reduced epochs from 100 to 20, added early stopping"
- "Fixed: External data violation → Removed pre-trained model, using from-scratch training"

### 6. Fix Major Issues

For each Major issue:

1. Read the issue description
2. Locate the problem
3. Make the fix
4. Document: "Fixed: {issue} → {what was done}"

### 7. Handle Minor Issues

For Minor issues:
- Fix them if straightforward
- Note as "Deferred" if complex

### 8. Generate Fix Report

Create a fix report:

```markdown
## Fix Report

**Original Review:** From sidecar, step-10 validation
**Fixer:** Implementer (Fix Instance)
**Date:** {date}

### Fixes Applied
1. **{Issue from review}**
   - Fix: {what was done}
   - Verified: yes

### Constraints Verification (Post-Fix)
| Constraint | Limit | Fixed Value | Compliant |
|------------|-------|-------------|-----------|
| Runtime | {limit} | {new value} | yes |
| Memory | {limit} | {new value} | yes |

### Issues Deferred
1. **{Minor issue}**
   - Reason: {why deferred}
```

### 9. Update Sidecar

Update {sidecarFile}:
- Add 'step-10b-technical-spec-fix' to stepsCompleted
- Set lastStep to 'step-10b-technical-spec-fix'
- Update lastUpdated date
- Append fix report under the original review report
- Add session note: "Technical spec fixes implemented, constraints verified"

### 10. Summary and Proceed

"**Technical Specification Fixes Complete**

**Fixes applied:** {count}
**Constraint violations resolved:** {count}
**Issues deferred:** {count}

**Documents updated:**
- technical-spec.md (fixes applied)

**Next step:** Implementation
- Agent: Implementer
- Task: Build the baseline pipeline per specification

**[C]ontinue** to implementation"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Review report loaded from sidecar
- All Critical issues fixed (especially constraints)
- All Major issues fixed
- Each fix documented
- Post-fix constraint verification performed
- Fix report generated

### ❌ SYSTEM FAILURE:

- Doing a new review instead of fixing
- Missing constraint violations from the report
- Not documenting fixes
- Not verifying constraints post-fix

**Master Rule:** Fix what was found. Constraint violations must be resolved. Document everything.
