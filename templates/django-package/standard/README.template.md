<div align="center">

{% if logo_path %}<img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
{% endif %}{{ "\n" }}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}
{% endif %}{{ "\n" }}
{% if navigation %}{{ navigation }}
{% endif %}
</div>

---
## Why {{ display_name }}?

{{ why_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Installation

{{ installation_text }}

```bash
{{ install_command }}
```

## Configuration

{% for step in configuration_steps %}### {{ step.name }}

{% if step.description %}{{ step.description }}

{% endif %}```{{ step.language }}
{{ step.code }}
```

{% endfor %}{% if settings %}### Settings

| Setting | Default | Purpose |
| --- | --- | --- |
{% for setting in settings %}| `{{ setting.name }}` | `{{ setting.default }}` | {{ setting.purpose }} |
{% endfor %}

{% endif %}## Quick Start

{{ quickstart_intro }}

```{{ quickstart_language }}
{{ quickstart_code }}
```

## Usage Examples

{% for example in examples %}### {{ example.name }}

{{ example.description }}

```{{ example.language }}
{{ example.code }}
```

{% endfor %}## Compatibility

{{ compatibility_intro }}

| Django | Python | Status |
| --- | --- | --- |
{% for row in compatibility %}| {{ row.django }} | {{ row.python }} | {{ row.status }} |
{% endfor %}

## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}## Contributing

{{ contributing_text }}

## License

{{ license_text }}
