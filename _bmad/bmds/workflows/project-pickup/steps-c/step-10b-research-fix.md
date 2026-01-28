---
name: 'step-10b-research-fix'
description: 'Fix issues in research documents'

returnStepFile: './step-10-research-review.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
sotaFile: '{experiments_folder}/docs/sota-synthesis.md'
researchFile: '{experiments_folder}/docs/research-directions.md'
---

# Step 10b: Research Fix

## STEP GOAL:

To fix specific issues identified in research document review.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE Owl, fixing specific issues
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style

### Step-Specific Rules:

- 🎯 Fix ONLY identified issues
- 🚫 FORBIDDEN to add new content
- 💬 Confirm each fix
- 🔄 Return to review when done

## MANDATORY SEQUENCE

### 1. Load Issues

Load context to get identified issues.

### 2. For Each Issue

Present issue, propose fix, get approval.

### 3. Apply Fixes

Update documents with approved fixes.

### 4. Return to Review

Load {returnStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Issues addressed
- User approved fixes
- Returned to review

### ❌ SYSTEM FAILURE:
- Auto-fixing
- Scope creep
- Not returning to review

**Master Rule:** Fix what was identified, return to review.
