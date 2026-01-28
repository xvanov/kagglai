# Review Criteria

**Purpose:** Pass/fail criteria for Design Review (Step 2) and Code Review (Step 4).

---

## Design Review Criteria (Step 2)

The DS Reviewer evaluates the experiment design (readme.md) against these criteria.

### Required for PASS

All must be true:

#### 1. Hypothesis Quality

- [ ] **Falsifiable:** Hypothesis can be proven false by experiment
- [ ] **Specific:** Clear expected outcome with quantified threshold
- [ ] **Isolated:** Tests exactly one variable
- [ ] **Motivated:** Clear rationale linked to Current Understanding or SOTA

#### 2. Methodology Soundness

- [ ] **Controlled:** Baseline clearly defined with exact checkpoint/config paths
- [ ] **Isolated changes:** Only the independent variable changes
- [ ] **Measurable:** Primary metric specified with exact evaluation method
- [ ] **Reproducible:** All paths, seeds, and commands specified

#### 3. Documentation Completeness

- [ ] **Paths exist:** All referenced files/checkpoints are valid paths
- [ ] **Dataset specified:** Exact dataset for evaluation (not test set for tuning)
- [ ] **Success criteria:** Clear threshold for validation/invalidation
- [ ] **References:** Links to Current Understanding, SOTA, Architecture

#### 4. Anti-Pattern Prevention

- [ ] **No multi-variable:** Not testing multiple changes simultaneously
- [ ] **No test leakage:** Not using test set for tuning decisions
- [ ] **No scope creep:** Focused on single hypothesis
- [ ] **No assumptions:** Risks and assumptions documented

### Automatic FAIL

Any of these triggers rejection:

- Missing hypothesis statement
- Multiple independent variables (not isolated)
- Test set used for evaluation during tuning
- Missing baseline specification
- No success criteria defined
- Hardcoded paths that don't exist

### Feedback Format (if REJECTED)

```markdown
## Design Review: REJECTED

### Issues Found

1. **[Category]:** {Specific issue}
   - Location: {Where in readme.md}
   - Fix: {What needs to change}

2. **[Category]:** {Specific issue}
   - Location: {Where in readme.md}
   - Fix: {What needs to change}

### Required Changes

Before resubmission, address:
- [ ] {Change 1}
- [ ] {Change 2}

### Guidance

{Additional context to help with redesign}
```

---

## Code Review Criteria (Step 4)

The Code Reviewer evaluates the implementation against the plan.md.

### Required for PASS

All must be true:

#### 1. Spec Alignment

- [ ] **Exact match:** Code changes match plan.md exactly
- [ ] **No extras:** No undocumented changes
- [ ] **No omissions:** All specified changes implemented
- [ ] **Correct files:** Changes in specified files only

#### 2. Code Quality

- [ ] **Syntax valid:** Code runs without syntax errors
- [ ] **Logic correct:** Implementation matches intended behavior
- [ ] **Conventions followed:** Code follows project style
- [ ] **No regressions:** Doesn't break existing functionality

#### 3. Reproducibility

- [ ] **Seeds set:** Random seeds configured as specified
- [ ] **Paths correct:** All file paths valid and accessible
- [ ] **Commands work:** Training/evaluation commands execute
- [ ] **Config logged:** Configuration will be saved with experiment

#### 4. Anti-Pattern Prevention

- [ ] **No scope creep:** No features beyond spec
- [ ] **No hardcoded values:** Uses config, not magic numbers
- [ ] **No silent changes:** All modifications documented
- [ ] **No test contamination:** Test set not used inappropriately

### Automatic FAIL

Any of these triggers rejection:

- Changes to files not in plan.md
- Missing changes specified in plan.md
- Undocumented modifications
- Hardcoded values that should be configurable
- Test set accessed during training/tuning
- Syntax errors preventing execution

### Feedback Format (if REJECTED)

```markdown
## Code Review: REJECTED

### Issues Found

1. **[Category]:** {Specific issue}
   - File: `{path}`
   - Line: {XX-YY}
   - Expected: {What plan.md specified}
   - Found: {What was implemented}
   - Fix: {How to correct}

2. **[Category]:** {Specific issue}
   - File: `{path}`
   - Line: {XX-YY}
   - Expected: {What plan.md specified}
   - Found: {What was implemented}
   - Fix: {How to correct}

### Undocumented Changes Detected

- `{file}`: {description of unexpected change}

### Required Fixes

Before resubmission:
- [ ] {Fix 1}
- [ ] {Fix 2}

### Guidance

{Additional context to help with reimplementation}
```

---

## Validate Mode Criteria (Quality Check)

For completed experiments (Validate mode), check:

### Documentation Completeness

- [ ] readme.md fully populated
- [ ] plan.md fully populated
- [ ] results.md fully populated
- [ ] All paths in documents are valid
- [ ] Hypothesis Registry entry updated

### Reproducibility

- [ ] Checkpoint saved to documented path
- [ ] Config saved to documented path
- [ ] Training command documented and executable
- [ ] Evaluation command documented and executable
- [ ] Seeds documented

### Traceability

- [ ] Git commit recorded
- [ ] Current Understanding updated (if lessons learned)
- [ ] Current Architecture updated (if VALIDATED)
- [ ] Hypothesis Registry status correct

### Metrics Integrity

- [ ] Metrics evaluated on correct dataset (not test for tuning)
- [ ] Baseline and experiment metrics from same evaluation
- [ ] Delta calculation correct
- [ ] Verdict matches success criteria

---

## Review Outcome Actions

### Design Review PASS

1. Update experiment status: PENDING → APPROVED_FOR_IMPLEMENTATION
2. Proceed to Step 3 (Implementation)

### Design Review FAIL

1. Update experiment status: PENDING → NEEDS_REVISION
2. Generate feedback document
3. Human initiates new Step 1 session with feedback

### Code Review PASS

1. Update experiment status: APPROVED_FOR_IMPLEMENTATION → READY_FOR_EXECUTION
2. Proceed to Step 5 (Execution)

### Code Review FAIL

1. Update experiment status: APPROVED_FOR_IMPLEMENTATION → NEEDS_REIMPLEMENTATION
2. Generate feedback document
3. Human initiates new Step 3 session with feedback
