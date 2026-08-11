from __future__ import annotations

import argparse
from pathlib import Path

from .apply import STANDARD_KEYS, apply_to_repository, build_apply_plan
from .renderer import SUPPORTED_TYPES, load_config, render_from_config


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

    apply_parser = subparsers.add_parser(
        "apply",
        help="Apply a README and selected repository standards to an existing repository.",
    )
    apply_parser.add_argument("target", help="Existing repository directory")
    apply_parser.add_argument(
        "--type",
        dest="project_type",
        required=True,
        choices=tuple(sorted(SUPPORTED_TYPES)),
        help="Explicit RepoForge project type",
    )
    apply_parser.add_argument(
        "--profile",
        required=True,
        choices=("minimal", "standard", "full"),
        help="README documentation profile",
    )
    apply_parser.add_argument(
        "--config",
        required=True,
        help="Combined RepoForge YAML configuration",
    )
    apply_parser.add_argument(
        "--standards",
        choices=("none", "default", "recommended"),
        default="default",
        help=(
            "Base standards policy: none=README only, default=matrix defaults, "
            "recommended=defaults plus recommendations"
        ),
    )
    apply_parser.add_argument(
        "--include",
        action="append",
        choices=tuple(sorted(STANDARD_KEYS)),
        default=[],
        help="Explicitly include a repository standard, including an optional one",
    )
    apply_parser.add_argument(
        "--exclude",
        action="append",
        choices=tuple(sorted(STANDARD_KEYS)),
        default=[],
        help="Explicitly exclude a repository standard selected by the base policy",
    )
    apply_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show create/overwrite/unchanged actions without writing files",
    )
    apply_parser.add_argument(
        "--force",
        action="store_true",
        help="Allow overwriting selected files whose content differs",
    )
    apply_parser.add_argument(
        "--template-root",
        default=None,
        help="Optional path to RepoForge's templates directory",
    )
    apply_parser.add_argument(
        "--standards-root",
        default=None,
        help="Optional path to RepoForge's standards directory",
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

    if args.command == "apply":
        config = load_config(args.config)
        plan = build_apply_plan(
            args.project_type,
            args.profile,
            config,
            standards_policy=args.standards,
            include=set(args.include),
            exclude=set(args.exclude),
            template_root=args.template_root,
            standards_root=args.standards_root,
        )
        results = apply_to_repository(
            args.target,
            plan,
            force=args.force,
            dry_run=args.dry_run,
        )
        for result in results:
            print(f"[{result.status}] {result.path}")
        return 0

    raise RuntimeError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
