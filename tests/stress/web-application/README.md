# Web Application stress suite

These cases pressure-test the `web-application` family against very different deployable product shapes.

The suite verifies that documentation depth does not imply infrastructure complexity. In particular, a Full application may legitimately have no public API, queue, worker, or object storage.

Cases are small overrides merged onto the canonical profile config and rendered through the normal RepoForge renderer with `tests/branding.yml`.
