const fs = require('fs-extra');
const path = require('node:path');
const chalk = require('chalk');

/**
 * BMDS (BMAD Data Science) Module Installer
 *
 * Creates project structure and initializes MLOps tooling
 */
async function install(options) {
  const { projectRoot, config, logger } = options;

  try {
    logger.log(chalk.blue('Installing BMDS (BMAD Data Science)...'));

    // =======================================================================
    // CREATE DIRECTORY STRUCTURE
    // =======================================================================

    const directories = [
      { key: 'bmds_output_folder', subdirs: ['docs', 'problem-inputs'] },
      { key: 'source_folder', subdirs: ['data', 'models', 'training', 'evaluation', 'utils'] },
      { key: 'data_folder', subdirs: ['raw', 'processed', 'splits'] },
      { key: 'models_folder', subdirs: ['checkpoints', 'production'] },
      { key: 'experiments_folder', subdirs: [] },
      { key: 'notebooks_folder', subdirs: ['exploration', 'analysis'] },
      { key: 'outputs_folder', subdirs: ['predictions', 'reports'] },
    ];

    for (const dir of directories) {
      const dirValue = config[dir.key];
      if (dirValue) {
        const dirPath = resolvePath(projectRoot, dirValue);
        await ensureDirectory(dirPath, logger);

        // Create subdirectories
        for (const subdir of dir.subdirs) {
          await ensureDirectory(path.join(dirPath, subdir), logger);
        }
      }
    }

    // =======================================================================
    // CREATE LIVING DOCUMENTS
    // =======================================================================

    const bmdsFolder = resolvePath(projectRoot, config.bmds_output_folder);

    await createLivingDocument(
      path.join(bmdsFolder, 'current-understanding.md'),
      getCurrentUnderstandingTemplate(config.project_name),
      logger
    );

    await createLivingDocument(
      path.join(bmdsFolder, 'current-architecture.md'),
      getCurrentArchitectureTemplate(config.project_name),
      logger
    );

    await createLivingDocument(
      path.join(bmdsFolder, 'hypothesis-registry.md'),
      getHypothesisRegistryTemplate(config.project_name),
      logger
    );

    // =======================================================================
    // INITIALIZE MLFLOW (if enabled)
    // =======================================================================

    if (config.enable_mlflow) {
      logger.log(chalk.yellow('MLflow integration enabled'));
      logger.log(chalk.dim('  Run: pip install mlflow'));
      logger.log(chalk.dim('  Tracking URI: ' + (config.mlflow_tracking_uri || './mlruns')));
    }

    // =======================================================================
    // INITIALIZE DVC (if enabled)
    // =======================================================================

    if (config.enable_dvc) {
      logger.log(chalk.yellow('DVC integration enabled'));
      logger.log(chalk.dim('  Run: pip install dvc'));
      logger.log(chalk.dim('  Then: dvc init'));
    }

    // =======================================================================
    // CREATE .gitignore ADDITIONS
    // =======================================================================

    await appendGitignore(projectRoot, logger);

    // =======================================================================
    // CREATE requirements.txt TEMPLATE
    // =======================================================================

    await createRequirements(projectRoot, config, logger);

    logger.log(chalk.green('✓ BMDS installation complete'));
    logger.log('');
    logger.log(chalk.cyan('Next steps:'));
    logger.log(chalk.dim('  1. pip install -r requirements.txt'));
    logger.log(chalk.dim('  2. Run project-init workflow to set up your project'));

    return true;
  } catch (error) {
    logger.error(chalk.red(`Error installing BMDS: ${error.message}`));
    return false;
  }
}

// =============================================================================
// HELPER FUNCTIONS
// =============================================================================

function resolvePath(projectRoot, configValue) {
  // Remove {project-root}/ prefix if present
  const cleanPath = configValue.replace(/^\{project-root\}[\/\\]?/, '');
  return path.join(projectRoot, cleanPath);
}

async function ensureDirectory(dirPath, logger) {
  if (!(await fs.pathExists(dirPath))) {
    logger.log(chalk.dim(`  Creating: ${path.relative(process.cwd(), dirPath)}/`));
    await fs.ensureDir(dirPath);
  }
}

async function createLivingDocument(filePath, content, logger) {
  if (!(await fs.pathExists(filePath))) {
    logger.log(chalk.dim(`  Creating: ${path.basename(filePath)}`));
    await fs.writeFile(filePath, content, 'utf8');
  }
}

async function appendGitignore(projectRoot, logger) {
  const gitignorePath = path.join(projectRoot, '.gitignore');
  const bmdsIgnores = `
# BMDS - Data Science Artifacts
data/raw/
data/processed/
data/splits/
models/checkpoints/
models/production/
*.pkl
*.joblib
*.h5
*.pt
*.pth
*.onnx

# MLflow
mlruns/
mlartifacts/

# DVC
/dvc.lock
*.dvc

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Outputs
outputs/predictions/
outputs/reports/*.pdf
`;

  try {
    let existingContent = '';
    if (await fs.pathExists(gitignorePath)) {
      existingContent = await fs.readFile(gitignorePath, 'utf8');
    }

    if (!existingContent.includes('# BMDS')) {
      logger.log(chalk.dim('  Updating .gitignore'));
      await fs.appendFile(gitignorePath, bmdsIgnores);
    }
  } catch (error) {
    logger.warn(chalk.yellow(`Could not update .gitignore: ${error.message}`));
  }
}

async function createRequirements(projectRoot, config, logger) {
  const requirementsPath = path.join(projectRoot, 'requirements.txt');

  if (await fs.pathExists(requirementsPath)) {
    return; // Don't overwrite existing requirements
  }

  let content = `# BMDS Data Science Requirements
# Core
numpy
pandas
scikit-learn
scipy

# Visualization
matplotlib
seaborn

# Jupyter
jupyter
ipykernel
`;

  if (config.enable_mlflow) {
    content += `
# MLflow
mlflow
`;
  }

  if (config.enable_dvc) {
    content += `
# DVC
dvc
`;
  }

  content += `
# Deep Learning (uncomment as needed)
# torch
# torchvision
# tensorflow
# keras

# Tabular Models (uncomment as needed)
# xgboost
# lightgbm
# catboost
`;

  logger.log(chalk.dim('  Creating requirements.txt'));
  await fs.writeFile(requirementsPath, content, 'utf8');
}

// =============================================================================
// LIVING DOCUMENT TEMPLATES
// =============================================================================

function getCurrentUnderstandingTemplate(projectName) {
  return `# Current Understanding: ${projectName || 'Project'}

> This document captures what we know about the data, problem, and effective approaches.
> Updated after each experiment with new learnings.

---

## Problem Context

*To be populated during project-init*

## Data Insights

*To be populated during EDA*

## What Works

*To be populated as experiments validate approaches*

## What Doesn't Work

*To be populated as experiments invalidate approaches*

## Open Questions

*Questions that need investigation*

---

*Last updated: ${new Date().toISOString().split('T')[0]}*
`;
}

function getCurrentArchitectureTemplate(projectName) {
  return `# Current Architecture: ${projectName || 'Project'}

> This document describes the current production-ready system.
> Only updated when validated experiments are integrated.

---

## System Overview

*To be populated after baseline implementation*

## Data Pipeline

*Data loading, preprocessing, feature engineering*

## Model Architecture

*Current model configuration*

## Training Configuration

*Hyperparameters, optimization settings*

## Evaluation

*Metrics, validation strategy*

---

*Last updated: ${new Date().toISOString().split('T')[0]}*
`;
}

function getHypothesisRegistryTemplate(projectName) {
  return `# Hypothesis Registry: ${projectName || 'Project'}

> All hypotheses and their outcomes, maintaining a complete audit trail.

---

## Registry

| ID | Hypothesis | Status | Result | Learnings |
|----|------------|--------|--------|-----------|
| - | *None yet* | - | - | - |

---

## Experiment Index

*Links to experiment folders*

---

## Statistics

- **Total Experiments:** 0
- **Validated:** 0
- **Invalidated:** 0
- **In Progress:** 0

---

*Last updated: ${new Date().toISOString().split('T')[0]}*
`;
}

module.exports = { install };
