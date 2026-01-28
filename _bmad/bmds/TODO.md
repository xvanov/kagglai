# TODO: BMDS (BMAD Data Science)

Development and refinement roadmap for the bmds module.

---

## Agents (Completed)

All agents have been adapted from KagglAI:

- [x] data-analyst (Atlas) — Data Analyst
- [x] researcher (Owl) — Research Specialist
- [x] data-scientist (Feynman) — Data Scientist
- [x] implementer (Rex) — Implementation Engineer

### Agent Refinements Needed

- [ ] Review agent instructions for any remaining Kaggle-specific language
- [ ] Add MLflow-specific guidance to each agent
- [ ] Add DVC-specific guidance to implementer
- [ ] Test agent menu triggers

---

## Workflows (Completed)

All workflows have been adapted from KagglAI:

- [x] project-init (17 step files)
- [x] experiment-cycle (10 step files)

### Workflow Refinements Needed

- [ ] Review all step files for remaining competition-specific language
- [ ] Update step file references to use `{bmds_output_folder}` consistently
- [ ] Test full project-init workflow end-to-end
- [ ] Test full experiment-cycle workflow end-to-end
- [ ] Add notebook generation steps to EDA phases

---

## Installation Testing

- [ ] Test installation with `bmad install bmds`
- [ ] Verify module.yaml prompts work correctly
- [ ] Test installer.js creates all directories
- [ ] Verify .gitignore additions work
- [ ] Test requirements.txt generation
- [ ] Verify living document templates are created

---

## MLflow Integration

- [ ] Document MLflow setup in getting-started.md
- [ ] Add MLflow experiment creation to project-init
- [ ] Add MLflow logging examples to implementer sidecar
- [ ] Test experiment tracking end-to-end

---

## DVC Integration

- [ ] Document DVC setup in getting-started.md
- [ ] Add DVC initialization to project-init
- [ ] Add data tracking examples to implementer sidecar
- [ ] Test data versioning end-to-end

---

## Documentation

- [x] README.md — Module overview
- [x] TODO.md — This file
- [ ] docs/getting-started.md — Quick start guide
- [ ] docs/agents.md — Agent reference
- [ ] docs/workflows.md — Workflow reference
- [ ] docs/examples.md — Practical examples
- [ ] Add troubleshooting section

---

## KagglAI Extension

Once BMDS is stable, refactor KagglAI as an extension:

- [ ] Create KagglAI extension module structure
- [ ] Override problem-statement with challenge-spec
- [ ] Add submission format validation
- [ ] Add leaderboard tracking
- [ ] Add competition-specific agent guidance

---

## Future Enhancements

- [ ] Add `model-audit` workflow for production model analysis
- [ ] Add `research-deep` workflow for comprehensive literature review
- [ ] Consider multi-user hypothesis registry support
- [ ] Add experiment comparison dashboard generation
- [ ] Integration with cloud MLOps platforms (SageMaker, Vertex AI)

---

## Next Steps

1. Test installation on a fresh project
2. Run through project-init workflow manually
3. Run through experiment-cycle workflow manually
4. Fix any issues discovered
5. Create KagglAI extension module

---

_Last updated: 2026-01-27_
