from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
LOGO_WIDTH = 160


def replace(path: Path, pattern: str, replacement: str) -> bool:
    text = path.read_text(encoding="utf-8")
    updated = re.sub(pattern, replacement, text, flags=re.MULTILINE)
    if updated == text:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    changed = 0

    for path in sorted(TEMPLATES.glob("*/*/config.example.yml")):
        changed += replace(
            path,
            r"^logo_width:\s*\d+\s*$",
            f"logo_width: {LOGO_WIDTH}",
        )

    for path in sorted(TEMPLATES.glob("*/*/README.template.md")):
        changed += replace(
            path,
            r"logo_width\s*\|\s*default\(\d+\)",
            f"logo_width | default({LOGO_WIDTH})",
        )

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_previews.py")],
        cwd=ROOT,
        check=True,
    )

    print(f"normalized {changed} template/config files; regenerated previews")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
