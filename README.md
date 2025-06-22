# sonar-qube-gh-action

A simple repository to demonstrate how to use the official SonarQube GitHub Action: <https://github.com/SonarSource/sonarqube-scan-action>
Also, uses:

- **uv** for dependency management, virtual environments, etc.
  - uv GitHub repo: <https://github.com/astral-sh/uv>
  - uv documentation: <https://docs.astral.sh/uv/>
- **Ruff** for linting and formatting.
  - Ruff GitHub repo: <https://github.com/astral-sh/ruff>
  - Ruff documentation: <https://docs.astral.sh/ruff/>
- **Python Semantic Release** for automatic Semantic Versioning of this Python project.
  - Documentation: <https://python-semantic-release.readthedocs.io/en/latest/index.html>

## Stats

- This project on SonarQube Cloud: <https://sonarcloud.io/project/overview?id=aqib-oss_sonar-qube-gh-action>

| Source                        | Status                                                                                                                                                                                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GitHub Actions main workflow  | [![main-workflow](https://github.com/aqib-oss/sonar-qube-gh-action/actions/workflows/main-workflow.yaml/badge.svg)](https://github.com/aqib-oss/sonar-qube-gh-action/actions/workflows/main-workflow.yaml)    |
| GitHub Action PR workflow     | [![pr-workflow](https://github.com/aqib-oss/sonar-qube-gh-action/actions/workflows/pr-workflow.yaml/badge.svg)](https://github.com/aqib-oss/sonar-qube-gh-action/actions/workflows/pr-workflow.yaml)          |
| SonarQube Quality Gate status | [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=aqib-oss_sonar-qube-gh-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=aqib-oss_sonar-qube-gh-action) |
| SonarQube Code Coverage       | [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=aqib-oss_sonar-qube-gh-action&metric=coverage)](https://sonarcloud.io/summary/new_code?id=aqib-oss_sonar-qube-gh-action)                |

## Dev notes

- [How to contribute - setup, PR, etc.](CONTRIBUTING.md)
- Committing the `uv.lock` file is recommended to ensure reproducibility of the environment for binaries or applications.
  - It should NOT be committed for libraries.
