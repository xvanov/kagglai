---
name: 'step-e-01-assess'
description: 'Assess existing project pickup and determine edit scope'

sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
docsFolder: '{experiments_folder}/docs'
conversionStep: '../steps-c/step-02-discovery.md'
---

# Edit Mode: Assess & Edit

## STEP GOAL:

To assess an existing project pickup and allow editing of specific documents or sections.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE THE EDITOR, helping modify existing documents
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Step-Specific Rules:

- 🎯 Focus on targeted edits
- 🚫 FORBIDDEN to recreate from scratch (use create mode)
- 💬 Understand what user wants to change
- 📄 Make surgical edits

## MANDATORY SEQUENCE

### 1. Verify Project Pickup Exists

Check for {sidecarFile}:

**IF not found:**
"**No project pickup found.**

Would you like to:
**[C]reate** - Run project pickup create mode
**[E]xit** - Exit edit mode"

Route accordingly.

**IF found but incomplete:**
"**Project pickup is in progress (not complete).**

Would you like to:
**[C]ontinue** - Continue the in-progress workflow
**[E]dit anyway** - Edit existing documents"

### 2. Show Current State

"**Current Project Pickup State:**

**Project:** {project_name}
**Status:** {status}
**Last updated:** {date}

**Documents:**
1. problem-statement.md - {exists/missing}
2. eda-report.md - {exists/missing}
3. sota-synthesis.md - {exists/missing}
4. research-directions.md - {exists/missing}
5. technical-spec.md - {exists/missing}
6. current-understanding.md - {exists/missing}
7. current-architecture.md - {exists/missing}
8. hypothesis-registry.md - {exists/missing}

**What would you like to edit?**
Enter document number or name:"

### 3. Load Selected Document

Load the selected document.

"**Editing: {document_name}**

Current content:
{show document or table of contents}

What would you like to change?
- Describe the edit you want to make
- Or specify section to modify"

### 4. Make Edits

For each edit request:
- Show current content
- Propose updated content
- Get user approval
- Apply edit

"**Proposed Change:**

**Current:**
{current text}

**Proposed:**
{new text}

Accept? [Y]es / [M]odify / [R]eject"

### 5. Save and Offer More

Save edits to document.

"**Edit saved.**

Would you like to:
**[E]dit more** - Edit another section/document
**[V]alidate** - Run validation on changes
**[D]one** - Exit edit mode"

### 6. Update Sidecar

Note edits in sidecar session notes.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Project pickup exists
- User-requested edits made
- Changes confirmed before saving
- Session documented

### ❌ SYSTEM FAILURE:
- Editing non-existent project
- Making changes without confirmation
- Not documenting edits

**Master Rule:** Targeted edits with user confirmation.
