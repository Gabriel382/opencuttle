# Node Manifest and Registry

This document explains how OpenCuttle describes and stores node metadata in Sprint 2.

## Purpose

OpenCuttle separates two things:

- **runtime nodes** — the actual Python objects that receive and handle messages
- **node manifests** — the metadata that describes those nodes

This makes it possible to:
- inspect nodes without touching runtime internals
- build a registry of available nodes
- support future CLI inspection
- prepare for routing, adapters, and orchestration later

## What is a node manifest?

A node manifest is a small structured document that describes one node.

In OpenCuttle v0, it is intentionally small and stable.

### Required fields

- `name`
- `type`
- `description`
- `skills`
- `tags`

### Optional fields

- `model`
- `version`
- `priority`
- `persona`
- `memory_scope`

## Field meanings

### `name`
Unique logical node name.

Example:

```text
demo-echo-node
````

### `type`

Node category.

Allowed v0 values:

* `node`
* `model`
* `adapter`
* `bus`

### `description`

Short human-readable explanation of what the node does.

### `skills`

List of declared node skills.

Example:

```json
["echo", "demo", "local-testing"]
```

### `tags`

Free-form labels for filtering and future routing.

Example:

```json
["local", "demo", "reference"]
```

### `model`

Optional backend or model label.

### `version`

Optional node version.

### `priority`

Optional integer hint for future routing.

### `persona`

Optional persona/profile label.

### `memory_scope`

Optional memory hint.

Allowed v0 values:

* `none`
* `task`
* `session`
* `shared`

## Example manifest

```json
{
  "name": "demo-echo-node",
  "type": "node",
  "description": "Minimal reference node that echoes received payloads",
  "skills": ["echo", "demo", "local-testing"],
  "tags": ["local", "demo", "reference"],
  "model": "none",
  "version": "0.1.0",
  "priority": 10,
  "persona": "friendly-demo",
  "memory_scope": "none"
}
```

## What is the node registry?

The node registry is the dedicated metadata layer for OpenCuttle nodes.

Its role is to:

* store validated node manifests
* retrieve manifests by name
* list all registered manifests
* reject duplicate node names

The registry is intentionally independent of:

* the CLI
* the orchestrator
* persistence
* adapters

In Sprint 2, it is still local and in-memory only.

## How node registration works in Sprint 2

In Sprint 2, node registration happens in two layers:

1. the **local bus** stores the runtime node object for dispatch
2. the **node registry** stores the node manifest for inspection

So when a node is registered:

* it becomes available to receive messages through the local bus
* its metadata becomes available through the registry

## Registration flow

The current registration flow is:

1. create a runtime node object
2. create or provide a node manifest
3. call `LocalBus.register_node(...)`
4. the bus stores the runtime node
5. the registry stores the validated manifest

## Example registration flow

```python
from core.local_bus import LocalBus, EchoNode

bus = LocalBus()
node = EchoNode(name="node-b")

manifest = {
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

bus.register_node(node, manifest=manifest)
```

## Why this matters

This separation between runtime node and metadata registry is important because it prepares OpenCuttle for:

* CLI inspection
* adapters
* routing policies
* node summaries
* orchestration later

## Current limitations

Sprint 2 is still intentionally small.

Current limitations:

* registry is in-memory only
* no persistence yet
* no health model yet
* no trust boundary metadata yet
* no advanced capability scoring yet
* no orchestrator integration yet

## Summary

In Sprint 2:

* the **local bus** is responsible for runtime dispatch
* the **node registry** is responsible for metadata storage
* the **node manifest** is the contract describing a node
