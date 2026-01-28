# Image EDA Validation Checklist

**Purpose:** Quality gates for each phase of the Image EDA workflow.

---

## Phase 2: Data Acquisition

- [ ] Data source identified and documented
- [ ] Sampling strategy defined (if not downloading full dataset)
- [ ] Download/access script created and tested
- [ ] Script is reproducible (can be re-run)
- [ ] Data integrity verified (file counts, sizes)
- [ ] Script saved to `experiments/eda/01_data_sampling.py`

---

## Phase 3: Basic Statistics

- [ ] All image files scanned
- [ ] Dimensions (width, height) analyzed
- [ ] File formats identified
- [ ] Channel counts documented
- [ ] File sizes analyzed
- [ ] Directory structure mapped
- [ ] Outliers identified (unusual sizes, formats)
- [ ] Script saved to `experiments/eda/02_basic_stats.py`

---

## Phase 4: Label Analysis

- [ ] Label format identified (COCO, YOLO, VOC, custom)
- [ ] All label files parsed
- [ ] Class distribution computed
- [ ] Unlabeled images identified
- [ ] Class imbalance assessed
- [ ] Label quality issues documented
- [ ] Semantic confusion identified (if any)
- [ ] Script saved to `experiments/eda/03_label_analysis.py`

---

## Phase 5: Visual Pattern Analysis

- [ ] Sample of images visually inspected
- [ ] "Good" examples identified and documented
- [ ] "Bad" examples identified and documented
- [ ] Pattern categories defined
- [ ] Perfect matching vs random placement assessed
- [ ] Edge cases documented
- [ ] Script saved to `experiments/eda/04_visual_patterns.py`

---

## Phase 6: Data Quality Assessment

- [ ] Quality levels defined (high/medium/low)
- [ ] Images categorized by quality
- [ ] Filtering strategies proposed
- [ ] Filtering thresholds determined (e.g., white pixel %)
- [ ] "Garbage" data quantified
- [ ] Cleaning recommendations documented
- [ ] Script saved to `experiments/eda/05_data_quality.py`

---

## Phase 7: Insight Generation

- [ ] Findings from all phases synthesized
- [ ] Critical insights identified
- [ ] Data strengths documented
- [ ] Data weaknesses documented
- [ ] Surprising discoveries noted
- [ ] Insights document created: `experiments/eda/06_insights.md`
- [ ] `current-understanding.md` Section 2 updated

---

## Phase 8: Dashboard Generation

- [ ] Streamlit app structure created
- [ ] Image browser component working
- [ ] Statistics display panels implemented
- [ ] Label overlay visualization working
- [ ] Insights summary displayed
- [ ] App runs without errors
- [ ] Dashboard saved to `experiments/eda/dashboard/`

---

## Phase 9: Model Selection

- [ ] Data characteristics summarized for model selection
- [ ] SoTA models researched (if web browsing enabled)
- [ ] Model families evaluated
- [ ] Recommendations documented with rationale
- [ ] Training considerations noted
- [ ] Expected challenges identified
- [ ] `current-understanding.md` Section 3 updated
- [ ] `eda-report-images.md` finalized

---

## Phase 10: Completion

- [ ] All scripts present in `experiments/eda/`
- [ ] All scripts are runnable
- [ ] Dashboard is functional
- [ ] `eda-report-images.md` complete
- [ ] `current-understanding.md` updated (Sections 2 and 3)
- [ ] State file shows all phases complete
- [ ] Handoff ready for experiment-cycle

---

## Overall Quality Gates

### Minimum Viable EDA

- [ ] At least 100 images analyzed (or full dataset if smaller)
- [ ] Class distribution documented
- [ ] At least 3 key insights identified
- [ ] Dashboard displays images and basic stats
- [ ] At least 1 model family recommended

### Comprehensive EDA

- [ ] Full dataset analyzed
- [ ] Label quality thoroughly assessed
- [ ] Visual patterns categorized
- [ ] Filtering strategies with quantified impact
- [ ] 5+ key insights with evidence
- [ ] Dashboard fully interactive
- [ ] Multiple model families compared
- [ ] Training strategy recommendations
