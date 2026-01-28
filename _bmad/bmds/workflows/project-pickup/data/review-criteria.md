# Review Criteria

**Purpose:** Standards for Author/Validator review cycles in the project-setup workflow.

---

## General Review Principles

### Reviewer Mindset
1. **Assume errors exist** - Actively look for omissions and mistakes
2. **Verify, don't trust** - Check claims against sources
3. **Be specific** - Point to exact issues, not vague concerns
4. **Be constructive** - Provide fixes, not just criticism
5. **Be thorough** - Complete review before reporting

### Review Output Format
```markdown
## Review Report

**Document:** {document name}
**Reviewer:** {agent role}
**Date:** {date}

### Summary
{1-2 sentence overall assessment}

### Critical Issues (Must Fix)
1. **{Issue}**
   - Location: {section/line}
   - Problem: {description}
   - Fix: {recommended fix}

### Major Issues (Should Fix)
1. **{Issue}**
   - Location: {section/line}
   - Problem: {description}
   - Fix: {recommended fix}

### Minor Issues (Can Fix Later)
1. **{Issue}**
   - Location: {section/line}
   - Problem: {description}

### Verification Checklist
- [x] {Check 1}
- [ ] {Check 2 - failed}

### Recommendation
{APPROVE / APPROVE WITH FIXES / REJECT}
```

---

## Problem Statementification Review

### What to Check
1. **Against Original Sources**
   - Every claim traceable to source document
   - No interpretation errors
   - No missing constraints

2. **Completeness**
   - All required sections filled
   - No placeholder text remaining
   - All edge cases addressed

3. **Accuracy**
   - Metric formula exact (test with example if possible)
   - Data schemas match actual files
   - Timeline dates verified

4. **Clarity**
   - Unambiguous language
   - No conflicting statements
   - Technical terms defined

### Common Issues
- Missing compute constraints
- Incomplete submission format
- Vague evaluation criteria
- Outdated timeline

---

## EDA Report Review

### What to Check
1. **Data Coverage**
   - All files analyzed
   - All features examined
   - All splits compared

2. **Statistical Validity**
   - Calculations correct (spot check)
   - Appropriate statistics used
   - Distributions described accurately

3. **Insight Quality**
   - Patterns are non-obvious
   - Evidence supports claims
   - Recommendations are actionable

4. **Completeness**
   - Missing data analyzed
   - Quality issues documented
   - Train-test consistency checked

### Common Issues
- Missing feature analysis
- Unsubstantiated claims
- Overlooked data quality issues
- Vague recommendations

---

## SoTA Synthesis Review

### What to Check
1. **Source Accuracy**
   - Paper summaries faithful to originals
   - Benchmark numbers correct
   - Claims properly attributed

2. **Coverage**
   - Major approaches included
   - Recent work covered
   - Relevant projects analyzed

3. **Relevance**
   - Focus on applicable techniques
   - Project constraints considered
   - Data characteristics matched

4. **Quality**
   - Comparisons fair
   - Limitations acknowledged
   - Recommendations justified

### Common Issues
- Misrepresented paper findings
- Missing recent advances
- Irrelevant techniques included
- Unsupported recommendations

---

## Research Directions Review

### What to Check
1. **Grounding**
   - Each direction links to evidence
   - Claims supported by spec, EDA, or SoTA
   - No wishful thinking

2. **Practicality**
   - Difficulty assessments realistic
   - Dependencies identified
   - Timeline achievable

3. **Completeness**
   - Multiple directions (3-5+)
   - Priorities justified
   - Excluded approaches documented

4. **Measurability**
   - Success criteria concrete
   - Experiments well-defined
   - Pivot triggers specified

### Common Issues
- Unsupported priority rankings
- Unrealistic difficulty estimates
- Missing dependencies
- Vague success criteria

---

## Technical Specification Review

### What to Check
1. **Feasibility**
   - Compute constraints met
   - Dependencies available
   - Implementation path clear

2. **Completeness**
   - All pipeline stages specified
   - Error handling addressed
   - Testing strategy defined

3. **Consistency**
   - Matches problem-statement constraints
   - Uses EDA insights appropriately
   - Implements research direction #1

4. **Clarity**
   - No ambiguous steps
   - Commands executable
   - Configuration documented

### Common Issues
- Constraint violations
- Missing pipeline stages
- Unclear implementation steps
- No error handling

---

## Code Review

### What to Check
1. **Correctness**
   - Logic correct
   - Edge cases handled
   - No obvious bugs

2. **Quality**
   - Code readable
   - Functions documented
   - Consistent style

3. **Reproducibility**
   - Seeds set
   - Dependencies pinned
   - Instructions complete

4. **Performance**
   - Efficient implementation
   - Memory usage reasonable
   - Runtime acceptable

### Common Issues
- Missing error handling
- Hardcoded values
- No documentation
- Irreproducible results

---

## Review Process

### Step 1: Initial Read
- Read document completely
- Note first impressions
- Identify major sections

### Step 2: Source Verification
- Check claims against sources
- Verify calculations
- Confirm references

### Step 3: Completeness Check
- Run through checklist
- Note missing sections
- Check for placeholders

### Step 4: Quality Assessment
- Evaluate depth
- Assess clarity
- Check consistency

### Step 5: Report Generation
- Document all issues
- Prioritize by severity
- Provide fixes

### Step 6: Recommendation
- APPROVE: No issues or only suggestions
- APPROVE WITH FIXES: Minor issues, can fix quickly
- REJECT: Critical issues, needs rework

---

## Fix-Only Step Guidelines

When a review step runs too long and routes to a fix-only step:

1. **Read the review report completely**
2. **Address Critical issues first**
3. **Then address Major issues**
4. **Document what was fixed**
5. **Note any issues deferred**

Fix report format:
```markdown
## Fix Report

**Original Review:** {path to review report}
**Fixer:** {agent role}
**Date:** {date}

### Fixes Applied
1. **{Issue from review}**
   - Fix: {what was done}
   - Verified: {yes/no}

### Issues Deferred
1. **{Issue}**
   - Reason: {why deferred}
   - Plan: {when/how to address}
```
