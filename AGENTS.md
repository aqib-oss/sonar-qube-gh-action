# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Copilot, etc.) working in this repository.

This repository demonstrates SonarQube Cloud GitHub Action integration with a Python project using modern tooling: uv, Ruff, Pyright, pytest and Python Semantic Release (PSR).

## Setup

- Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Install the project and all extras/dev dependencies: `uv sync --locked --all-extras --dev`
- Optional named venv (what `pyrightconfig.json` points at):
  `uv venv sonar_qube_gh_action && source sonar_qube_gh_action/bin/activate`

## Commands

| Task | Command |
|---|---|
| Run all tests (with coverage) | `uv run pytest` |
| Run one test | `uv run pytest tests/sonar_qube_gh_action/test_calculator.py::test_sum` |
| Lint | `uvx ruff check .` (fix: `uvx ruff check --fix .`) |
| Format | `uvx ruff format .` (check: `uvx ruff format --check .`) |
| Type check | `uv run pyright .` |
| Pre-commit hooks | `pre-commit run --all-files` |
| Check lockfile is current | `uv lock --check` |
| Upgrade all / one package | `uv lock --upgrade` / `uv lock --upgrade-package <package>` |

Before opening a PR, run lint, format check, Pyright and tests. CI (`pr-workflow.yaml`) runs the same checks.

Pyright resolves imports from the `sonar_qube_gh_action` venv configured in `pyrightconfig.json`. If it reports
`Import "pytest" could not be resolved` while `.venv` is synced, that venv is missing or stale; it is a local
environment issue, not a code issue.

## Project structure

- `src/sonar_qube_gh_action/` - source code
- `tests/sonar_qube_gh_action/` - tests, mirroring `src` (`calculator.py` -> `test_calculator.py`)
- `pyproject.toml` - project metadata, dependencies and PSR config
- `.pytest.ini` - pytest config; enforces 80% minimum coverage and writes `coverage-reports/coverage.xml`
- `.ruff.toml` - Ruff lint/format config (line length 88, Python 3.11 target)
- `pyrightconfig.json` - Pyright config (basic mode)
- `sonar-project.properties` - SonarQube Cloud config; reads coverage from `coverage-reports/coverage.xml`
- `.github/workflows/` - `pr-workflow.yaml` (PR checks) and `main-workflow.yaml` (tests, Sonar scan, release)

## Code conventions

- Use type hints on functions and on variables where they aid clarity, as the existing code does.
- Prefix unused variables with an underscore.
- Tests use Arrange-Act-Assert with comments marking each section:

  ```python
  def test_sum():
      # Arrange
      calculator: Calculator = Calculator()

      # Act
      result: int = calculator.sum(4, 3)

      # Assert
      assert result == 7
  ```

## Git and pull requests

- Never commit directly to `main`. Create a branch with a conventional prefix: `feat/`, `fix/`, `chore/`, `docs/`, `ci/`.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/); PSR derives the version from them:
  - `fix:` -> patch, `feat:` -> minor, `BREAKING CHANGE:` footer -> major
  - Others: `perf:`, `build:`, `ci:`, `refactor:`, `docs:`, `test:`, `chore:`, `style:`
- PRs are squash-merged. The squash commit uses the PR title (or the commit message, for single-commit PRs), so both
  must be conventional commits.
- **PR descriptions must follow `.github/pull_request_template.md`**: a `# Description of the change - What and Why`
  section and a `## Testing details` section. Read the template and fill in both sections rather than writing a
  free-form description.

## Dependencies and tool versions

- `uv.lock` is committed. CI installs with `--locked`, so always commit `uv.lock` together with `pyproject.toml` changes.
- Keep the uv version consistent everywhere it is pinned:
  - `pyproject.toml` -> `[project.optional-dependencies].build` (`uv ~= X.Y.Z`)
  - `.github/workflows/*.yaml` -> `astral-sh/setup-uv` `version:` input
  - local uv (`uv self update`)
- Keep the `python-semantic-release` version in `pyproject.toml` in sync with the
  `python-semantic-release/python-semantic-release` and `publish-action` tags in `main-workflow.yaml`.
- Dependabot (`.github/dependabot.yml`) opens weekly pip update PRs and security alerts against `uv.lock`.
  Pins in the `build` extra can block security fixes for transitive packages; check them when an alert's patched
  version can't be resolved.

## GitHub Actions

- Use action versions that run on a current Node.js runtime (node24). When upgrading, check each major release's
  breaking changes.
- `astral-sh/setup-uv` does not publish floating major tags (`v10` does not exist); pin an exact version such as
  `v10.3.2`. Verify a tag exists before using it: `gh api repos/<owner>/<repo>/git/ref/tags/<tag>`.
- Validate workflow changes with `uvx --from actionlint-py actionlint .github/workflows/*.yaml`.

## Releases

- Every merge to `main` runs `main-workflow.yaml`. PSR bumps the version, updates `CHANGELOG.md` and `uv.lock`,
  pushes a version commit and tag, builds with `uv build`, and creates a GitHub Release with the built assets.
- Don't edit the version in `pyproject.toml` or `CHANGELOG.md` by hand; PSR manages both.
- If a run pushes the tag but fails to create the GitHub Release, re-run the failed job. The
  `Recover | Create missing GitHub Release` step creates the missing release for that tag.

## Secrets

Repository secrets used by the workflows (they expire and must be rotated):

- `SONAR_TOKEN` - SonarQube Cloud token (generated at https://sonarcloud.io/). An expired token fails the Sonar scan step.
- `SEMVER_GH_TOKEN` - GitHub PAT used by PSR to create releases (also passed to the Sonar scan). An expired token
  fails with `401 Client Error: Unauthorized` when creating the release.
