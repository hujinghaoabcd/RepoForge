{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(500) }}">
</p>

{% endif %}{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} product overview" width="{{ screenshot_width | default(940) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}## Product Overview

{{ overview_text }}

{% if demo_link %}**Demo:** {{ demo_link }}

{% endif %}## Screenshots / Demo

{{ screenshot_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Architecture

{{ architecture_intro }}

| Component | Technology / service | Responsibility |
| --- | --- | --- |
{% for item in architecture %}| **{{ item.component }}** | {{ item.technology }} | {{ item.responsibility }} |
{% endfor %}

## Tech Stack

{% for item in stack %}- **{{ item.name }}** — {{ item.description }}
{% endfor %}

## Local Development

### Requirements

{% for item in requirements %}- {{ item }}
{% endfor %}

### Bootstrap

```bash
{{ local_command }}
```

{{ local_result }}

## Configuration and Secrets

{{ configuration_intro }}

| Group | Variable | Required | Purpose |
| --- | --- | --- | --- |
{% for item in environment %}| {{ item.group }} | `{{ item.name }}` | {{ item.required }} | {{ item.purpose }} |
{% endfor %}

## Database and Migrations

{{ database_text }}

```bash
{{ migration_command }}
```

{% if backup_text %}### Backup / Restore Boundary

{{ backup_text }}

{% endif %}{% if api_text %}## Public API / Webhooks

{{ api_text }}

{% if api_links %}{% for item in api_links %}- **{{ item.name }}:** {{ item.link }}
{% endfor %}

{% endif %}{% endif %}{% if auth_text %}## Authentication and Authorization

{{ auth_text }}

{% endif %}{% if jobs_text %}## Background Jobs and Queues

{{ jobs_text }}

{% if jobs_command %}```bash
{{ jobs_command }}
```

{% endif %}{% endif %}{% if storage_text %}## Object Storage / Media

{{ storage_text }}

{% endif %}{% if search_text %}## Search

{{ search_text }}

{% endif %}{% if email_text %}## Email

{{ email_text }}

{% endif %}## Deployment

{{ deployment_intro }}

{% for deployment in deployments %}### {{ deployment.name }}

{{ deployment.description }}

```bash
{{ deployment.command }}
```

{% endfor %}## CI/CD

{{ cicd_text }}

## Observability and Operations

{% for item in operations %}- **{{ item.name }}** — {{ item.description }}
{% endfor %}

## Security

{% for item in security_notes %}- {{ item }}
{% endfor %}

## Testing

{{ testing_text }}

```bash
{{ test_command }}
```

{% if e2e_command %}```bash
{{ e2e_command }}
```

{% endif %}## Upgrade Notes

{% for item in upgrade_notes %}- {{ item }}
{% endfor %}

## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}## Contributing

{{ contributing_text }}

## License

{{ license_text }}
