# Web Application Stress Suite

These cases pressure-test the `web-application` family against materially different application shapes.

They intentionally cover:

- a tiny internal dashboard;
- a traditional server-rendered monolith;
- a split frontend/API application;
- a self-hosted multi-service platform with workers and object storage;
- a Full-profile monolith with no queue, object storage, public API, search, or email.

The last case protects the rule that Full controls documentation depth rather than inventing infrastructure.

Each override is merged onto the canonical config for its profile and rendered through the normal RepoForge renderer with the shared preview logo.
