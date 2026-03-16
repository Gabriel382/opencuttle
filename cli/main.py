from __future__ import annotations

# Standard library imports
import argparse
import sys
from typing import Sequence

# Local imports
from examples.demo_local_bus import run_demo


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="opencuttle",
        description="OpenCuttle CLI — local-first orchestration bus for heterogeneous agent systems.",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    run_parser = subparsers.add_parser(
        "run",
        help="Run the local OpenCuttle runtime",
        description="Run the local OpenCuttle runtime.",
    )
    run_parser.set_defaults(handler=handle_run)

    node_parser = subparsers.add_parser(
        "node",
        help="Inspect registered nodes",
        description="Inspect registered nodes.",
    )
    node_subparsers = node_parser.add_subparsers(dest="node_command", metavar="NODE_COMMAND")

    node_list_parser = node_subparsers.add_parser(
        "list",
        help="List registered nodes",
        description="List registered nodes.",
    )
    node_list_parser.set_defaults(handler=handle_node_list)

    node_inspect_parser = node_subparsers.add_parser(
        "inspect",
        help="Inspect one registered node",
        description="Inspect one registered node.",
    )
    node_inspect_parser.add_argument("name", help="Name of the node to inspect")
    node_inspect_parser.set_defaults(handler=handle_node_inspect)

    task_parser = subparsers.add_parser(
        "task",
        help="Run tasks through OpenCuttle",
        description="Run tasks through OpenCuttle.",
    )
    task_subparsers = task_parser.add_subparsers(dest="task_command", metavar="TASK_COMMAND")

    task_run_parser = task_subparsers.add_parser(
        "run",
        help="Run a simple task",
        description="Run a simple task.",
    )
    task_run_parser.add_argument("text", nargs="?", help="Task text to execute")
    task_run_parser.set_defaults(handler=handle_task_run)

    logs_parser = subparsers.add_parser(
        "logs",
        help="Show runtime logs",
        description="Show runtime logs.",
    )
    logs_parser.set_defaults(handler=handle_logs)

    return parser


def handle_run(args: argparse.Namespace) -> int:
    """
    Run the current local OpenCuttle runtime flow.

    Returns:
        Process exit code.
    """
    print("Starting OpenCuttle local runtime...\n")

    try:
        run_demo()
        return 0
    except FileNotFoundError as exc:
        print(f"OpenCuttle setup error: {exc}")
        return 1
    except Exception as exc:
        print(f"OpenCuttle runtime error: {exc}")
        return 1


def handle_node_list(args: argparse.Namespace) -> int:
    print("`opencuttle node list` will be implemented in Issue 23.")
    return 0


def handle_node_inspect(args: argparse.Namespace) -> int:
    print(f"`opencuttle node inspect {args.name}` will be implemented in Issue 24.")
    return 0


def handle_task_run(args: argparse.Namespace) -> int:
    text = args.text if args.text else "<no task text provided>"
    print(f"`opencuttle task run` will be implemented in Issue 25. Input: {text}")
    return 0


def handle_logs(args: argparse.Namespace) -> int:
    print("`opencuttle logs` will be implemented in Issue 26.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not hasattr(args, "handler"):
        parser.print_help()
        return 0

    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())