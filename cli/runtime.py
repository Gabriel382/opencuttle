from __future__ import annotations

# Standard library imports
from datetime import datetime, UTC
from typing import Any

# Local imports
from core.local_bus import EchoNode, LocalBus
from core.message_ids import generate_message_id, generate_task_id
from core.demo_node import DemoEchoNode


def build_default_local_bus() -> LocalBus:
    """
    Build the current default local OpenCuttle runtime context.

    Returns:
        A LocalBus instance with default demo nodes registered.
    """
    bus = LocalBus()

    node = DemoEchoNode(name="node-b")
    bus.register_node(node, manifest=node.manifest)
    
    return bus


def run_simple_task(task_text: str) -> dict[str, Any]:
    """
    Run one simple text task through the current local OpenCuttle runtime.

    Args:
        task_text:
            The user-provided task text.

    Returns:
        The response envelope returned by the target node.
    """
    bus = build_default_local_bus()

    message = {
        "id": generate_message_id(),
        "task_id": generate_task_id(),
        "parent_task_id": None,
        "sender": "cli-user",
        "target": "node-b",
        "type": "invoke",
        "payload": {
            "text": task_text,
        },
        "metadata": {
            "source": "cli-task-run",
        },
        "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }

    return bus.send(message)