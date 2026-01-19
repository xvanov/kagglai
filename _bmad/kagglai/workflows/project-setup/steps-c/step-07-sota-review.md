---
name: 'step-07-sota-review'
description: 'Fresh Researcher validates SoTA synthesis and implements fixes'

nextStepFile: './step-08-research-directions.md'
fixOnlyFile: './step-07b-sota-fix.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
sotaFile: '{experiments_folder}/docs/sota-synthesis.md'
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
reviewCriteriaFile: '../data/review-criteria.md'
validationChecklistFile: '../data/validation-checklist.md'
papersFolder: '{experiments_folder}/challenge-inputs/papers'
---

# Step 7: SoTA Synthesis Review

## STEP GOAL:

To validate the state of the art synthesis against sources and quality criteria, identify issues, implement fixes, and populate Section 3 of current-understanding.md. This uses the Author/Validator pattern - you are a FRESH instance reviewing another's work.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER assume citations are accurate - verify them
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A VALIDATOR, skeptical of unsourced claims
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are a FRESH Researcher instance - no memory of authoring
- ✅ Check that cited sources support the claims made
- ✅ Verify benchmark numbers match actual sources
- ✅ Assess whether recommendations fit this specific competition

### Step-Specific Rules:

- 🎯 Focus on VALIDATION of sources and applicability
- 🚫 FORBIDDEN to approve without verifying key claims
- 💬 Be specific about citation errors or unsupported claims
- 🚪 Must produce a review report regardless of outcome

## EXECUTION PROTOCOLS:

- 🎯 Read SoTA synthesis with skeptical eye
- 💾 Spot-check citations and benchmark numbers
- 📖 Verify recommendations match competition constraints
- 🚫 FORBIDDEN to just skim - verify key claims

## CONTEXT BOUNDARIES:

- The sota-synthesis.md was authored by a previous Researcher instance
- You can spot-check citations via web search
- Challenge spec defines the constraints for applicability
- EDA report defines data characteristics for relevance assessment

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 07: SoTA Synthesis Review**

I am a fresh Researcher instance reviewing the state of the art synthesis. I will verify sources, check for unsupported claims, and assess applicability to this competition.

Beginning systematic review..."

### 2. Load Review Standards

Read {reviewCriteriaFile} for the "SoTA Synthesis Review" section.
Read {validationChecklistFile} for the "SoTA Synthesis Validation" checklist.

### 3. Load Context Documents

Read {challengeSpecFile} to understand constraints.
Read {edaReportFile} to understand data characteristics.

### 4. Read the SoTA Synthesis

Read {sotaFile} completely.

**While reading, note:**
- Claims that seem unsupported
- Benchmark numbers that should be verified
- Recommendations that may not fit constraints
- Missing coverage areas

### 5. Verify Key Claims

**Source Accuracy Check (spot-check 3-5 key claims):**
- Select important claims with citations
- Verify the claim matches what the source says
- Check that benchmark numbers are accurate

**Coverage Check:**
- [ ] Major architecture families covered
- [ ] Recent advances included (last 2 years)
- [ ] Similar competitions analyzed

**Relevance Check:**
- [ ] Recommendations consider competition constraints
- [ ] Data characteristics matched to approaches
- [ ] Trade-offs acknowledged

### 6. Apply Validation Checklist

Work through the SoTA Synthesis Validation checklist:

**Completeness:**
- [ ] All major architecture families covered
- [ ] Recent advances included (last 2 years)
- [ ] Similar competitions analyzed
- [ ] Applicability to this competition assessed
- [ ] All sources properly cited

**Accuracy:**
- [ ] Paper summaries accurate
- [ ] Benchmark scores verified
- [ ] Claims have citations
- [ ] Recommendations grounded in evidence

**Relevance:**
- [ ] Focus on applicable techniques
- [ ] Competition constraints considered
- [ ] Data characteristics matched to approaches

### 7. Generate Review Report

Create a review report:

```markdown
## SoTA Synthesis Review Report

**Document:** sota-synthesis.md
**Reviewer:** Researcher (Validator Instance)
**Date:** {date}

### Summary
{1-2 sentence overall assessment}

### Critical Issues (Must Fix)
{Unsourced major claims, wrong citations}

### Major Issues (Should Fix)
{Missing coverage, questionable recommendations}

### Minor Issues (Can Fix Later)
{Style, additional sources}

### Verification Results
- Source check: {N/M claims verified}
- Coverage check: {passed/gaps noted}
- Relevance check: {passed/concerns noted}

### Recommendation
{APPROVE / APPROVE WITH FIXES / REJECT}
```

### 8. Implement Fixes (or Route to Fix-Only)

**IF no Critical or Major issues:**
- Report: "**Review passed with minor or no issues.**"
- Proceed to Section 9

**IF Critical or Major issues exist:**
- Assess the scope of fixes needed

**IF fixes are straightforward:**
- Make the fixes directly to {sotaFile}
- Document each fix made
- Proceed to Section 9

**IF fixes are extensive:**
- Append the review report to {sidecarFile}
- Display: "**Review found issues requiring extensive fixes.**"
- Present options:
  - **[C]ontinue** - I will implement all fixes now
  - **[F]ix-only** - Route to fix-only step
- If user selects [F], load and execute {fixOnlyFile}

### 9. Update current-understanding.md Section 3

Update {currentUnderstandingFile} Section 3 (Model/Research):

```markdown
## 3. Model/Research

### 3.1 State of the Art Summary
- **Dominant Approaches:** {top approaches for this problem}
- **Recent Advances:** {key developments last 2 years}
- **Similar Competition Insights:** {what worked before}

### 3.2 Recommended Starting Point
- **Primary Approach:** {most promising approach}
- **Rationale:** {why this fits the data and constraints}
- **Alternatives:** {backup approaches}

### 3.3 Key Techniques to Consider
- {Technique 1} - {brief rationale}
- {Technique 2} - {brief rationale}
- {Technique 3} - {brief rationale}

### 3.4 Constraints Impact
- **Compute Limits:** {how they affect approach}
- **External Data Rules:** {implications}
- **Other Constraints:** {considerations}
```

### 10. Update Sidecar

Update {sidecarFile}:
- Add 'step-07-sota-review' to stepsCompleted
- Set lastStep to 'step-07-sota-review'
- Update lastUpdated date
- Add session note summarizing review outcome
- Append review report if not already added

### 11. Summary and Proceed

"**SoTA Synthesis Review Complete**

**Review outcome:** {APPROVED / APPROVED WITH FIXES}

**Verification:**
- Sources checked: {count}
- Issues found: {count by severity}
- Fixes applied: {count}

**Documents updated:**
- sota-synthesis.md {if fixes applied}
- current-understanding.md (Section 3 populated)

**Next step:** Research Directions - Prioritize approaches with user

**[C]ontinue** to research directions"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Key claims verified against sources
- Coverage and relevance assessed
- Review report generated with specific issues
- Fixes implemented (or routed to fix-only)
- current-understanding.md Section 3 populated
- Clear handoff to research directions

### ❌ SYSTEM FAILURE:

- Approving without verifying any sources
- Vague issue descriptions
- Not checking against competition constraints
- Skipping the validation checklist
- Not populating current-understanding.md
- Leaving critical issues unfixed

**Master Rule:** Verify sources. Check applicability. Be specific about issues.
