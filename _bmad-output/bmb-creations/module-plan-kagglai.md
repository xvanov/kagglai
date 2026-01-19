# Module Plan: KagglAI

## Purpose

KagglAI is a cohesive data science agent module designed to transform a solo Kaggle competitor into a full team. It implements a structured, scientific-method-based workflow for running experiments, validating hypotheses, and iteratively improving model performance across any competition type (tabular, vision, NLP, time series).

## Goals

- **Primary Goals:**
  - Deliver state-of-the-art techniques through systematic research integration
  - Enable fast, efficient iteration through structured workflow
  - Maintain living documentation of learnings (Current Understanding + Hypothesis Registry)
  - Ensure quality through built-in review checkpoints (experiment validation, code review)

- **Secondary Goals:**
  - Build reproducible experiment pipelines
  - Accumulate competition-transferable knowledge
  - Reduce cognitive load on solo competitor

## Agents

### 1. Data Analyst
**Role:** Competition & Data Expert

**Capabilities:**
- Parse and synthesize competition rules, constraints, evaluation metrics
- Conduct thorough exploratory data analysis (EDA)
- Identify data quality issues, distributions, anomalies
- Understand data deeply - schema, relationships, edge cases
- Document findings to inform hypothesis generation

**Key Outputs:**
- Competition summary (rules, constraints, evaluation criteria)
- EDA report (distributions, correlations, missing data, anomalies)
- Initial insights for Current Understanding document

---

### 2. Researcher
**Role:** SOTA Scout

**Capabilities:**
- Web search for relevant techniques and approaches
- Find and synthesize research papers
- Identify state-of-the-art methods for the specific domain
- Analyze winning solutions from similar past competitions
- Extract actionable techniques from academic literature

**Key Outputs:**
- Research synthesis report
- Recommended techniques with citations
- Prior art summary (past competition solutions)

---

### 3. Data Scientist
**Role:** Hypothesis Engine

**Capabilities:**
- Generate hypotheses based on data understanding and research
- Design rigorous experiments to test hypotheses
- Create detailed experiment plans (methodology, expected outcomes)
- Review experiment plans for soundness (validation step)
- Run experiments and collect results
- Evaluate results against success criteria
- Update Hypothesis Registry with outcomes
- Update Current Understanding document with learnings
- Determine next steps based on experiment outcomes

**Key Outputs:**
- Hypothesis entries in registry
- Experiment definition documents
- Experiment evaluation reports
- Updated Current Understanding document

---

### 4. Implementer
**Role:** Code Executor

**Capabilities:**
- Read experiment descriptions and implement code
- Write clean, reproducible experiment code
- Review code for correctness and alignment with experiment design
- Integrate successful experiments into production pipeline
- Maintain code quality and consistency

**Key Outputs:**
- Experiment implementation code
- Code review feedback
- Production pipeline updates

---

## Living Documents

### Current Understanding Document
A continuously updated document capturing:
- What we know about the data
- What models/approaches work (and why)
- Key insights and patterns discovered
- Accumulated learnings across experiments

### Hypothesis Registry
Structured log of all hypotheses with fields:
- **Hypothesis:** Clear statement (e.g., "YOLOv8 will outperform RCNN on this dataset")
- **Experiment Methodology:** How we'll test it
- **Results:** Quantitative outcomes
- **Status:** Validated / Rejected
- **Next Steps:** What to do based on outcome

---

## Workflow

```
Phase 1: UNDERSTAND
├── Data Analyst → Competition analysis + deep EDA
└── Researcher → SOTA research synthesis

Phase 2: HYPOTHESIZE
├── Data Scientist → Generate hypothesis + experiment design
└── Data Scientist (review mode) → Validate experiment plan

Phase 3: IMPLEMENT
├── Implementer → Write experiment code
└── Implementer (review mode) → Code review

Phase 4: EVALUATE
├── Data Scientist → Run experiment, evaluate, update docs
└── Implementer (optional) → Integrate into production pipeline

[Loop back to Phase 2 with new hypotheses]
```

---

## Context

- **Environment:** Kaggle competitions (any type: tabular, vision, NLP, time series)
- **Timeline:** Variable - weekend sprints to multi-month competitions
- **Constraints:** Competition rules, compute limits, submission limits
- **Integration:** Works as BMAD-style module with structured workflow

## Users

- **Target Audience:** Solo Kaggle competitors who want team-level capability
- **Skill Level:** Intermediate to advanced data scientists
- **Usage Pattern:** Follow structured workflow per competition, iterate through hypothesis cycles

---

## Agent Build Order

1. **Data Analyst** - Entry point, sets foundation
2. **Researcher** - Informs hypothesis generation
3. **Data Scientist** - Core hypothesis engine
4. **Implementer** - Executes and integrates

---

## Notes

- Agents operate in same agent/different mode pattern (like BMAD dev agent)
- Review checkpoints prevent wasted effort on flawed experiments
- Living documents accumulate value across competition lifecycle
