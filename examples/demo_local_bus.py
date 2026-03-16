from __future__ import annotations

# Standard library imports
from datetime import datetime, UTC
import logging

# Local imports
from core.local_bus import LocalBus, EchoNode
from core.message_ids import generate_message_id, generate_task_id


def build_demo_message(sender: str, target: str) -> dict:
    """
    Build a valid demo message envelope.
    """
    return {
        "id": generate_message_id(),
        "task_id": generate_task_id(),
        "parent_task_id": None,
        "sender": sender,
        "target": target,
        "type": "invoke",
        "payload": {
            "text": "Hello from node A"
        },
        "metadata": {
            "source": "demo"
        },
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }


def main() -> None:
    """
    Run the minimal two-node OpenCuttle local bus demo.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )

    print("=== OpenCuttle Demo: two-node local bus ===")

    # Create the local bus.
    bus = LocalBus()

    # Define the two demo nodes conceptually.
    node_a_name = "node-a"
    node_b = EchoNode(name="node-b")

    print(f"Creating node A: {node_a_name}")
    print(f"Creating node B: {node_b.name}")

    # Register only the receiving node in the bus.
    # Node A is represented as the logical sender in this minimal demo.
    bus.register_node(node_b)
    print("\nRegistered node manifests:")
    for manifest in bus.list_node_manifests():
        print(manifest)
    
    print("\nRuntime nodes:")
    for node in bus.list_nodes():
        print(f"- {node.name} ({node.__class__.__name__})")

    print("\nNode summary:")
    print(bus.format_node_summary("node-b"))

    # Build the message sent from node A to node B.
    message = build_demo_message(sender=node_a_name, target=node_b.name)

    print("\nNode A sends a message through the OpenCuttle bus:")
    print(message)

    # Dispatch synchronously through the local bus.
    response = bus.send(message)

    print("\nNode B responds:")
    print(response)

    print("\nDemo complete.")
    print("OpenCuttle local bus successfully routed one message from node A to node B.")


if __name__ == "__main__":
    main()