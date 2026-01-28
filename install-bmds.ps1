# BMDS Installer Script for Windows
# Usage: .\install-bmds.ps1 -TargetRepo "C:\path\to\target\repo"

param(
    [Parameter(Position=0)]
    [string]$TargetRepo,

    [switch]$Minimal,
    [switch]$SkipStructure,
    [switch]$Help
)

# Colors for output (Windows Terminal supports these)
function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

function Show-Usage {
    Write-Host @"
Usage: .\install-bmds.ps1 [OPTIONS] <target-repo-path>

Install BMDS (BMAD Data Science) module into a target repository.

Options:
  -Minimal          Only install BMDS + core (skip other modules)
  -SkipStructure    Don't create project folder structure
  -Help             Show this help message

Examples:
  .\install-bmds.ps1 C:\path\to\my-project
  .\install-bmds.ps1 -Minimal C:\path\to\my-project
"@
    exit 1
}

# Show help if requested
if ($Help) {
    Show-Usage
}

# Validate target repo
if ([string]::IsNullOrEmpty($TargetRepo)) {
    Write-ColorOutput "Error: Target repository path is required" "Red"
    Show-Usage
}

# Get script directory (source repo)
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceBmad = Join-Path $ScriptDir "_bmad"

# Convert to absolute path and validate
try {
    $TargetRepo = Resolve-Path $TargetRepo -ErrorAction Stop
} catch {
    Write-ColorOutput "Error: Target path does not exist: $TargetRepo" "Red"
    exit 1
}

$TargetBmad = Join-Path $TargetRepo "_bmad"

Write-Host ""
Write-ColorOutput "========================================" "Blue"
Write-ColorOutput "  BMDS Installer (Windows)" "Blue"
Write-ColorOutput "========================================" "Blue"
Write-Host ""
Write-Host "Source: " -NoNewline
Write-ColorOutput $SourceBmad "Yellow"
Write-Host "Target: " -NoNewline
Write-ColorOutput $TargetRepo "Yellow"
Write-Host ""

# Check source exists
$BmdsSource = Join-Path $SourceBmad "bmds"
if (-not (Test-Path $BmdsSource)) {
    Write-ColorOutput "Error: BMDS module not found at $BmdsSource" "Red"
    exit 1
}

# Create _bmad directory if needed
if (-not (Test-Path $TargetBmad)) {
    New-Item -ItemType Directory -Path $TargetBmad -Force | Out-Null
}

# =============================================================================
# INSTALL CORE (if needed)
# =============================================================================

$CoreTarget = Join-Path $TargetBmad "core"
$CoreSource = Join-Path $SourceBmad "core"

if (-not (Test-Path $CoreTarget)) {
    Write-ColorOutput "Installing BMAD core..." "Green"
    Copy-Item -Path $CoreSource -Destination $CoreTarget -Recurse -Force
    Write-Host "  " -NoNewline
    Write-ColorOutput "[OK]" "Green" -NoNewline
    Write-Host " Copied core/"
} else {
    Write-Host "  " -NoNewline
    Write-ColorOutput "[->]" "Yellow" -NoNewline
    Write-Host " core/ already exists, skipping"
}

# =============================================================================
# INSTALL BMDS MODULE
# =============================================================================

$BmdsTarget = Join-Path $TargetBmad "bmds"

if (Test-Path $BmdsTarget) {
    Write-Host ""
    Write-ColorOutput "Warning: BMDS already exists at $BmdsTarget" "Yellow"
    $response = Read-Host "Overwrite? (y/N)"
    if ($response -match "^[Yy]$") {
        Remove-Item -Path $BmdsTarget -Recurse -Force
        Copy-Item -Path $BmdsSource -Destination $BmdsTarget -Recurse -Force
        Write-Host "  " -NoNewline
        Write-ColorOutput "[OK]" "Green" -NoNewline
        Write-Host " Copied bmds/"
    } else {
        Write-ColorOutput "Skipping BMDS installation" "Yellow"
    }
} else {
    Write-ColorOutput "Installing BMDS module..." "Green"
    Copy-Item -Path $BmdsSource -Destination $BmdsTarget -Recurse -Force
    Write-Host "  " -NoNewline
    Write-ColorOutput "[OK]" "Green" -NoNewline
    Write-Host " Copied bmds/"
}

# =============================================================================
# INSTALL CONFIG (if needed)
# =============================================================================

$ConfigTarget = Join-Path $TargetBmad "_config"
$ConfigSource = Join-Path $SourceBmad "_config"

if (-not (Test-Path $ConfigTarget)) {
    Write-ColorOutput "Installing BMAD config..." "Green"
    Copy-Item -Path $ConfigSource -Destination $ConfigTarget -Recurse -Force
    Write-Host "  " -NoNewline
    Write-ColorOutput "[OK]" "Green" -NoNewline
    Write-Host " Copied _config/"
}

# =============================================================================
# INSTALL MEMORY (if needed)
# =============================================================================

$MemoryTarget = Join-Path $TargetBmad "_memory"
$MemorySource = Join-Path $SourceBmad "_memory"

if (-not (Test-Path $MemoryTarget)) {
    Write-ColorOutput "Installing BMAD memory..." "Green"
    Copy-Item -Path $MemorySource -Destination $MemoryTarget -Recurse -Force
    Write-Host "  " -NoNewline
    Write-ColorOutput "[OK]" "Green" -NoNewline
    Write-Host " Copied _memory/"
}

# =============================================================================
# UPDATE MANIFEST
# =============================================================================

$ManifestFile = Join-Path $ConfigTarget "manifest.yaml"

if (Test-Path $ManifestFile) {
    $manifestContent = Get-Content $ManifestFile -Raw
    if ($manifestContent -match "bmds") {
        Write-Host "  " -NoNewline
        Write-ColorOutput "[->]" "Yellow" -NoNewline
        Write-Host " bmds already in manifest"
    } else {
        Write-ColorOutput "Adding bmds to manifest..." "Green"
        # Add bmds after modules: line
        $manifestContent = $manifestContent -replace "(modules:)", "`$1`n  - bmds"
        Set-Content -Path $ManifestFile -Value $manifestContent -NoNewline
        Write-Host "  " -NoNewline
        Write-ColorOutput "[OK]" "Green" -NoNewline
        Write-Host " Updated manifest.yaml"
    }
} else {
    Write-ColorOutput "Creating manifest..." "Green"
    if (-not (Test-Path $ConfigTarget)) {
        New-Item -ItemType Directory -Path $ConfigTarget -Force | Out-Null
    }
    $today = Get-Date -Format "yyyy-MM-ddTHH:mm:sszzz"
    $manifestContent = @"
installation:
  version: 6.0.0
  installDate: $today
modules:
  - core
  - bmds
ides:
  - claude-code
"@
    Set-Content -Path $ManifestFile -Value $manifestContent
    Write-Host "  " -NoNewline
    Write-ColorOutput "[OK]" "Green" -NoNewline
    Write-Host " Created manifest.yaml"
}

# =============================================================================
# INSTALL CLAUDE CODE COMMAND STUBS
# =============================================================================

$SourceCommands = Join-Path $ScriptDir ".claude\commands\bmad"
$TargetClaudeDir = Join-Path $TargetRepo ".claude\commands"
$TargetCommands = Join-Path $TargetClaudeDir "bmad"

if (Test-Path $SourceCommands) {
    Write-ColorOutput "Installing Claude Code command stubs..." "Green"

    # Create .claude/commands if needed
    if (-not (Test-Path $TargetClaudeDir)) {
        New-Item -ItemType Directory -Path $TargetClaudeDir -Force | Out-Null
    }

    # Remove existing and copy fresh
    if (Test-Path $TargetCommands) {
        Remove-Item -Path $TargetCommands -Recurse -Force
    }
    Copy-Item -Path $SourceCommands -Destination $TargetCommands -Recurse -Force
    Write-Host "  " -NoNewline
    Write-ColorOutput "[OK]" "Green" -NoNewline
    Write-Host " Copied .claude/commands/bmad/"
} else {
    Write-ColorOutput "Warning: Claude Code commands not found at $SourceCommands" "Yellow"
}

# =============================================================================
# CREATE PROJECT STRUCTURE
# =============================================================================

if (-not $SkipStructure) {
    Write-ColorOutput "Creating project structure..." "Green"

    # BMDS output folder
    $bmdsOutput = Join-Path $TargetRepo "_bmds"
    New-Item -ItemType Directory -Path (Join-Path $bmdsOutput "docs") -Force | Out-Null
    New-Item -ItemType Directory -Path (Join-Path $bmdsOutput "problem-inputs") -Force | Out-Null
    Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created _bmds/docs/"
    Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created _bmds/problem-inputs/"

    # Source code
    @("data", "models", "training", "evaluation", "utils") | ForEach-Object {
        New-Item -ItemType Directory -Path (Join-Path $TargetRepo "src\$_") -Force | Out-Null
    }
    Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created src/"

    # Data folders
    @("raw", "processed", "splits") | ForEach-Object {
        New-Item -ItemType Directory -Path (Join-Path $TargetRepo "data\$_") -Force | Out-Null
    }
    Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created data/"

    # Models
    @("checkpoints", "baselines") | ForEach-Object {
        New-Item -ItemType Directory -Path (Join-Path $TargetRepo "models\$_") -Force | Out-Null
    }
    Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created models/"

    # Experiments
    New-Item -ItemType Directory -Path (Join-Path $bmdsOutput "experiments") -Force | Out-Null
    Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created _bmds/experiments/"

    # Notebooks
    @("exploration", "analysis") | ForEach-Object {
        New-Item -ItemType Directory -Path (Join-Path $TargetRepo "notebooks\$_") -Force | Out-Null
    }
    Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created notebooks/"

    # Outputs
    @("predictions", "reports") | ForEach-Object {
        New-Item -ItemType Directory -Path (Join-Path $TargetRepo "outputs\$_") -Force | Out-Null
    }
    Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created outputs/"

    # Create living documents
    $today = Get-Date -Format "yyyy-MM-dd"
    $docsFolder = Join-Path $bmdsOutput "docs"

    $currentUnderstanding = Join-Path $docsFolder "current-understanding.md"
    if (-not (Test-Path $currentUnderstanding)) {
        $content = @"
# Current Understanding

**Last Updated:** $today

---

## 1. Problem & Task

*To be populated during project-init*

## 2. Data

*To be populated during EDA*

## 3. Model

*To be populated during research*

## 4. Training & Pipeline

*To be populated during implementation*

## 5. Post-Processing

*To be populated as needed*

## 6. Open Questions

*Questions that need investigation*

---

## Change Log

| Date | Source | Section | Summary |
|------|--------|---------|---------|
"@
        Set-Content -Path $currentUnderstanding -Value $content
        Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created current-understanding.md"
    }

    $currentArchitecture = Join-Path $docsFolder "current-architecture.md"
    if (-not (Test-Path $currentArchitecture)) {
        $content = @"
# Current Architecture

**Last Updated:** $today

---

## System Overview

*To be populated after baseline implementation*

## Data Pipeline

*Data loading, preprocessing, feature engineering*

## Model Architecture

*Current model configuration*

## Training Configuration

*Hyperparameters, optimization settings*

## Inference Pipeline

*How to generate predictions*

---

## Change Log

| Date | Source | Summary |
|------|--------|---------|
"@
        Set-Content -Path $currentArchitecture -Value $content
        Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created current-architecture.md"
    }

    $hypothesisRegistry = Join-Path $docsFolder "hypothesis-registry.md"
    if (-not (Test-Path $hypothesisRegistry)) {
        $content = @"
# Hypothesis Registry

**Last Updated:** $today

---

## Active Hypotheses

*None yet - run project-init to generate initial hypotheses*

## Validated Hypotheses

*Hypotheses confirmed by experiments*

## Rejected Hypotheses

*Hypotheses disproven by experiments*

---

## Experiment Log

| EXP-ID | Hypothesis | Status | Result | Date |
|--------|------------|--------|--------|------|

---

## Statistics

- **Total Experiments:** 0
- **Validated:** 0
- **Rejected:** 0
- **In Progress:** 0
"@
        Set-Content -Path $hypothesisRegistry -Value $content
        Write-Host "  " -NoNewline; Write-ColorOutput "[OK]" "Green" -NoNewline; Write-Host " Created hypothesis-registry.md"
    }
}

# =============================================================================
# DONE
# =============================================================================

Write-Host ""
Write-ColorOutput "========================================" "Green"
Write-ColorOutput "  BMDS Installation Complete!" "Green"
Write-ColorOutput "========================================" "Green"
Write-Host ""
Write-Host "Installed to: " -NoNewline
Write-ColorOutput $TargetRepo "Yellow"
Write-Host ""
Write-ColorOutput "Next steps:" "Blue"
Write-Host "  1. cd $TargetRepo"
Write-Host "  2. Add problem definition files to _bmds/problem-inputs/"
Write-Host "  3. Run: /bmad:bmds:workflows:project-init"
Write-Host ""
Write-ColorOutput "Available workflows:" "Blue"
Write-Host "  - /bmad:bmds:workflows:project-init    (Initialize new project)"
Write-Host "  - /bmad:bmds:workflows:project-pickup  (Pick up brownfield project)"
Write-Host "  - /bmad:bmds:workflows:image-eda       (Image data EDA)"
Write-Host "  - /bmad:bmds:workflows:experiment-cycle (Run experiments)"
Write-Host ""
Write-ColorOutput "Available agents:" "Blue"
Write-Host "  - /bmad:bmds:agents:data-analyst   (Atlas - EDA specialist)"
Write-Host "  - /bmad:bmds:agents:researcher     (Owl - SOTA research)"
Write-Host "  - /bmad:bmds:agents:data-scientist (Feynman - Hypothesis design)"
Write-Host "  - /bmad:bmds:agents:implementer    (Rex - Implementation)"
Write-Host ""
