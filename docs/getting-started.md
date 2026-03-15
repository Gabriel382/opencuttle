# Getting Started

This guide explains how to set up and run OpenCuttle locally.

## What exists in Sprint 1

At the end of Sprint 1, OpenCuttle includes:

- a professional repository structure
- a Make-based developer workflow
- a base message envelope
- message validation
- message serialization/deserialization
- message and task ID helpers
- a minimal in-memory local bus
- a two-node demo

This is the first working version of OpenCuttle.

## Prerequisites

You need:

- Git
- Python 3.x
- Make

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/opencuttle.git
cd opencuttle
````

Set up the development environment:

```bash
make dev
```

## Useful commands

```bash
make doctor
make run
make demo
make test
make lint
```

## Run the first demo

Run:

```bash
make demo
```

This demo shows:

* node A creating a message
* node B registered in the local bus
* message routing by target node name
* node B returning a response
* minimal logs printed in the terminal

## What the current demo proves

The Sprint 1 demo proves that OpenCuttle already has a working local runtime loop:

1. create a valid message envelope
2. send it through the local bus
3. resolve the target node
4. execute the target synchronously
5. return a validated response

## Current limitations

Sprint 1 is intentionally small.

Current limitations:

* **in-memory only** — the bus lives only inside the current Python process
* **no persistence** — messages, nodes, and task history are not stored yet
* **no adapters yet** — external systems like Ollama, MCP, A2A, or OpenClaw are not connected yet
* **no orchestrator yet** — there is no central routing brain beyond direct target-based dispatch

## Next steps

* Read the [Architecture](architecture.md)
* Read the [Message Envelope](message-envelope.md)
* Read the [Local Bus](local-bus.md)
