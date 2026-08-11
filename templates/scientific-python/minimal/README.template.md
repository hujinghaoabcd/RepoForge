<div align="center">

{% if logo_path %}<img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
{% endif %}{{ "\n" }}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}
{% endif %}{{ "\n" }}
</div>

---
## Installation

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
