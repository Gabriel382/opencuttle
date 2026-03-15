
# Architecture

This document describes the high-level architecture of OpenCuttle.

## Overview

OpenCuttle is a local-first orchestration bus for heterogeneous agent systems.

Its purpose is to connect and coordinate:
- models
- agents
- multi-agent systems
- protocols
- tools
- recursive sub-buses

## Core components

The architecture is organized around several core areas:

- `core/` — runtime primitives, message envelope, bus foundations
- `orchestrator/` — orchestration and routing logic
- `adapters/` — bridges to external systems
- `memory/` — memory scopes and persistence
- `policies/` — routing and delegation policies
- `sdk/` — developer SDKs
- `examples/` — runnable demos and examples

## Design principles

- Local-first
- Adapter-first
- Observable by default
- Memory-aware
- Recursive by design
- Small stable core

## Planned runtime model

At a high level:

```text
User / CLI
   ↓
OpenCuttle Orchestrator
   ↓
OpenCuttle Bus
   ↓
Nodes / Adapters / External Systems
````

## Status

This document is a stub and will evolve as the implementation becomes concrete.
