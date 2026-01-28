---
name: 'step-e-03-apply-edit'
description: 'Apply edits to the selected document'

sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
---

# Step E-03: Apply Edit

## STEP GOAL:

To collaborate with the user to apply edits to their selected document, ensuring edits are clear, well-documented, and don't introduce inconsistencies.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER make edits without user input and approval
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: This is a collaborative editing session
- 📋 YOU ARE A COLLABORATIVE EDITOR
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are helping the user edit their document
- ✅ User provides the changes, you help implement them cleanly
- ✅ Ensure edits maintain document structure
- ✅ Flag any consistency concerns

### Step-Specific Rules:

- 🎯 Focus on COLLABORATIVE EDITING
- 🚫 FORBIDDEN to make significant changes without approval
- 💬 Discuss proposed changes before implementing
- 🚪 Document all edits made

## EXECUTION PROTOCOLS:

- 🎯 Load the selected document
- 💾 Understand what the user wants to change
- 📖 Make edits collaboratively
- 🚫 FORBIDDEN to change document structure without approval

## CONTEXT BOUNDARIES:

- User has selected a document to edit
- Document path should be passed from step E-02
- This is a collaborative session - user directs the changes
- You help implement changes cleanly and consistently

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Announce Edit Session

"**Edit Session: {Document Name}**

I'll load the current document so we can make edits together."

### 2. Load Current Document

Read the selected document completely.

Present a summary:
"**Current Document Structure:**

{List major sections}

**What would you like to edit?**

Options:
- Specify a section to modify
- Describe the change you want to make
- Show me a specific section to update"

### 3. Understand User's Edit Request

Wait for user to describe what they want to change.

**Ask clarifying questions if needed:**
- "Which section does this affect?"
- "What should the new content say?"
- "Are you replacing existing content or adding to it?"

### 4. Propose the Edit

Before making changes, show what you plan to do:

"**Proposed Edit:**

**Section:** {section name}
**Change type:** {Add/Replace/Remove}

**Before:**
```
{current content}
```

**After:**
```
{proposed new content}
```

**Approve this edit?**
- **[Y]es** - Apply this edit
- **[N]o** - Revise the proposal
- **[S]kip** - Cancel this edit"

### 5. Apply Approved Edits

**IF approved:**
- Apply the edit to the document
- Confirm: "Edit applied to {document name}"

**IF not approved:**
- Ask for clarification
- Revise proposal
- Return to step 4

**IF skipped:**
- Confirm: "Edit cancelled"
- Ask: "Would you like to make a different edit?"

### 6. Check for Additional Edits

"**Edit applied.**

Would you like to make additional edits to this document?
- **[Y]es** - Continue editing
- **[N]o** - Finish editing session"

**IF yes:** Return to step 3
**IF no:** Continue to step 7

### 7. Consistency Check

If edits were made to core documents (problem-statement, EDA, SoTA, research-directions, technical-spec):

"**Consistency Check:**

Your edit to **{document name}** may affect other documents:
{List potentially affected documents based on dependencies}

Would you like me to:
1. **Note** the potential inconsistencies (add TODO to affected docs)
2. **Review** the affected documents now
3. **Skip** the consistency check

The choice is yours - inconsistencies can be addressed later during experimentation."

### 8. Update Sidecar

Add entry to sidecar noting the edit:

```markdown
### Edit Session - {date}
- **Document:** {document name}
- **Changes:** {summary of edits}
- **User:** {edit mode}
```

### 9. Finish Edit Session

"**Edit Session Complete**

**Document edited:** {document name}
**Edits made:** {count}
**Consistency notes:** {any warnings}

The document has been updated. You can:
- Run the workflow in **[V]alidate** mode to check all documents
- Start a new **[E]dit** session for another document
- Return to **[C]reate** mode to continue/restart the workflow"

---

## HANDLING SPECIAL CASES

### Structural Changes
If user wants to change document structure significantly:
- Warn about breaking consistency with templates
- Suggest adding to existing sections instead
- If they insist, help them restructure clearly

### Conflicting Information
If new content conflicts with existing:
- Point out the conflict
- Ask user to clarify intent
- Update all related mentions

### Missing Information
If user wants to add info that should have been in original:
- Help them add it to the right section
- Suggest checking if it affects other documents

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Document loaded and understood
- User's intent clearly captured
- Edits proposed before applying
- All edits approved by user
- Consistency concerns flagged
- Sidecar updated with edit log

### ❌ SYSTEM FAILURE:

- Making edits without approval
- Changing structure without warning
- Not flagging consistency issues
- Losing user's changes
- Not documenting edits

**Master Rule:** Collaborate. Propose before applying. Document all changes.
