# Changelog

All notable changes to RepoForge will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/2.0.0/).
RepoForge is currently preparing the `0.1.0a1` Alpha package release; no stable release has been published yet.

## [Unreleased]

### Added

- Seven README project families with independent Minimal, Standard, and Full profiles.
- Renderer-backed README examples, previews, stress suites, and Python 3.11–3.13 CI coverage.
- Unified centered README identity headers with compact logos, badges, navigation, and body-only media placement.
- Repository community standards for Code of Conduct, contributing, security, and support.
- Configurable GitHub Bug Report and Feature Request Issue Forms, issue chooser configuration, and pull request template standards.
- Repository metadata standards for `CITATION.cff` and `CHANGELOG.md`.
- Explicit `repoforge init` generation of one combined, project-owned `repoforge.yml` across all 21 project type/profile combinations.
- Safety-first `repoforge apply` with complete-plan rendering, conflict preflight, `--dry-run`, `--force`, and standards policy overrides.
- Review-first `repoforge diff` with unified create/overwrite diffs, configurable context, unchanged-file reporting, and no target-repository writes.
- CI-facing `repoforge check` with managed-file drift detection, repository config validation, CFF/Issue Form checks, placeholder diagnostics, and strict warning handling.
- Managed Sections v1 for README `identity`, `badges`, and `navigation`, preserving user-owned body prose across `diff`, `apply`, and `check`.
- PyPI distribution metadata under the `repoforge-standards` name while preserving the `repoforge` import package and CLI.
- `repoforge --version` backed by one canonical package version source.
- Self-contained wheel runtime data for all README templates and repository standards, plus rebuildable sdist packaging.
- Distribution integrity checks and fresh wheel/sdist installation smoke tests outside the source checkout.
- TestPyPI/PyPI Trusted Publishing workflow with isolated OIDC publish jobs and tag/version verification.
- GitHub Release creation for verified tag releases.

### Changed

- Removed automatic project-type detection from the planned RepoForge workflow; project type and profile are selected explicitly.
- Replaced preview-specific illustrative screenshots with a neutral empty placeholder.
- Consolidated `init`, `diff`, `apply`, and `check` around the same explicit project selection and repository standards plan.
- New `repoforge init` configs default to `readme_management: managed-sections`; legacy configs without the field retain whole-file README ownership.
- GitHub Actions checkout/setup-python workflows use the Node 24 based v6 actions for the `0.1.0a1` release line.
