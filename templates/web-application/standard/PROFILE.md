# Web Application — Standard Profile

Standard is the default profile for most maintained web applications.

## Goal

Balance product presentation with the normal developer and self-host/operator contract.

## Required sections

1. product identity;
2. Overview;
3. Screenshots / Demo;
4. Features;
5. Tech Stack;
6. Local Development;
7. Environment Variables;
8. Database;
9. Deployment;
10. Project Structure;
11. Testing;
12. Documentation;
13. License.

## Capability-dependent additions

A Standard application may also expose concise notes for:

- authentication;
- email;
- object storage;
- background workers;
- external APIs.

Do not add empty sections only because another application needs them.

## Recommended limits

- roughly 110–230 lines;
- 4–8 core features;
- one primary local workflow;
- compact environment-variable table;
- one primary database/migration workflow;
- one or two supported deployment paths;
- short project tree rather than exhaustive repository inventory.

Large architecture, complete environment references, production runbooks, and security policies belong in docs.
