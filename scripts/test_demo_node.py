from __future__ import annotations

from core.demo_node import DemoEchoNode, build_demo_node_manifest
from core.message_ids import generate_message_id, generate_task_id


def make_valid_message() -> dict:
    return {
        "id": generate_message_id(),
        "task_id": generate_task_id(),
        "parent_task_id": None,
        "sender": "node-a",
        "target": "node-b",
        "type": "invoke",
        "payload": {
            "text": "Hello from test"
        },
        "metadata": {
            "source": "pytest"
        },
        "timestamp": "2026-03-16T00:00:00Z",
    }


def test_demo_node_has_default_manifest() -> None:
    node = DemoEchoNode()

    assert node.manifest["name"] == "demo-echo-node"
    assert node.manifest["type"] == "node"
    assert "echo" in node.manifest["skills"]


def test_demo_node_can_use_custom_name() -> None:
    node = DemoEchoNode(name="node-b")

    assert node.name == "node-b"
    assert node.manifest["name"] == "node-b"


def test_demo_node_returns_valid_response_shape() -> None:
    node = DemoEchoNode(name="node-b")
    message = make_valid_message()

    response = node.handle_message(message)

    assert response["type"] == "response"
    assert response["sender"] == "node-b"
    assert response["target"] == "node-a"
    assert response["task_id"] == message["task_id"]
    assert response["payload"]["received_by"] == "node-b"
    assert response["payload"]["original_payload"] == message["payload"]


def test_build_demo_node_manifest_returns_expected_metadata() -> None:
    manifest = build_demo_node_manifest("node-b")

    assert manifest["name"] == "node-b"
    assert manifest["type"] == "node"
    assert manifest["description"]
    assert "demo" in manifest["skills"]