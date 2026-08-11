# Packaging runtime data

RepoForge's source tree keeps the human-maintained template and standards families at the repository root:

```text
templates/
standards/
```

Those directories are part of the repository authoring experience and remain the canonical source assets.

A normal installed Python distribution cannot rely on the user's current working directory containing those trees. During `build_py`, `setup.py` copies them into the installed package:

```text
repoforge/_data/templates/
repoforge/_data/standards/
```

At runtime, RepoForge resolves assets in this order:

1. an explicit `--template-root` / `--standards-root` override;
2. packaged `repoforge/_data/...` assets;
3. the repository/source-checkout fallback used during development.

This preserves the current top-level repository organization while making the wheel self-contained.

`MANIFEST.in` also includes the canonical top-level `templates/` and `standards/` trees in the source distribution. That is required because installing an sdist first rebuilds a wheel, and the build hook needs access to those canonical assets.

The CI packaging job verifies both artifact types and then installs each into a fresh virtual environment outside the RepoForge checkout. A release is not considered package-ready unless the installed CLI can initialize a repository without relying on the source tree.
