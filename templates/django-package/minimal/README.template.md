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
