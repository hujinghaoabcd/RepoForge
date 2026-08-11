from pathlib import Path

import pytest

from repoforge.apply import PlannedFile
from repoforge.diff import build_repository_diff, format_repository_diff


def test_diff_new_file_uses_dev_null_and_does_not_write(tmp_path):
    plan = [PlannedFile(Path("README.md"), "# New\n", "readme")]

    results = build_repository_diff(tmp_path, plan)

    assert len(results) == 1
    assert results[0].status == "create"
    assert "--- /dev/null" in results[0].diff
    assert "+++ b/README.md" in results[0].diff
    assert "+# New" in results[0].diff
    assert not (tmp_path / "README.md").exists()


def test_diff_overwrite_shows_old_and_new_lines(tmp_path):
    (tmp_path / "README.md").write_text("# Old\nkeep\n", encoding="utf-8")
    plan = [PlannedFile(Path("README.md"), "# New\nkeep\n", "readme")]

    results = build_repository_diff(tmp_path, plan)

    assert results[0].status == "overwrite"
    assert "--- a/README.md" in results[0].diff
    assert "+++ b/README.md" in results[0].diff
    assert "-# Old" in results[0].diff
    assert "+# New" in results[0].diff


def test_diff_omits_unchanged_by_default(tmp_path):
    (tmp_path / "README.md").write_text("same\n", encoding="utf-8")
    plan = [PlannedFile(Path("README.md"), "same\n", "readme")]

    assert build_repository_diff(tmp_path, plan) == []
    assert format_repository_diff([]) == "No changes.\n"


def test_diff_can_list_unchanged_files(tmp_path):
    (tmp_path / "README.md").write_text("same\n", encoding="utf-8")
    plan = [PlannedFile(Path("README.md"), "same\n", "readme")]

    results = build_repository_diff(tmp_path, plan, include_unchanged=True)

    assert results[0].status == "unchanged"
    assert results[0].diff == ""
    assert format_repository_diff(results) == "[unchanged] README.md\n"


def test_diff_context_must_be_non_negative(tmp_path):
    plan = [PlannedFile(Path("README.md"), "# New\n", "readme")]

    with pytest.raises(ValueError, match="zero or greater"):
        build_repository_diff(tmp_path, plan, context=-1)
