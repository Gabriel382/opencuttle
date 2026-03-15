
# Message Envelope

This document describes the base message format used in OpenCuttle.

## Purpose

The message envelope is the core communication primitive in OpenCuttle.

It is used to represent messages exchanged between:
- users
- orchestrators
- nodes
- adapters
- sub-buses

## v0 schema decisions

For v0, OpenCuttle keeps the message envelope intentionally small.

### Required fields

- `id`
- `task_id`
- `sender`
- `target`
- `type`
- `payload`
- `metadata`
- `timestamp`

### Optional fields

- `parent_task_id`

### Message types

OpenCuttle v0 supports four message types:

- `invoke`
- `response`
- `error`
- `event`

This set is intentionally minimal so the local bus can remain simple and stable during the first implementation milestones.

## Example shape

```json
{
  "id": "msg_0001",
  "task_id": "task_0001",
  "parent_task_id": null,
  "sender": "user",
  "target": "demo-node",
  "type": "invoke",
  "payload": {
    "text": "Hello from OpenCuttle"
  },
  "metadata": {
    "priority": "normal",
    "source": "cli"
  },
  "timestamp": "2026-03-15T18:00:00Z"
}
````

## Validation

The envelope will later support:

* required field validation
* type validation
* serialization and deserialization
* correlation handling

## Status

This document is a stub and will be refined during the Message Envelope milestone.

