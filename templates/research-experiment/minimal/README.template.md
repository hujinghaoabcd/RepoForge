# {{ project_name }}

**{{ tagline }}**

{% if badges %}{{ badges }}

{% endif %}{% if paper_link %}Paper: {{ paper_link }}

{% endif %}## Environment

{{ environment_text }}

```bash
{{ environment_command }}
```

## Data

{{ data_text }}

Expected path: `{{ data_path }}`

## Run

{{ run_text }}

```bash
{{ run_command }}
```

## Expected Output

{{ output_text }}
{% if expected_result %}

Expected sanity check: {{ expected_result }}
{% endif %}

## Citation

{{ citation.intro }}
{% if citation.paper %}

Paper: {{ citation.paper }}
{% endif %}{% if citation.cff %}
Software citation metadata: [`CITATION.cff`]({{ citation.cff }}).
{% endif %}

## License

{{ license_text }}
