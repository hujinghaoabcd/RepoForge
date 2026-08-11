# Support

This document explains where to ask for help with {{ project_name }} and where different kinds of reports belong.

## Getting help

{% for channel in support_channels %}### {{ channel.name }}

{{ channel.description }}

{{ channel.location }}

{% endfor %}## Before asking

Please check the README, documentation, existing issues, and release notes when relevant. A concise reproducible example is usually more useful than a long description without context.

For technical questions, include the information needed to understand your environment, such as project version, operating system, runtime version, relevant configuration, and the smallest example that demonstrates the problem.

## Use the right channel

- **Bug or feature work:** follow `CONTRIBUTING.md` and use the repository issue tracker.
- **Security vulnerability:** follow `SECURITY.md` and report privately.
- **Conduct concern:** follow `CODE_OF_CONDUCT.md` and report privately.
- **Project-specific usage help:** use one of the support channels above.

## Support boundaries

{{ support_boundaries }}

Support is provided on a best-effort basis unless the project explicitly documents a separate service-level or commercial support agreement.
