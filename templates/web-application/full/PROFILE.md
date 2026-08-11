# Web Application — Full Profile

Use Full for a production-oriented or self-hosted web application whose correct operation depends on multiple runtime services, explicit security boundaries, or non-trivial deployment/upgrade procedures.

## Expected sections

- Product Overview, screenshots/demo, and Features;
- Architecture;
- Local Development;
- Configuration and Secrets;
- Database and Migrations when applicable;
- API when public/supported;
- Authentication and Authorization when present;
- Background Jobs and Queues when present;
- File/Object Storage when present;
- Deployment;
- CI/CD when relevant;
- Observability and Operations;
- Backup and Restore when persistent data requires it;
- Security;
- Testing;
- Documentation;
- Upgrade Notes;
- Contributing;
- License.

## Capability rule

Full is deeper documentation, not a checklist of technologies. Optional sections must disappear when the application does not actually have the corresponding surface. A single-process Full application may have no queue, no object storage, and no public API.

## README boundary

Keep exact reverse-proxy directives, exhaustive environment-variable references, disaster-recovery runbooks, provider-specific manifests, complete API schemas, and incident procedures in dedicated documentation. The README should expose the operational contract and route readers to the authoritative manuals.
