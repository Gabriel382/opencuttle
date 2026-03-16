from __future__ import annotations

"""
Example-facing demo node module.

This module re-exports the official OpenCuttle reference demo node so that
contributors can find it easily under `examples/` while the canonical
implementation remains in `core/`.
"""

# Local imports
from core.demo_node import DemoEchoNode, build_demo_node_manifest

__all__ = ["DemoEchoNode", "build_demo_node_manifest"]