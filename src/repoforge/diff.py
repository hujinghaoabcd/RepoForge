from __future__ import annotations

from dataclasses import dataclass
from difflib import unified_diff
from pathlib import Path
from typing import Literal

from .apply import PlannedFile, materialize_planned_content


DiffStatus = Literal["create", "overwrite", "unchanged"]


@dataclass(frozen=True)
class FileDiff:
    path: Path
    status: DiffStatus
    diff: str
    source: str


def _read_existing(path: Path) -> str | None:
    if not path.exists():
        return None
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _unified_text_diff(path: Path, old: str | None, new: str, context: int) -> str:
    old_lines = [] if old is None else old.splitlines(keepends=True)
    new_lines = new.splitlines(keepends=True)
    fromfile = "/dev/null" if old is None else f"a/{path.as_posix()}"
    tofile = f"b/{path.as_posix()}"
    return "".join(
        unified_diff(
            old_lines,
            new_lines,
            fromfile=fromfile,
            tofile=tofile,
            n=context,
        )
    )


def build_repository_diff(
    target: str | Path,
    plan: list[PlannedFile],
    *,
    context: int = 3,
    include_unchanged: bool = False,
) -> list[FileDiff]:
    if context < 0:
        raise ValueError("Diff context must be zero or greater.")

    root = Path(target).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Target repository does not exist: {root}")

    results: list[FileDiff] = []
    for item in plan:
        destination = root / item.path
        old = _read_existing(destination)
        desired = materialize_planned_content(destination, item)

        if not destination.exists():
            status: DiffStatus = "create"
        elif destination.is_file() and old == desired:
            status = "unchanged"
        else:
            status = "overwrite"

        if status == "unchanged" and not include_unchanged:
            continue

        text_diff = "" if status == "unchanged" else _unified_text_diff(
            item.path,
            old,
            desired,
            context,
        )
        results.append(FileDiff(item.path, status, text_diff, item.source))

    return results


def format_repository_diff(results: list[FileDiff]) -> str:
    if not results:
        return "No changes.\n"

    sections: list[str] = []
    for result in results:
        header = f"[{result.status}] {result.path.as_posix()}"
        if result.status == "unchanged":
            sections.append(header)
            continue
        body = result.diff.rstrip("\n")
        sections.append(f"{header}\n{body}")
    return "\n\n".join(sections) + "\n"
