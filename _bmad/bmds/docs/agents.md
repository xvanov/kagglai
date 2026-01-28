# Agents Reference

BMDS includes 4 specialized agents that form your data science team.

---

## 🔍 Atlas — Data Analyst

**ID:** `bmad:bmds:agents:data-analyst`

**Role:** Data analysis specialist responsible for understanding data through systematic exploration, profiling, and insight extraction.

**When to Use:**
- Starting a new project and need to understand the data
- Investigating data quality issues
- Exploring feature relationships
- Creating EDA reports and notebooks

**Key Capabilities:**
- Comprehensive EDA (distributions, correlations, anomalies)
- Data profiling and quality assessment
- Missing data analysis
- Feature relationship mapping
- Notebook generation

**Menu Commands:**
| Trigger | Description |
|---------|-------------|
| AP | Analyze problem definition |
| ED | Run exploratory data analysis |
| DP | Generate data profile report |
| FA | Find anomalies and outliers |
| MF | Map feature relationships |
| QC | Data quality assessment |
| NB | Generate EDA notebook |
| UU | Update Current Understanding |

---

## 📚 Owl — Research Specialist

**ID:** `bmad:bmds:agents:researcher`

**Role:** Research synthesis specialist focused on state-of-the-art intelligence gathering and architecture recommendations.

**When to Use:**
- Researching approaches for a problem domain
- Analyzing academic papers
- Finding benchmark datasets
- Proposing model architectures

**Key Capabilities:**
- Academic paper analysis (arxiv, conferences)
- Benchmark and leaderboard research
- Technique extraction and comparison
- Architecture proposals with citations
- Research synthesis across sources

**Menu Commands:**
| Trigger | Description |
|---------|-------------|
| SR | Search and synthesize research |
| PA | Propose SOTA architecture |
| PP | Parse and summarize a paper |
| ST | Identify SOTA for a task type |
| BM | Find relevant benchmarks |
| TR | Generate technique recommendations |
| UR | Update research in Current Understanding |

---

## 🧪 Feynman — Data Scientist

**ID:** `bmad:bmds:agents:data-scientist`

**Role:** Hypothesis-driven experimentation expert who designs rigorous experiments and maintains living knowledge documents.

**When to Use:**
- Formulating new hypotheses to test
- Designing experiment methodology
- Evaluating experiment results
- Suggesting new research directions
- Tracking experiment status

**Key Capabilities:**
- Testable hypothesis generation
- Isolated experiment design (single variable)
- Falsifiability and validity checking
- Result evaluation and learning extraction
- Hypothesis registry maintenance

**Menu Commands:**
| Trigger | Description |
|---------|-------------|
| NH | Generate new hypothesis |
| DE | Design experiment for hypothesis |
| RV | Review experiment design |
| EV | Evaluate results and update docs |
| NR | Suggest new research directions |
| SS | Show status summary |
| UD | Update living documents |

---

## 🔧 Rex — Implementation Engineer

**ID:** `bmad:bmds:agents:implementer`

**Role:** Production-grade implementation specialist who writes high-quality code and manages integration of validated changes.

**When to Use:**
- Implementing experiment code
- Code review for quality
- Integrating validated experiments
- Creating technical specifications
- Updating architecture documentation

**Key Capabilities:**
- Production-grade code implementation
- DRY principle enforcement
- Code review with severity levels
- Integration planning and execution
- Architecture documentation

**Menu Commands:**
| Trigger | Description |
|---------|-------------|
| IM | Implement experiment from definition |
| CR | Code review for production readiness |
| IP | Integrate validated changes |
| RF | Analyze and refactor code |
| AD | Update architecture documentation |
| TS | Create technical specification |

---

## Agent Collaboration

The agents work together in a structured flow:

```
Atlas (EDA) → Owl (Research) → Feynman (Hypothesis) → Rex (Implement)
                                      ↓
                              Feynman (Evaluate) → Rex (Integrate)
```

**Key Handoff Points:**
- Atlas → Owl: Data insights inform research direction
- Owl → Feynman: Research findings become hypotheses
- Feynman → Rex: Approved designs become code
- Rex → Feynman: Completed code is evaluated
- Feynman → Rex: Validated experiments are integrated

---

## Invoking Agents

**Direct invocation:**
```
/bmad:bmds:agents:data-analyst
```

**Within workflows:**
Agents are automatically invoked at appropriate workflow steps.

**Menu navigation:**
After invoking an agent, use menu triggers (e.g., `ED` for EDA) to access specific capabilities.
