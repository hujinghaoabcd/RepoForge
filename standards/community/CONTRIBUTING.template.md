# Contributing to {{ project_name }}

Thank you for improving {{ project_name }}. This guide describes the expected contribution workflow for issues, code, documentation, tests, and pull requests.

## Before you start

- Search existing issues and pull requests before opening a duplicate.
- For substantial changes, open an issue first so scope and design can be discussed.
- Keep one pull request focused on one coherent change whenever practical.
- Follow the project's participation policies in all project spaces.

## Development setup

{{ development_intro }}

```bash
{{ setup_command }}
```

## Development checks

Run the checks relevant to your change before opening a pull request.

{% for check in checks %}### {{ check.name }}

```bash
{{ check.command }}
```

{% endfor %}## Issues

Use {{ issue_url }} for reproducible bugs, feature proposals, documentation problems, and other actionable project work.

A useful issue normally includes:

- the problem or proposed change;
- the environment or version when relevant;
- the smallest reproducible example available;
- expected and actual behavior for bugs;
- logs, screenshots, or traces only when they materially help diagnosis.

Security vulnerabilities and sensitive conduct reports must not be filed as public issues.

## Pull requests

{{ pull_request_expectations }}

Before requesting review:

- update or add tests when behavior changes;
- update user-facing documentation when interfaces or workflows change;
- avoid unrelated formatting or refactoring in the same pull request;
- make sure generated files or snapshots are updated when the project requires them;
- explain any intentionally skipped check.

## Commit and branch guidance

{{ branch_policy }}

{{ commit_guidance }}

## Review

Review may request changes to correctness, tests, compatibility, documentation, maintainability, security, or project scope. A review request is not a guarantee that a contribution will be merged.

{% if related_policies %}## Related project policies

{% for policy in related_policies %}- {{ policy.name }}: `{{ policy.path }}`
{% endfor %}
{% endif %}Thank you for contributing to {{ project_name }}.
