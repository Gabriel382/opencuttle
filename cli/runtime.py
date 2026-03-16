from __future__ import annotations

# Local imports
from core.local_bus import EchoNode, LocalBus


def build_default_local_bus() -> LocalBus:
    """
    Build the current default local OpenCuttle runtime context.

    This helper exists so CLI commands can inspect or run against
    a small consistent local runtime without duplicating setup logic.

    Returns:
        A LocalBus instance with default demo nodes registered.
    """
    bus = LocalBus()

    demo_manifest = {
        "name": "node-b",
        "type": "node",
        "description": "Explicit demo node manifest",
        "skills": ["echo", "demo"],
        "tags": ["local", "reference"],
        "model": "none",
        "version": "0.1.0",
        "priority": 5,
        "persona": "friendly-demo",
        "memory_scope": "none",
    }

    bus.register_node(EchoNode(name="node-b"), manifest=demo_manifest)
    return bus