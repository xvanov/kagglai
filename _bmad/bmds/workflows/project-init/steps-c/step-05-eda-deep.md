---
name: 'step-05-eda-deep'
description: 'Data Analyst performs deep-dive EDA discovering patterns and insights'

nextStepFile: './step-06-sota-research.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
challengeSpecFile: '{experiments_folder}/docs/problem-statement.md'
currentUnderstandingFile: '{experiments_folder}/docs/current-understanding.md'
dataRawFolder: '{experiments_folder}/data/raw'

# Advanced tools
advancedElicitationEnabled: true
partyModeEnabled: true
---

# Step 5: EDA Deep Dive - Pattern Discovery & Insights

## STEP GOAL:

To discover meaningful patterns, relationships, and insights in the data that will inform modeling decisions. This is a collaborative, creative analysis session building on the basic statistics from step 04.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER skip user engagement on significant findings
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A COLLABORATIVE ANALYST discovering patterns together
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the Data Analyst doing creative pattern discovery
- ✅ This is COLLABORATIVE - discuss findings with the user
- ✅ Your intuitions matter but evidence is required
- ✅ User may have domain knowledge you don't

### Step-Specific Rules:

- 🎯 Focus on PATTERNS, RELATIONSHIPS, and ACTIONABLE INSIGHTS
- 🚫 FORBIDDEN to just report statistics (that was step 04)
- 💬 Share interesting findings as you discover them
- 🚪 This is Session 2 of EDA - fresh context for deep analysis

## EXECUTION PROTOCOLS:

- 🎯 Build on basic statistics to discover patterns
- 💾 Complete remaining EDA report sections (6-10)
- 📖 Collaborate with user on interpretation
- 🚫 FORBIDDEN to work in isolation - this is a dialogue

## CONTEXT BOUNDARIES:

- Basic statistics exist in eda-report.md (sections 1-5)
- This is a fresh session - don't re-do basic stats
- User may have domain knowledge to share
- You have access to Advanced Elicitation and Party Mode tools

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 05: EDA Deep Dive - Pattern Discovery**

This is Session 2 of EDA. I have fresh context to dive deep into patterns and relationships.

Let me load the basic statistics and begin pattern discovery..."

### 2. Load Context

Read {edaReportFile} to understand the data characteristics from step 04.
Read {challengeSpecFile} to remember the evaluation metric and constraints.

Summarize key points:
- "**Target:** {target variable and type}"
- "**Features:** {count by type}"
- "**Key issues:** {from basic EDA}"

### 3. Feature Relationship Analysis

Analyze relationships systematically:

**Correlation Analysis:**
- Compute correlation matrix for numeric features
- Identify highly correlated pairs (|r| > 0.8)
- These may indicate redundancy or multicollinearity

**Feature-Target Relationships:**
- For each feature, assess relationship with target
- For classification: compare distributions across classes
- For regression: compute correlations, look at scatter patterns

**Interaction Effects:**
- Look for features that interact
- Cross-tabulations for categorical combinations
- Conditional relationships

**COLLABORATIVE CHECKPOINT:**
"I've found the following notable relationships:
{list relationships}

Do any of these align with domain expectations? Any surprises?"

Wait for user input before proceeding.

### 4. Train-Test Consistency Analysis

Compare train and test distributions:

**Distribution Drift:**
- For each feature, compare train vs test distributions
- Flag features with significant drift
- Compute drift scores (KS statistic, PSI, etc.)

**Leakage Check:**
- Identify potential leakage features
- Check for time-based leakage if temporal
- Check for ID-based leakage
- Look for features that seem "too predictive"

"**Train-Test Consistency Analysis:**
- Features with drift: {list}
- Potential leakage concerns: {list}

Any of these warrant further investigation?"

### 5. Deep Dive Insights

This is the creative discovery phase. Look for:

**Key Patterns:**
- Segment the data in different ways
- Look for subgroups with distinct behaviors
- Identify edge cases and their characteristics

**Surprising Findings:**
- What defies expectations?
- What patterns are non-obvious?

**Domain-Specific Observations:**
- Apply any domain knowledge
- Ask user about domain relevance

For each significant finding:
```
**{Pattern Name}**
- Description: {what was found}
- Evidence: {statistical support}
- Implication: {how this affects modeling}
```

**COLLABORATIVE CHECKPOINT:**
"I've discovered these key patterns:
{summarize patterns}

What's your interpretation? Any domain context that helps explain these?"

### 6. Develop Recommendations

Based on all findings, develop actionable recommendations:

**Feature Engineering Opportunities:**
| Opportunity | Description | Priority |
|-------------|-------------|----------|
| {name} | {description} | {High/Med/Low} |

**Data Preprocessing Pipeline:**
1. {Step 1}
2. {Step 2}
3. ...

**Validation Strategy:**
- Recommended split approach
- Stratification considerations
- Time-based considerations if applicable

"**My recommendations:**
{summarize recommendations}

Do these align with your thinking? Any adjustments needed?"

### 7. Complete EDA Report

Update {edaReportFile} with sections 6-10:
- Section 6: Feature Relationships (from analysis)
- Section 7: Deep Dive Insights (patterns discovered)
- Section 8: Train-Test Consistency (drift and leakage)
- Section 9: Recommendations (actionable items)
- Section 10: Additional Notes (open questions, external data opportunities)

### 8. Update current-understanding.md Section 2

Update {currentUnderstandingFile} Section 2 (Data):

```markdown
## 2. Data

### 2.1 Data Characteristics
- **Size:** {train rows} train, {test rows} test
- **Features:** {count by type}
- **Target:** {target description and distribution}

### 2.2 Key Findings
- {Finding 1 - most important pattern}
- {Finding 2}
- {Finding 3}

### 2.3 Data Quality Notes
- **Missing Data:** {summary}
- **Quality Issues:** {summary}
- **Train-Test Drift:** {summary}

### 2.4 Recommended Approach
- **Feature Engineering:** {key opportunities}
- **Preprocessing:** {key steps}
- **Validation:** {recommended strategy}
```

### 9. Update Sidecar

Update {sidecarFile}:
- Add 'step-05-eda-deep' to stepsCompleted
- Set lastStep to 'step-05-eda-deep'
- Update lastUpdated date
- Add session note: "EDA deep dive complete - {count} key patterns discovered"
- Note key findings summary

### 10. Summary and Proceed

"**EDA Deep Dive Complete**

**Analysis Summary:**
- Feature relationships documented: {count}
- Key patterns discovered: {count}
- Train-test consistency: {status}
- Recommendations developed: {count}

**Documents updated:**
- eda-report.md (fully complete)
- current-understanding.md (Section 2 populated)

**Next step:** State of the Art Research

**Select an option:**
- **[A]dvanced Elicitation** - Explore any findings more deeply
- **[P]arty Mode** - Multi-agent discussion of findings
- **[C]ontinue** - Proceed to SoTA research"

Wait for user selection.

**IF [A]:** Use advanced elicitation techniques to explore user questions
**IF [P]:** Initiate party mode for multi-perspective discussion
**IF [C]:** Load, read entire file, then execute {nextStepFile}

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Built on basic stats (didn't redo them)
- Feature relationships analyzed thoroughly
- Train-test consistency checked
- Multiple meaningful patterns discovered
- User engaged at checkpoints
- Recommendations are actionable
- EDA report sections 6-10 completed
- current-understanding.md Section 2 populated

### ❌ SYSTEM FAILURE:

- Re-doing basic statistics from step 04
- Working in isolation without user engagement
- Surface-level analysis only
- No patterns discovered (not looking hard enough)
- Vague or non-actionable recommendations
- Skipping collaborative checkpoints
- Template placeholders remaining

**Master Rule:** This is COLLABORATIVE pattern discovery. Engage the user. Find meaningful insights. Make actionable recommendations.
