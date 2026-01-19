# Coding Standards

Rex's enforcement guidelines for production-quality code.

---

## Core Principles

### DRY (Don't Repeat Yourself)
- Every piece of logic exists exactly once
- Extract common patterns into reusable functions
- If you copy-paste, you're doing it wrong
- Refactor immediately when duplication is detected

### Clarity Over Cleverness
- Code should be readable without comments
- If it needs a comment, simplify the code first
- Use descriptive names that explain intent
- Avoid abbreviations unless universally understood

### Explicit Over Implicit
- No magic numbers - use named constants
- No hidden side effects
- Function signatures tell the full story
- Dependencies are visible, not hidden

---

## Python Standards

### Naming
- `snake_case` for functions and variables
- `PascalCase` for classes
- `UPPER_SNAKE_CASE` for constants
- Prefix private methods with `_`

### Structure
- One class per file (with rare exceptions)
- Imports at top, grouped: stdlib, third-party, local
- Functions under 50 lines (refactor if longer)
- Classes under 300 lines (split if larger)

### Type Hints
- All function parameters typed
- All return values typed
- Use `Optional[]` explicitly for nullable
- Prefer `list[T]` over `List[T]` (Python 3.9+)

### Documentation
- Docstrings for public functions/classes
- Format: one-line summary, blank line, details
- Document parameters only if not obvious from types
- No redundant comments restating what code does

---

## ML-Specific Standards

### Data Pipeline
- All transformations must be reproducible
- Random seeds explicit and configurable
- Data validation at pipeline boundaries
- Log data shapes at each transformation step

### Model Code
- Separate model definition from training logic
- Configuration via config files, not hardcoded
- Checkpoint saving with full reproducibility metadata
- Clear separation: preprocessing / model / postprocessing

### Experiments
- Each experiment in isolated directory
- Results include: config, metrics, model artifacts
- No modifications to shared code without integration

---

## Performance Guidelines

### Python Performance
- Profile before optimizing
- Use vectorized operations (numpy/pandas)
- Avoid loops over dataframes
- Consider memory footprint for large datasets

### When to Use C/C++
- Proven bottleneck in profiling
- Inner loops with millions of iterations
- Custom CUDA kernels
- Always benchmark before and after

---

## Anti-Patterns (Reject These)

- God functions (>100 lines)
- Deep nesting (>3 levels)
- Boolean parameters (use enums or separate functions)
- Silent failures (always raise or log errors)
- Global mutable state
- Hardcoded paths or credentials
- Commented-out code in production
