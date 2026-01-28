# Gap Analysis Template

**Purpose:** Compare brownfield state against project-init end-state to identify what needs to be created or standardized.

---

## Gap Analysis Report

**Project:** {project_name}
**Brownfield Path:** {brownfield_path}
**Analysis Date:** {date}
**Analyst:** {agent}

---

## 1. Documentation Gaps

### Primary Documents

| Document | Required | Brownfield Status | Gap | Action |
|----------|----------|-------------------|-----|--------|
| problem-statement.md | Yes | Missing/Partial/Complete | {description} | Create/Update/None |
| eda-report.md | Yes | Missing/Partial/Complete | {description} | Create/Update/None |
| sota-synthesis.md | Yes | Missing/Partial/Complete | {description} | Create/Update/None |
| research-directions.md | Yes | Missing/Partial/Complete | {description} | Create/Update/None |
| technical-spec.md | Yes | Missing/Partial/Complete | {description} | Create/Update/None |

### Handoff Documents

| Document | Required | Brownfield Status | Gap | Action |
|----------|----------|-------------------|-----|--------|
| current-understanding.md | Yes | Missing/Partial/Complete | {description} | Create/Update/None |
| current-architecture.md | Yes | Missing/Partial/Complete | {description} | Create/Update/None |
| hypothesis-registry.md | Yes | Missing/Partial/Complete | {description} | Create/Update/None |

---

## 2. Implementation Gaps

### Folder Structure

| Folder | Required | Brownfield Status | Action |
|--------|----------|-------------------|--------|
| src/ | Yes | Exists/Missing/Different | Create/Reorganize/None |
| models/baselines/ | Yes | Exists/Missing | Create/Move/None |
| submissions/ | Yes | Exists/Missing | Create/None |
| data/raw/ | Yes | Exists/Missing | Create/Link/None |
| docs/ | Yes | Exists/Missing | Create/None |

### Code Components

| Component | Required | Brownfield Status | Gap | Action |
|-----------|----------|-------------------|-----|--------|
| train.py | Yes | Exists/Missing | {description} | Create/Adapt/None |
| predict.py | Yes | Exists/Missing | {description} | Create/Adapt/None |
| Data loader | Yes | Exists/Missing | {description} | Create/Adapt/None |
| Preprocessor | Yes | Exists/Missing | {description} | Create/Adapt/None |
| Submission generator | Yes | Exists/Missing | {description} | Create/Adapt/None |

---

## 3. Knowledge Gaps

### Problem Understanding

| Aspect | Required | Brownfield Has | Gap |
|--------|----------|----------------|-----|
| Clear objective | Yes | Yes/No/Partial | {description} |
| Evaluation metric | Yes | Yes/No/Partial | {description} |
| Constraints documented | Yes | Yes/No/Partial | {description} |
| Data schema | Yes | Yes/No/Partial | {description} |

### Data Understanding

| Aspect | Required | Brownfield Has | Gap |
|--------|----------|----------------|-----|
| Feature analysis | Yes | Yes/No/Partial | {description} |
| Target distribution | Yes | Yes/No/Partial | {description} |
| Missing data analysis | Yes | Yes/No/Partial | {description} |
| Quality issues | Yes | Yes/No/Partial | {description} |
| Train-test consistency | Yes | Yes/No/Partial | {description} |

### Research Understanding

| Aspect | Required | Brownfield Has | Gap |
|--------|----------|----------------|-----|
| SoTA techniques | Yes | Yes/No/Partial | {description} |
| Similar competitions | Yes | Yes/No/Partial | {description} |
| What worked | Yes | Yes/No/Partial | {description} |
| What didn't work | Yes | Yes/No/Partial | {description} |

---

## 4. Gap Priority Matrix

### Critical (Block experiment-cycle)

| Gap | Impact | Effort | Priority |
|-----|--------|--------|----------|
| {gap} | {impact} | {effort} | Must Fix |

### Major (Reduce effectiveness)

| Gap | Impact | Effort | Priority |
|-----|--------|--------|----------|
| {gap} | {impact} | {effort} | Should Fix |

### Minor (Nice to have)

| Gap | Impact | Effort | Priority |
|-----|--------|--------|----------|
| {gap} | {impact} | {effort} | Can Defer |

---

## 5. Gap Resolution Plan

### Phase 1: Critical Gaps

1. **{Gap 1}**
   - Current state: {description}
   - Required state: {description}
   - Resolution: {what to do}
   - Responsible: {agent}

### Phase 2: Major Gaps

1. **{Gap 1}**
   - Current state: {description}
   - Required state: {description}
   - Resolution: {what to do}
   - Responsible: {agent}

### Phase 3: Minor Gaps (Deferred)

1. **{Gap 1}**
   - Note: {why deferred}

---

## 6. Brownfield Value Extraction

### What to Keep

| Artifact | Location | Value | Integration |
|----------|----------|-------|-------------|
| {artifact} | {path} | {why valuable} | {how to use} |

### What to Adapt

| Artifact | Location | Issue | Adaptation |
|----------|----------|-------|------------|
| {artifact} | {path} | {problem} | {how to fix} |

### What to Discard

| Artifact | Location | Reason |
|----------|----------|--------|
| {artifact} | {path} | {why not useful} |

---

## 7. End-State Checklist

After gap resolution, verify:

### Documents
- [ ] problem-statement.md exists and complete
- [ ] eda-report.md exists and complete
- [ ] sota-synthesis.md exists and complete
- [ ] research-directions.md exists and complete
- [ ] technical-spec.md exists and complete
- [ ] current-understanding.md exists and complete
- [ ] current-architecture.md exists and complete
- [ ] hypothesis-registry.md exists with initial hypotheses

### Implementation
- [ ] src/ folder organized with working code
- [ ] models/baselines/ contains trained model
- [ ] submissions/ contains valid submission file
- [ ] Baseline can be reproduced

### Ready for experiment-cycle
- [ ] All handoff documents complete
- [ ] Baseline performance documented
- [ ] Initial hypotheses registered
- [ ] Extension points identified
