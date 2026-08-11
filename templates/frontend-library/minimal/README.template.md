<div align="center">

{% if logo_path %}<img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
{% endif %}{{ "\n" }}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}
{% endif %}{{ "\n" }}
</div>

---
## Install

```bash
{{ install_command }}
```

{% if setup_note %}{{ setup_note }}

{% endif %}## Quick Start

```{{ quickstart_language }}
{{ quickstart_code }}
```

## Browser Support

{{ browser_support }}

## License

{{ license_text }}
