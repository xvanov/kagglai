---
name: 'step-03-discovery-review'
description: 'User reviews discovery findings and decides what to include/exclude'

nextStepFile: './step-04-structure-setup.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
---

# Step 3: Discovery Review

## STEP GOAL:

To have the user review discovery findings and explicitly decide what brownfield artifacts to include, exclude, or flag for special attention.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE FACILITATOR, user makes decisions
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You facilitate the review, user decides
- ✅ User knows their codebase better than you
- ✅ Some artifacts may be for different problems - user clarifies
- ✅ Document all decisions for downstream steps

### Step-Specific Rules:

- 🎯 Focus ONLY on user review and decisions
- 🚫 FORBIDDEN to make inclusion decisions without user
- 💬 Ask clarifying questions about unclear artifacts
- 📋 Document all decisions in sidecar

## MANDATORY SEQUENCE

### 1. Load Discovery Report

Load {sidecarFile} and read the Discovery Report section.

"**Let's review what I found in your brownfield codebase.**

I'll walk you through each category. For each artifact, tell me:
- **Include** - Use this in the project pickup
- **Exclude** - Skip this (wrong problem, outdated, etc.)
- **Unsure** - We'll discuss it"

### 2. Review Documentation

Present each documentation artifact:

"**Documentation Artifacts:**

| # | Type | Location | Quality | Include? |
|---|------|----------|---------|----------|
{rows with numbers}

For each, type the number and I/E/U (Include/Exclude/Unsure):
Example: `1I, 2E, 3U`"

Record decisions.

### 3. Review Data Pipeline

"**Data Pipeline Components:**

| # | Component | Location | Status | Include? |
|---|-----------|----------|--------|----------|
{rows}

Which components should we include?"

Record decisions.

### 4. Review Models

"**Model Artifacts:**

| # | Model | Location | Status | Include? |
|---|-------|----------|--------|----------|
{rows}

Which models are relevant to your current problem?"

Record decisions.

### 5. Review Experiments

"**Experiment History:**

| # | ID | Location | Result | Include? |
|---|-----|----------|--------|----------|
{rows}

Which experiments have learnings we should capture?"

Record decisions.

### 6. Review EDA

"**EDA Artifacts:**

| # | Notebook | Coverage | Include? |
|---|----------|----------|----------|
{rows}

Which EDA work is relevant?"

Record decisions.

### 7. Clarify Unsure Items

For any items marked Unsure:

"**Let's clarify the items you were unsure about:**

**{artifact_name}** at `{location}`
- What I found: {description}
- Quality: {rating}

Is this relevant to your current problem? What context can you provide?"

Resolve each Unsure to Include or Exclude.

### 8. Confirm Exclusions

"**You're excluding these artifacts:**

{list of excluded items with reasons}

**Confirming:** These will NOT be used in the project pickup. Any changes?"

### 9. Update Sidecar with Decisions

Add to {sidecarFile}:

```markdown
## Inclusion Decisions

**Reviewed:** {current_date}

### Included Artifacts
| Category | Artifact | Location | Notes |
|----------|----------|----------|-------|
{included items}

### Excluded Artifacts
| Category | Artifact | Location | Reason |
|----------|----------|----------|--------|
{excluded items}

### Key Decisions
- {decision 1}
- {decision 2}
```

Update `stepsCompleted` array.

### 10. Summary and Proceed

"**Review Complete**

**Including:** {X} artifacts across {Y} categories
**Excluding:** {Z} artifacts

**Next step:** Structure Setup - I'll create the BMDS folder structure and organize the included artifacts.

**[C]ontinue** to Structure Setup"

Load {nextStepFile} when user confirms.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All artifacts reviewed with user
- Clear Include/Exclude decisions recorded
- Unsure items resolved
- Decisions documented in sidecar
- User confirms exclusions

### ❌ SYSTEM FAILURE:

- Making inclusion decisions without user
- Skipping artifact categories
- Not resolving Unsure items
- Not documenting decisions

**Master Rule:** User decides what's relevant. Document all decisions.
