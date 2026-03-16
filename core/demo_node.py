from __future__ import annotations

# Standard library imports
from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any

# Local imports
from core.message_ids import generate_message_id


def build_demo_node_manifest(name: str = "demo-echo-node") -> dict[str, Any]:
    """
    Build the default manifest for the official OpenCuttle demo node.

    Args:
        name:
            The logical node name.

    Returns:
        A valid v0 node manifest.
    """
    return {
        "name": name,
        "type": "node",
        "description": "Official OpenCuttle reference demo node that echoes received payloads",
        "skills": ["echo", "demo", "local-testing"],
        "tags": ["local", "demo", "reference"],
        "model": "none",
        "version": "0.1.0",
        "priority": 10,
        "persona": "friendly-demo",
        "memory_scope": "none",
    }


@dataclass
class DemoEchoNode:
    """
    Official OpenCuttle reference demo node.

    This node is intentionally simple:
    - it accepts a valid message
    - it returns a valid response
    - it echoes the original payload
    - it preserves the task relationship
    """

    name: str = "demo-echo-node"
    manifest: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Ensure the node always has attached manifest metadata.
        """
        if not self.manifest:
            self.manifest = build_demo_node_manifest(self.name)

    def handle_message(self, message: dict[str, Any]) -> dict[str, Any]:
        """
        Handle an incoming message and return a response envelope.

        Args:
            message:
                A valid OpenCuttle message envelope.

        Returns:
            A valid OpenCuttle response envelope.
        """
        return {
            "id": generate_message_id(),
            "task_id": message["task_id"],
            "parent_task_id": message.get("parent_task_id"),
            "sender": self.name,
            "target": message["sender"],
            "type": "response",
            "payload": {
                "received_by": self.name,
                "original_payload": message["payload"],
                "message": "DemoEchoNode handled the message successfully.",
            },
            "metadata": {
                "source": "demo_node",
                "status": "ok",
                "node_type": "reference-demo-node",
            },
            "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        }