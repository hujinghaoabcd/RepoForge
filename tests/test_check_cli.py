from copy import deepcopy
from pathlib import Path

import yaml

from repoforge.cli import main
from repoforge.renderer import load_config

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "examples" / "apply" / "scientific-python-standard.yml"
TEMPLATES = ROOT / "templates"
STANDARDS = ROOT / "standards"


def _write_config(target: Path, *, example_author: bool = False) -> Path:
    config = deepcopy(load_config(CONFIG))
    config["repoforge"] = {
        "config_version": 1,
        "project_type": "scientific-python",
        "profile": "standard",
    }
    config["code_of_conduct"]["reporting_contact"] = "conduct@example.org"
    config["security"]["reporting_contact"] = "security@example.org"
    if not example_author:
        config["citation"]["authors"] = [
            {
                "family_names": "Smith",
                "given_names": "Alex",
                "orcid": None,
                "affiliation": "Example Lab",
            }
        ]
    path = target / "repoforge.yml"
    path.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")
    return path


def _plan_args(target: Path) -> list[str]:
    return [
        str(target),
        "--template-root",
        str(TEMPLATES),
        "--standards-root",
        str(STANDARDS),
    ]


def test_check_cli_defaults_to_target_repoforge_config(tmp_path, capsys):
    config = _write_config(tmp_path)
    assert main(["apply", str(tmp_path), "--config", str(config), "--template-root", str(TEMPLATES), "--standards-root", str(STANDARDS)]) == 0
    capsys.readouterr()

    exit_code = main(["check", *_plan_args(tmp_path)])
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "PASS  repoforge.yml" in output
    assert "PASS  README.md" in output
    assert "0 failed" in output
    assert "Repository standards are in sync." in output


def test_check_cli_returns_nonzero_for_drift(tmp_path, capsys):
    config = _write_config(tmp_path)
    assert main(["apply", str(tmp_path), "--config", str(config), "--template-root", str(TEMPLATES), "--standards-root", str(STANDARDS)]) == 0
    capsys.readouterr()
    (tmp_path / "README.md").write_text("# drift\n", encoding="utf-8")

    exit_code = main(["check", *_plan_args(tmp_path)])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "FAIL  README.md" in output
    assert "repoforge diff" in output


def test_check_cli_strict_promotes_warning_to_failure(tmp_path, capsys):
    config = _write_config(tmp_path, example_author=True)
    assert main(["apply", str(tmp_path), "--config", str(config), "--template-root", str(TEMPLATES), "--standards-root", str(STANDARDS)]) == 0
    capsys.readouterr()

    assert main(["check", *_plan_args(tmp_path)]) == 0
    output = capsys.readouterr().out
    assert "WARN  repoforge.yml" in output

    assert main(["check", *_plan_args(tmp_path), "--strict"]) == 1


def test_check_cli_handles_missing_default_config(tmp_path, capsys):
    exit_code = main(["check", *_plan_args(tmp_path)])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "FAIL  repoforge.yml" in output
    assert "1 failed" in output
