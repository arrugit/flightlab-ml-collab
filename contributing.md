
# Contributing to FlightLab

## Team Responsibilities
- Areeba: Data owner — dataset management, DVC tracking, data validation, and data-update pull requests.
- Khadija: Model owner and platform lead — model training, configuration, experiments, environment setup, pre-commit hooks, CI, and release workflow.
- Both members must author their own commits, open pull requests, and review each other's work.

## Branch Strategy

We maintain three permanent branches:
- `main`: Production-ready project and releases.
- `staging`: Release validation.
- `dev`: Integration branch for completed features.

### Feature and Data Branches
- `feat/<name>`: New features, notebooks, tests, and pipeline changes.
- `data/<name>`: Dataset updates and data validation changes.
- `fix/<name>`: Bug fixes.
- `exp/<member>-<idea>`: Isolated experiments.

Create feature and data branches from `dev` and open pull requests back into `dev`.

Experiment branches must not be merged directly. Apply the selected experiment's changes to a feature branch and submit them through a pull request.

For hotfixes, create a `fix/<name>` branch from `main`. Merge the fix into `main` through a pull request, then bring the fix back into `dev`.

Promote changes from `dev` to `staging`, then from `staging` to `main`, using pull requests.

## Commit Messages

Use Conventional Commits:
- `feat: add training pipeline`
- `fix: handle missing flight values`
- `data: track initial dataset with DVC`
- `test: add dataset validation tests`
- `docs: document project setup`
- `ci: add GitHub Actions workflow`
- `exp: test random forest parameters`

Keep commits focused on a single logical change.

## Pull Requests and Reviews
- Every change after initial repository setup must go through a pull request.
- Each member must author commits and review the other member's pull requests.
- Request changes when corrections are needed, then review the updated pull request.
- Do not push directly to `dev`, `staging`, or `main` after initial setup.
- Require at least one approval before merging, subject to the repository's available settings.

## Merge Strategy
Use **Squash and merge** for feature and data pull requests. This keeps the target branch history concise while preserving the original commits in the pull request.

Use pull requests for release promotions from `dev` to `staging` and from `staging` to `main`.

## Data and Model Artifacts
- Do not commit raw datasets or generated model artifacts directly to Git.
- Use DVC to track datasets and model artifacts.
- Run `dvc push` successfully before pushing Git commits that reference newly added DVC-tracked data or artifacts.
- Never commit API keys, access tokens, passwords, or other secrets.