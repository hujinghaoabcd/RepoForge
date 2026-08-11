from __future__ import annotations

import argparse
from pathlib import Path

from .renderer import render_from_config


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="repoforge")
    subparsers = parser.add_subparsers(dest="command", required=True)

    render = subparsers.add_parser("render", help="Render a README from one profile template.")
    render.add_argument("project_type", help="Project type, e.g. scientific-python")
    render.add_argument("profile", choices=("minimal", "standard", "full"))
    render.add_argument("--config", required=True, help="YAML configuration file")
    render.add_argument("--output", default="README.generated.md", help="Output Markdown path")
    render.add_argument(
        "--template-root",
        default=None,
        help="Optional path to RepoForge's templates directory",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "render":
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        rendered = render_from_config(
            args.project_type,
            args.profile,
            args.config,
            template_root=args.template_root,
        )
        output.write_text(rendered, encoding="utf-8")
        print(output)
        return 0

    raise RuntimeError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
