from pathlib import Path
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_init_cli_creates_config_and_apply_can_use_embedded_selection(tmp_path):
    target = tmp_path / "demo-project"
    target.mkdir()

    init_result = subprocess.run(
        [
            sys.executable,
            "-m",
            "repoforge.cli",
            "init",
            str(target),
            "--type",
            "scientific-python",
            "--profile",
            "standard",
            "--name",
            "DemoProject",
            "--repository-url",
            "https://github.com/example/demo-project",
            "--template-root",
            str(ROOT / "templates"),
            "--standards-root",
            str(ROOT / "standards"),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    config_path = target / "repoforge.yml"
    assert config_path.exists()
    assert "Review the generated config" in init_result.stdout

    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    assert config["repoforge"]["project_type"] == "scientific-python"
    assert config["repoforge"]["profile"] == "standard"
    assert config["project_name"] == "DemoProject"

    apply_result = subprocess.run(
        [
            sys.executable,
            "-m",
            "repoforge.cli",
            "apply",
            str(target),
            "--config",
            str(config_path),
            "--dry-run",
            "--template-root",
            str(ROOT / "templates"),
            "--standards-root",
            str(ROOT / "standards"),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "[create] README.md" in apply_result.stdout
    assert not (target / "README.md").exists()
