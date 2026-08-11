{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(280) }}">
</p>

{% endif %}{% if demo_image %}<p align="center">
  <img src="{{ demo_image }}" alt="{{ project_name }} demo" width="{{ demo_width | default(900) }}">
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

{% if demo_url %}## Demo

{{ demo_url }}

{% endif %}## Installation

```bash
{{ install_command }}
```

{% if setup_text %}{{ setup_text }}

{% endif %}## Quick Start

```{{ quickstart_language }}
{{ quickstart_code }}
```

## API Overview

| API | Purpose |
| --- | --- |
{% for item in api_items %}| `{{ item.name }}` | {{ item.purpose }} |
{% endfor %}

{% if styling_text %}## Styling and Theming

{{ styling_text }}

{% endif %}{% if integrations %}## Framework Integration

{% for item in integrations %}- **{{ item.name }}:** {{ item.description }}{% if item.link %} — {{ item.link }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}{% endif %}## Compatibility

| Target | Supported range | Notes |
| --- | --- | --- |
{% for item in compatibility %}| **{{ item.target }}** | {{ item.range }} | {{ item.notes }} |
{% endfor %}

## Development and Testing

```bash
{{ development_command }}
```

```bash
{{ test_command }}
```

{% if documentation %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}{{ "\n" }}{% endfor %}{{ "\n" }}{% endif %}## License

{{ license_text }}
