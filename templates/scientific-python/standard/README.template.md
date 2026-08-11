{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(420) }}">
</p>
{% endif %}

# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}
{% endif %}
{% if navigation %}{{ navigation }}
{% endif %}

## Why {{ project_name }}?

{{ why_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Installation

```bash
{{ install_command }}
```

{% if verify_command %}Verify the installation:

```bash
{{ verify_command }}
```
{% endif %}

## Quick Start

{{ quickstart_intro }}

```python
{{ quickstart_code }}
```

{% if methods %}## Methods and Capabilities

| Method / area | Purpose | Notes |
| --- | --- | --- |
{% for method in methods %}| `{{ method.name }}` | {{ method.purpose }} | {{ method.notes }} |
{% endfor %}

{% endif %}
{% if validation %}## Validation

{{ validation.summary }}

{% for item in validation.items %}- {{ item }}
{% endfor %}

{% endif %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}
{% endfor %}

{% if citation %}## Citation

{{ citation.intro }}

{% if citation.cff %}Citation metadata is available in [`CITATION.cff`]({{ citation.cff }}).
{% endif %}
{% endif %}## Support and Contributing

{{ support_text }}
{% if contributing_link %}
Contributions are welcome. See [CONTRIBUTING.md]({{ contributing_link }}).
{% endif %}

## License

{{ license_text }}
