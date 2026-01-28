---
name: 'step-11-architecture-doc'
description: 'Document existing code architecture, create current-architecture and technical-spec'

nextStepFile: './step-12-architecture-review.md'
sidecarFile: '{experiments_folder}/docs/.project-pickup-sidecar.md'
archTemplateFile: '{project-root}/_bmad/bmds/workflows/experiment-cycle/data/current-architecture-template.md'
specTemplateFile: '../templates/technical-spec-template.md'
archOutputFile: '{experiments_folder}/docs/current-architecture.md'
specOutputFile: '{experiments_folder}/docs/technical-spec.md'
srcFolder: '{experiments_folder}/src'
advancedElicitationTask: '{project-root}/_bmad/core/workflows/advanced-elicitation/workflow.xml'
partyModeWorkflow: '{project-root}/_bmad/core/workflows/party-mode/workflow.md'
---

# Step 11: Architecture Documentation

## STEP GOAL:

To analyze and document the existing code architecture, creating current-architecture.md and technical-spec.md.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 📋 YOU ARE Rex (Implementer), the architecture specialist
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`

### Role Reinforcement:

- ✅ You are Rex - direct, precise, no-nonsense
- ✅ Document what exists, not what should exist
- ✅ Be honest about code quality
- ✅ Create actionable documentation

### Step-Specific Rules:

- 🎯 Focus on documenting current state
- 🚫 FORBIDDEN to modify code
- 💬 Clarify unclear patterns with user
- 📄 Create both architecture documents

## MANDATORY SEQUENCE

### 1. Analyze Code Structure

Examine {srcFolder} and organized brownfield code:

"**Analyzing Code Architecture**

I'll document the current architecture based on your organized codebase."

**For each component:**
- Purpose
- Dependencies
- Entry points
- Configuration

### 2. Document Model Architecture

"**Model Architecture:**

**Core Model:**
| Property | Value |
|----------|-------|
| Family | {e.g., YOLOv8} |
| Variant | {e.g., yolov8m} |
| Pretrained weights | {path} |
| Config | {path} |

**Modifications:**
{any customizations from base}"

### 3. Document Data Pipeline

"**Data Pipeline:**

**Preprocessing:**
| Step | Implementation | Parameters |
|------|---------------|------------|
{rows}

**Augmentations:**
| Augmentation | Probability | Config |
|--------------|-------------|--------|
{rows}"

### 4. Document Training Configuration

"**Training Configuration:**

| Parameter | Value | Config Location |
|-----------|-------|-----------------|
| Optimizer | {name} | {path} |
| Learning rate | {value} | {path} |
| Batch size | {value} | {path} |
..."

### 5. Document Inference Pipeline

"**Inference:**

**Single Sample:**
```bash
{command to run inference}
```

**Batch Inference:**
```bash
{command}
```

**Evaluation:**
```bash
{command}
```"

### 6. Create Current Architecture Document

Load {archTemplateFile} and create {archOutputFile}:

```markdown
---
lastUpdated: {date}
performance: {metric} = {value}
productionCheckpoint: {path}
---

# Current Architecture

## 1. Model Architecture
{documented above}

## 2. Data Pipeline
{documented above}

## 3. Training Configuration
{documented above}

## 4. Post-Processing
{if applicable}

## 5. Inference
{documented above}

## 6. Validated Changes Log
| Date | Change | Impact | Files |
|------|--------|--------|-------|
{from brownfield history}

## 7. Reproducibility
{environment, commands, seeds}
```

### 7. Create Technical Spec

Load {specTemplateFile} and create {specOutputFile}:

```markdown
---
created: {date}
status: CURRENT STATE
---

# Technical Specification

## Overview
{what the system does}

## Architecture Diagram
{text description or ASCII}

## Components

### Data Loading
- Implementation: {path}
- Purpose: {description}
- Interface: {inputs/outputs}

### Preprocessing
...

### Model
...

### Training
...

### Evaluation
...

## Configuration
{key configs and their locations}

## Extension Points
{where new experiments can plug in}

## Known Limitations
{honest assessment}
```

### 8. Update Sidecar

Update stepsCompleted.

### 9. Menu

"**Architecture Documentation Complete**

- current-architecture.md created
- technical-spec.md created

**[A]** Advanced Elicitation
**[P]** Party Mode
**[C]** Continue to Architecture Review"

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:
- Code structure analyzed
- Both documents created
- Honest about code quality
- Extension points identified
- User confirmed accuracy

### ❌ SYSTEM FAILURE:
- Documenting aspirational not actual
- Missing key components
- Not identifying limitations
- Modifying code

**Master Rule:** Document what exists honestly and completely.
