# Web Application — Standard Profile

Standard is the default for a maintained deployable web application.

## Required outcome

The README should make the product visible and make the normal developer/operator path reproducible without becoming a complete operations handbook.

## Expected sections

- Overview and optional demo/screenshot;
- Features;
- Tech Stack;
- Local Development;
- Environment Variables;
- Database and Migrations when applicable;
- Deployment;
- Project Structure;
- Testing;
- Documentation;
- License.

## Rules

- distinguish local development from production deployment;
- expose required service dependencies and local access points;
- list only environment variables needed to get started;
- explain the migration contract when persistent schema exists;
- link to deeper deployment, API, and operations documentation;
- do not turn README into an exhaustive `.env` or reverse-proxy reference.

Move to Full when production behavior depends on several services, explicit auth boundaries, workers/queues, object storage, backup/restore, observability, or non-trivial upgrade sequencing.
