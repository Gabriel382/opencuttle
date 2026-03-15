# Local Bus

This document describes the first local bus implementation in OpenCuttle.

## Purpose

The local bus is the first runtime communication layer in OpenCuttle.

Its role is to let nodes exchange messages inside a single local OpenCuttle instance.

## What exists in Sprint 1

In Sprint 1, the local bus supports:

- node registration
- target-based message routing
- synchronous request/response flow
- message validation before dispatch
- response validation before returning
- minimal terminal logging

This is the smallest working OpenCuttle runtime.

## Simple architecture

The current architecture is intentionally minimal:

```text
Node A
  ↓
OpenCuttle Local Bus
  ↓
Node B
  ↓
Response back to Node A
````

## Message flow

The current local bus flow is:

1. a sender creates a valid OpenCuttle message envelope
2. the bus validates the incoming message
3. the bus resolves the target node by name
4. if the target is missing, the bus raises a clear error
5. the target node handles the message synchronously
6. the bus validates the response envelope
7. the response is returned to the caller

## Unknown target behavior

If a message targets a node that is not registered in the local bus, OpenCuttle raises a clear local bus error.

This prevents silent failures and makes routing mistakes easy to diagnose.

## Logging

The local bus currently emits minimal logs for:

* node registration
* message dispatch
* missing target errors
* response generation

These logs are only meant to make the first runtime behavior visible and understandable.

## Current limitations

The Sprint 1 local bus is intentionally limited:

* **in-memory only** — no sockets, no network, no shared state across processes
* **no persistence** — no stored message history or replay yet
* **no adapters yet** — only local Python nodes are supported
* **no orchestrator yet** — the bus dispatches directly to a named target
* **no async runtime** — dispatch is synchronous
* **no retries or failover** — error handling is still minimal

## Why this version matters

This first local bus matters because it proves the core OpenCuttle loop:

* create a message
* validate it
* dispatch it
* handle it
* return a response

That is the foundation for everything that comes later:

* adapters
* orchestration
* policies
* memory
* hierarchy
* observability

## Next evolution

Later milestones will extend the local bus with:

* persistence
* adapters
* richer routing
* tracing
* hierarchy and recursion
* reliability features

````

---

# How to validate Issue 15

Run these checks:

```bash
make demo
make test
````

Then manually verify:

* `docs/getting-started.md` contains demo steps
* `docs/local-bus.md` explains the architecture simply
* the limitations are clearly listed
* a newcomer could understand what Sprint 1 already does

That is enough to satisfy the acceptance criteria.
