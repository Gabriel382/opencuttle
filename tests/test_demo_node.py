from examples.node_registration_example import main

def test_examples_demo_node_reexports_reference_node() -> None:
    from examples.demo_node import DemoEchoNode
    from core.demo_node import DemoEchoNode as CoreDemoEchoNode

    assert DemoEchoNode is CoreDemoEchoNode


def test_node_registration_example_runs(capsys) -> None:
    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "node registration" in captured.out.lower()
    assert "registered node manifests" in captured.out.lower()
    assert "node-b" in captured.out