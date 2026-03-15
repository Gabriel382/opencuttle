from __future__ import annotations

# Standard library imports
from datetime import datetime, UTC

# Local imports
from core.local_bus import LocalBus, EchoNode
from core.message_ids import generate_message_id, generate_task_id


def main() -> None:
    """
    Run the minimal OpenCuttle local bus demo.
    """
    bus = LocalBus()

    # Create and register a demo target node.
    node_b = EchoNode(name="node-b")
    bus.register_node(node_b)

    # Build a valid message from a logical sender to the registered target.
    message = {
        "id": generate_message_id(),
        "task_id": generate_task_id(),
        "parent_task_id": None,
        "sender": "node-a",
        "target": "node-b",
        "type": "invoke",
        "payload": {
            "text": "Hello from OpenCuttle demo"
        },
        "metadata": {
            "source": "demo"
        },
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }

    print("==> Dispatching message through OpenCuttle local bus")
    print(message)

    response = bus.dispatch(message)

    print("\n==> Response received")
    print(response)


if __name__ == "__main__":
    main()