# Repository Standards

RepoForge treats repository standards as a layer beside the README template system.

README profiles answer **how much project-facing documentation belongs on the landing page**. Repository standards answer **which community, contribution, support, and security contracts should exist around the repository**.

These are deliberately separate concerns:

- `minimal`, `standard`, and `full` remain independent README templates;
- community-health files are shared repository-level contracts rather than 21 duplicated copies;
- `standards/matrix.yml` decides whether each file is `default`, `recommended`, or `optional` for a project type/profile combination;
- project-specific values such as contribution commands, support channels, and reporting contacts come from configuration.

## First standards pack

The first pack contains:

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

## Matrix states

| State | Meaning |
| --- | --- |
| `default` | A future `repoforge apply` should generate the file unless explicitly disabled. |
| `recommended` | RepoForge should recommend the file, but the user decides whether to generate it. |
| `optional` | Useful only when the repository has the corresponding collaboration/support need. |

The matrix is a default policy, not a claim about what every repository must contain. Public contribution mode, organizational policy, private repositories, regulated environments, and project-specific support processes may override it.

## Design rule

> Community-health depth is not the same thing as README depth.

A `minimal` README can still belong to a serious public project that needs a security policy or code of conduct. Conversely, a `full` research archive may not need a user-support channel.

## Next packs

After this first pack stabilizes, RepoForge can add:

```text
.github/ISSUE_TEMPLATE/
├── bug_report.yml
├── feature_request.yml
└── config.yml

.github/pull_request_template.md
CITATION.cff
CHANGELOG.md
```

Only after these contracts are stable should `repoforge apply` write them into another repository.
