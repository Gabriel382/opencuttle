# Local Bus

This document describes the first local bus implementation in OpenCuttle.

## Purpose

The local bus is the first runtime communication layer in OpenCuttle.

It is responsible for enabling local message exchange between nodes inside one OpenCuttle instance.

## Initial goals

The first version of the local bus should support:
- in-memory communication
- target-based dispatch
- basic request/response
- minimal demo flows

## Expected behavior

A simple flow looks like this:

```text
Node A
  ↓
OpenCuttle Local Bus
  ↓
Node B
  ↓
Response back to Node A
````

## Limitations of v0

The first version is expected to be:

* in-memory only
* local only
* minimal
* not persistent
* not distributed

## v0 implementation

OpenCuttle local bus v0 is an in-memory synchronous dispatcher.

It currently supports:
- node registration
- target-based dispatch
- one request / one response flow
- no network access
- no persistence
- no async runtime

The goal of v0 is to prove the smallest working OpenCuttle runtime.

## Dispatch flow

OpenCuttle local bus v0 dispatches messages synchronously by target node name.

### Current flow

1. validate incoming message
2. resolve the target node from the local registry
3. raise a clear error if the target does not exist
4. call the target node synchronously
5. validate the returned response envelope
6. return the response to the caller

### Unknown target behavior

If a message targets a node that is not registered in the local bus, OpenCuttle raises a clear local bus error.

### Logging

The v0 local bus emits minimal log events for:
- node registration
- message dispatch
- missing target errors
- response generation

## Status

This document is a stub and will evolve during the Local Bus milestone.