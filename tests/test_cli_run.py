from __future__ import annotations

from cli.main import main


def test_cli_run_executes_successfully(capsys) -> None:
    exit_code = main(["run"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "starting opencuttle local runtime" in captured.out.lower()
    assert "demo complete" in captured.out.lower()