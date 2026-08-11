# Releasing RepoForge

RepoForge keeps its public brand, import package, and CLI name while using a distinct PyPI distribution name:

```text
Project / GitHub:   RepoForge
PyPI distribution: repoforge-standards
Python import:      repoforge
CLI command:        repoforge
```

After publication, users install the distribution and invoke the existing CLI:

```bash
python -m pip install repoforge-standards
repoforge --version
```

## Release architecture

`.github/workflows/release.yml` has three deliberately separated responsibilities:

1. **Build** the sdist and wheel without OIDC publishing permission.
2. **Publish** the already-built artifact from a minimal job with `id-token: write`.
3. **Create a GitHub Release** only after a tag-triggered PyPI publish succeeds.

Manual workflow runs publish only to **TestPyPI**. A `v*` tag publishes to **PyPI**. The tag must exactly match the package version, for example:

```text
package version: 0.1.0a1
tag:             v0.1.0a1
```

A mismatched tag fails before publishing.

## One-time Trusted Publishing setup

No PyPI API token is stored in this repository. Configure GitHub Actions as a Trusted Publisher on both TestPyPI and PyPI.

Use these values:

```text
PyPI project:  repoforge-standards
Owner:         hujinghaoabcd
Repository:    RepoForge
Workflow:      release.yml
```

For TestPyPI use the GitHub environment:

```text
testpypi
```

For PyPI use:

```text
pypi
```

If `repoforge-standards` does not yet exist on an index, configure a **pending publisher** for that project name. A pending publisher creates the project on first successful publish; it does not reserve the name before that publish.

Create matching GitHub repository environments named `testpypi` and `pypi`. For the production `pypi` environment, enable deployment protection such as required approval before publication when available for the repository plan.

The environment names in GitHub, the environment names configured in the Trusted Publisher entries, and the names in `release.yml` must match exactly.

## Build locally before a release

Install release tooling:

```bash
python -m pip install -e ".[release]"
```

Build both artifacts:

```bash
rm -rf dist build
python -m build
python -m twine check dist/*
python scripts/verify_distribution.py dist --version 0.1.0a1
```

On Windows PowerShell, remove the directories with:

```powershell
Remove-Item -Recurse -Force dist, build -ErrorAction SilentlyContinue
python -m build
python -m twine check dist/*
python scripts/verify_distribution.py dist --version 0.1.0a1
```

The verifier checks:

- distribution name and version metadata;
- wheel-bundled README templates;
- wheel-bundled repository standards;
- sdist inclusion of the source template/standards trees needed to rebuild a wheel.

The normal test workflow goes further: it installs the built wheel and sdist into fresh virtual environments outside the source checkout and runs the CLI there. This guards against releases that work only because the repository checkout happens to contain `templates/` or `standards/`.

## TestPyPI first

After the `testpypi` Trusted Publisher and GitHub environment are configured, open **Actions → release → Run workflow**.

A manual run:

```text
workflow_dispatch
      ↓
build + verify
      ↓
publish-testpypi
```

It does **not** create a GitHub tag and does **not** publish to production PyPI.

After the TestPyPI upload succeeds, test installation in a clean environment. Because dependencies may not all exist on TestPyPI, install RepoForge from TestPyPI while allowing dependencies from normal PyPI when needed:

```bash
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  repoforge-standards==0.1.0a1

repoforge --version
```

## Production release

Before creating the release tag:

1. Confirm `main` is green.
2. Confirm `__version__` is the intended version.
3. Confirm the README version badge matches.
4. Update `CHANGELOG.md`.
5. Complete a successful TestPyPI smoke test.
6. Confirm the production `pypi` Trusted Publisher and GitHub environment are configured.

Then tag the exact release commit:

```bash
git switch main
git pull --ff-only
git tag -a v0.1.0a1 -m "RepoForge 0.1.0a1"
git push origin v0.1.0a1
```

The tag-triggered workflow performs:

```text
v0.1.0a1
   ↓
build + verify
   ↓
PyPI Trusted Publishing
   ↓
GitHub Release + sdist/wheel assets
```

Pre-release version tags such as `v0.1.0a1`, `v0.1.0b1`, and `v0.1.0rc1` are created as GitHub pre-releases.

## Version ownership

The canonical source version is:

```python
repoforge.__version__
```

`pyproject.toml` reads that value dynamically, and:

```bash
repoforge --version
```

reports the same version. Do not maintain a second literal version in project metadata.

## Release safety rules

- Never add a long-lived PyPI API token to repository or environment secrets for the normal release path.
- Do not grant `id-token: write` to the build job.
- Do not publish artifacts rebuilt inside the publish job; publish only the artifact produced by the build job.
- Do not create a production tag whose value differs from `repoforge.__version__`.
- Do not bypass the TestPyPI smoke for the first release of a new packaging layout.
- Treat changes to `.github/workflows/release.yml` as security-sensitive release changes.
