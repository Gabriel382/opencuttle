Perfect. For **Issue 27**, the job is to make the CLI **discoverable, copy-pasteable, and honest about what is implemented versus still stubbed**. That fits both GitHub’s general documentation guidance and Python’s `argparse` model, which is specifically meant to create user-friendly CLIs with built-in help and subcommands. ([GitHub Docs][1])

## What to update

I would update **`docs/getting-started.md`** and optionally add a small **CLI section to `README.md`**.

The most important doc is `docs/getting-started.md`, because this issue is about helping a newcomer actually run the CLI.

---

# Recommended `docs/getting-started.md`

Use this as the updated version:

````md
# Getting Started

This guide explains how to set up and run OpenCuttle locally.

## What exists right now

At the current stage, OpenCuttle includes:

- a professional repository structure
- a Make-based developer workflow
- a base message envelope
- message validation
- message serialization/deserialization
- message and task ID helpers
- a minimal in-memory local bus
- a two-node demo
- a first CLI structure
- a node registry
- node inspection helpers

This is still an early local-first prototype, but it is already runnable.

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

## CLI overview

OpenCuttle now includes a first CLI.

You can inspect its help with:

```bash
PYTHONPATH=. python3 -m cli.main --help
```

Current CLI command groups:

* `run`
* `node`
* `task`
* `logs`

## CLI examples

### Show CLI help

```bash
PYTHONPATH=. python3 -m cli.main --help
```

### Run the current local runtime

```bash
PYTHONPATH=. python3 -m cli.main run
```

This currently runs the local two-node demo/runtime flow.

### List registered nodes

```bash
PYTHONPATH=. python3 -m cli.main node list
```

This shows the currently registered nodes from the local runtime context.

### Inspect one node

```bash
PYTHONPATH=. python3 -m cli.main node inspect node-b
```

This prints readable metadata for one registered node.

### Run one simple task

```bash
PYTHONPATH=. python3 -m cli.main task run "hello opencuttle"
```

This sends a simple text task through the current local demo/runtime path and prints the response.

### Show log guidance

```bash
PYTHONPATH=. python3 -m cli.main logs
```

This explains the current log situation in v0.

## Run the first demo

You can still run the standalone demo with:

```bash
make demo
```

This demo shows:

* node A creating a message
* node B registered in the local bus
* message routing by target node name
* node B returning a response
* minimal logs printed in the terminal

## What the current CLI actually does

The CLI is real, but still intentionally small.

At this stage:

* `run` uses the current local demo/runtime flow
* `node list` inspects the local in-memory runtime context
* `node inspect` prints full metadata for one registered node
* `task run` sends a simple text task through the local bus
* `logs` explains current terminal-only logging behavior

## Current limitations

OpenCuttle is still in an early local-first stage.

Current limitations include:

* **in-memory only** — the bus and registry live only inside the current Python process
* **no persistence** — no stored task history, registry state, or replay yet
* **no adapters yet** — external systems like Ollama, MCP, A2A, or OpenClaw are not connected yet
* **no orchestrator yet** — CLI task execution still uses the current demo/local bus path
* **no persisted logs yet** — logs are currently visible only during command execution
* **CLI still partial** — some commands are implemented minimally and will evolve in later milestones

## Recommended first steps

If you are new to OpenCuttle, try this order:

1. inspect the CLI help
2. run the local runtime
3. list registered nodes
4. inspect one node
5. run a simple task

Example sequence:

```bash
PYTHONPATH=. python3 -m cli.main --help
PYTHONPATH=. python3 -m cli.main run
PYTHONPATH=. python3 -m cli.main node list
PYTHONPATH=. python3 -m cli.main node inspect node-b
PYTHONPATH=. python3 -m cli.main task run "hello opencuttle"
```

---

## Node registration example

A minimal example showing how a node is registered with the local bus and node registry is available in:

```text
examples/node_registration_example.py
```

Run it with:

```bash
PYTHONPATH=. python3 examples/node_registration_example.py
```

# How to validate it

Check these manually:

1. `docs/getting-started.md` contains real CLI examples
2. a newcomer can copy-paste at least:
   - `PYTHONPATH=. python3 -m cli.main --help`
   - `PYTHONPATH=. python3 -m cli.main run`
   - `PYTHONPATH=. python3 -m cli.main node list`
3. the limitations are clearly written
4. the docs do not imply features that are not implemented yet

You can also sanity check the actual commands:

```bash
PYTHONPATH=. .venv/bin/python -m cli.main --help
PYTHONPATH=. .venv/bin/python -m cli.main run
PYTHONPATH=. .venv/bin/python -m cli.main node list
PYTHONPATH=. .venv/bin/python -m cli.main node inspect node-b
PYTHONPATH=. .venv/bin/python -m cli.main task run "hello opencuttle"
PYTHONPATH=. .venv/bin/python -m cli.main logs
```

If those all work and the docs match them, the issue is done.

## Next steps

* Read the [Architecture](architecture.md)
* Read the [Message Envelope](message-envelope.md)
* Read the [Local Bus](local-bus.md)
* Read the [Node Manifest and Registry](node-manifest.md)