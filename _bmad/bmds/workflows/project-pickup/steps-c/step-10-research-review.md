---
name: 'step-10-research-review'
description: 'Review research documents and update current-understanding section 3'

nextStepFile: './step-11-architecture-doc.md'
fixStepFile: './step-10b-research-fix.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
sotaFile: '{experiments_folder}/docs/sota-synthesis.md'
researchFile: '{experiments_folder}/docs/research-directions.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
reviewCriteriaFile: '../data/review-criteria.md'
---

# Step 10: Research Review

## STEP GOAL:

To validate research documents and update current-understanding.md section 3 (Model).

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE A FRESH VALIDATOR
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ Fresh reviewer perspective
- ✅ Validate research quality and completeness
- ✅ Ensure directions are actionable
- ✅ Update current-understanding section 3

### Step-Specific Rules:

- 🎯 Focus on validation and current-understanding update
- 🚫 FORBIDDEN to auto-fix
- 💬 Present findings clearly
- 📋 Route to fix if needed

## MANDATORY SEQUENCE

### 1. Load Documents

Load {sotaFile} and {researchFile}.
Load {reviewCriteriaFile}.

### 2. Validate SoTA Synthesis

Check:
- [ ] Problem type clearly stated
- [ ] SoTA approaches identified
- [ ] Brownfield approaches documented
- [ ] Gaps identified
- [ ] Sources cited

Report findings.

### 3. Validate Research Directions

Check:
- [ ] Priorities clearly ranked
- [ ] Each direction has evidence
- [ ] Effort estimates provided
- [ ] First experiments suggested
- [ ] Not-recommended list included

Report findings.

### 4. User Decision

If issues found:
"**[F]ix** - Route to fix step
**[A]ccept** - Accept as-is
**[C]ontinue** - Continue"

### 5. Update Current Understanding Section 3

```markdown
## 3. Model

### 3.1 Architecture Landscape
| Family | Strengths | Weaknesses | SoTA Reference |
|--------|-----------|------------|----------------|
{from sota-synthesis}

### 3.2 Current Best Approach
- **Architecture:** {from brownfield or recommended}
- **Why chosen:** {rationale}
- **Performance:** {metric} = {value}

### 3.3 Known Failure Modes
| Failure Mode | Frequency | Potential Fix | Status |
|--------------|-----------|---------------|--------|
{from brownfield learnings}
```

Add to Change Log.

### 6. Update Sidecar and Proceed

"**Research Review Complete**

- SoTA synthesis: {VALIDATED/ACCEPTED}
- Research directions: {VALIDATED/ACCEPTED}
- Current understanding: Section 3 updated

**[C]ontinue** to Architecture Documentation"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Both documents validated
- Issues reported clearly
- Current understanding section 3 updated
- User confirmed or routed to fix

### ❌ SYSTEM FAILURE:
- Auto-fixing
- Skipping validation
- Not updating current-understanding

**Master Rule:** Validate, report, update current-understanding, let user decide.
