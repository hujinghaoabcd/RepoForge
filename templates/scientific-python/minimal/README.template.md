{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if intro %}{{ intro }}

{% endif %}## Installation

```bash
{{ install_command }}
```

## Quick Start

```python
{{ quickstart_code }}
```

## Documentation

{{ documentation }}

{% if citation %}## Citation

{{ citation }}

{% endif %}## License

{{ license_text }}
