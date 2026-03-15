# OpenCuttle Roadmap

This roadmap starts from the **simplest possible useful version** and grows toward a complete local-first orchestration platform for heterogeneous agent systems.

OpenCuttle is intentionally being built in layers:
1. make it work
2. make it easy to use
3. make it robust
4. make it extensible
5. make it foundational

---

## Vision

OpenCuttle will become a **local-first orchestration bus** for:
- models
- agents
- multi-agent systems
- protocols
- tools
- recursive sub-buses

Each connected node can expose:
- identity
- capabilities
- skills
- model or backend
- memory
- personality/profile
- trust boundaries
- operational metadata

And one orchestrator in the middle can:
- route
- delegate
- observe
- remember
- recover
- compose

---

## Milestone 0 — Identity and scope
Status: planned

Goals:
- finalize the project name and positioning
- publish core principles
- define what OpenCuttle is and is not

Deliverables:
- README
- roadmap
- contributing guide
- security policy

---

## Milestone 1 — Repository bootstrap
Status: planned

Goals:
- create a clean repository structure
- make local development easy
- establish baseline tooling

Deliverables:
- `Makefile`
- root layout
- lint/test/dev targets
- initial docs structure

---

## Milestone 2 — Message envelope
Status: planned

Goals:
- define the base message schema
- establish message IDs, task IDs, and correlation semantics

Deliverables:
- envelope schema
- validation logic
- serialization layer

---

## Milestone 3 — Local bus v0
Status: planned

Goals:
- implement the simplest local bus
- support request/response between nodes

Deliverables:
- in-memory local bus
- basic pub/sub or dispatch flow
- minimal demo with two nodes

---

## Milestone 4 — Node registry
Status: planned

Goals:
- let nodes register themselves
- expose capabilities and metadata

Deliverables:
- node manifest format
- registry implementation
- CLI inspection support

---

## Milestone 5 — CLI v0
Status: planned

Goals:
- make OpenCuttle usable without custom code

Deliverables:
- `opencuttle run`
- `opencuttle node list`
- `opencuttle node inspect`
- `opencuttle task run`
- `opencuttle logs`

---

## Milestone 6 — Demo node
Status: planned

Goals:
- create a minimal reference node
- establish the smallest working node contract

Deliverables:
- echo/demo node
- registration example
- task execution example

---

## Milestone 7 — Orchestrator v0
Status: planned

Goals:
- route simple tasks to the right node
- support rule-based delegation

Deliverables:
- central orchestrator
- basic skill routing
- simple end-to-end task execution

---

## Milestone 8 — Persistence v0
Status: planned

Goals:
- persist task history and logs locally

Deliverables:
- local storage
- task history
- execution log persistence

---

## Milestone 9 — Config files
Status: planned

Goals:
- make the system configurable without code edits

Deliverables:
- `opencuttle.yaml`
- node config files
- policy config files

---

# Phase 2 — Real integrations

## Milestone 10 — Subprocess adapter
Status: planned

Goals:
- wrap local scripts and binaries as nodes

Deliverables:
- subprocess adapter
- config examples
- timeout handling

---

## Milestone 11 — Ollama adapter
Status: planned

Goals:
- connect local Ollama models as first-class nodes

Deliverables:
- Ollama adapter
- model metadata exposure
- example route using local models

---

## Milestone 12 — HTTP adapter
Status: planned

Goals:
- connect generic HTTP JSON services

Deliverables:
- HTTP adapter
- request/response mapping
- auth and timeout config basics

---

## Milestone 13 — WebSocket adapter
Status: planned

Goals:
- support long-lived or streaming nodes

Deliverables:
- WebSocket adapter
- connection lifecycle handling

---

## Milestone 14 — MCP adapter
Status: planned

Goals:
- integrate MCP-based systems into OpenCuttle

Deliverables:
- MCP adapter
- capability discovery
- invocation bridge

---

## Milestone 15 — A2A adapter
Status: planned

Goals:
- integrate A2A-compatible agents as nodes

Deliverables:
- A2A adapter
- description/invocation bridge
- example external agent integration

---

## Milestone 16 — OpenClaw adapter
Status: planned

Goals:
- connect OpenClaw agents or workspaces as nodes

Deliverables:
- OpenClaw adapter
- one real example with delegated execution

---

# Phase 3 — Policy and routing

## Milestone 17 — Routing policies v1
Status: planned

Goals:
- support configurable routing behavior

Deliverables:
- `fastest`
- `cheapest`
- `local-only`
- `preferred-node`
- `fallback-chain`

---

## Milestone 18 — Capability matching
Status: planned

Goals:
- improve node selection beyond simple name matching

Deliverables:
- skill scoring
- weighted matching
- priority-aware routing

---

## Milestone 19 — Profiles and personas
Status: planned

Goals:
- give nodes operational identity

Deliverables:
- node profile model
- persona fields
- routing by role/style/specialization

---

## Milestone 20 — Multi-step orchestration
Status: planned

Goals:
- support task decomposition into multiple steps

Deliverables:
- planner/executor chains
- sequential and parallel delegation primitives

---

# Phase 4 — Memory

## Milestone 21 — Memory v1
Status: planned

Goals:
- support useful memory scopes

Deliverables:
- task memory
- session memory
- node-private memory
- shared memory

---

## Milestone 22 — Episodic memory
Status: planned

Goals:
- remember useful prior execution context

Deliverables:
- success/failure memory
- node preference memory
- history-based routing hints

---

## Milestone 23 — Persona memory
Status: planned

Goals:
- preserve identity-related context per node

Deliverables:
- persona memory layer
- durable preferences
- scoped behavior memory

---

## Milestone 24 — Memory policies
Status: planned

Goals:
- govern what is remembered and for how long

Deliverables:
- ephemeral memory
- durable memory
- task-only retention
- private vs shared policies

---

# Phase 5 — Observability

## Milestone 25 — Trace tree
Status: planned

Goals:
- expose full delegation trees

Deliverables:
- task trace graph
- parent/child execution views
- correlation-aware logs

---

## Milestone 26 — Metrics
Status: planned

Goals:
- measure node and policy performance

Deliverables:
- latency
- failures
- retries
- token/cost tracking
- throughput

---

## Milestone 27 — Replay mode
Status: planned

Goals:
- replay task executions for debugging

Deliverables:
- run replay
- trace replay
- deterministic-ish debug support where possible

---

## Milestone 28 — Minimal web UI
Status: planned

Goals:
- provide inspection and mission-control basics

Deliverables:
- nodes view
- tasks view
- logs view
- traces view
- memory view

---

# Phase 6 — Hierarchy and recursion

## Milestone 29 — Bus as node
Status: planned

Goals:
- allow one OpenCuttle instance to behave as a node in another

Deliverables:
- bus-node adapter
- capability summarization
- nested delegation support

---

## Milestone 30 — Supervisor bus
Status: planned

Goals:
- orchestrate multiple OpenCuttle instances

Deliverables:
- multi-bus orchestration
- top-level supervisor routing

---

## Milestone 31 — Federation policies
Status: planned

Goals:
- choose between local, clustered, and remote layers

Deliverables:
- hierarchical escalation
- federated routing strategies
- domain-aware routing

---

# Phase 7 — Reliability

## Milestone 32 — Retries, timeout, cancel
Status: planned

Goals:
- support resilient execution

Deliverables:
- timeout controls
- retry policies
- cancellation
- failure classification

---

## Milestone 33 — Health and heartbeat
Status: planned

Goals:
- track node liveness and readiness

Deliverables:
- health checks
- heartbeat model
- degraded node handling

---

## Milestone 34 — Queue control
Status: planned

Goals:
- manage load safely

Deliverables:
- queue limits
- concurrency control
- backpressure
- prioritization

---

## Milestone 35 — Failover
Status: planned

Goals:
- recover across nodes and routes

Deliverables:
- fallback chains
- alternate routes
- graceful degradation

---

# Phase 8 — SDKs and developer ecosystem

## Milestone 36 — Python SDK
Status: planned

Goals:
- make node creation easy in Python

Deliverables:
- registration helpers
- invoke/stream helpers
- memory helpers

---

## Milestone 37 — Go SDK
Status: planned

Goals:
- support performant and systems-oriented integrations

Deliverables:
- Go SDK
- adapter examples

---

## Milestone 38 — Templates
Status: planned

Goals:
- let users scaffold nodes and adapters quickly

Deliverables:
- `opencuttle init node-python`
- `opencuttle init adapter-http`
- `opencuttle init adapter-ollama`

---

## Milestone 39 — Example gallery
Status: planned

Goals:
- demonstrate real patterns clearly

Deliverables:
- examples for local models
- examples for external systems
- examples for recursive buses

---

# Phase 9 — Smarter routing

## Milestone 40 — Semantic capability matching
Status: planned

Goals:
- route using semantic similarity and richer descriptions

Deliverables:
- capability embeddings
- semantic matching layer
- hybrid rule + semantic routing

---

## Milestone 41 — Adaptive routing
Status: planned

Goals:
- learn from prior outcomes

Deliverables:
- performance-informed node ranking
- policy adjustment signals

---

## Milestone 42 — Cost/performance optimization
Status: planned

Goals:
- optimize across speed, cost, and quality

Deliverables:
- optimization heuristics
- escalation strategies
- route simulation support

---

# Phase 10 — Security and governance

## Milestone 43 — Permissions
Status: planned

Goals:
- enforce node-level permissions

Deliverables:
- file/network/tool access control
- memory scope restrictions

---

## Milestone 44 — Secret handling
Status: planned

Goals:
- manage credentials safely

Deliverables:
- secret loading strategy
- environment and vault compatibility

---

## Milestone 45 — Signed node manifests
Status: planned

Goals:
- improve trust and compatibility checks

Deliverables:
- manifest signing concept
- integrity validation

---

# Phase 11 — Production-grade experience

## Milestone 46 — Mission Control UI v2
Status: planned

Goals:
- make runtime inspection excellent

Deliverables:
- graph visualization
- advanced trace navigation
- policy comparison
- replay UI

---

## Milestone 47 — Packaging and distribution
Status: planned

Goals:
- make installation excellent across platforms

Deliverables:
- binaries
- Docker support
- improved `make install`
- release automation

---

## Milestone 48 — Adapter registry
Status: planned

Goals:
- make ecosystem growth easier

Deliverables:
- adapter index
- discovery format
- publishing guidelines

---

## Milestone 49 — Benchmarks
Status: planned

Goals:
- evaluate OpenCuttle rigorously

Deliverables:
- latency benchmarks
- routing benchmarks
- failover benchmarks
- adapter benchmarks

---

## Milestone 50 — OpenCuttle 1.0
Status: planned

Goals:
- publish a stable first major release

Release criteria:
- stable core
- stable CLI
- reliable local bus
- memory scopes
- tracing
- at least several official adapters
- hierarchy support
- production-quality docs

---

## Suggested first implementation slice

For a strong first version, build in this order:

1. Milestones 1–9
2. Milestones 10–13
3. Milestones 17–21
4. Milestones 25–28
5. Milestones 14–16
6. Milestones 29–35
7. Milestones 36–39
8. Milestones 40–50

This keeps the project useful early without overcommitting too soon.

---

## Definition of success

OpenCuttle succeeds if:
- users can install it fast
- users can connect existing systems without rewrites
- orchestration is visible and debuggable
- routing is useful and configurable
- the core stays small and extensible
- recursive composition feels natural
