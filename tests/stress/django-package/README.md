# Django package stress suite

These cases exercise reusable Django packages whose integration shape is deliberately different from the canonical audit-app example.

The suite checks five pressure points:

1. a tiny template-tag app that needs no models, middleware, URLs, or migrations;
2. middleware whose ordering is part of correctness;
3. a permission backend that needs `INSTALLED_APPS`, `AUTHENTICATION_BACKENDS`, and migrations;
4. a broad admin extension with package models, public API, templates, permissions, and optional workers;
5. a Full-profile middleware/security package with no models or admin surface at all.

The last case is intentional: **Full describes documentation depth, not a requirement to invent every optional Django surface.**
