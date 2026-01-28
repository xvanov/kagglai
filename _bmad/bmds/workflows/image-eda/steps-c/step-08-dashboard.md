---
name: 'step-08-dashboard'
description: 'Spawn Rex (Implementer) to build interactive Streamlit dashboard - USER CHECKPOINT for review'

nextStepFile: './step-09-model-selection.md'
stateFile: '{experiments_folder}/.image-eda-state.yaml'
dashboardFolder: '{experiments_folder}/eda/dashboard'
phaseOutputFile: '{experiments_folder}/.phase-08-output.md'
edaReportFile: '{docs_folder}/eda-report-images.md'
dashboardRequirements: '../data/dashboard-requirements.md'
implementerAgent: '{project-root}/_bmad/bmds/agents/implementer/implementer.agent.yaml'
---

# Step 8: Dashboard Generation

## STEP GOAL:

To spawn Rex (Implementer agent) to build an interactive Streamlit dashboard for exploring EDA findings, then checkpoint with user for review and modifications.

## MANDATORY EXECUTION RULES (READ FIRST):

### Universal Rules:

- 🛑 NEVER generate content without user input
- 📖 CRITICAL: Read the complete step file before taking any action
- 🔄 CRITICAL: When loading next step with 'C', ensure entire file is read
- 📋 YOU ARE THE ORCHESTRATOR spawning a sub-agent
- ✅ YOU MUST ALWAYS SPEAK OUTPUT in your agent communication style with the config `{communication_language}`
- ⚙️ TOOL/SUBPROCESS FALLBACK: If subprocess/sub-agent unavailable, perform in main thread

### Role Reinforcement:

- ✅ You are the workflow orchestrator delegating to Rex (Implementer)
- ✅ Rex specializes in building clean, functional applications
- ✅ This is a USER CHECKPOINT - user reviews and can request changes
- ✅ Dashboard should be shareable with team

### Step-Specific Rules:

- 🎯 Spawn Rex to build Streamlit dashboard
- 🚫 FORBIDDEN to build dashboard yourself - delegate to Rex
- 💬 USER CHECKPOINT - get explicit approval before proceeding
- 🤖 Sub-agent should stay under 50% context window

## EXECUTION PROTOCOLS:

- 🎯 Load dashboard requirements and all phase outputs
- 💾 Rex writes dashboard to {dashboardFolder}
- 📖 Rex writes summary to {phaseOutputFile}
- ⏸️ CHECKPOINT: User reviews dashboard before proceeding

## CONTEXT BOUNDARIES:

- All analysis and insights complete (Phases 3-7)
- Dashboard consolidates all findings
- User can run dashboard locally to review
- This is the main deliverable of the EDA

## MANDATORY SEQUENCE

**CRITICAL:** Follow this sequence exactly.

### 1. Load Requirements and Context

Load {dashboardRequirements} for dashboard specifications.

Load {stateFile} and all phase outputs:
- `phase_outputs.phase_03` through `phase_outputs.phase_07`

### 2. Spawn Rex (Implementer) Sub-Agent

**Launch a sub-agent with the following task:**

"You are Rex (Implementer). Build an interactive Streamlit dashboard for Image EDA.

**Dashboard Requirements:** (from {dashboardRequirements})

**EDA Findings to Display:**
- Basic Stats: {phase_03 summary}
- Label Analysis: {phase_04 summary}
- Visual Patterns: {phase_05 summary}
- Data Quality: {phase_06 summary}
- Insights: {phase_07 summary}

**Your Task:**
Create dashboard at `{dashboardFolder}/`:

1. **App Structure:**
   ```
   {dashboardFolder}/
   ├── app.py              # Main Streamlit app
   ├── pages/
   │   ├── 1_overview.py
   │   ├── 2_image_browser.py
   │   ├── 3_label_analysis.py
   │   ├── 4_quality_assessment.py
   │   └── 5_insights.py
   └── utils/
       └── data_loader.py
   ```

2. **Overview Page:**
   - Dataset statistics summary
   - Class distribution chart
   - Quality breakdown
   - Key insights bullets

3. **Image Browser:**
   - Grid view of thumbnails
   - Filter by class, quality level
   - Click to expand with metadata
   - Label overlay toggle

4. **Label Analysis:**
   - Class distribution visualization
   - Imbalance indicator
   - Problem labels section

5. **Quality Assessment:**
   - Quality distribution chart
   - Good vs bad examples side-by-side
   - Filter threshold controls
   - Preview filtered dataset

6. **Insights Summary:**
   - Critical findings
   - Strengths/weaknesses
   - Recommendations

**Code Quality:**
- Use `@st.cache_data` for performance
- Lazy loading for images
- Clear error handling
- Mobile-responsive layout

**After building, write summary to {phaseOutputFile} including:**
- Dashboard location
- How to run
- Features implemented
- Any limitations"

### 3. Verify Sub-Agent Output

After Rex completes, verify:
- [ ] Dashboard app exists at {dashboardFolder}/app.py
- [ ] All pages created
- [ ] Phase output file exists

### 4. Update State File (Before Checkpoint)

Update {stateFile}:
```yaml
stepsCompleted: [..., 'step-08-dashboard']
currentPhase: 'dashboard-generated'
phase_outputs:
  phase_08: '{phaseOutputFile}'
```

### 5. USER CHECKPOINT - Present Dashboard for Review

"**Phase 8: Dashboard Generated**

**Dashboard Location:** `{dashboardFolder}/`

**To preview the dashboard, run:**
```bash
streamlit run {dashboardFolder}/app.py
```

**Features Implemented:**
{list from phase output}

---

**This is a checkpoint. Please review the dashboard before proceeding.**

You can:
- Run the dashboard locally to explore
- Ask questions about the data or findings
- Request modifications to the dashboard

**Review Options:**

**[Q]** Ask questions about the data or findings
**[M]** Request modifications to the dashboard
**[C]** Continue to Phase 9: Model Selection (dashboard approved)"

### 6. Handle User Review

#### IF Q (Questions):

"What would you like to know about the data or findings?"

Answer user's question using phase output files.
After answering, redisplay review options.

#### IF M (Modifications):

"What modifications would you like to the dashboard?"

Capture modification request, then spawn Rex again:

"Rex, please modify the dashboard at `{dashboardFolder}/` with the following changes:

{user's modification request}

Update the dashboard and report what was changed."

After Rex completes, redisplay review options.

#### IF C (Continue):

User has approved the dashboard.
Load, read entire file, then execute {nextStepFile}

#### IF Any Other:

Help user, then redisplay review options.

---

## 🚨 SYSTEM SUCCESS/FAILURE METRICS

### ✅ SUCCESS:

- Rex sub-agent spawned with clear requirements
- Dashboard created with all required pages
- Dashboard is functional and runnable
- User checkpoint presented
- User explicitly approves before proceeding

### ❌ SYSTEM FAILURE:

- Building dashboard directly instead of delegating
- Skipping user checkpoint
- Proceeding without user approval
- Dashboard not functional

**Master Rule:** Orchestrator delegates. Rex builds. User approves at checkpoint.
