from __future__ import annotations

# Standard library imports
from datetime import datetime, UTC

# Local imports
from core.local_bus import (
    EchoNode,
    LocalBus,
    NodeAlreadyRegisteredError,
    NodeNotFoundError,
)
from core.message_ids import generate_message_id, generate_task_id


def make_message(sender: str, target: str) -> dict:
    """
    Create a valid message envelope for local bus tests.
    """
    return {
        "id": generate_message_id(),
        "task_id": generate_task_id(),
        "parent_task_id": None,
        "sender": sender,
        "target": target,
        "type": "invoke",
        "payload": {
            "text": "Hello from test"
        },
        "metadata": {
            "source": "pytest"
        },
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }


def test_register_node_success() -> None:
    """
    Registering a new node should succeed.
    """
    bus = LocalBus()
    node = EchoNode(name="node-b")

    bus.register_node(node)

    assert bus.has_node("node-b") is True


def test_register_duplicate_node_fails() -> None:
    """
    Registering the same node name twice should fail clearly.
    """
    bus = LocalBus()
    node = EchoNode(name="node-b")

    bus.register_node(node)

    try:
        bus.register_node(node)
        assert False, "Expected duplicate registration to fail"
    except NodeAlreadyRegisteredError as exc:
        assert "already registered" in str(exc).lower()


def test_dispatch_between_two_nodes_works() -> None:
    """
    One node should be able to send a message to another through the bus.
    """
    bus = LocalBus()
    node_b = EchoNode(name="node-b")

    bus.register_node(node_b)

    message = make_message(sender="node-a", target="node-b")
    response = bus.dispatch(message)

    assert response["type"] == "response"
    assert response["sender"] == "node-b"
    assert response["target"] == "node-a"
    assert response["task_id"] == message["task_id"]
    assert response["payload"]["received_by"] == "node-b"


def test_dispatch_to_unknown_target_fails() -> None:
    """
    Dispatching to an unregistered node should fail clearly.
    """
    bus = LocalBus()

    message = make_message(sender="node-a", target="missing-node")

    try:
        bus.dispatch(message)
        assert False, "Expected dispatch to fail for missing target"
    except NodeNotFoundError as exc:
        assert "not registered" in str(exc).lower()