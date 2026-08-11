{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
</p>

{% endif %}{% if method_figure %}<p align="center">
  <img src="{{ method_figure }}" alt="{{ project_name }} method overview" width="{{ figure_width | default(760) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}## Scientific Problem

{{ problem_text }}

## Method Overview

{{ method_overview.text }}
{% if method_overview.equation %}

{{ method_overview.equation }}
{% endif %}

## Key Contributions

{% for contribution in contributions %}- {{ contribution }}
{% endfor %}

## Installation

{% if install_note %}{{ install_note }}

{% endif %}```bash
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
{% endif %}{% if validation.link %}

See {{ validation.link }} for complete validation scope and tolerances.
{% endif %}

## Limitations

{% for limitation in limitations %}- {{ limitation }}
{% endfor %}

## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}
{% endfor %}

## Citation

{{ citation.intro }}
{% if citation.paper %}

Method paper: {{ citation.paper }}
{% endif %}{% if citation.bibtex %}

```bibtex
{{ citation.bibtex }}
```
{% endif %}{% if citation.cff %}
Software citation metadata: [`CITATION.cff`]({{ citation.cff }}).
{% endif %}

## Support and Contributing

{{ support_text }}
{% if contributing_link %}

Contributions are welcome. See [CONTRIBUTING.md]({{ contributing_link }}).
{% endif %}

## License

{{ license_text }}
