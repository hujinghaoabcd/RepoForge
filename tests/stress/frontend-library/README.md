# Frontend Library stress suite

These renderer-backed cases pressure-test `frontend-library` against packages with very different consumer contracts.

The suite protects two rules:

1. required setup such as CSS and peer dependencies must stay visible near install/usage;
2. Full means deeper consumer documentation, not automatic React/Vue adapters, SSR support, or every distribution feature.

Stress overrides are merged onto the canonical profile config and rendered through the normal RepoForge renderer with the shared 280px preview branding.
