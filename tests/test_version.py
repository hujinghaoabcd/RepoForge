from __future__ import annotations

from importlib.metadata import metadata, version

from repoforge import __version__


def test_distribution_identity_and_version() -> None:
    assert version("repoforge-standards") == __version__ == "0.1.0a1"
    assert metadata("repoforge-standards")["Name"] == "repoforge-standards"
