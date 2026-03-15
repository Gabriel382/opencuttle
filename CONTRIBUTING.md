# Contributing to OpenCuttle

First off, thank you for considering contributing to OpenCuttle.

OpenCuttle aims to be a **local-first orchestration bus for heterogeneous agent systems**. We want it to be simple to install, easy to extend, and robust enough to become foundational infrastructure for multi-agent interoperability.

We welcome contributions of all kinds:
- bug reports
- documentation improvements
- examples
- adapters
- tests
- architecture proposals
- performance improvements
- observability tooling
- routing and memory policies

---

## Table of contents

- [Ways to contribute](#ways-to-contribute)
- [Before you start](#before-you-start)
- [Development principles](#development-principles)
- [Project priorities](#project-priorities)
- [Getting started](#getting-started)
- [Development workflow](#development-workflow)
- [Pull request guidelines](#pull-request-guidelines)
- [Code style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)
- [Adapters](#adapters)
- [Architecture changes](#architecture-changes)
- [Good first contributions](#good-first-contributions)
- [Community expectations](#community-expectations)

---

## Ways to contribute

You do **not** need to start with core runtime code.

Valuable contributions include:
- improving docs and examples
- reporting reproducible bugs
- adding tests
- implementing small adapters
- improving CLI UX
- refining tracing and logs
- proposing routing or memory policies
- tightening interfaces and type definitions

---

## Before you start

Before opening a large pull request, please:
1. check whether an issue already exists
2. open an issue for substantial changes
3. explain the problem, motivation, and rough design

For small fixes, feel free to open a PR directly.

For large changes, we strongly prefer:
- one issue
- one clear proposal
- one scoped implementation

---

## Development principles

OpenCuttle follows a few core principles:

### 1. Keep the core small
The core bus and orchestration primitives should remain simple and durable.

### 2. Prefer adapters over rewrites
OpenCuttle should integrate existing systems instead of forcing migration into a single framework.

### 3. Local-first is a feature
Anything that improves local usability, startup speed, debuggability, and installation simplicity is valuable.

### 4. Observability is part of the product
Logs, traces, metrics, and replayability are not optional extras.

### 5. Recursion is native
A sub-bus should be able to behave as a node in a larger OpenCuttle system.

### 6. Earn complexity slowly
We value maintainability more than cleverness.

---

## Project priorities

At this stage, the highest-value areas are:

1. core message envelope and runtime contracts
2. local bus reliability
3. CLI ergonomics
4. node registry and capability metadata
5. adapters for real systems
6. routing policies
7. memory scopes
8. tracing and replay
9. recursive bus composition

---

## Getting started

Clone the repository:

```bash
git clone https://github.com/YOUR_ORG/opencuttle.git
cd opencuttle
````

Install development dependencies:

```bash
make dev
```

Run checks:

```bash
make test
make lint
make doctor
```

Run the project locally:

```bash
make run
```

---

## Development workflow

A typical workflow looks like this:

1. fork the repository
2. create a feature branch
3. make a focused change
4. add or update tests
5. update docs if needed
6. run local checks
7. open a pull request

Example:

```bash
git checkout -b feat/ollama-adapter
```

Please keep branches focused. One PR should ideally solve one problem.

---

## Pull request guidelines

### Scope

Keep PRs small and reviewable whenever possible.

### Description

A good PR description should include:

* what changed
* why it changed
* how it was tested
* whether docs were updated
* any known limitations

### Linked issues

Please link related issues when applicable.

### Breaking changes

If your change is breaking, call it out clearly and explain:

* what breaks
* why the change is necessary
* how users should migrate

---

## Code style

General expectations:

* prefer clear names over short names
* prefer explicit behavior over magic
* keep modules focused
* avoid premature abstraction
* write comments where intent is non-obvious
* preserve stable interfaces when possible

### Comments

Write comments for:

* non-obvious orchestration behavior
* envelope semantics
* retry/fallback behavior
* memory scope decisions
* adapter edge cases

### Configuration

If behavior is configurable, document the config clearly.

---

## Testing

Every meaningful contribution should include appropriate validation.

Expected types of testing:

* unit tests for small logic
* integration tests for adapters and routing
* regression tests for bug fixes
* smoke tests for CLI flows

At minimum:

* new behavior should be tested
* bug fixes should include a reproducer when possible

Run:

```bash
make test
```

If you add an adapter, include:

* a minimal happy-path test
* one failure-path test
* fixture or mock setup if appropriate

---

## Documentation

Documentation is part of the contribution.

Please update docs when you change:

* CLI commands
* config schema
* adapter contracts
* routing behavior
* memory behavior
* architecture assumptions

Useful docs to update may include:

* `README.md`
* `docs/getting-started.md`
* `docs/architecture.md`
* `docs/adapters.md`
* `docs/policies.md`
* `docs/memory.md`

---

## Adapters

Adapters are one of the most important extension points in OpenCuttle.

Examples:

* Ollama
* OpenClaw
* A2A
* MCP
* subprocess
* HTTP
* WebSocket

### Adapter design rules

Adapters should be:

* small
* well-scoped
* easy to test
* explicit about capabilities
* explicit about trust boundaries
* explicit about failure modes

### Adapter PR checklist

An adapter PR should ideally include:

* adapter implementation
* capability description
* config example
* one runnable example
* tests
* docs

---

## Architecture changes

For changes affecting core architecture, please open an issue first.

This includes:

* message envelope changes
* node manifest changes
* registry changes
* orchestration model changes
* memory model changes
* policy engine changes
* recursion/hierarchy changes

We prefer discussing these before implementation to avoid costly rework.

---

## Good first contributions

Good starter contributions include:

* improving CLI messages
* fixing docs
* adding examples
* writing tests for existing modules
* adding a small local adapter
* improving trace output
* improving configuration validation

Look for issues labeled:

* `good first issue`
* `help wanted`
* `documentation`
* `adapter`

---

## Community expectations

Be respectful, constructive, and specific.

Good collaboration looks like:

* explaining tradeoffs
* asking clarifying questions
* focusing on the code and design, not the person
* keeping discussion concrete and actionable

We want OpenCuttle to be technically strong and welcoming to contributors.

---

## Need help?

If you are unsure where to start:

* open a discussion
* comment on an issue
* ask for guidance in a draft PR

Small, well-executed contributions are highly valued.
