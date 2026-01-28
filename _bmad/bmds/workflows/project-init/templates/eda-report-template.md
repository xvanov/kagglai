# Exploratory Data Analysis Report

**Project:** {project_name}
**Created:** {date}
**Last Updated:** {date}
**Author:** Data Analyst Agent

---

## 1. Data Overview

### 1.1 Dataset Summary
| Dataset | Rows | Columns | Size | Location |
|---------|------|---------|------|----------|
| Train | {N} | {N} | {size} | `data/raw/{file}` |
| Test | {N} | {N} | {size} | `data/raw/{file}` |
| Other | {N} | {N} | {size} | `data/raw/{file}` |

### 1.2 Data Integrity
- **Checksums Verified:** {yes/no}
- **Expected Files Present:** {yes/no}
- **Download Date:** {date}
- **Issues Found:** {none/list}

---

## 2. Feature Analysis

### 2.1 Feature Types
| Category | Count | Features |
|----------|-------|----------|
| Numeric (continuous) | {N} | {list} |
| Numeric (discrete) | {N} | {list} |
| Categorical | {N} | {list} |
| Text | {N} | {list} |
| DateTime | {N} | {list} |
| ID/Index | {N} | {list} |

### 2.2 Feature Statistics

#### Numeric Features
| Feature | Mean | Std | Min | 25% | 50% | 75% | Max | Missing |
|---------|------|-----|-----|-----|-----|-----|-----|---------|
| {feature} | {val} | {val} | {val} | {val} | {val} | {val} | {val} | {%} |

#### Categorical Features
| Feature | Unique | Top Value | Top Freq | Missing |
|---------|--------|-----------|----------|---------|
| {feature} | {N} | {value} | {%} | {%} |

---

## 3. Target Variable Analysis

### 3.1 Target Distribution
- **Target Column:** {name}
- **Type:** {continuous/binary/multiclass/multilabel}
- **Distribution:** {description}

**For Classification:**
| Class | Count | Percentage |
|-------|-------|------------|
| {class} | {N} | {%} |

**For Regression:**
- Mean: {val}
- Std: {val}
- Skewness: {val}
- Kurtosis: {val}

### 3.2 Class Imbalance Assessment
- **Imbalance Ratio:** {majority/minority ratio}
- **Severity:** {none/mild/moderate/severe}
- **Recommended Handling:** {strategy}

---

## 4. Missing Data Analysis

### 4.1 Missing Data Summary
| Feature | Missing Count | Missing % | Pattern |
|---------|---------------|-----------|---------|
| {feature} | {N} | {%} | {MCAR/MAR/MNAR} |

### 4.2 Missing Data Patterns
- **Correlated Missingness:** {description}
- **Recommended Imputation:** {strategy per feature}

---

## 5. Data Quality Issues

### 5.1 Identified Issues
| Issue | Severity | Affected | Mitigation |
|-------|----------|----------|------------|
| {description} | {High/Med/Low} | {features/rows} | {approach} |

### 5.2 Outliers
| Feature | Outlier Count | Method | Action |
|---------|---------------|--------|--------|
| {feature} | {N} | {IQR/Z-score/etc.} | {keep/cap/remove} |

### 5.3 Duplicates
- **Duplicate Rows:** {N} ({%})
- **Near-Duplicates:** {N} ({%})
- **Recommendation:** {action}

---

## 6. Feature Relationships

### 6.1 Correlation Analysis
**Highly Correlated Features (|r| > 0.8):**
| Feature 1 | Feature 2 | Correlation |
|-----------|-----------|-------------|
| {f1} | {f2} | {r} |

### 6.2 Feature-Target Relationships
| Feature | Correlation with Target | Importance Rank |
|---------|------------------------|-----------------|
| {feature} | {r or metric} | {rank} |

### 6.3 Interaction Effects
- {Notable interactions discovered}

---

## 7. Deep Dive Insights

### 7.1 Key Patterns Discovered
1. **{Pattern Name}**
   - Description: {what was found}
   - Evidence: {statistical support}
   - Implication: {how this affects modeling}

2. **{Pattern Name}**
   - Description: {what was found}
   - Evidence: {statistical support}
   - Implication: {how this affects modeling}

### 7.2 Surprising Findings
- {Unexpected discoveries}

### 7.3 Domain-Specific Observations
- {Insights requiring domain knowledge}

---

## 8. Train-Test Consistency

### 8.1 Distribution Comparison
| Feature | Train Mean | Test Mean | Drift Score |
|---------|------------|-----------|-------------|
| {feature} | {val} | {val} | {score} |

### 8.2 Leakage Check
- **Potential Leakage Features:** {list or none}
- **Time-Based Leakage:** {assessment}
- **ID-Based Leakage:** {assessment}

---

## 9. Recommendations

### 9.1 Feature Engineering Opportunities
| Opportunity | Description | Priority |
|-------------|-------------|----------|
| {name} | {description} | {High/Med/Low} |

### 9.2 Data Preprocessing Pipeline
1. {Step 1 - e.g., handle missing values}
2. {Step 2 - e.g., encode categoricals}
3. {Step 3 - e.g., scale numerics}

### 9.3 Validation Strategy
- **Recommended Split:** {strategy}
- **Stratification:** {yes/no, on what}
- **Time-Based:** {if applicable}

---

## 10. Additional Notes

### 10.1 Open Questions
- [ ] {Question requiring further investigation}

### 10.2 External Data Opportunities
- {Potential external data sources}

### 10.3 Visualization References
- {Paths to generated plots if any}

---

## Validation Checklist

- [ ] All data files loaded and verified
- [ ] Feature types correctly identified
- [ ] Target distribution analyzed
- [ ] Missing data patterns documented
- [ ] Data quality issues catalogued
- [ ] Feature relationships explored
- [ ] Train-test consistency checked
- [ ] Recommendations actionable
