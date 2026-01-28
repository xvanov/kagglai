# EXP-XXX: {Title}

## Hypothesis

{Clear, falsifiable statement of what we're testing}

## Motivation

- Why this hypothesis?
- Evidence from Current Understanding: `[Source: docs/current-understanding.md#Section]`
- SOTA reference: `[Source: docs/sota-synthesis.md#Section]`

## Methodology

### Independent Variable

- **What changes:** {Precise description}
- **Baseline value:** {Exact current value}
- **Experiment value:** {Exact new value}

### Dependent Variable

- **Primary metric:** {Exact metric name, e.g., "CDA Score"}
- **Evaluation dataset:** {Exact path, e.g., `data/val/` or `data/test/`}
- **Calculation:** {Formula or reference to evaluation script at `{path}`}

### Control & Isolation

- **Baseline checkpoint:** `{exact path to model weights}`
- **Baseline config:** `{exact path to config file}`
- **Changes isolated to:** `{list of files/modules}`
- **NOT changing:** `{explicit list of what stays constant}`

## Expected Outcome

- **If validated:** {Quantified expectation, e.g., ">2% CDA improvement"}
- **If invalidated:** {What we learn, next hypothesis}

## Success Criteria

| Metric | Dataset | Threshold | Evaluation Script |
|--------|---------|-----------|-------------------|
| {Primary} | `{path}` | {>X%} | `{script_path}` |
| {Secondary} | `{path}` | {threshold} | `{script_path}` |

## Risks & Assumptions

- [ ] Assumes {assumption} - verified by {how}
- [ ] Risk: {risk} - mitigated by {how}

## References

- Current Understanding: `docs/current-understanding.md#relevant-section`
- Architecture: `docs/current-architecture.md#relevant-section`
- Problem Statement: `docs/problem-statement.md#relevant-section`
- Related experiments: `experiments/EXP-XXX/`
