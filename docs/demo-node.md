# Demo Node Contract

This document explains the smallest valid OpenCuttle node shape in Sprint 2.

The goal is to help contributors understand how to build a simple node that works with the current local bus and registry model.

## Purpose

In OpenCuttle v0, a node is a runtime object that:

- has a name
- can receive a valid message envelope
- can return a valid response envelope
- can be registered in the local bus
- can expose metadata through a node manifest

The official reference implementation is the `DemoEchoNode`.

## Required properties

At the current stage, the smallest practical OpenCuttle node should provide:

- `name`
- `manifest`
- `handle_message(message)`

## `name`

The node must have a logical name.

Example:

```python
name = "node-b"
````

This name is used for:

* local bus registration
* message targeting
* runtime inspection

## `manifest`

The node should expose a valid node manifest.

The manifest describes the node metadata used by the registry.

Example fields include:

* `name`
* `type`
* `description`
* `skills`
* `tags`

Optional fields may include:

* `model`
* `version`
* `priority`
* `persona`
* `memory_scope`

Example:

```python
manifest = {
    "name": "node-b",
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
```

## `handle_message(message)`

A node must implement a method named:

```python
handle_message(message)
```

It receives one valid OpenCuttle message envelope and must return one valid OpenCuttle response envelope.

### Minimal expectations

The method should:

1. accept a message dictionary
2. read relevant input from the message
3. produce a valid response envelope
4. preserve task continuity where appropriate
5. target the response back to the original sender

## Expected response behavior

At the current stage, a response should:

* have a new message ID
* preserve the original `task_id`
* optionally preserve `parent_task_id`
* set `sender` to the current node
* set `target` to the original sender
* use `"response"` as the message type
* include a valid payload
* include metadata
* include a valid timestamp

## Minimal response example

```python
response = {
    "id": generate_message_id(),
    "task_id": message["task_id"],
    "parent_task_id": message.get("parent_task_id"),
    "sender": self.name,
    "target": message["sender"],
    "type": "response",
    "payload": {
        "received_by": self.name,
        "original_payload": message["payload"],
    },
    "metadata": {
        "source": "demo_node",
        "status": "ok",
    },
    "timestamp": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
}
```

## Registration expectations

In Sprint 2, node registration happens through the local bus:

```python
bus.register_node(node, manifest=node.manifest)
```

This does two things:

1. registers the runtime node for dispatch
2. registers the manifest in the node registry

That means a valid node should be ready for both:

* runtime execution
* metadata inspection

## Minimal example node

```python
from dataclasses import dataclass, field
from datetime import datetime, UTC

from core.message_ids import generate_message_id


def build_demo_node_manifest(name: str = "demo-echo-node") -> dict:
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
    name: str = "demo-echo-node"
    manifest: dict = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.manifest:
            self.manifest = build_demo_node_manifest(self.name)

    def handle_message(self, message: dict) -> dict:
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
```

## How to build your own node

If you want to create a similar node, follow this checklist:

* choose a stable `name`
* define a valid `manifest`
* implement `handle_message(message)`
* return a valid response envelope
* register the node through `LocalBus.register_node(...)`

## Current limitations

The Sprint 2 demo node contract is intentionally small.

It does not yet define:

* async behavior
* streaming behavior
* retries
* persistence
* health reporting
* advanced capability scoring
* permissions
* trust boundaries

These will come in later milestones.

## Summary

A minimal valid OpenCuttle node in Sprint 2 is:

* a named runtime object
* with a valid manifest
* with a `handle_message()` method
* returning a valid response envelope
* registerable through the local bus

The `DemoEchoNode` is the official reference implementation.