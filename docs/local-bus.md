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

## Status

This document is a stub and will evolve during the Local Bus milestone.