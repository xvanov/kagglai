---
name: 'step-02-challenge-spec'
description: 'Data Analyst authors the challenge specification from input documents'

nextStepFile: './step-03-challenge-spec-review.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
templateFile: '../templates/challenge-spec-template.md'
outputFile: '{experiments_folder}/docs/challenge-spec.md'

# Input files to read
descriptionFile: '{experiments_folder}/challenge-inputs/description.md'
rulesFile: '{experiments_folder}/challenge-inputs/rules.md'
dataAccessFile: '{experiments_folder}/challenge-inputs/data-access.md'
submissionFile: '{experiments_folder}/challenge-inputs/submission-format.md'
---

# Step 2: Author Challenge Specification

## STEP GOAL:

To systematically extract and synthesize all competition requirements from input documents into a comprehensive, structured challenge specification that serves as the single source of truth for the entire project.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without reading all input sources first
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A SYSTEMATIC EXTRACTOR, not a content inventor
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the Data Analyst agent creating a critical reference document
- ✅ Every fact must be traceable to a source document
- ✅ Ambiguity should be flagged, not resolved by assumption
- ✅ Missing information should be explicitly noted as missing

### Step-Specific Rules:

- 🎯 Focus ONLY on extraction and synthesis - do not analyze data yet
- 🚫 FORBIDDEN to make assumptions about unspecified details
- 💬 Quote source documents when capturing exact requirements
- 🚪 This document becomes the foundation for all subsequent work

## EXECUTION PROTOCOLS:

- 🎯 Read ALL input documents before starting to write
- 💾 Create challenge-spec.md using the template structure
- 📖 Cross-reference between documents to catch inconsistencies
- 🚫 FORBIDDEN to fill in placeholders with assumptions

## CONTEXT BOUNDARIES:

- Input documents have been verified present in step 01
- You have access to: description.md, rules.md, data-access.md, submission-format.md
- The template provides the structure - you fill it with extracted facts
- This spec will be reviewed by a fresh validator instance

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 02: Challenge Specification Authoring**

I will now systematically extract all competition requirements from your input documents and synthesize them into a structured challenge specification.

Reading input documents..."

### 2. Read All Input Documents

Read each file completely before proceeding:

1. {descriptionFile} - Competition overview and problem statement
2. {rulesFile} - Rules, scoring, evaluation criteria
3. {dataAccessFile} - Data access instructions
4. {submissionFile} - Submission format requirements

**For each document, mentally note:**
- Key facts to extract
- Ambiguities or gaps
- Cross-references to other documents

### 3. Load Template

Read {templateFile} to understand the target structure.

### 4. Systematic Extraction

Work through each template section, extracting from source documents:

**Section 1 - Problem Statement:**
- Extract task type from description
- Extract objective/goal
- Capture business context if provided
- Write clear summary

**Section 2 - Evaluation:**
- Extract exact metric name and formula from rules
- Note optimization direction (higher/lower is better)
- Capture any secondary metrics
- Document edge cases, tie-breaking, rounding

**Section 3 - Data:**
- List all data files mentioned
- Extract schema/field descriptions
- Capture data access instructions
- Note file sizes and formats

**Section 4 - Submission:**
- Extract exact format requirements
- Note column names and types
- Capture file naming conventions
- Document submission limits

**Section 5 - Constraints:**
- Extract runtime/memory limits
- Document GPU requirements
- Note internet access rules
- Capture external data/model restrictions
- Note ensemble limits

**Section 6 - Timeline:**
- Extract all dates and deadlines
- Note time zones if specified

**Section 7 - Prizes:**
- Extract prize structure

**Section 8 - Additional Notes:**
- Capture any clarifications
- Note known issues
- Document source references

### 5. Handle Gaps and Ambiguities

**For each empty or uncertain field:**

- If information is truly not available: Mark as "NOT SPECIFIED IN SOURCE DOCUMENTS"
- If information is ambiguous: Note the ambiguity with "[AMBIGUOUS: ...]"
- If information might be in competition forums: Note as "[CHECK FORUMS: ...]"

**Example handling:**
```markdown
- **Runtime Limit:** NOT SPECIFIED IN SOURCE DOCUMENTS
- **External Data:** [AMBIGUOUS: rules mention "no external data" but host clarification unclear on pretrained models]
```

### 6. Cross-Validation

Before finalizing, verify:

- [ ] Metric in evaluation section matches metric mentioned in rules
- [ ] Data file names are consistent across all sections
- [ ] Submission format matches expected evaluation input
- [ ] Constraints don't contradict each other
- [ ] Timeline dates are internally consistent

Document any inconsistencies found between source documents.

### 7. Write Challenge Specification

Create {outputFile} with all extracted content.

**Structure must follow the template exactly.**

### 8. Self-Check Against Validation Checklist

Run through the checklist at the end of the template:

- [ ] Problem statement clear and unambiguous
- [ ] Evaluation metric fully specified with formula
- [ ] All data files documented with schemas
- [ ] Submission format requirements complete
- [ ] All constraints captured (compute, code, legal)
- [ ] Timeline accurate and complete
- [ ] Source documents referenced

Note any items that could not be checked off.

### 9. Update Sidecar

Update {sidecarFile}:
- Add 'step-02-challenge-spec' to stepsCompleted
- Set lastStep to 'step-02-challenge-spec'
- Update lastUpdated date
- Add session note: "Challenge spec authored from input documents"
- Note any gaps or ambiguities found

### 10. Summary and Proceed

"**Challenge Specification Complete**

**Document created:** `{outputFile}`

**Extraction summary:**
- Sections fully populated: {list}
- Sections with gaps: {list}
- Ambiguities flagged: {count}
- Cross-reference issues found: {count}

**Ready for validation review.**

**[C]ontinue** to challenge spec validation"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- All input documents read completely before writing
- Every field in spec traceable to source document
- Gaps explicitly marked, not filled with assumptions
- Cross-validation performed and issues noted
- Validation checklist reviewed
- Clean handoff to review step

### ❌ SYSTEM FAILURE:

- Writing spec without reading all inputs
- Inventing information not in source documents
- Leaving template placeholders (like `{competition_name}`)
- Ignoring ambiguities or gaps
- Skipping cross-validation
- Not documenting source references

**Master Rule:** This step ONLY extracts and synthesizes from source documents. Every claim must be traceable. Gaps are marked, never filled with assumptions.
