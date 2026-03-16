from __future__ import annotations

from cli.main import build_parser, main


def test_root_parser_builds() -> None:
    parser = build_parser()
    assert parser.prog == "opencuttle"


def test_main_without_args_shows_help_and_returns_zero(capsys) -> None:
    exit_code = main([])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "usage:" in captured.out.lower()
    assert "opencuttle" in captured.out.lower()


def test_run_subcommand_executes_runtime_flow(capsys) -> None:
    exit_code = main(["run"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "starting opencuttle local runtime" in captured.out.lower()
    assert "demo complete" in captured.out.lower()


def test_node_list_subcommand_shows_registered_nodes(capsys) -> None:
    exit_code = main(["node", "list"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "registered nodes" in captured.out.lower()
    assert "node-b" in captured.out
    assert "type: node" in captured.out.lower()


def test_node_list_output_is_readable(capsys) -> None:
    exit_code = main(["node", "list"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "description:" in captured.out.lower()
    assert "skills:" in captured.out.lower()
    assert "tags:" in captured.out.lower()