{% if logo_path %}<p align="center">
  <img src="{{ logo_path }}" alt="{{ project_name }}" width="{{ logo_width | default(440) }}">
</p>

{% endif %}# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if language_switch %}{{ language_switch }}

{% endif %}{% if navigation %}{{ navigation }}

{% endif %}## What {{ project_name }} is

{{ overview_text }}

## Why use it?

{{ why_text }}

## Scientific scope

{{ scope_text }}

## Features

{% for feature in features %}- **{{ feature.name }}** — {{ feature.description }}
{% endfor %}

## Installation

### Stable release

```bash
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

{% endfor %}{% endif %}{% if development_install %}### Development install

```bash
{{ development_install }}
```

{% endif %}## Five-minute example

{% if quickstart_intro %}{{ quickstart_intro }}

{% endif %}```python
{{ quickstart_code }}
```

{% if methods %}## Method catalogue

| Method / area | Purpose | New-data operation | Important boundary |
| --- | --- | --- | --- |
{% for method in methods %}| `{{ method.name }}` | {{ method.purpose }} | {{ method.operation }} | {{ method.notes }} |
{% endfor %}

{% endif %}{% if method_selection %}## Choosing a method

{{ method_selection }}

{% endif %}{% if data_contracts %}## Data contracts and conventions

{% for item in data_contracts %}- {{ item }}
{% endfor %}

{% endif %}{% if representative_example %}## Representative workflow

{{ representative_example.intro }}

```python
{{ representative_example.code }}
```

{% if representative_example.link %}See {{ representative_example.link }} for the complete workflow.
{% endif %}

{% endif %}{% if validation %}## Validation and reproducibility

{{ validation.summary }}

{% if validation["items"] %}{% for item in validation["items"] %}- {{ item }}
{% endfor %}
{% endif %}{% if validation.link %}
See {{ validation.link }} for reference cases, tolerances, and claim boundaries.
{% endif %}

{% endif %}{% if examples %}## Examples

{% for example in examples %}- **{{ example.name }}:** {{ example.link }}{% if example.description %} — {{ example.description }}{% endif %}
{% endfor %}

{% endif %}## Documentation

{% for doc in documentation %}- **{{ doc.name }}:** {{ doc.link }}{% if doc.description %} — {{ doc.description }}{% endif %}
{% endfor %}

{% if project_status %}## Project status and API stability

{{ project_status }}

{% endif %}{% if limitations %}## Limitations and interpretation boundaries

{% for limitation in limitations %}- {{ limitation }}
{% endfor %}

{% endif %}{% if citation %}## Citation

{{ citation.intro }}

{% if citation.bibtex %}```bibtex
{{ citation.bibtex }}
```

{% endif %}{% if citation.cff %}Citation metadata is available in [`CITATION.cff`]({{ citation.cff }}).
{% endif %}{% if citation.doi %}DOI: {{ citation.doi }}
{% endif %}

{% endif %}## Support and Contributing

{{ support_text }}
{% if contributing_link %}
Contributions are welcome. See [CONTRIBUTING.md]({{ contributing_link }}).
{% endif %}

## License

{{ license_text }}
