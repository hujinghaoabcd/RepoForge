from pathlib import Path

from repoforge.cli import main

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "examples" / "apply" / "scientific-python-standard.yml"
TEMPLATES = ROOT / "templates"
STANDARDS = ROOT / "standards"


def _args(target: Path, *extra: str) -> list[str]:
    return [
        "diff",
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


def _apply_args(target: Path) -> list[str]:
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
    ]


def test_diff_cli_new_repository_shows_create_without_writing(tmp_path, capsys):
    assert main(_args(tmp_path)) == 0
    output = capsys.readouterr().out

    assert "[create] README.md" in output
    assert "--- /dev/null" in output
    assert "+++ b/README.md" in output
    assert "[create] CITATION.cff" in output
    assert not (tmp_path / "README.md").exists()
    assert not (tmp_path / "CITATION.cff").exists()


def test_diff_cli_after_apply_reports_no_changes(tmp_path, capsys):
    assert main(_apply_args(tmp_path)) == 0
    capsys.readouterr()

    assert main(_args(tmp_path)) == 0
    assert capsys.readouterr().out == "No changes.\n"


def test_diff_cli_detects_manual_readme_change(tmp_path, capsys):
    assert main(_apply_args(tmp_path)) == 0
    capsys.readouterr()

    readme = tmp_path / "README.md"
    original = readme.read_text(encoding="utf-8")
    readme.write_text("MANUAL HEADER\n" + original, encoding="utf-8")

    assert main(_args(tmp_path, "--context", "1")) == 0
    output = capsys.readouterr().out

    assert "[overwrite] README.md" in output
    assert "-MANUAL HEADER" in output
    assert "[overwrite] CITATION.cff" not in output


def test_diff_cli_show_unchanged_lists_matching_files(tmp_path, capsys):
    assert main(_apply_args(tmp_path)) == 0
    capsys.readouterr()

    assert main(_args(tmp_path, "--show-unchanged")) == 0
    output = capsys.readouterr().out

    assert "[unchanged] README.md" in output
    assert "[unchanged] CITATION.cff" in output
