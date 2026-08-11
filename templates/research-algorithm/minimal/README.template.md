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

{% if quickstart_intro %}{{ quickstart_intro }}

{% endif %}```python
{{ quickstart_code }}
```

## Validation

{{ validation.summary }}
{% if validation["checks"] %}
{% for check in validation["checks"] %}- {{ check }}
{% endfor %}
{% endif %}

## Citation

{{ citation.intro }}
{% if citation.paper %}
Method paper: {{ citation.paper }}
{% endif %}{% if citation.cff %}
Software citation metadata: [`CITATION.cff`]({{ citation.cff }}).
{% endif %}

## License

{{ license_text }}
