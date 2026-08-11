# Repository Standards

RepoForge treats repository standards as a layer beside the README template system.

README profiles answer **how much project-facing documentation belongs on the landing page**. Repository standards answer **which community, contribution, support, security, collaboration, citation, and release-history contracts should exist around the repository**.

These are deliberately separate concerns:

- `minimal`, `standard`, and `full` remain independent README templates;
- community-health files are shared repository-level contracts rather than 21 duplicated copies;
- `standards/matrix.yml` decides whether each community-health file is `default`, `recommended`, or `optional` for a project type/profile combination;
- GitHub issue and pull-request forms live in their own `standards/github/` pack;
- citation and changelog policy live in a separate `standards/metadata/` pack and matrix;
- project-specific values such as contribution commands, support channels, reporting contacts, repository URLs, citation authors, and release-history behavior come from configuration;
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

## Metadata pack

```text
standards/metadata/
├── matrix.yml
├── config.example.yml
├── CITATION.template.cff
└── CHANGELOG.template.md
```

The intended generated files are:

```text
CITATION.cff
CHANGELOG.md
```

Citation and changelog defaults are deliberately different:

- research software, original algorithms, and reproducibility repositories prioritize `CITATION.cff`;
- reusable packages, frontend libraries, web applications, and desktop applications prioritize `CHANGELOG.md`;
- projects can explicitly opt in or out regardless of the matrix recommendation.

The citation template follows Citation File Format `1.2.0` conventions. The changelog template follows Keep a Changelog `2.0.0`, keeps an `Unreleased` section, and emits only non-empty change categories rather than filling the file with empty headings.

## Matrix states

| State | Meaning |
| --- | --- |
| `default` | A future `repoforge apply` should generate the file unless explicitly disabled. |
| `recommended` | RepoForge should recommend the file, but the user decides whether to generate it. |
| `optional` | Useful only when the repository has the corresponding collaboration, citation, support, or release-management need. |

The matrices are default policies, not claims about what every repository must contain. Public contribution mode, organizational policy, private repositories, regulated environments, archival repositories, and project-specific release/support processes may override them.

## Design rules

> Community-health depth is not the same thing as README depth.

A `minimal` README can still belong to a serious public project that needs a security policy or code of conduct. Conversely, a `full` research archive may not need a user-support channel.

> Structured GitHub forms should request actionable information without inventing repository labels, assignees, projects, or support channels.

RepoForge therefore keeps default labels and assignees out of the generic forms. Repositories can add those after generation if they actually maintain them.

> Citation and release history are project metadata, not decorative README sections.

A research repository can need citation metadata even when it has little release history; a product or package can need a carefully maintained changelog without being an academic citation target.

## Next implementation stage

The standard-file contracts now cover the first three packs:

```text
README templates
Community health
GitHub collaboration
Repository metadata
```

The next implementation stage is `repoforge apply`, using explicit `--type` and `--profile` selection to write the selected README and standards into another repository. A `diff`/dry-run layer should be built into that workflow before overwriting existing files.
