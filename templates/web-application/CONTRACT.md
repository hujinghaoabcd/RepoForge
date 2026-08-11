# Web Application Template Contract

This family is for complete web products and deployable browser-based systems.

Use `web-application` when the repository's public identity is an application that users or operators run, deploy, configure, or access through a browser. Typical examples include:

- SaaS products;
- self-hosted business applications;
- internal platforms;
- dashboards and portals;
- full-stack Django, Rails, Laravel, Node, Go, Java, or similar systems;
- frontend + API + database systems;
- monolithic web applications;
- web systems with background workers, object storage, search, email, or other services.

Do **not** use this family for:

- a reusable Django app or middleware package — use `django-package`;
- a reusable frontend component/plugin/library — use `frontend-library`;
- a scientific Python library — use `scientific-python`;
- a desktop application whose primary delivery surface is native desktop — use `desktop-application`.

## Primary README questions

A web-application README should answer:

1. What product/system is this and who is it for?
2. What does it look like?
3. Can I try a hosted demo or deployed instance?
4. What is the shortest reliable local-development path?
5. Which configuration and external services are required?
6. How is persistent data created, migrated, backed up, or upgraded?
7. How is the application deployed?
8. What authentication, authorization, security, and secret-handling boundaries matter?
9. How do developers test and contribute?
10. For larger systems, how do architecture, workers, storage, CI/CD, observability, and operations fit together?

## Independent profiles

Each profile is a separate artifact:

```text
templates/web-application/
├── minimal/
│   ├── PROFILE.md
│   ├── README.template.md
│   ├── README.example.md
│   └── config.example.yml
├── standard/
└── full/
```

Visible approved previews live under:

```text
tests/previews/web-application/
├── minimal.md
├── standard.md
└── full.md
```

## Shared rules

- show the application identity before implementation detail;
- prefer one real product screenshot or hero image over decorative diagrams;
- distinguish **using the product**, **self-hosting/deploying it**, and **contributing to development**;
- make the fastest local-development path copyable;
- list required external services and configuration without publishing secrets;
- treat database migrations and persistent storage as operational contracts when they exist;
- distinguish production deployment from local development;
- disclose security-sensitive setup and backup boundaries;
- keep environment-variable encyclopedias, deployment runbooks, and troubleshooting catalogs in docs when large;
- do not invent API, background-worker, object-storage, payment, email, search, or observability sections when the application does not have those capabilities.

## Profile selection

### Minimal

Use for a small application with one main runtime path and simple deployment.

The README should make the app visible and runnable without becoming a developer manual.

### Standard

Default for most maintained web applications.

Use when the project needs explicit product overview, screenshots/demo, stack, local development, environment configuration, database, deployment, project structure, testing, and documentation links.

### Full

Use when several operational surfaces materially affect correctness or deployment, such as:

- separate frontend/backend services;
- multiple databases or caches;
- background workers/queues;
- object storage;
- search services;
- email providers;
- authentication/SSO;
- public APIs or webhooks;
- reverse proxies;
- CI/CD;
- observability;
- backup/restore procedures;
- production migrations;
- multi-tenant or permission boundaries;
- several deployment modes.

Full still means **deeper documentation**, not automatically more application capabilities.

## README boundary

Keep concise operational entry points in the README. Move substantial details to dedicated docs:

- complete `.env` reference;
- Kubernetes manifests and cluster operations;
- full reverse-proxy configuration;
- complete API reference;
- incident-response procedures;
- exhaustive monitoring dashboards;
- backup/restore runbooks;
- every deployment provider;
- architecture decision records;
- long troubleshooting catalogs;
- full database schemas.
