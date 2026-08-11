# Security Policy

## Supported versions

RepoForge is currently in Alpha development. Security fixes target the latest `main` branch and the latest published development version.

| Version / branch | Supported |
| --- | --- |
| `main` | ✅ |
| latest `0.1.0.dev*` | ✅ |
| older snapshots | ❌ |

## Reporting a vulnerability

Please report suspected vulnerabilities privately to the project maintainer using a private contact method published on the maintainer's GitHub profile.

If GitHub private vulnerability reporting becomes enabled for this repository, that channel is preferred.

Do **not** open a public issue for a vulnerability that could expose users, credentials, secrets, private data, or an exploitable weakness before maintainers have had a reasonable opportunity to investigate it.

## What to include

When possible, include:

- the affected version or commit;
- the component involved;
- steps to reproduce or a minimal proof of concept;
- the expected security impact;
- any known workaround or mitigation;
- whether the issue has already been disclosed elsewhere.

Do not include real secrets, unrelated personal data, or destructive payloads unless maintainers explicitly request them through a safe channel.

## Response and disclosure

Maintainers will acknowledge credible reports as soon as practical and will communicate next steps once enough information is available to assess the issue.

Please coordinate public disclosure with maintainers so users have a reasonable opportunity to update or mitigate the issue.

## Scope

Security reports may concern RepoForge's Python package, CLI, template rendering behavior, generated repository files, or maintained automation where a defect could create a meaningful security impact.

Ordinary rendering bugs, template disagreements, feature requests, and usage questions should follow `CONTRIBUTING.md` and `SUPPORT.md` instead.
