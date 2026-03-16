from __future__ import annotations

# Standard library imports
from datetime import datetime, UTC
import logging
from typing import Any

# Local imports
from core.local_bus import LocalBus, EchoNode
from core.message_ids import generate_message_id, generate_task_id


def build_demo_message(sender: str, target: str) -> dict[str, Any]:
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


def run_demo() -> dict[str, Any]:
    """
    Run the minimal two-node OpenCuttle local bus demo.

    Returns:
        The response envelope returned by node B.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s",
    )

    print("=== OpenCuttle Demo: two-node local bus ===")

    bus = LocalBus()

    node_a_name = "node-a"
    node_b = EchoNode(name="node-b")

    print(f"Creating node A: {node_a_name}")
    print(f"Creating node B: {node_b.name}")

    bus.register_node(node_b)

    print("\nRegistered node manifests:")
    for manifest in bus.list_node_manifests():
        print(manifest)

    message = build_demo_message(sender=node_a_name, target=node_b.name)

    print("\nNode A sends a message through the OpenCuttle bus:")
    print(message)

    response = bus.send(message)

    print("\nNode B responds:")
    print(response)

    print("\nDemo complete.")
    print("OpenCuttle local bus successfully routed one message from node A to node B.")

    return response


def main() -> int:
    """
    Script entrypoint for the local bus demo.

    Returns:
        Process exit code.
    """
    run_demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())