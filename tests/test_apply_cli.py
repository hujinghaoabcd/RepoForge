from pathlib import Path

from repoforge.cli import main

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "examples" / "apply" / "scientific-python-standard.yml"
TEMPLATES = ROOT / "templates"
STANDARDS = ROOT / "standards"


def _args(target: Path, *extra: str) -> list[str]:
    return [
        "apply",
        str(target),
        "--type",
        "scientific-python",
        "--profile",
        "standard",
        "--config",
        str(CONFIG),
        "--template-root",
        str(TEMPLATES),
        "--standards-root",
        str(STANDARDS),
        *extra,
    ]


def test_apply_cli_dry_run_does_not_write(tmp_path, capsys):
    exit_code = main(_args(tmp_path, "--dry-run"))
    assert exit_code == 0
    assert not (tmp_path / "README.md").exists()

    output = capsys.readouterr().out
    assert "[create] README.md" in output
    assert "[create] CITATION.cff" in output


def test_apply_cli_writes_default_repository_pack(tmp_path):
    exit_code = main(_args(tmp_path))
    assert exit_code == 0

    expected = (
        "README.md",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "CITATION.cff",
        "CHANGELOG.md",
        ".github/ISSUE_TEMPLATE/01-bug-report.yml",
        ".github/ISSUE_TEMPLATE/02-feature-request.yml",
        ".github/ISSUE_TEMPLATE/config.yml",
        ".github/pull_request_template.md",
    )
    for relative in expected:
        assert (tmp_path / relative).is_file(), relative

    assert not (tmp_path / "SUPPORT.md").exists()


def test_apply_cli_second_run_is_unchanged(tmp_path, capsys):
    assert main(_args(tmp_path)) == 0
    capsys.readouterr()

    assert main(_args(tmp_path)) == 0
    output = capsys.readouterr().out
    assert "[unchanged] README.md" in output
    assert "[overwrite]" not in output


def test_apply_cli_recommended_policy_adds_support(tmp_path):
    assert main(_args(tmp_path, "--standards", "recommended")) == 0
    assert (tmp_path / "SUPPORT.md").is_file()
