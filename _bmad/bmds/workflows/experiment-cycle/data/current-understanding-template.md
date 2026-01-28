# Current Understanding

**Last Updated:** {YYYY-MM-DD}
**Updated By:** {EXP-XXX or manual}

---

## 1. Problem & Task

### 1.1 Objective

- Competition/task: {name}
- Goal: {what we're optimizing for}
- Source: `docs/problem-statement.md`

### 1.2 Evaluation Metric

- **Metric:** {exact name, e.g., "Competition Detection Accuracy (CDA)"}
- **Formula:** {exact formula or reference}
- **Implementation:** `{path to eval script}`
- **Gotchas:** {known edge cases, e.g., "FP penalty is 2x FN penalty"}

### 1.3 Constraints & Rules

- {Rule 1} - Source: `docs/problem-statement.md#Section`
- {Rule 2} - Source: `docs/problem-statement.md#Section`
- **Forbidden:** {explicit list of what's not allowed}

---

## 2. Data

### 2.1 Dataset Overview

| Split | Path | Samples | Class Distribution |
|-------|------|---------|-------------------|
| Train | `data/train/` | {N} | {distribution} |
| Val | `data/val/` | {N} | {distribution} |
| Test | `data/test/` | {N} | DO NOT USE until final |

### 2.2 Data Quality Issues

| Issue | Severity | Affected Samples | Mitigation |
|-------|----------|------------------|------------|
| {e.g., Label noise} | {High/Med/Low} | `{path or count}` | {approach} |
| {e.g., Class imbalance} | {severity} | {details} | {approach} |

### 2.3 Data Insights

- {Insight 1} - Discovered: EXP-XXX
- {Insight 2} - Discovered: EDA
- {Insight 3} - Source: `{path}`

---

## 3. Model

### 3.1 Architecture Landscape

| Family | Strengths | Weaknesses | SOTA Reference |
|--------|-----------|------------|----------------|
| {e.g., YOLO} | {list} | {list} | `docs/sota-synthesis.md#Section` |
| {e.g., Faster R-CNN} | {list} | {list} | `docs/sota-synthesis.md#Section` |

### 3.2 Current Best Approach

- **Architecture:** {name}
- **Why chosen:** {rationale with evidence}
- **Config:** `{exact path}`
- **Weights:** `{exact path}`
- **Performance:** {metric} = {value} on `{dataset}`

### 3.3 Known Failure Modes

| Failure Mode | Frequency | Example | Potential Fix | Status |
|--------------|-----------|---------|---------------|--------|
| {e.g., Small objects} | {X%} | `{path to example}` | {hypothesis} | {Untested/EXP-XXX} |
| {e.g., Occlusion} | {X%} | `{path to example}` | {hypothesis} | {status} |

---

## 4. Training & Pipeline

### 4.1 Effective Strategies

| Strategy | Impact | Evidence | Config |
|----------|--------|----------|--------|
| {e.g., Mosaic augmentation} | {+X% metric} | EXP-XXX | `{config_path}` |
| {e.g., Cosine LR schedule} | {+X% metric} | EXP-YYY | `{config_path}` |

### 4.2 Ineffective Strategies (Don't Repeat)

| Strategy | Result | Evidence | Why It Failed |
|----------|--------|----------|---------------|
| {e.g., Heavy rotation} | {-X% metric} | EXP-YYY | {reason} |
| {e.g., Larger batch size} | {no improvement} | EXP-ZZZ | {reason} |

---

## 5. Post-Processing

### 5.1 Current Pipeline

1. {Step 1} - Config: `{path}`, Implementation: `{path}`
2. {Step 2} - Config: `{path}`, Implementation: `{path}`

### 5.2 Threshold Tuning

| Parameter | Current Value | Tuned On | Evidence | Script |
|-----------|---------------|----------|----------|--------|
| Confidence | {X.XX} | `data/val/` | EXP-XXX | `{path}` |
| NMS IoU | {X.XX} | `data/val/` | EXP-YYY | `{path}` |

---

## 6. Open Questions

Priority scale: High (blocking progress), Medium (important), Low (nice to know)

- [ ] {Question 1} - Priority: High - Potential hypothesis: {idea}
- [ ] {Question 2} - Priority: Medium - Potential hypothesis: {idea}
- [ ] {Question 3} - Priority: Low - Notes: {context}

---

## Change Log

| Date | Source | Section Updated | Summary |
|------|--------|-----------------|---------|
| {date} | EXP-XXX | {section} | {what changed} |
| {date} | Manual | {section} | {what changed} |
