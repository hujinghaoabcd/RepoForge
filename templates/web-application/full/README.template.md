{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(280) }}">
</p>

{% endif %}{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} product screenshot" width="{{ screenshot_width | default(900) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}## Product Overview

{{ overview_text }}

{% if demo_url %}Demo: {{ demo_url }}

{% endif %}## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Architecture

{{ architecture_intro }}

| Component | Technology / service | Responsibility |
| --- | --- | --- |
{% for item in architecture %}| **{{ item.component }}** | {{ item.technology }} | {{ item.responsibility }} |
{% endfor %}

## Local Development

### Requirements

{% for item in requirements %}- {{ item }}
{% endfor %}

### Bootstrap

```bash
{{ local_command }}
```

{% if local_urls %}### Local access points

{% for item in local_urls %}- **{{ item.name }}:** {{ item.url }}
{% endfor %}

{% endif %}## Configuration and Secrets

{{ configuration_intro }}

| Variable | Required | Secret | Purpose |
| --- | --- | --- | --- |
{% for item in environment %}| `{{ item.name }}` | {{ item.required }} | {{ item.secret }} | {{ item.purpose }} |
{% endfor %}

{% if database_text %}## Database and Migrations

{{ database_text }}

{% if migration_command %}```bash
{{ migration_command }}
```

{% endif %}{% endif %}{% if api_text %}## API

{{ api_text }}

{% if api_docs %}API documentation: {{ api_docs }}

{% endif %}{% endif %}{% if auth_text %}## Authentication and Authorization

{{ auth_text }}

{% endif %}{% if background_text %}## Background Jobs and Queues

{{ background_text }}

{% endif %}{% if storage_text %}## File and Object Storage

{{ storage_text }}

{% endif %}## Deployment

{{ deployment_intro }}

{% for item in deployment_steps %}### {{ item.name }}

{{ item.description }}

{% if item.command %}```bash
{{ item.command }}
```

{% endif %}{% endfor %}{% if ci_cd_text %}## CI/CD

{{ ci_cd_text }}

{% endif %}## Observability and Operations

{% for item in operations %}### {{ item.name }}

{{ item.description }}

{% if item.command %}```bash
{{ item.command }}
```

{% endif %}{% endfor %}{% if backup_text %}## Backup and Restore

{{ backup_text }}

{% endif %}## Security

{% for note in security_notes %}- {{ note }}
{% endfor %}

## Testing

{{ testing_text }}

```bash
{{ test_command }}
```

{% if documentation %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}{% endif %}## Upgrade Notes

{% for note in upgrade_notes %}- {{ note }}
{% endfor %}

## Contributing

{{ contributing_text }}

## License

{{ license_text }}
