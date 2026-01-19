# Agent Creation Complete!

## Agent Summary

- **Name:** Atlas
- **Title:** Competition Data Analyst
- **Type:** Expert (Module agent)
- **Module:** KagglAI
- **Icon:** 🔍
- **Purpose:** Deep competition analysis and exploratory data analysis for data science competitions
- **Status:** Ready for installation

## File Locations

- **Agent Config:** `_bmad-output/bmb-creations/data-analyst/data-analyst.agent.yaml`
- **Sidecar Folder:** `_bmad-output/bmb-creations/data-analyst/data-analyst-sidecar/`

## Commands

| Trigger | Description |
|---------|-------------|
| `AC` | Analyze competition rules and constraints |
| `ED` | Run exploratory data analysis |
| `DP` | Generate data profile report |
| `FA` | Find anomalies and outliers |
| `MF` | Map feature relationships |
| `QC` | Data quality assessment |
| `UU` | Update Current Understanding doc |

## Installation

To install Atlas as part of a custom KagglAI module:

### 1. Create Module Structure

```
kagglai/
├── module.yaml              # Contains: unitary: true
├── agents/
│   └── data-analyst/
│       ├── data-analyst.agent.yaml
│       └── _memory/
│           └── data-analyst-sidecar/
│               ├── memories.md
│               └── instructions.md
└── workflows/               # Future: KagglAI workflows
```

### 2. Create module.yaml

```yaml
unitary: true
name: kagglai
description: Data science competition agent module
```

### 3. Install via BMAD

- New projects: BMAD installer will prompt for local custom modules
- Existing projects: Use "Modify BMAD Installation" to add your module

## Documentation

See: https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/modules/bmb-bmad-builder/custom-content-installation.md#standalone-content-agents-workflows-tasks-tools-templates-prompts

---

*Created: 2026-01-17*
*Workflow: BMAD Agent Builder*
