def test_examples_demo_node_reexports_reference_node() -> None:
    from examples.demo_node import DemoEchoNode
    from core.demo_node import DemoEchoNode as CoreDemoEchoNode

    assert DemoEchoNode is CoreDemoEchoNode