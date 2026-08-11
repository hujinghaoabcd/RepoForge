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
{% if language_switch %}{{ language_switch }}
{% endif %}

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
{% endif %}
{% if optional_install_commands %}
### Optional features

{% for item in optional_install_commands %}```bash
{{ item.command }}  # {{ item.description }}
```
{% endfor %}
{% endif %}

## Quick Start

{{ quickstart_intro }}

```python
{{ quickstart_code }}
```

{% if quickstart_result %}{{ quickstart_result }}
{% endif %}

{% if methods %}## Methods and capabilities

{% if methods_intro %}{{ methods_intro }}

{% endif %}| Method / area | Purpose | Notes |
| --- | --- | --- |
{% for method in methods %}| `{{ method.name }}` | {{ method.purpose }} | {{ method.notes }} |
{% endfor %}

{% endif %}
{% if representative_example %}## Representative Example

{{ representative_example.intro }}

```python
{{ representative_example.code }}
```

{% if representative_example.link %}See {{ representative_example.link }} for the complete workflow.
{% endif %}

{% endif %}
{% if validation %}## Validation

{{ validation.summary }}

{% if validation.items %}{% for item in validation.items %}- {{ item }}
{% endfor %}
{% endif %}
{% if validation.link %}
See {{ validation.link }} for the validation scope, reference cases, and known boundaries.
{% endif %}

{% endif %}## Documentation

{% if documentation_intro %}{{ documentation_intro }}

{% endif %}{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}
{% endfor %}

{% if citation %}## Citation

{{ citation.intro }}

{% if citation.bibtex %}```bibtex
{{ citation.bibtex }}
```
{% endif %}
{% if citation.cff %}Citation metadata is available in [`CITATION.cff`]({{ citation.cff }}).
{% endif %}
{% if citation.doi %}DOI: {{ citation.doi }}
{% endif %}

{% endif %}
{% if limitations %}## Limitations

{% for limitation in limitations %}- {{ limitation }}
{% endfor %}

{% endif %}## Support and Contributing

{% if support_text %}{{ support_text }}

{% endif %}{% if contributing_link %}Contributions are welcome. Please read [CONTRIBUTING.md]({{ contributing_link }}) before opening a pull request.
{% endif %}

## License

{{ license_text }}
