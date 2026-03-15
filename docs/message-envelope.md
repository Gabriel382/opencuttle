
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

## Planned fields

The initial envelope is expected to contain fields such as:

- `id`
- `task_id`
- `parent_task_id`
- `sender`
- `target`
- `type`
- `payload`
- `metadata`
- `timestamp`

## Example shape

```json
{
  "id": "msg_001",
  "task_id": "task_001",
  "parent_task_id": null,
  "sender": "user",
  "target": "demo-node",
  "type": "invoke",
  "payload": {},
  "metadata": {},
  "timestamp": "2026-03-15T00:00:00Z"
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

