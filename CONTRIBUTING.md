# Contributing to RepoForge

Thank you for improving RepoForge. Contributions may target templates, renderer behavior, documentation standards, stress cases, tests, or repository tooling.

## Before you start

- Search existing issues and pull requests before opening a duplicate.
- For substantial changes to template contracts or CLI behavior, open an issue first so scope can be discussed.
- Keep one pull request focused on one coherent change whenever practical.
- Follow `CODE_OF_CONDUCT.md` in all RepoForge project spaces.

## Development setup

Clone the repository and install it in editable mode with test dependencies:

```bash
git clone https://github.com/hujinghaoabcd/RepoForge.git
cd RepoForge
python -m pip install -e ".[test]"
```

## Run the tests

```bash
python -m pytest
```

GitHub Actions also tests RepoForge on Python 3.11, 3.12, and 3.13 and performs CLI render smoke tests for every implemented project family.

## Template changes

When changing README templates:

- keep `minimal`, `standard`, and `full` as independent artifacts;
- do not fabricate capabilities just because a project uses the Full profile;
- preserve the centered header contract;
- keep screenshots and diagrams in body content, not in the identity header;
- update `README.example.md` and the corresponding golden preview;
- update or add a stress case when the change introduces a new edge case;
- keep project-family `CONTRACT.md` and `PROFILE.md` files aligned with behavior.

Regenerate previews with:

```bash
python scripts/generate_previews.py
```

## Issues

Use the repository issue tracker for reproducible bugs, documentation problems, feature proposals, and concrete template-design discussions.

A useful issue normally includes the affected project type/profile, the current output, the desired output, and the smallest configuration needed to reproduce the problem.

Security vulnerabilities and sensitive conduct reports must not be filed as public issues.

## Pull requests

Before requesting review:

- run the full test suite;
- update tests when behavior changes;
- update documentation when public commands, files, or contracts change;
- avoid unrelated reformatting or refactoring;
- explain intentional compatibility changes or snapshot updates;
- ensure generated examples and previews still match the real renderer.

## Commits and branches

Use a short-lived branch from the current `main` branch. Commit messages should describe the change, not the development session or sequence of attempts.

## Review scope

Review may request changes to correctness, profile boundaries, compatibility, tests, documentation, maintainability, security, or repository standards. A review request does not guarantee that a change will be merged.

## Related policies

- Code of Conduct: `CODE_OF_CONDUCT.md`
- Security: `SECURITY.md`
- Support: `SUPPORT.md`
