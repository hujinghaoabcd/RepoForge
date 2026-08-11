{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}## Install

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
