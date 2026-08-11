from __future__ import annotations

import argparse
from email.parser import Parser
from pathlib import Path
import tarfile
import zipfile

EXPECTED_DISTRIBUTION = "repoforge-standards"
EXPECTED_RUNTIME_FILES = {
    "repoforge/_data/templates/scientific-python/standard/README.template.md",
    "repoforge/_data/templates/research-algorithm/full/README.template.md",
    "repoforge/_data/templates/desktop-application/full/README.template.md",
    "repoforge/_data/standards/matrix.yml",
    "repoforge/_data/standards/community/CODE_OF_CONDUCT.template.md",
    "repoforge/_data/standards/metadata/CITATION.template.cff",
}
EXPECTED_SDIST_SUFFIXES = {
    "templates/scientific-python/standard/README.template.md",
    "templates/desktop-application/full/README.template.md",
    "standards/matrix.yml",
    "standards/community/CODE_OF_CONDUCT.template.md",
    "standards/metadata/CITATION.template.cff",
    "setup.py",
    "MANIFEST.in",
}


def _one(path: Path, pattern: str) -> Path:
    matches = sorted(path.glob(pattern))
    if len(matches) != 1:
        raise SystemExit(
            f"Expected exactly one {pattern!r} in {path}, found {len(matches)}"
        )
    return matches[0]


def verify_wheel(wheel: Path, expected_version: str) -> None:
    with zipfile.ZipFile(wheel) as archive:
        names = set(archive.namelist())
        missing = EXPECTED_RUNTIME_FILES - names
        if missing:
            raise SystemExit(
                "Wheel is missing RepoForge runtime data:\n"
                + "\n".join(f"  - {name}" for name in sorted(missing))
            )

        metadata_names = [name for name in names if name.endswith(".dist-info/METADATA")]
        if len(metadata_names) != 1:
            raise SystemExit(
                f"Expected one wheel METADATA file, found {len(metadata_names)}"
            )
        metadata = Parser().parsestr(
            archive.read(metadata_names[0]).decode("utf-8")
        )

    if metadata["Name"] != EXPECTED_DISTRIBUTION:
        raise SystemExit(
            f"Unexpected distribution name: {metadata['Name']!r}; "
            f"expected {EXPECTED_DISTRIBUTION!r}"
        )
    if metadata["Version"] != expected_version:
        raise SystemExit(
            f"Unexpected wheel version: {metadata['Version']!r}; "
            f"expected {expected_version!r}"
        )


def verify_sdist(sdist: Path) -> None:
    with tarfile.open(sdist, "r:gz") as archive:
        names = archive.getnames()

    missing = {
        suffix
        for suffix in EXPECTED_SDIST_SUFFIXES
        if not any(name.endswith("/" + suffix) for name in names)
    }
    if missing:
        raise SystemExit(
            "Source distribution is missing build/runtime sources:\n"
            + "\n".join(f"  - {name}" for name in sorted(missing))
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dist", type=Path, help="Directory containing one wheel and one sdist")
    parser.add_argument("--version", required=True, help="Expected package version")
    args = parser.parse_args()

    dist = args.dist.expanduser().resolve()
    verify_wheel(_one(dist, "*.whl"), args.version)
    verify_sdist(_one(dist, "*.tar.gz"))
    print(f"Verified RepoForge distributions in {dist}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
