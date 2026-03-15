# 🦑 OpenCuttle — Local-First Orchestration Bus for Agent Systems

<p align="center">
  <img src="docs/assets/opencuttle-logo.svg" alt="OpenCuttle" width="220">
</p>

<p align="center">
  <strong>Connect. Route. Orchestrate.</strong><br/>
  A local-first orchestration bus for heterogeneous agent systems, models, and tools.
</p>

<p align="center">
  <a href="https://github.com/YOUR_ORG/opencuttle/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/YOUR_ORG/opencuttle/ci.yml?branch=main&style=for-the-badge" alt="CI status">
  </a>
  <a href="https://github.com/YOUR_ORG/opencuttle/releases">
    <img src="https://img.shields.io/github/v/release/YOUR_ORG/opencuttle?include_prereleases&style=for-the-badge" alt="GitHub release">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License">
  </a>
  <a href="https://github.com/YOUR_ORG/opencuttle/stargazers">
    <img src="https://img.shields.io/github/stars/YOUR_ORG/opencuttle?style=for-the-badge" alt="GitHub stars">
  </a>
</p>

<p align="center">
  <a href="https://YOUR_DOCS_URL">Docs</a> ·
  <a href="https://github.com/YOUR_ORG/opencuttle/tree/main/examples">Examples</a> ·
  <a href="https://github.com/YOUR_ORG/opencuttle/blob/main/ROADMAP.md">Roadmap</a> ·
  <a href="https://github.com/YOUR_ORG/opencuttle/releases">Releases</a> ·
  <a href="https://github.com/YOUR_ORG/opencuttle/blob/main/CONTRIBUTING.md">Contributing</a>
</p>

---

**OpenCuttle** is a **local-first orchestration bus** for **heterogeneous agent systems**.

It lets you connect and coordinate:
- local models like **Ollama**
- multi-agent systems like **OpenClaw**
- protocol-based systems like **A2A** and **MCP**
- local scripts, subprocesses, HTTP services, and WebSocket agents
- entire **sub-buses**, recursively, as nodes inside larger systems

Instead of forcing everything into one framework, OpenCuttle acts as the **bus in the middle**:
it discovers nodes, understands their capabilities, routes tasks, applies policies, tracks execution, and preserves memory.

If you want a reusable infrastructure layer for **agent orchestration**, **not just another agent framework**, this is it.

---

## Why OpenCuttle?

Modern AI systems are fragmented.

You might have:
- one local coding model
- one OpenClaw workspace
- one HTTP agent
- one MCP tool server
- one planner agent
- one remote premium model
- one internal script that solves a critical task

They all work.  
They do **not** work together cleanly.

OpenCuttle provides a common orchestration layer so that every system can participate as a **node** in a larger network.

## Core ideas

- **Local-first** — runs well on your machine, not just in the cloud
- **Adapter-first** — bring your existing systems instead of rewriting everything
- **Policy-driven** — route by cost, speed, specialty, trust, or constraints
- **Memory-aware** — preserve task, node, and shared memory
- **Recursive by design** — one OpenCuttle can become a node inside another
- **Observable by default** — inspect traces, routing, failures, and delegation trees

---

## What OpenCuttle can connect

OpenCuttle nodes can represent:

- **Models**
  - Ollama
  - local LLM runtimes
  - remote LLM APIs

- **Agent systems**
  - OpenClaw
  - A2A agents
  - custom orchestrators
  - future adapters for LangGraph / CrewAI / AutoGen

- **Tools and services**
  - MCP-compatible systems
  - HTTP endpoints
  - WebSocket services
  - local subprocesses
  - Python / Go workers

- **Recursive buses**
  - a whole OpenCuttle cluster exposed as a single higher-level node

---

## Highlights

- **Unified node registry** — every connected system exposes identity, capabilities, model, skills, and routing metadata
- **Central orchestrator** — one agent in the middle delegates tasks across nodes
- **Adapter system** — connect heterogeneous runtimes without rewriting them
- **Routing policies** — choose fast, cheap, local-only, specialist-first, fallback-chain, and more
- **Shared and per-node memory** — keep context where it belongs
- **Execution traces** — inspect the full delegation tree
- **Recursive architecture** — compose small buses into bigger ones

---

## Install

> Early goal: OpenCuttle should be as easy to install as the best local-first projects.


### Development commands

OpenCuttle uses a small Make-based developer workflow.

- `make dev` — set up the local development environment
- `make test` — run tests
- `make lint` — run lint checks
- `make build` — build local artifacts
- `make run` — run the local OpenCuttle entrypoint
- `make clean` — remove temporary files and caches
- `make doctor` — inspect local tool availability
- `make demo` — run the current demo

### Recommended

```bash
git clone https://github.com/YOUR_ORG/opencuttle.git
cd opencuttle
make install
````

### Development

```bash
git clone https://github.com/YOUR_ORG/opencuttle.git
cd opencuttle
make dev
```

### Verify your environment

```bash
make doctor
```

---

## Quick start

Start the OpenCuttle bus:

```bash
opencuttle run
```

List connected nodes:

```bash
opencuttle node list
```

Inspect a node:

```bash
opencuttle node inspect ollama-coder
```

Send a task through the orchestrator:

```bash
opencuttle task run "Summarize this architecture and suggest improvements"
```

Run a specific route:

```bash
opencuttle task run "Write tests for this module" --policy local-fast
```

---

## Example: local model + external agent system

```text
User request
   │
   ▼
OpenCuttle Orchestrator
   ├─ local-ollama-coder
   ├─ opencuttle-openclaw-adapter
   └─ http-research-node
```

A request can be:

1. analyzed by the orchestrator
2. routed to the best node for the task
3. decomposed into subtasks
4. merged back into one coherent result

---

## How it works

```text
                  ┌──────────────────────┐
                  │        User / CLI     │
                  └──────────┬───────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │   OpenCuttle Orchestrator    │
              │  routing • memory • policy   │
              └──────────┬─────────┬─────────┘
                         │         │
         ┌───────────────┘         └────────────────┐
         ▼                                          ▼
┌────────────────────┐                    ┌────────────────────┐
│   Local adapters   │                    │  Remote adapters   │
│ Ollama / scripts   │                    │ HTTP / WS / A2A    │
│ subprocess / MCP   │                    │ OpenClaw / others  │
└─────────┬──────────┘                    └─────────┬──────────┘
          │                                           │
          └──────────────────┬────────────────────────┘
                             ▼
                    ┌──────────────────┐
                    │   Node Registry   │
                    │ capabilities/meta │
                    └──────────────────┘
```

---

## Node model

Every node in OpenCuttle can expose:

* `name`
* `type`
* `description`
* `skills`
* `model`
* `latency_hint`
* `cost_hint`
* `memory_scope`
* `persona`
* `priority`
* `tags`
* `health`

Example:

```json
{
  "name": "ollama-coder",
  "type": "model",
  "description": "Fast local coding model",
  "skills": ["coding", "refactoring", "test-generation"],
  "model": "qwen2.5-coder",
  "latency_hint": "low",
  "cost_hint": "local",
  "memory_scope": "session",
  "persona": "precise-engineer",
  "tags": ["local", "fast", "cheap"]
}
```

---

## Routing policies

OpenCuttle is policy-driven.

Examples:

* `local-only`
* `fastest`
* `cheapest`
* `specialist-first`
* `fallback-chain`
* `trusted-only`
* `human-in-the-loop`
* `hierarchical-escalation`

Example:

```yaml
policy: local-first
fallback:
  - ollama-fast
  - openclaw-generalist
  - remote-premium
constraints:
  allow_remote: false
  require_memory: true
```

---

## Memory model

OpenCuttle supports multiple memory scopes:

* **task memory** — current task only
* **session memory** — active conversation or workflow
* **node memory** — private memory of a specific node
* **shared memory** — visible across nodes in a workspace
* **bus memory** — higher-level orchestration context

This makes it possible to preserve both **identity** and **collaboration**.

---

## Adapters

Official adapters planned:

* [ ] Ollama
* [ ] subprocess / local scripts
* [ ] HTTP JSON
* [ ] WebSocket
* [ ] MCP
* [ ] A2A
* [ ] OpenClaw
* [ ] OpenCuttle-as-node

Adapter interface goals:

* small
* stable
* easy to implement
* easy to test
* language-agnostic

---

## Current status

OpenCuttle is under active development.

### Near-term goals

* core bus
* node registry
* orchestrator v0
* local persistence
* Ollama adapter
* subprocess adapter
* trace tree
* simple CLI
* make-based install flow

### Long-term goals

* recursive buses
* semantic routing
* adaptive policies
* mission-control UI
* SDKs in Python and Go
* adapter marketplace

See the full roadmap in [ROADMAP.md](ROADMAP.md).

---

## Repository structure

```text
opencuttle/
├── cmd/              # CLI entrypoints
├── core/             # bus, envelopes, runtime primitives
├── orchestrator/     # central orchestration logic
├── adapters/         # external system adapters
├── memory/           # memory scopes and persistence
├── policies/         # routing and delegation policies
├── sdk/              # SDKs and client libraries
├── examples/         # minimal real examples
├── docs/             # architecture and guides
├── tests/            # integration and unit tests
└── scripts/          # release/dev helper scripts
```

---

## Philosophy

OpenCuttle is built around a simple belief:

> The future is not one agent.
> The future is many systems cooperating cleanly.

Most projects try to become the one framework that owns everything.
OpenCuttle is different: it tries to become the **orchestration layer that lets everything work together**.

---

## Design principles

* **Do not force migration**
* **Prefer adapters over rewrites**
* **Keep the core small**
* **Make local use first-class**
* **Treat observability as part of the product**
* **Make recursion a native concept**
* **Stay composable**
* **Earn complexity slowly**

---

## Security

OpenCuttle coordinates systems with different trust levels.

Security goals:

* local-first by default
* explicit permissions for adapters
* clear trust boundaries
* auditable routing decisions
* configurable memory isolation
* future support for signed node manifests and policy-based restrictions

See [SECURITY.md](SECURITY.md).

---

## Documentation

* [Getting Started](docs/getting-started.md)
* [Architecture](docs/architecture.md)
* [Node Model](docs/node-model.md)
* [Policies](docs/policies.md)
* [Memory](docs/memory.md)
* [Adapters](docs/adapters.md)
* [Tracing](docs/tracing.md)
* [Roadmap](ROADMAP.md)

---

## Examples

Planned examples:

* Ollama + subprocess node
* OpenClaw adapter + local model
* A2A node + HTTP tool node
* hierarchical OpenCuttle bus
* specialist routing with fallbacks

---

## Contributing

Contributions are welcome.

If you want to help:

1. read [CONTRIBUTING.md](CONTRIBUTING.md)
2. pick an issue or open a proposal
3. keep adapters small and well-documented
4. prefer clean interfaces over clever abstractions

We especially welcome:

* adapter contributions
* routing policy ideas
* observability improvements
* examples and docs
* reproducible bug reports

---

## License

MIT — see [LICENSE](LICENSE).

---

## A note on the name

**OpenCuttle** is inspired by cuttlefish: adaptive, intelligent, modular, and expressive.
That felt right for a system designed to coordinate many moving parts without losing flexibility.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_ORG/opencuttle\&type=Date)](https://www.star-history.com/#YOUR_ORG/opencuttle&Date)
