{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(420) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}{{ intro_text }}

## Installation

```bash
{{ install_command }}
```

## Setup

{% for step in setup_steps %}### {{ step.name }}

{% if step.description %}{{ step.description }}

{% endif %}```{{ step.language }}
{{ step.code }}
```

{% endfor %}## Quick Start

{{ quickstart_intro }}

```{{ quickstart_language }}
{{ quickstart_code }}
```

## Compatibility

{{ compatibility_text }}

## License

{{ license_text }}
