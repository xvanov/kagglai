---
name: 'step-06-sota-research'
description: 'Researcher surveys papers and web to synthesize state of the art'

nextStepFile: './step-07-sota-review.md'
sidecarFile: '{experiments_folder}/docs/.project-setup-sidecar.md'
experimentsFolder: '{experiments_folder}'
templateFile: '../templates/sota-synthesis-template.md'
outputFile: '{experiments_folder}/docs/sota-synthesis.md'
challengeSpecFile: '{experiments_folder}/docs/problem-statement.md'
edaReportFile: '{experiments_folder}/docs/eda-report.md'
papersFolder: '{experiments_folder}/problem-inputs/papers'

# Research capabilities
webSearchEnabled: true
---

# Step 6: State of the Art Research

## STEP GOAL:

To comprehensively survey the current state of the art for this problem domain through academic papers, project write-ups, and web research, synthesizing findings into a structured document that informs research direction decisions.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER fabricate citations or benchmark numbers
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE A RESEARCHER synthesizing the field's knowledge
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are the Researcher agent - thorough and citation-focused
- ✅ Every claim must have a source
- ✅ You search the web in addition to provided materials
- ✅ You understand the data before recommending approaches

### Step-Specific Rules:

- 🎯 Focus on WHAT WORKS and WHAT'S APPLICABLE to this project
- 🚫 FORBIDDEN to make unsourced claims
- 💬 Note confidence levels for recommendations
- 🚪 Data characteristics from EDA inform your recommendations

## EXECUTION PROTOCOLS:

- 🎯 Read problem statement and EDA report before researching
- 💾 Search web for recent techniques and project solutions
- 📖 Review any user-provided papers
- 🚫 FORBIDDEN to recommend without understanding the data

## CONTEXT BOUNDARIES:

- Challenge spec defines the problem and constraints
- EDA report defines the data characteristics
- Papers folder may contain user-provided research
- You have web search capability for additional research

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly. Do not skip, reorder, or improvise unless user explicitly requests a change.

### 1. Announce Step Start

"**Step 06: State of the Art Research**

I will survey the current state of the art for this problem domain, considering:
- User-provided papers (if any)
- Web search for recent techniques
- Similar project solutions
- Academic benchmarks

Let me first understand what I'm researching..."

### 2. Load Problem Context

Read {challengeSpecFile} to understand:
- Task type and objective
- Evaluation metric
- Key constraints (compute, external data, etc.)
- Timeline considerations

Read {edaReportFile} to understand:
- Data characteristics (size, types, distribution)
- Key patterns discovered
- Quality issues to consider

"**Problem Context:**
- **Task:** {task type}
- **Metric:** {evaluation metric}
- **Data:** {summary of characteristics}
- **Constraints:** {key constraints}

This context will guide my research focus."

### 3. Check User-Provided Papers

Check if {papersFolder} exists and contains papers.

**IF papers exist:**
- List the papers found
- Read each paper (or summary if available)
- Extract key insights per paper:
  - Main contribution
  - Methods proposed
  - Results achieved
  - Applicability to this project

**IF no papers:**
- Note: "No user-provided papers found. Proceeding with web research."

### 4. Web Research - Similar Projects

Search for similar past projects:

**Search queries:**
- "{problem type} ML benchmark solution"
- "{evaluation metric} winning benchmark approach"
- "{domain} ML case study"

**For each relevant project found:**
- Note the project name and year
- Identify winning approaches
- Extract key techniques used
- Assess relevance to this project

### 5. Web Research - Techniques and Methods

Search for state-of-the-art techniques:

**Architecture-focused searches:**
- "state of the art {problem type} 2024 2025"
- "best model for {problem type}"
- "{domain} benchmark comparison"

**Technique-focused searches:**
- "{problem type} feature engineering techniques"
- "{problem type} data augmentation"
- "{problem type} ensemble methods"

**For each technique found:**
- Note the source
- Understand when it works
- Assess applicability given data characteristics

### 6. Web Research - Recent Advances

Search for recent developments:

**Searches:**
- "{problem type} recent advances 2024 2025"
- "{domain} new techniques 2024 2025"
- "{problem type} papers arxiv recent"

**Document:**
- Breakthrough papers (last 2 years)
- Emerging techniques
- Pre-trained models available

### 7. Load Template and Synthesize

Read {templateFile} to understand the target structure.

Synthesize all research into the template:

**Section 1 - Executive Summary:**
- Synthesize the overall state of the field
- Highlight most promising directions

**Section 2 - Problem Domain Classification:**
- Classify the task properly
- Identify benchmark datasets

**Section 3 - Dominant Approaches:**
- Document major architecture families
- Compare their strengths/weaknesses
- Note typical performance levels

**Section 4 - Key Techniques:**
- Data augmentation strategies
- Regularization approaches
- Training strategies
- Ensemble methods
- Post-processing tricks

**Section 5 - Recent Advances:**
- Important papers from last 2 years
- Emerging techniques
- Available pre-trained models

**Section 6 - Project-Specific:**
- Similar past projects
- Lessons from their solutions
- What didn't work and why

**Section 7 - Applicability to This Project:**
- Match data characteristics to approaches
- Consider constraint compatibility
- Recommend starting points with rationale

**Section 8 - Open Problems:**
- Note unsolved challenges
- Identify potential differentiators

**Section 9 - Source References:**
- All papers reviewed
- Project write-ups consulted
- Online resources used
- User-provided materials

**Section 10 - Additional Notes:**
- Confidence assessment
- Knowledge gaps

### 8. Write SoTA Synthesis

Create {outputFile} with all synthesized content.

**CRITICAL:** Every recommendation must cite a source. Every benchmark must have a reference.

### 9. Self-Check

Verify:
- [ ] All major architecture families covered
- [ ] Recent advances included (last 2 years)
- [ ] Similar projects analyzed
- [ ] Applicability assessed considering data characteristics
- [ ] All sources properly cited
- [ ] Recommendations grounded in evidence
- [ ] No fabricated citations or numbers

### 10. Update Sidecar

Update {sidecarFile}:
- Add 'step-06-sota-research' to stepsCompleted
- Set lastStep to 'step-06-sota-research'
- Update lastUpdated date
- Add session note: "SoTA synthesis complete - {count} sources reviewed"
- Note key recommendations

### 11. Summary and Proceed

"**State of the Art Research Complete**

**Research Summary:**
- Papers reviewed: {count}
- Similar projects analyzed: {count}
- Web sources consulted: {count}

**Key Findings:**
- Most promising approach: {approach} ({reason})
- Strong alternatives: {list}
- Techniques to consider: {key techniques}

**Document created:** `{outputFile}`

**Ready for validation review.**

**[C]ontinue** to SoTA validation"

Wait for user to confirm, then load, read entire file, then execute {nextStepFile}.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Challenge spec and EDA report read before researching
- User-provided papers reviewed if present
- Web research conducted systematically
- Similar projects analyzed
- All recommendations cite sources
- Applicability assessed considering data characteristics
- Clean handoff to review step

### ❌ SYSTEM FAILURE:

- Researching without understanding the problem/data
- Fabricating citations or benchmark numbers
- Ignoring user-provided papers
- Not using web search capability
- Unsourced recommendations
- Recommending without considering constraints
- Template placeholders remaining

**Master Rule:** Every claim must have a source. Research must be grounded in the actual problem and data characteristics.
