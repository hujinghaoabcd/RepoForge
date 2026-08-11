from __future__ import annotations

from pathlib import Path

from setuptools import setup
from setuptools.command.build_py import build_py as _build_py


ROOT = Path(__file__).resolve().parent
RUNTIME_DATA_DIRS = ("templates", "standards")


class build_py(_build_py):
    """Copy RepoForge's external runtime data into the installed package."""

    def _runtime_outputs(self) -> list[Path]:
        outputs: list[Path] = []
        package_root = Path(self.build_lib) / "repoforge" / "_data"
        for directory in RUNTIME_DATA_DIRS:
            source_root = ROOT / directory
            if not source_root.is_dir():
                raise RuntimeError(f"Required runtime data directory is missing: {source_root}")
            for source in source_root.rglob("*"):
                if source.is_file():
                    outputs.append(package_root / directory / source.relative_to(source_root))
        return outputs

    def run(self) -> None:
        super().run()
        package_root = Path(self.build_lib) / "repoforge" / "_data"
        for directory in RUNTIME_DATA_DIRS:
            source_root = ROOT / directory
            if not source_root.is_dir():
                raise RuntimeError(f"Required runtime data directory is missing: {source_root}")
            for source in source_root.rglob("*"):
                if not source.is_file():
                    continue
                destination = package_root / directory / source.relative_to(source_root)
                self.mkpath(str(destination.parent))
                self.copy_file(str(source), str(destination))

    def get_outputs(self, include_bytecode: int = 1) -> list[str]:
        outputs = list(super().get_outputs(include_bytecode=include_bytecode))
        outputs.extend(str(path) for path in self._runtime_outputs())
        return outputs


setup(cmdclass={"build_py": build_py})
