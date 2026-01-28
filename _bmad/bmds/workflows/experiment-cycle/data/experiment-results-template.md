# Results: EXP-XXX

## Execution Record

| Item | Value |
|------|-------|
| Date | {YYYY-MM-DD HH:MM} |
| Duration | {X hours Y minutes} |
| Git commit | `{full hash}` |
| Checkpoint | `{exact_path}` |
| Config used | `{exact_path}` |
| Logs | `{exact_path}` |

## Metrics

### Primary Metric

| Metric | Dataset | Baseline | Experiment | Delta | Threshold |
|--------|---------|----------|------------|-------|-----------|
| {name} | `{path}` | {X.XX%} | {Y.YY%} | {+/-Z.ZZ%} | {>W%} |

**Evaluation command used:**
```bash
{exact command}
```

**Source:** Output at `{exact path to metrics file}`

### Secondary Metrics

| Metric | Dataset | Baseline | Experiment | Delta |
|--------|---------|----------|------------|-------|
| {name} | `{path}` | {value} | {value} | {delta} |
| {name} | `{path}` | {value} | {value} | {delta} |

### Resource Usage

| Resource | Value |
|----------|-------|
| GPU | {model, count} |
| Training time | {hours} |
| Inference time | {ms/sample} |
| Peak memory | {GB} |

## Observations

- {What happened during training}
- {Unexpected behaviors}
- {Convergence patterns}
- {Notable warnings or issues}

## Error Analysis (if applicable)

- Failure cases saved to: `{path to error samples}`
- Error patterns identified:
  - {Pattern 1}: {frequency}, {description}
  - {Pattern 2}: {frequency}, {description}

## Verdict

**{VALIDATED / INVALIDATED}**

**Rationale:** {Why this verdict based on success criteria from readme.md}

## Lessons Learned

1. {Key insight for Current Understanding}
2. {What to update in `docs/current-understanding.md#Section`}
3. {Implications for future experiments}

## Integration (if VALIDATED)

- [ ] Code merged to main: commit `{hash}`
- [ ] Architecture doc updated: `docs/current-architecture.md`
- [ ] Checkpoint promoted to: `models/production/{name}`
- [ ] Config promoted to: `configs/production/{name}`

## Next Steps

- [ ] Follow-up hypothesis: {if any}
- [ ] Update Current Understanding: `docs/current-understanding.md#{sections}`
- [ ] Update Hypothesis Registry: entry EXP-XXX
