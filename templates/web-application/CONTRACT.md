# Web Application Template Contract

This family is for repositories whose primary public identity is a runnable or deployable web product, service, portal, dashboard, SaaS application, or self-hosted system.

Use `web-application` when users or operators consume the deployed application itself. Use `django-package` when the repository is primarily installed into another Django project as a reusable component.

## Primary questions

A web-application README should answer:

1. What product does this repository run?
2. Is there a demo or screenshot?
3. How can a contributor run it locally?
4. Which runtime services and configuration values are required?
5. Where is persistent data stored and how are schema changes applied?
6. How is the supported deployment performed?
7. Which authentication, authorization, API, worker, storage, or external-service boundaries matter?
8. What must an operator monitor, back up, secure, and review during upgrades?

## Independent profiles

Each profile is a separate artifact:

```text
minimal/
standard/
full/
```

with its own `PROFILE.md`, `README.template.md`, `README.example.md`, and `config.example.yml`.

## Shared rules

- show the product before explaining implementation;
- distinguish user-facing product identity from contributor setup;
- distinguish local development from production deployment;
- never present development servers as production servers;
- keep secrets out of committed examples;
- state persistent-data and migration responsibilities when relevant;
- expose critical self-hosting warnings such as backup requirements near deployment/operations guidance;
- route exhaustive infrastructure and API details into `docs/`;
- make optional Full sections capability-dependent.

## Profile selection

### Minimal

Small web apps with one normal local-run path, a small configuration surface, and simple deployment.

### Standard

Default maintained web applications with a database or backend, multiple development dependencies, explicit environment variables, and a documented deployment path.

### Full

Applications where safe operation depends on multiple services or several of: database migrations, authentication/authorization, public APIs, workers/queues, object storage, CI/CD, structured logs, health checks, backup/restore, upgrade sequencing, security policy, or self-hosting contracts.

## Excluded content

Even Full should move these out of README when substantial:

- complete `.env` references;
- full OpenAPI/GraphQL schemas;
- provider-specific infrastructure manifests;
- exhaustive Nginx/Caddy configuration;
- incident-response procedures;
- full backup/disaster-recovery runbooks;
- internal production credentials/topology;
- exhaustive troubleshooting encyclopedias.
