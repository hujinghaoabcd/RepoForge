from __future__ import annotations

import argparse
from pathlib import Path

import yaml
from jinja2 import UndefinedError

from . import __version__
from .apply import STANDARD_KEYS, apply_to_repository, build_apply_plan
from .check import check_exit_code, check_repository, format_check_results
from .diff import build_repository_diff, format_repository_diff
from .init_config import init_repository_config, resolve_project_selection
from .renderer import SUPPORTED_TYPES, load_config, render_from_config


def _add_plan_selection_args(
    parser: argparse.ArgumentParser,
    *,
    config_required: bool = True,
) -> None:
    parser.add_argument("target", help="Existing repository directory")
    parser.add_argument(
        "--type",
        dest="project_type",
        choices=tuple(sorted(SUPPORTED_TYPES)),
        help="Explicit RepoForge project type; optional when stored in repoforge.yml",
    )
    parser.add_argument(
        "--profile",
        choices=("minimal", "standard", "full"),
        help="README profile; optional when stored in repoforge.yml",
    )
    parser.add_argument(
        "--config",
        required=config_required,
        default=None,
        help=(
            "Combined RepoForge YAML configuration"
            if config_required
            else "Combined RepoForge YAML configuration; defaults to TARGET/repoforge.yml"
        ),
    )
    parser.add_argument(
        "--standards",
        choices=("none", "default", "recommended"),
        default="default",
        help=(
            "Base standards policy: none=README only, default=matrix defaults, "
            "recommended=defaults plus recommendations"
        ),
    )
    parser.add_argument(
        "--include",
        action="append",
        choices=tuple(sorted(STANDARD_KEYS)),
        default=[],
        help="Explicitly include a repository standard, including an optional one",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        choices=tuple(sorted(STANDARD_KEYS)),
        default=[],
        help="Explicitly exclude a repository standard selected by the base policy",
    )
    parser.add_argument(
        "--template-root",
        default=None,
        help="Optional path to RepoForge's templates directory",
    )
    parser.add_argument(
        "--standards-root",
        default=None,
        help="Optional path to RepoForge's standards directory",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="repoforge")
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
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

    init_parser = subparsers.add_parser(
        "init",
        help="Create a combined repoforge.yml starter configuration for an existing repository.",
    )
    init_parser.add_argument("target", help="Existing repository directory")
    init_parser.add_argument(
        "--type",
        dest="project_type",
        required=True,
        choices=tuple(sorted(SUPPORTED_TYPES)),
        help="Explicit RepoForge project type",
    )
    init_parser.add_argument(
        "--profile",
        required=True,
        choices=("minimal", "standard", "full"),
        help="README documentation profile",
    )
    init_parser.add_argument(
        "--name",
        default=None,
        help="Project name; defaults to the target directory name",
    )
    init_parser.add_argument(
        "--repository-url",
        default=None,
        help="Repository URL used by generated support, issue, and citation settings",
    )
    init_parser.add_argument(
        "--output",
        default="repoforge.yml",
        help="Config path relative to the target repository",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing RepoForge config",
    )
    init_parser.add_argument(
        "--template-root",
        default=None,
        help="Optional path to RepoForge's templates directory",
    )
    init_parser.add_argument(
        "--standards-root",
        default=None,
        help="Optional path to RepoForge's standards directory",
    )

    diff_parser = subparsers.add_parser(
        "diff",
        help="Show unified diffs for files selected by the RepoForge apply plan.",
    )
    _add_plan_selection_args(diff_parser)
    diff_parser.add_argument(
        "--context",
        type=int,
        default=3,
        help="Number of unchanged context lines shown around each diff hunk",
    )
    diff_parser.add_argument(
        "--show-unchanged",
        action="store_true",
        help="Also list selected files whose generated content already matches",
    )

    check_parser = subparsers.add_parser(
        "check",
        help="Validate RepoForge-managed repository files and CI-facing contracts.",
    )
    _add_plan_selection_args(check_parser, config_required=False)
    check_parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a non-zero exit code for warnings as well as failures",
    )

    apply_parser = subparsers.add_parser(
        "apply",
        help="Apply a README and selected repository standards to an existing repository.",
    )
    _add_plan_selection_args(apply_parser)
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
    return parser


def _config_path_from_args(args: argparse.Namespace) -> Path:
    if args.config:
        return Path(args.config).expanduser().resolve()
    return Path(args.target).expanduser().resolve() / "repoforge.yml"


def _build_plan_from_args(args: argparse.Namespace):
    config = load_config(_config_path_from_args(args))
    project_type, profile = resolve_project_selection(
        config,
        args.project_type,
        args.profile,
    )
    plan = build_apply_plan(
        project_type,
        profile,
        config,
        standards_policy=args.standards,
        include=set(args.include),
        exclude=set(args.exclude),
        template_root=args.template_root,
        standards_root=args.standards_root,
    )
    return config, plan


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

    if args.command == "init":
        output = init_repository_config(
            args.target,
            args.project_type,
            args.profile,
            project_name=args.name,
            repository_url=args.repository_url,
            output=args.output,
            force=args.force,
            template_root=args.template_root,
            standards_root=args.standards_root,
        )
        print(output)
        print("Review the generated config before running repoforge apply.")
        return 0

    if args.command == "diff":
        _, plan = _build_plan_from_args(args)
        results = build_repository_diff(
            args.target,
            plan,
            context=args.context,
            include_unchanged=args.show_unchanged,
        )
        print(format_repository_diff(results), end="")
        return 0

    if args.command == "check":
        try:
            config, plan = _build_plan_from_args(args)
            results = check_repository(args.target, plan, config)
        except (FileNotFoundError, ValueError, yaml.YAMLError, UndefinedError) as exc:
            print(f"FAIL  repoforge.yml  {exc}")
            print("\nSummary: 0 passed, 0 warnings, 1 failed.")
            return 1
        print(format_check_results(results), end="")
        return check_exit_code(results, strict=args.strict)

    if args.command == "apply":
        _, plan = _build_plan_from_args(args)
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
