SHELL := /bin/bash

PROJECT_NAME := opencuttle
PYTHON ?= python3

.PHONY: help dev test lint build run clean doctor demo

help:
	@echo "OpenCuttle development targets"
	@echo ""
	@echo "  make dev     - Set up local development environment"
	@echo "  make test    - Run tests"
	@echo "  make lint    - Run linting checks"
	@echo "  make build   - Build project artifacts"
	@echo "  make run     - Run OpenCuttle locally"
	@echo "  make clean   - Remove temporary files"
	@echo "  make doctor  - Check local environment"
	@echo "  make demo    - Run the Sprint 1 demo"

dev:
	@echo "==> Setting up development environment"
	@if [ -f requirements-dev.txt ]; then \
		$(PYTHON) -m pip install -r requirements-dev.txt; \
	else \
		echo "No requirements-dev.txt found yet. Skipping dependency install."; \
	fi

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

run:
	@echo "==> Running OpenCuttle"
	@if [ -f scripts/run.py ]; then \
		$(PYTHON) scripts/run.py; \
	else \
		echo "scripts/run.py not found yet."; \
		echo "Create it in Sprint 1 so 'make run' has a real entrypoint."; \
		exit 1; \
	fi

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
		$(PYTHON) examples/demo_local_bus.py; \
	else \
		echo "examples/demo_local_bus.py not found yet."; \
		echo "Create it as part of Milestone 3."; \
		exit 1; \
	fi