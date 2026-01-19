---
name: 'step-04-eda-basic'
description: 'Data Analyst pulls data and generates basic statistics'

nextStepFile: './step-05-eda-deep.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
templateFile: '../templates/eda-report-template.md'
outputFile: '{experiments_folder}/docs/eda-report.md'
challengeSpecFile: '{experiments_folder}/docs/challenge-spec.md'
dataAccessFile: '{experiments_folder}/challenge-inputs/data-access.md'
dataRawFolder: '{experiments_folder}/data/raw'
---

# Step 4: EDA Basic - Data Pull & Basic Statistics

## STEP GOAL:

To ensure data is available locally, verify its integrity, and generate comprehensive basic statistics that characterize all features and the target variable. This creates the foundation for deep-dive analysis in the next session.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER proceed without verifying data is present and valid
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A DATA ANALYST generating foundational statistics
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the Data Analyst responsible for data integrity
- ✅ Data must be pulled/verified before any analysis
- ✅ Basic statistics must be comprehensive and accurate
- ✅ This forms the foundation for deeper analysis

### Step-Specific Rules:

- 🎯 Focus on data acquisition and basic stats - save deep patterns for next step
- 🚫 FORBIDDEN to do deep analysis (pattern discovery, complex relationships)
- 💬 Be systematic - cover every feature, every file
- 🚪 This is Session 1 of EDA - context-fresh design

## EXECUTION PROTOCOLS:

- 🎯 Check if data exists, pull if needed
- 💾 Verify data integrity (checksums, expected files)
- 📖 Generate comprehensive basic statistics
- 🚫 FORBIDDEN to discover patterns (that's step 05)

## CONTEXT BOUNDARIES:

- Challenge spec is complete and validated
- Data access instructions are in challenge-inputs/
- Data should be stored in data/raw/
- This is a PRESCRIPTIVE step - follow the checklist systematically

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 04: EDA Basic - Data Pull & Statistics**

This is Session 1 of EDA. I will:
1. Verify/pull the competition data
2. Check data integrity
3. Generate comprehensive basic statistics

Beginning data acquisition check..."

### 2. Check Data Availability

Check if {dataRawFolder} exists and contains data files.

**Read {challengeSpecFile} Section 3 (Data) to identify expected files.**

**IF data files are present:**
- Report: "Data files found at `{dataRawFolder}`"
- List the files found
- Proceed to Section 3 (Verification)

**IF data files are NOT present:**
- Report: "Data not found. Reading data access instructions..."
- Read {dataAccessFile}
- Execute the data pull instructions
- This may involve:
  - Kaggle API download
  - URL download
  - Manual instruction for user
- Wait for confirmation data is available

### 3. Verify Data Integrity

Perform integrity checks:

**File Verification:**
- [ ] All expected files present (from challenge-spec)
- [ ] File sizes reasonable (not truncated)
- [ ] Files can be opened/parsed

**Checksum Verification (if provided):**
- [ ] Compute checksums of downloaded files
- [ ] Compare against expected values

**Format Verification:**
- [ ] Files are in expected format (CSV, Parquet, etc.)
- [ ] Headers present as expected
- [ ] Basic parse test succeeds

**IF integrity issues found:**
- Document the issues
- Ask user: "Data integrity issues found: {issues}. How would you like to proceed?"
- Wait for resolution

### 4. Load Template

Read {templateFile} to understand the target structure.

### 5. Generate Basic Statistics

Work through systematically:

**Section 1 - Data Overview:**
- Load each dataset
- Record row/column counts
- Record file sizes
- Document location

**Section 2 - Feature Analysis:**
- Classify each feature by type (numeric, categorical, text, datetime, ID)
- For numeric features: mean, std, min, percentiles, max, missing%
- For categorical features: unique count, top value, top frequency, missing%
- Create the feature statistics tables

**Section 3 - Target Variable Analysis:**
- Identify target column (from challenge-spec)
- Compute distribution statistics
- For classification: class counts and percentages
- For regression: mean, std, skewness, kurtosis
- Assess class imbalance if applicable

**Section 4 - Missing Data Analysis:**
- Count missing values per feature
- Calculate missing percentages
- Note initial pattern observations (detailed patterns in step 05)

**Section 5 - Data Quality Issues (Initial):**
- Count duplicates
- Identify obvious outliers (simple methods like IQR)
- Note obvious issues (wrong types, impossible values)

### 6. Create Initial EDA Report

Create {outputFile} with sections 1-5 populated.

**Leave sections 6-10 for step 05 (Deep Dive):**
- Section 6: Feature Relationships - "To be analyzed in EDA Deep Dive"
- Section 7: Deep Dive Insights - "To be analyzed in EDA Deep Dive"
- Section 8: Train-Test Consistency - "To be analyzed in EDA Deep Dive"
- Section 9: Recommendations - "To be developed in EDA Deep Dive"
- Section 10: Additional Notes - "To be added in EDA Deep Dive"

### 7. Quality Check

Before proceeding, verify:

- [ ] All expected data files were analyzed
- [ ] Every feature has statistics recorded
- [ ] Target variable is clearly identified and analyzed
- [ ] Missing data is documented
- [ ] No placeholder text remains in populated sections

### 8. Update Sidecar

Update {sidecarFile}:
- Add 'step-04-eda-basic' to stepsCompleted
- Set lastStep to 'step-04-eda-basic'
- Update lastUpdated date
- Add session note: "Data pulled/verified, basic statistics generated"
- Note any data issues found

### 9. Summary and Proceed

"**EDA Basic Complete**

**Data Status:**
- Location: `{dataRawFolder}`
- Files: {list}
- Integrity: {verified/issues}

**Statistics Generated:**
- Features analyzed: {count}
- Target variable: {name} ({type})
- Missing data features: {count with missing}
- Quality issues noted: {count}

**Next step:** EDA Deep Dive - Pattern discovery and insights

Note: The next step will be a fresh session for context efficiency. Take a moment to review the basic statistics before proceeding.

**[C]ontinue** to EDA deep dive"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Data verified present or successfully pulled
- Integrity checks performed
- All features have statistics
- Target variable analyzed
- Missing data documented
- Quality issues noted
- Sections 1-5 of EDA report populated

### ❌ SYSTEM FAILURE:

- Proceeding without data verification
- Missing features in analysis
- No statistics for target variable
- Template placeholders remaining
- Doing deep analysis (patterns, relationships) - that's step 05
- Skipping integrity checks

**Master Rule:** This step is about DATA ACQUISITION and BASIC STATISTICS only. Be comprehensive but don't analyze patterns - that's next session.
