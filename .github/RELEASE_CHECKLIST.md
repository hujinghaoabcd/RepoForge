# Release checklist

- [ ] `main` CI is green.
- [ ] `repoforge --version` matches the intended release.
- [ ] README version badge matches the package version.
- [ ] `CHANGELOG.md` is updated.
- [ ] `python -m build` succeeds.
- [ ] `python -m twine check dist/*` succeeds.
- [ ] `python scripts/verify_distribution.py dist --version <version>` succeeds.
- [ ] TestPyPI Trusted Publisher is configured for `repoforge-standards` with workflow `release.yml` and environment `testpypi`.
- [ ] TestPyPI workflow dispatch succeeds.
- [ ] Fresh TestPyPI install is smoke-tested.
- [ ] PyPI Trusted Publisher is configured for `repoforge-standards` with workflow `release.yml` and environment `pypi`.
- [ ] Production `pypi` environment protection is reviewed.
- [ ] Release tag is exactly `v<repoforge.__version__>`.
