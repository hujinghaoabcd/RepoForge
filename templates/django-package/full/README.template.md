{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
</p>

{% endif %}{% if screenshot_path %}<p align="center">
  <img src="{{ screenshot_path }}" alt="{{ project_name }} screenshot" width="{{ screenshot_width | default(900) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}## Why {{ display_name }}?

{{ why_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Installation

### Stable install

```bash
{{ install_command }}
```
{% if optional_install_command %}

### Optional integrations

```bash
{{ optional_install_command }}
```
{% endif %}

## Quick Start

{{ quickstart_intro }}

```{{ quickstart_language }}
{{ quickstart_code }}
```

## Configuration Reference

{% for step in configuration_steps %}### {{ step.name }}

{% if step.description %}{{ step.description }}

{% endif %}```{{ step.language }}
{{ step.code }}
```

{% endfor %}{% if settings %}### Settings

| Setting | Default | Required | Purpose |
| --- | --- | --- | --- |
{% for setting in settings %}| `{{ setting.name }}` | `{{ setting.default }}` | {{ setting.required }} | {{ setting.purpose }} |
{% endfor %}

{% endif %}{% if assets_text %}### Templates / Static Assets

{{ assets_text }}

{% endif %}{% if models_text %}## Models and Migrations

{{ models_text }}

{% if migration_command %}```bash
{{ migration_command }}
```

{% endif %}{% endif %}{% if admin_text %}## Admin Integration

{{ admin_text }}

{% if admin_code %}```python
{{ admin_code }}
```

{% endif %}{% endif %}{% if public_api %}## Public Python API

| API | Purpose | Stability |
| --- | --- | --- |
{% for item in public_api %}| `{{ item.name }}` | {{ item.purpose }} | {{ item.stability }} |
{% endfor %}

{% endif %}{% if frontend_text %}## Frontend Integration

{{ frontend_text }}

{% endif %}## Permissions and Security Notes

{% for note in security_notes %}- {{ note }}
{% endfor %}

## Compatibility Matrix

{{ compatibility_intro }}

| Package | Supported / tested range | Notes |
| --- | --- | --- |
{% for row in compatibility %}| **{{ row.component }}** | {{ row.range }} | {{ row.notes }} |
{% endfor %}

## Testing

{{ testing_text }}

```bash
{{ test_command }}
```
{% if matrix_command %}

```bash
{{ matrix_command }}
```
{% endif %}

## Upgrade Notes

{% for note in upgrade_notes %}- {{ note }}
{% endfor %}

## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}## Support and Contributing

{{ contributing_text }}

## License

{{ license_text }}
