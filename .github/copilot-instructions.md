# Copilot Instructions

This repository demonstrates SonarQube GitHub Action integration with a Python project using modern tooling (uv, Ruff, Python Semantic Release).

## Build, Test, and Lint Commands

### Setup
- Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **Keep uv version in sync**: Ensure your local uv version matches the version in GitHub Actions workflows (currently v0.10.2)
  - Check current version: `uv --version`
  - Update to match workflows: `uv self update` (then specify version if needed)
  - Workflows use version: `0.10.2` (see `.github/workflows/main-workflow.yaml`)
- Create virtual environment: `uv venv sonar_qube_gh_action && source sonar_qube_gh_action/bin/activate`
- Install dependencies: `uv sync --locked --all-extras --dev`

### Testing
- Run all tests: `uv run pytest`
- Run specific test: `uv run pytest tests/sonar_qube_gh_action/test_calculator.py::test_sum`
- Run specific test file: `uv run pytest tests/sonar_qube_gh_action/test_calculator.py`
- Pytest is configured in `.pytest.ini` with coverage requirements (80% minimum)

### Linting and Formatting
- Check linting: `uvx ruff check .`
- Fix linting issues: `uvx ruff check --fix .`
- Format code: `uvx ruff format .`
- Check formatting: `uvx ruff format --check .`
- Type checking: `uv run pyright .`

### Dependency Management
- Check if lockfile is up-to-date: `uv lock --check`
- Update lockfile: `uv lock`
- Upgrade all packages: `uv lock --upgrade`
- Upgrade single package: `uv lock --upgrade-package <package>`

### Pre-commit Hooks
```shell
uv tool install pre-commit@latest
pre-commit install
pre-commit run --all-files
```

## Architecture

### Project Structure
- `src/sonar_qube_gh_action/` - Main source code
- `tests/sonar_qube_gh_action/` - Test files (mirrors src structure)
- `pyproject.toml` - Python project configuration and semantic-release config
- `sonar-project.properties` - SonarQube configuration
- `.pytest.ini` - Pytest configuration with coverage settings
- `.ruff.toml` - Ruff linter and formatter configuration

### Test Structure
Tests use the Arrange-Act-Assert pattern consistently:
```python
def test_example():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.sum(4, 3)

    # Assert
    assert result == 7
```

### CI/CD Workflows
- **main-workflow.yaml**: Runs on main branch - tests, SonarQube scan, and semantic versioning
- **pr-workflow.yaml**: Runs on PRs - validation and checks
- Python Semantic Release automatically manages versions based on conventional commits

## Key Conventions

### Git Workflow
- **Always create a new branch** for any changes - never work directly on main
- Branch naming: `feat/`, `fix/`, `chore/`, `docs/` prefixes
- Example: `git checkout -b feat/add-new-feature` or `git checkout -b chore/update-dependencies`
- Verify current branch: `git branch --show-current`
- Push with upstream: `git push --set-upstream origin <branch-name>`

### Commit Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/) for semantic versioning:
- `fix:` - Patch version bump
- `feat:` - Minor version bump
- `BREAKING CHANGE:` in footer - Major version bump
- Other prefixes: `perf:`, `build:`, `ci:`, `refactor:`, `docs:`, `test:`, `chore:`, `style:`

Example:
```
fix: NPE in get_salary method
```

For breaking changes:
```
feat: A whole new way of doing things

BREAKING CHANGE: The amazing option will now be replaced with the boring option.
```

### Coverage Requirements
- Minimum 80% code coverage enforced via pytest configuration
- Coverage reports generated in `coverage-reports/coverage.xml`
- SonarQube reads coverage from this location

### Code Style
- Line length: 88 characters (Black-compatible)
- Python target: 3.11
- Ruff handles both linting and formatting
- Type hints required (enforced by Pyright)
- Unused variables must be underscore-prefixed

### File Naming
- Test files mirror source structure: `src/sonar_qube_gh_action/calculator.py` → `tests/sonar_qube_gh_action/test_calculator.py`
- Test functions prefixed with `test_`

### Lockfile Management
- `uv.lock` is committed (recommended for applications, not libraries)
- Always sync with `--locked` flag in CI to ensure reproducibility
- **Version consistency**: uv lockfile revision may change when using different uv versions
  - This is normal behavior and backwards compatible
  - Keep local uv version aligned with CI/CD workflows to minimize revision changes
