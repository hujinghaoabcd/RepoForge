<div align="center">

{% if logo_path %}<img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(160) }}">
{% endif %}{{ "\n" }}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}
{% endif %}{{ "\n" }}
{% if language_switch %}{{ language_switch }}
{% endif %}{{ "\n" }}
{% if navigation %}{{ navigation }}
{% endif %}
</div>

---
## Why {{ project_name }}?

{{ why_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Installation

{% if install_note %}{{ install_note }}

{% endif %}```bash
{{ install_command }}
```

{% if verify_command %}Verify the installation:

```bash
{{ verify_command }}
```

{% endif %}{% if optional_install_commands %}### Optional features

{% for item in optional_install_commands %}```bash
{{ item.command }}  # {{ item.description }}
```

{% endfor %}{% endif %}## Quick Start

{% if quickstart_intro %}{{ quickstart_intro }}

{% endif %}```python
{{ quickstart_code }}
```

{% if methods %}## Methods and Capabilities

| Method / area | Purpose | Notes |
| --- | --- | --- |
{% for method in methods %}| `{{ method.name }}` | {{ method.purpose }} | {{ method.notes }} |
{% endfor %}

{% endif %}{% if validation %}## Validation

{{ validation.summary }}

{% if validation["items"] %}{% for item in validation["items"] %}- {{ item }}
{% endfor %}
{% endif %}{% if validation.link %}
See {{ validation.link }} for reference cases, tolerances, and claim boundaries.
{% endif %}

{% endif %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}
{% endfor %}

{% if citation %}## Citation

{{ citation.intro }}

{% if citation.cff %}Citation metadata is available in [`CITATION.cff`]({{ citation.cff }}).
{% endif %}{% if citation.doi %}DOI: {{ citation.doi }}
{% endif %}

{% endif %}{% if limitations %}## Limitations

{% for limitation in limitations %}- {{ limitation }}
{% endfor %}

{% endif %}## Support and Contributing

{{ support_text }}
{% if contributing_link %}
Contributions are welcome. See [CONTRIBUTING.md]({{ contributing_link }}).
{% endif %}

## License

{{ license_text }}
