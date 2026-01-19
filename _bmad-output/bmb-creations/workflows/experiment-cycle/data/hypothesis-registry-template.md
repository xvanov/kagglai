# Hypothesis Registry

**Last Updated:** {date}
**Total Experiments:** {count}

---

## Status Legend

| Status | Meaning |
|--------|---------|
| PENDING | Experiment designed, not yet executed |
| VALIDATED | Hypothesis confirmed by experiment |
| INVALIDATED | Hypothesis disproven by experiment |
| SKIPPED | Not executed (rules violation, dependencies, etc.) |
| NEEDS_REVISION | Design review rejected, awaiting redesign |
| NEEDS_REIMPLEMENTATION | Code review rejected, awaiting fixes |

---

## Registry

<!-- Add new experiments at the top -->

### EXP-001: {Title}

- **Status:** PENDING
- **Dates:** {YYYY-MM}
- **Hypothesis:** {Clear, falsifiable statement}
- **Baseline:** {metric} = {value} on `{dataset_path}`
- **Result:** {Pending execution}
- **Lesson:** {To be determined}
- **Details:** `experiments/EXP-001-{short-name}/`

---

<!-- Template for new entries:

### EXP-XXX: {Title}

- **Status:** PENDING
- **Dates:** {YYYY-MM}
- **Hypothesis:** {Clear, falsifiable statement}
- **Baseline:** {metric} = {value} on `{dataset_path}`
- **Result:** {Pending execution | metric = value (+/- delta)}
- **Lesson:** {Key insight for Current Understanding}
- **Details:** `experiments/EXP-XXX-{short-name}/`

-->
