from __future__ import annotations

# Standard library imports
import json

# Local imports
from core.demo_node import DemoEchoNode
from core.local_bus import LocalBus


def main() -> int:
    """
    Show how to register a node using the current local bus + registry model.

    Returns:
        Process exit code.
    """
    print("=== OpenCuttle Example: node registration ===")

    # Create the local bus.
    bus = LocalBus()

    # Create the official reference demo node.
    node = DemoEchoNode(name="node-b")

    print("\nRegistering demo node...")
    bus.register_node(node, manifest=node.manifest)

    print("\nRegistered node manifests:")
    manifests = bus.list_node_manifests()
    print(json.dumps(manifests, indent=2, ensure_ascii=False))

    print("\nRegistered runtime nodes:")
    for runtime_node in bus.list_nodes():
        print(f"- {runtime_node.name} ({runtime_node.__class__.__name__})")

    print("\nExample complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())