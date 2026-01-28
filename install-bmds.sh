#!/bin/bash

# BMDS Installer Script
# Usage: ./install-bmds.sh /path/to/target/repo

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Get the directory where this script lives (source repo)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_BMAD="$SCRIPT_DIR/_bmad"

# Parse arguments
TARGET_REPO=""
MINIMAL=false
SKIP_STRUCTURE=false

usage() {
    echo "Usage: $0 [OPTIONS] <target-repo-path>"
    echo ""
    echo "Install BMDS (BMAD Data Science) module into a target repository."
    echo ""
    echo "Options:"
    echo "  -m, --minimal       Only install BMDS + core (skip other modules)"
    echo "  -s, --skip-structure  Don't create project folder structure"
    echo "  -h, --help          Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 /path/to/my-project"
    echo "  $0 --minimal /path/to/my-project"
    exit 1
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -m|--minimal)
            MINIMAL=true
            shift
            ;;
        -s|--skip-structure)
            SKIP_STRUCTURE=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        -*)
            echo -e "${RED}Unknown option: $1${NC}"
            usage
            ;;
        *)
            TARGET_REPO="$1"
            shift
            ;;
    esac
done

# Validate target repo
if [ -z "$TARGET_REPO" ]; then
    echo -e "${RED}Error: Target repository path is required${NC}"
    usage
fi

# Convert to absolute path
TARGET_REPO="$(cd "$TARGET_REPO" 2>/dev/null && pwd)" || {
    echo -e "${RED}Error: Target path does not exist: $TARGET_REPO${NC}"
    exit 1
}

TARGET_BMAD="$TARGET_REPO/_bmad"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  BMDS Installer${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "Source: ${YELLOW}$SOURCE_BMAD${NC}"
echo -e "Target: ${YELLOW}$TARGET_REPO${NC}"
echo ""

# Check source exists
if [ ! -d "$SOURCE_BMAD/bmds" ]; then
    echo -e "${RED}Error: BMDS module not found at $SOURCE_BMAD/bmds${NC}"
    exit 1
fi

# Create _bmad directory if needed
mkdir -p "$TARGET_BMAD"

# =============================================================================
# INSTALL CORE (if needed)
# =============================================================================

if [ ! -d "$TARGET_BMAD/core" ]; then
    echo -e "${GREEN}Installing BMAD core...${NC}"
    cp -r "$SOURCE_BMAD/core" "$TARGET_BMAD/core"
    echo -e "  ${GREEN}✓${NC} Copied core/"
else
    echo -e "  ${YELLOW}→${NC} core/ already exists, skipping"
fi

# =============================================================================
# INSTALL BMDS MODULE
# =============================================================================

if [ -d "$TARGET_BMAD/bmds" ]; then
    echo ""
    echo -e "${YELLOW}Warning: BMDS already exists at $TARGET_BMAD/bmds${NC}"
    read -p "Overwrite? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${YELLOW}Skipping BMDS installation${NC}"
    else
        rm -rf "$TARGET_BMAD/bmds"
        cp -r "$SOURCE_BMAD/bmds" "$TARGET_BMAD/bmds"
        echo -e "  ${GREEN}✓${NC} Copied bmds/"
    fi
else
    echo -e "${GREEN}Installing BMDS module...${NC}"
    cp -r "$SOURCE_BMAD/bmds" "$TARGET_BMAD/bmds"
    echo -e "  ${GREEN}✓${NC} Copied bmds/"
fi

# =============================================================================
# INSTALL CONFIG (if needed)
# =============================================================================

if [ ! -d "$TARGET_BMAD/_config" ]; then
    echo -e "${GREEN}Installing BMAD config...${NC}"
    cp -r "$SOURCE_BMAD/_config" "$TARGET_BMAD/_config"
    echo -e "  ${GREEN}✓${NC} Copied _config/"
fi

# =============================================================================
# INSTALL MEMORY (if needed)
# =============================================================================

if [ ! -d "$TARGET_BMAD/_memory" ]; then
    echo -e "${GREEN}Installing BMAD memory...${NC}"
    cp -r "$SOURCE_BMAD/_memory" "$TARGET_BMAD/_memory"
    echo -e "  ${GREEN}✓${NC} Copied _memory/"
fi

# =============================================================================
# UPDATE MANIFEST
# =============================================================================

MANIFEST_FILE="$TARGET_BMAD/_config/manifest.yaml"

if [ -f "$MANIFEST_FILE" ]; then
    # Check if bmds is already in manifest
    if grep -q "bmds" "$MANIFEST_FILE"; then
        echo -e "  ${YELLOW}→${NC} bmds already in manifest"
    else
        echo -e "${GREEN}Adding bmds to manifest...${NC}"
        # Add bmds to modules list
        sed -i '/^modules:/a\  - bmds' "$MANIFEST_FILE"
        echo -e "  ${GREEN}✓${NC} Updated manifest.yaml"
    fi
else
    echo -e "${GREEN}Creating manifest...${NC}"
    mkdir -p "$TARGET_BMAD/_config"
    cat > "$MANIFEST_FILE" << 'EOF'
installation:
  version: 6.0.0
  installDate: $(date -Iseconds)
modules:
  - core
  - bmds
ides:
  - claude-code
EOF
    echo -e "  ${GREEN}✓${NC} Created manifest.yaml"
fi

# =============================================================================
# CREATE PROJECT STRUCTURE
# =============================================================================

if [ "$SKIP_STRUCTURE" = false ]; then
    echo -e "${GREEN}Creating project structure...${NC}"

    # BMDS output folder
    mkdir -p "$TARGET_REPO/_bmds/docs"
    mkdir -p "$TARGET_REPO/_bmds/problem-inputs"
    echo -e "  ${GREEN}✓${NC} Created _bmds/docs/"
    echo -e "  ${GREEN}✓${NC} Created _bmds/problem-inputs/"

    # Source code
    mkdir -p "$TARGET_REPO/src/data"
    mkdir -p "$TARGET_REPO/src/models"
    mkdir -p "$TARGET_REPO/src/training"
    mkdir -p "$TARGET_REPO/src/evaluation"
    mkdir -p "$TARGET_REPO/src/utils"
    echo -e "  ${GREEN}✓${NC} Created src/"

    # Data folders
    mkdir -p "$TARGET_REPO/data/raw"
    mkdir -p "$TARGET_REPO/data/processed"
    mkdir -p "$TARGET_REPO/data/splits"
    echo -e "  ${GREEN}✓${NC} Created data/"

    # Models
    mkdir -p "$TARGET_REPO/models/checkpoints"
    mkdir -p "$TARGET_REPO/models/baselines"
    echo -e "  ${GREEN}✓${NC} Created models/"

    # Experiments (for experiment-cycle)
    mkdir -p "$TARGET_REPO/_bmds/experiments"
    echo -e "  ${GREEN}✓${NC} Created _bmds/experiments/"

    # Notebooks
    mkdir -p "$TARGET_REPO/notebooks/exploration"
    mkdir -p "$TARGET_REPO/notebooks/analysis"
    echo -e "  ${GREEN}✓${NC} Created notebooks/"

    # Outputs
    mkdir -p "$TARGET_REPO/outputs/predictions"
    mkdir -p "$TARGET_REPO/outputs/reports"
    echo -e "  ${GREEN}✓${NC} Created outputs/"

    # Create living documents if they don't exist
    if [ ! -f "$TARGET_REPO/_bmds/docs/current-understanding.md" ]; then
        cat > "$TARGET_REPO/_bmds/docs/current-understanding.md" << 'EOF'
# Current Understanding

**Last Updated:** $(date +%Y-%m-%d)

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
EOF
        echo -e "  ${GREEN}✓${NC} Created current-understanding.md"
    fi

    if [ ! -f "$TARGET_REPO/_bmds/docs/current-architecture.md" ]; then
        cat > "$TARGET_REPO/_bmds/docs/current-architecture.md" << 'EOF'
# Current Architecture

**Last Updated:** $(date +%Y-%m-%d)

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
EOF
        echo -e "  ${GREEN}✓${NC} Created current-architecture.md"
    fi

    if [ ! -f "$TARGET_REPO/_bmds/docs/hypothesis-registry.md" ]; then
        cat > "$TARGET_REPO/_bmds/docs/hypothesis-registry.md" << 'EOF'
# Hypothesis Registry

**Last Updated:** $(date +%Y-%m-%d)

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
EOF
        echo -e "  ${GREEN}✓${NC} Created hypothesis-registry.md"
    fi
fi

# =============================================================================
# DONE
# =============================================================================

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  BMDS Installation Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "Installed to: ${YELLOW}$TARGET_REPO${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "  1. cd $TARGET_REPO"
echo "  2. Add problem definition files to _bmds/problem-inputs/"
echo "  3. Run: /bmad:bmds:workflows:project-init"
echo ""
echo -e "${BLUE}Available workflows:${NC}"
echo "  - /bmad:bmds:workflows:project-init    (Initialize new project)"
echo "  - /bmad:bmds:workflows:project-pickup  (Pick up brownfield project)"
echo "  - /bmad:bmds:workflows:image-eda       (Image data EDA)"
echo "  - /bmad:bmds:workflows:experiment-cycle (Run experiments)"
echo ""
echo -e "${BLUE}Available agents:${NC}"
echo "  - /bmad:bmds:agents:data-analyst   (Atlas - EDA specialist)"
echo "  - /bmad:bmds:agents:researcher     (Owl - SOTA research)"
echo "  - /bmad:bmds:agents:data-scientist (Feynman - Hypothesis design)"
echo "  - /bmad:bmds:agents:implementer    (Rex - Implementation)"
echo ""
