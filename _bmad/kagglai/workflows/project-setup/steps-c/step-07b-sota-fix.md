---
name: 'step-07b-sota-fix'
description: 'Fix-only step for SoTA synthesis when review context was too large'

nextStepFile: './step-08-research-directions.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
sotaFile: '{experiments_folder}/docs/sota-synthesis.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
---

# Step 7b: SoTA Synthesis Fix-Only

## STEP GOAL:

To implement fixes identified in the review report (from step 07) in a fresh context. This step exists because the review step may have consumed too much context to effectively implement fixes.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate new research - only fix identified issues
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A FIXER, not a re-reviewer
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are implementing fixes from a previous review
- ✅ The review report is in the sidecar file
- ✅ Focus on fixing, not re-reviewing
- ✅ Verify each fix addresses the issue

### Step-Specific Rules:

- 🎯 Focus ONLY on issues from the review report
- 🚫 FORBIDDEN to do new research (that wastes context)
- 💬 Document each fix as you make it
- 🚪 This step gets the synthesis to an approvable state

## EXECUTION PROTOCOLS:

- 🎯 Read review report from sidecar file
- 💾 Fix issues in priority order (Critical → Major)
- 📖 Re-verify sources if fixing citation issues
- 🚫 FORBIDDEN to add new content beyond fixes

## CONTEXT BOUNDARIES:

- Review was completed in step 07 but fixes deferred
- Review report is saved in the sidecar file
- You have a fresh context to make fixes
- Only fix issues identified in the report

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 07b: SoTA Synthesis Fix-Only**

I'm a fresh Researcher instance here to implement the fixes identified in the review report.

Loading review report from sidecar..."

### 2. Load Review Report

Read {sidecarFile} and extract the review report from the "## Validation Reports" section.

**Extract:**
- Critical Issues list (must fix)
- Major Issues list (should fix)
- Minor Issues list (optional)

### 3. Read Current Synthesis

Read {sotaFile} to understand current state.

### 4. Fix Critical Issues

For each Critical issue:

1. Read the issue description
2. Locate the problem in the synthesis
3. If it's a citation issue, verify the correct information
4. Make the fix
5. Document: "Fixed: {issue} → {what was done}"

### 5. Fix Major Issues

For each Major issue:

1. Read the issue description
2. Locate the problem
3. Make the fix
4. Document: "Fixed: {issue} → {what was done}"

### 6. Handle Minor Issues

For Minor issues:
- Fix them if straightforward
- Note as "Deferred - can address later" if complex

### 7. Verify current-understanding.md Section 3

Check if {currentUnderstandingFile} Section 3 exists and is properly populated.

**IF Section 3 is missing or incomplete:**
- Populate it from the (now fixed) sota-synthesis.md:

```markdown
## 3. Model/Research

### 3.1 State of the Art Summary
- **Dominant Approaches:** {from synthesis}
- **Recent Advances:** {from synthesis}
- **Similar Competition Insights:** {from synthesis}

### 3.2 Recommended Starting Point
- **Primary Approach:** {from synthesis}
- **Rationale:** {from synthesis}
- **Alternatives:** {from synthesis}

### 3.3 Key Techniques to Consider
- {from synthesis}

### 3.4 Constraints Impact
- {from synthesis}
```

### 8. Generate Fix Report

Create a fix report:

```markdown
## Fix Report

**Original Review:** From sidecar, step-07 validation
**Fixer:** Researcher (Fix Instance)
**Date:** {date}

### Fixes Applied
1. **{Issue from review}**
   - Fix: {what was done}
   - Verified: yes

### Issues Deferred
1. **{Minor issue}**
   - Reason: {why deferred}
```

### 9. Update Sidecar

Update {sidecarFile}:
- Add 'step-07b-sota-fix' to stepsCompleted
- Set lastStep to 'step-07b-sota-fix'
- Update lastUpdated date
- Append fix report under the original review report
- Add session note: "SoTA synthesis fixes implemented"

### 10. Summary and Proceed

"**SoTA Synthesis Fixes Complete**

**Fixes applied:** {count}
**Issues deferred:** {count}

**Documents updated:**
- sota-synthesis.md (fixes applied)
- current-understanding.md (Section 3 verified)

**Next step:** Research Directions - Prioritize approaches with user

**[C]ontinue** to research directions"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Review report loaded from sidecar
- All Critical issues fixed
- All Major issues fixed
- Each fix documented
- current-understanding.md Section 3 verified
- Fix report generated

### ❌ SYSTEM FAILURE:

- Doing new research instead of fixing
- Missing issues from the review report
- Not documenting fixes
- Not verifying current-understanding.md

**Master Rule:** Fix what was found. Document what you fixed. Don't re-research.
