# Web Application — Full Profile

Full is for broad, mature, or operationally complex web applications.

## Goal

Make the README a complete **system entrance** for product evaluation, development, self-hosting, and operations without duplicating the documentation site.

## Expected core sections

1. Product Overview;
2. Screenshots / Demo;
3. Features;
4. Architecture;
5. Tech Stack;
6. Local Development;
7. Configuration and Secrets;
8. Database and Migrations;
9. Deployment;
10. CI/CD;
11. Observability and Operations;
12. Security;
13. Testing;
14. Upgrade Notes;
15. Documentation;
16. Contributing;
17. License.

## Capability-dependent sections

Render only when real:

- Public API / Webhooks;
- Authentication and Authorization;
- Background Jobs and Queues;
- Object Storage / Media;
- Search;
- Email;
- Payments;
- multi-tenancy;
- external-service integrations.

## Recommended limits

- roughly 180–380 lines;
- architecture as a concise component map;
- configuration grouped by purpose, not a complete `.env` encyclopedia;
- deployment focused on supported first-class paths;
- operations focused on logs, health, backups, and high-impact failure boundaries.

## Full does not mean “invent capabilities”

A Full application with no queue must not receive a queue section. A monolith does not need artificial frontend/backend service diagrams. A system without a public API should not advertise one.

Depth is selected independently from application architecture.
