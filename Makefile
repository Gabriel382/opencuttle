SHELL := /bin/bash

PROJECT_NAME := opencuttle
PYTHON := $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)

.PHONY: run cli test lint build clean doctor demo

test:
	@echo "==> Running tests"
	@if [ -d tests ] && find tests -type f | grep -q .; then \
		$(PYTHON) -m pytest -q; \
	else \
		echo "No tests found yet in ./tests"; \
	fi

lint:
	@echo "==> Running lint checks"
	@if command -v ruff >/dev/null 2>&1; then \
		ruff check .; \
	else \
		echo "ruff is not installed. Install it with: $(PYTHON) -m pip install ruff"; \
	fi

build:
	@echo "==> Building project"
	@mkdir -p dist
	@echo "Sprint 1 build placeholder" > dist/BUILD_INFO.txt
	@echo "Created dist/BUILD_INFO.txt"

clean:
	@echo "==> Cleaning temporary files"
	@rm -rf dist .pytest_cache .ruff_cache __pycache__
	@find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Clean complete"

doctor:
	@echo "==> OpenCuttle environment check"
	@echo "Project: $(PROJECT_NAME)"
	@echo "Python: $$($(PYTHON) --version 2>/dev/null || echo 'not found')"
	@echo "Git: $$(git --version 2>/dev/null || echo 'not found')"
	@echo "Pytest: $$($(PYTHON) -m pytest --version 2>/dev/null | head -n 1 || echo 'not installed')"
	@echo "Ruff: $$(ruff --version 2>/dev/null || echo 'not installed')"
	@echo "Working directory: $$(pwd)"

demo:
	@echo "==> Running OpenCuttle demo"
	@if [ -f examples/demo_local_bus.py ]; then \
		PYTHONPATH=. $(PYTHON) examples/demo_local_bus.py; \
	else \
		echo "examples/demo_local_bus.py not found yet."; \
		echo "Create it as part of Milestone 3."; \
		exit 1; \
	fi

run:
	@echo "==> Running OpenCuttle"
	@PYTHONPATH=. $(PYTHON) -m cli.main run

cli:
	@echo "==> OpenCuttle CLI help"
	@PYTHONPATH=. $(PYTHON) -m cli.main --help

help-cli:
	@PYTHONPATH=. $(PYTHON) -m cli.main --help

node-list:
	@echo "==> Listing OpenCuttle nodes"
	@PYTHONPATH=. $(PYTHON) -m cli.main node list

task-run:
	@echo "==> Running OpenCuttle task"
	@PYTHONPATH=. $(PYTHON) -m cli.main task run "hello opencuttle"

node-registration-example:
	@echo "==> Running OpenCuttle node registration example"
	@PYTHONPATH=. $(PYTHON) examples/node_registration_example.py

task-execution-example:
	@echo "==> Running OpenCuttle task execution example"
	@PYTHONPATH=. $(PYTHON) examples/task_execution_example.py