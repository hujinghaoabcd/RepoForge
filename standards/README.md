# Repository Standards

RepoForge treats repository standards as a layer beside the README template system.

README profiles answer **how much project-facing documentation belongs on the landing page**. Repository standards answer **which community, contribution, support, security, issue, and review contracts should exist around the repository**.

These are deliberately separate concerns:

- `minimal`, `standard`, and `full` remain independent README templates;
- community-health files are shared repository-level contracts rather than 21 duplicated copies;
- `standards/matrix.yml` decides whether each community-health file is `default`, `recommended`, or `optional` for a project type/profile combination;
- GitHub issue and pull-request forms live in their own `standards/github/` pack;
- project-specific values such as contribution commands, support channels, reporting contacts, repository URLs, and form behavior come from configuration;
- project type is always selected explicitly rather than inferred.

## Community standards pack

```text
standards/
├── matrix.yml
└── community/
    ├── CODE_OF_CONDUCT.template.md
    ├── CONTRIBUTING.template.md
    ├── SECURITY.template.md
    ├── SUPPORT.template.md
    └── config.example.yml
```

The intended generated repository files are:

```text
CODE_OF_CONDUCT.md
CONTRIBUTING.md
SECURITY.md
SUPPORT.md
```

## GitHub collaboration pack

```text
standards/github/
├── config.example.yml
├── ISSUE_TEMPLATE/
│   ├── bug_report.template.yml
│   ├── feature_request.template.yml
│   └── config.template.yml
└── pull_request_template.template.md
```

The intended generated paths are:

```text
.github/ISSUE_TEMPLATE/
├── 01-bug-report.yml
├── 02-feature-request.yml
└── config.yml

.github/pull_request_template.md
```

Bug and feature reports use GitHub Issue Forms so required information is structured at submission time. Pull requests use a Markdown template with summary, motivation, validation, compatibility/risk, and repository-standard checks.

## Matrix states

| State | Meaning |
| --- | --- |
| `default` | A future `repoforge apply` should generate the file unless explicitly disabled. |
| `recommended` | RepoForge should recommend the file, but the user decides whether to generate it. |
| `optional` | Useful only when the repository has the corresponding collaboration/support need. |

The matrix is a default policy, not a claim about what every repository must contain. Public contribution mode, organizational policy, private repositories, regulated environments, and project-specific support processes may override it.

## Design rules

> Community-health depth is not the same thing as README depth.

A `minimal` README can still belong to a serious public project that needs a security policy or code of conduct. Conversely, a `full` research archive may not need a user-support channel.

> Structured GitHub forms should request actionable information without inventing repository labels, assignees, projects, or support channels.

RepoForge therefore keeps default labels and assignees out of the generic forms. Repositories can add those after generation if they actually maintain them.

## Next standards pack

The next repository metadata layer is expected to cover:

```text
CITATION.cff
CHANGELOG.md
```

After the standard-file contracts stabilize, `repoforge apply` can write selected README, community-health, GitHub collaboration, and metadata files into another repository.
