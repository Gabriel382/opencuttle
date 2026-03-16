from __future__ import annotations

# Standard library imports
import json
from datetime import datetime, UTC

# Local imports
from core.demo_node import DemoEchoNode
from core.local_bus import LocalBus
from core.message_ids import generate_message_id, generate_task_id


def build_example_message(sender: str, target: str, text: str) -> dict:
    """
    Build a valid OpenCuttle message envelope for the task execution example.

    Args:
        sender:
            Logical sender name.
        target:
            Logical target node name.
        text:
            Message text payload.

    Returns:
        A valid OpenCuttle message envelope.
    """
    return {
        "id": generate_message_id(),
        "task_id": generate_task_id(),
        "parent_task_id": None,
        "sender": sender,
        "target": target,
        "type": "invoke",
        "payload": {
            "text": text,
        },
        "metadata": {
            "source": "task_execution_example",
        },
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }


def main() -> int:
    """
    Run a minimal full task execution flow using the official demo node.

    Returns:
        Process exit code.
    """
    print("=== OpenCuttle Example: task execution ===")

    # Create the local runtime.
    bus = LocalBus()

    # Create and register the official reference demo node.
    node = DemoEchoNode(name="node-b")
    bus.register_node(node, manifest=node.manifest)

    print("\nRegistered node metadata:")
    print(bus.format_node_summary("node-b"))

    # Build one valid message.
    message = build_example_message(
        sender="node-a",
        target="node-b",
        text="Hello from the task execution example",
    )

    print("\nOutgoing message:")
    print(json.dumps(message, indent=2, ensure_ascii=False))

    # Execute the message through the local bus.
    response = bus.send(message)

    print("\nResponse:")
    print(json.dumps(response, indent=2, ensure_ascii=False))

    print("\nExecution flow summary:")
    print("1. Node A created a valid message.")
    print("2. The local bus resolved node-b as the target.")
    print("3. DemoEchoNode handled the message.")
    print("4. A valid response envelope was returned.")

    print("\nExample complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())