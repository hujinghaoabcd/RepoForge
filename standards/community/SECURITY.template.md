# Security Policy

## Supported versions

{{ project_name }} provides security support for the versions listed below.

| Version / branch | Supported |
| --- | --- |
{% for item in supported_versions %}| {{ item.version }} | {{ item.status }} |
{% endfor %}
## Reporting a vulnerability

Please report suspected vulnerabilities privately through:

**{{ reporting_contact }}**

{{ reporting_instructions }}

Do not open a public issue for a vulnerability that could expose users, credentials, secrets, private data, or an exploitable weakness before maintainers have had a reasonable opportunity to investigate it.

## What to include

When possible, include:

- the affected version, commit, or deployment context;
- the component or endpoint involved;
- steps to reproduce or a minimal proof of concept;
- the expected security impact;
- any known workaround or mitigation;
- whether the issue has been disclosed elsewhere.

Do not include real secrets, unrelated personal data, or destructive payloads unless maintainers explicitly request them through a safe channel.

## Response and disclosure

{{ response_expectation }}

{{ disclosure_policy }}

## Scope

{{ security_scope }}

## Non-security issues

Ordinary bugs, feature requests, and usage questions should follow `CONTRIBUTING.md` and `SUPPORT.md` instead of this process.
