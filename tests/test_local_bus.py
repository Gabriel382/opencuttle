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
from core.message_validator import MessageEnvelopeValidationError

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


def make_valid_message(sender: str = "node-a", target: str = "node-b") -> dict:
    """
    Create a valid OpenCuttle message envelope for local bus tests.
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


def test_successful_message_flow() -> None:
    """
    A valid message should be routed to the target node and return a response.
    """
    bus = LocalBus()
    node_b = EchoNode(name="node-b")
    bus.register_node(node_b)

    message = make_valid_message(sender="node-a", target="node-b")
    response = bus.send(message)

    assert response["type"] == "response"
    assert response["sender"] == "node-b"
    assert response["target"] == "node-a"
    assert response["task_id"] == message["task_id"]
    assert response["payload"]["received_by"] == "node-b"
    assert response["payload"]["original_payload"] == message["payload"]


    
def test_send_routes_by_target_name() -> None:
    bus = LocalBus()
    node_b = EchoNode(name="node-b")
    bus.register_node(node_b)

    message = make_message(sender="node-a", target="node-b")
    response = bus.send(message)

    assert response["sender"] == "node-b"
    assert response["target"] == "node-a"


def test_unknown_target_returns_clear_error() -> None:
    bus = LocalBus()
    message = make_message(sender="node-a", target="missing-node")

    try:
        bus.send(message)
        assert False, "Expected send() to fail for missing target"
    except NodeNotFoundError as exc:
        assert "missing-node" in str(exc)
        assert "not registered" in str(exc).lower()



def test_invalid_envelope_is_rejected() -> None:
    """
    A malformed message envelope should fail before dispatch.
    """
    bus = LocalBus()
    node_b = EchoNode(name="node-b")
    bus.register_node(node_b)

    message = make_valid_message(sender="node-a", target="node-b")
    del message["target"]

    try:
        bus.send(message)
        assert False, "Expected invalid envelope to raise MessageEnvelopeValidationError"
    except MessageEnvelopeValidationError as exc:
        assert "target" in str(exc).lower()

def test_unknown_target_behavior() -> None:
    """
    Sending to an unregistered target should raise a clear local bus error.
    """
    bus = LocalBus()

    message = make_valid_message(sender="node-a", target="missing-node")

    try:
        bus.send(message)
        assert False, "Expected unknown target to raise NodeNotFoundError"
    except NodeNotFoundError as exc:
        assert "missing-node" in str(exc)
        assert "not registered" in str(exc).lower()