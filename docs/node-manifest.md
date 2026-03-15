# Node Manifest

This document defines the OpenCuttle node manifest used to describe registered nodes.

## Purpose

The node manifest is the standard metadata contract for OpenCuttle nodes.

It gives the system a consistent way to describe:
- identity
- category
- capabilities
- routing hints
- optional persona and memory metadata

This manifest will later support:
- node registry
- CLI inspection
- adapters
- routing policies
- orchestration

## v0 design goals

The v0 node manifest is intentionally small.

It should:
- describe a node clearly
- be easy to validate
- be easy to inspect from code or CLI
- avoid committing too early to advanced concepts

## Required fields

- `name`
- `type`
- `description`
- `skills`
- `tags`

## Optional fields

- `model`
- `version`
- `priority`
- `persona`
- `memory_scope`

## Field meanings

### `name`
Unique logical node name.

Recommended style:
- lowercase
- kebab-case
- stable across runs where possible

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

Short human-readable description of the node.

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

Optional model or backend label.

### `version`

Optional node version string.

### `priority`

Optional integer hint for future routing.

### `persona`

Optional short profile/persona label.

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

## Why the v0 schema is small

The first node manifest is intentionally minimal so it can stay stable while the registry and CLI are being built.

Not included yet:

* cost hints
* latency hints
* trust boundaries
* permissions
* health
* streaming capabilities
* adapter-specific settings

These can be added later once the registry and routing layers mature.

````

# Optional docs index update

If you have `docs/README.md`, add:

```md
- [Node Manifest](node-manifest.md)
````

# How to validate it

There are two practical validation levels here.

## 1. Manual structure check

Verify:

* `core/node_manifest_schema.json` exists
* `docs/node-manifest.md` exists
* the docs include one example manifest
* required and optional fields are clearly separated

## 2. JSON Schema validation check

If you want to validate it the same way you validated message envelopes, add a tiny temporary script or a future validator. For now, even a quick Python check is enough once you have `jsonschema` installed:

```bash
python3
```

```python
import json
from jsonschema import Draft202012Validator

with open("core/node_manifest_schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

manifest = {
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

Draft202012Validator(schema).validate(manifest)
print("manifest ok")
```

If it prints `manifest ok`, the schema and example align. Draft 2020-12 validation is the correct match for this schema style. ([JSON Schema][3])
