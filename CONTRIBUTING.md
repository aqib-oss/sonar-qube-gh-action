# CONTRIBUTING

## Table of Contents

- [Contributing](#contributing)
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
  - [Making a change](#making-a-change)
    - [Code Quality](#code-quality)
    - [Submitting a PR](#submitting-a-pr)

## Setup

- Install **uv**: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Upgrade `uv`: `uv self update`
- [Optional] Install **Ruff** globally: `uv tool install ruff@latest`
- Virtual environment:
  - Create a named virtual environment: `uv venv sonar_qube_gh_action`
  - Activate: `source sonar_qube_gh_action/bin/activate`
- Install the project: `uv sync --locked --all-extras`
  - Alternatively, you can use `pip`. To install the main dependencies: `uv pip install .`
    - To install the dev dependencies: `uv pip install --group dev`

## Making a change

- Create a branch for your changes e.g. `git checkout -b fix/npe-get-salary`
- To check if the `uv` lockfile is up-to-date, run: `uv lock --check`
- To update the `uv` lockfile, run: `uv lock`
- To upgrade all packages, run: `uv lock --upgrade`
- To only upgrade a single package, run: `uv lock --upgrade-package <package>`
- To upgrade a single package to a specific version, run: `uv lock --upgrade-package <package>==<version>`

### Code quality

- Lint to check if there are issues: `uvx ruff check .`
  - Also fix linting issues: `ruff check --fix .`
- Fix formatting issues: `uvx ruff format .`
  - Only check if there is any unformatted file: `uvx ruff format --check .`
- Pyright: `uv run pyright .`
- Run unit tests: `uv run pytest`
  [pytest config file](./.pytest.ini)

### Submitting a PR

- Add your changes to git: `git add .`
- Install and run the pre-commit hooks:

  ```shell
  uv tool install pre-commit@latest
  pre-commit install
  pre-commit run --all-files
  ```

  - The `pre-commit` hooks do NOT run on new files till they start to be tracked by `git`.

- Make a commit that follows the [Conventional Commits Specification](https://www.conventionalcommits.org/en/v1.0.0/) that works with the [Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/) package used for generating releases for this Python project.

  ```shell
  <type>[optional scope]: <description>

  [optional body]

  [optional footer(s)]
  ```

  - e.g. `git commit -m "fix: NPE is get_salary method"`
  - Start a commit message with one of the following: `fix:` | `feat:` | `perf:` | `build:` | `ci:` | `refactor:` | `docs:` | `test:` | `chore:` | `style:`
  - By default, if you do not set the start as above, the update is considered a patch.
  - For a breaking change, add "BREAKING CHANGE" in the footer of the full commit message e.g.

  ```shell
  feat: A whole new way of doing things
  BREAKING CHANGE: The amazing option will now be replaced with the boring option.
  ```

- Make sure to get the latest changes from the `main` branch. Fix any conflicts if needed.

  ```shell
  git fetch origin
  git merge origin/main
  ```

- Push your branch upstream:
  - For the initial push: `git push --set-upstream origin docs/update-docs`
  - For subsequent pushes: `git push`
- Create a PR on GitHub with your branch.
