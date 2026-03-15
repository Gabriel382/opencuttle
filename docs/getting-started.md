# Getting Started

This guide explains how to set up and run OpenCuttle locally.

## Prerequisites

- Git
- Python 3.x
- Make

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/opencuttle.git
cd opencuttle
````

Install development dependencies:

```bash
make dev
```

## Basic commands

```bash
make doctor
make run
make demo
make test
make lint
```

## First demo

This will run the current OpenCuttle demo:

```bash
make demo
```

## Current status

OpenCuttle is in early development.

At this stage, the project includes:

* repository structure
* base development workflow
* initial documentation
* early runtime foundations

## Next steps

* Read the [Architecture](architecture.md)
* Read the [Message Envelope](message-envelope.md)
* Read the [Local Bus](local-bus.md)
