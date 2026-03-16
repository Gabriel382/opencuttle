from examples.task_execution_example import main


def test_task_execution_example_runs(capsys) -> None:
    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "task execution" in captured.out.lower()
    assert "registered node metadata" in captured.out.lower()
    assert "outgoing message" in captured.out.lower()
    assert "response" in captured.out.lower()
    assert "example complete" in captured.out.lower()