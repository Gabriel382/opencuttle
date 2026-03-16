from __future__ import annotations

# Standard library imports
import logging
from dataclasses import dataclass
from typing import Protocol, Any
import json

# Local imports
from core.message_ids import generate_message_id
from core.message_validator import validate_message_envelope
from core.node_registry import (
    NodeManifestAlreadyRegisteredError,
    NodeRegistry,
)



logger = logging.getLogger(__name__)


class LocalBusError(Exception):
    """Raised when the local bus cannot complete an operation."""

class RuntimeNodeNotFoundError(LocalBusError):
    """Raised when a runtime node object cannot be found in the bus."""

class NodeAlreadyRegisteredError(LocalBusError):
    """Raised when trying to register a node name that already exists."""


class NodeNotFoundError(LocalBusError):
    """Raised when the target node is not registered in the bus."""


class BusNode(Protocol):
    """
    Protocol for a minimal OpenCuttle node.
    """

    name: str

    def handle_message(self, message: dict[str, Any]) -> dict[str, Any]:
        """Handle an incoming message and return a response message."""


def build_default_node_manifest(node: BusNode) -> dict[str, Any]:
    """
    Build a minimal default node manifest from a runtime node object.

    This keeps existing demos working even when no explicit manifest is passed.

    Args:
        node:
            The runtime node instance.

    Returns:
        A valid minimal node manifest.
    """
    return {
        "name": node.name,
        "type": "node",
        "description": f"Auto-generated manifest for node '{node.name}'",
        "skills": ["unknown"],
        "tags": ["local", "auto-generated"],
    }


@dataclass
class LocalBus:
    """
    Minimal in-memory OpenCuttle bus.

    This v0 bus:
    - stores runtime nodes in memory
    - stores node metadata in a dedicated registry
    - dispatches synchronously
    - does not use network access
    - does not persist state
    """

    nodes: dict[str, BusNode]
    registry: NodeRegistry

    def __init__(self) -> None:
        """Initialize an empty local bus and node registry."""
        self.nodes = {}
        self.registry = NodeRegistry()

    def register_node(
        self,
        node: BusNode,
        manifest: dict[str, Any] | None = None,
    ) -> None:
        """
        Register a node in the local bus and metadata registry.

        Args:
            node:
                The runtime node object.
            manifest:
                Optional explicit node manifest. If omitted, a default manifest
                is generated from the node.

        Raises:
            NodeAlreadyRegisteredError:
                If the node name is already registered in the bus or registry.
        """
        if node.name in self.nodes:
            raise NodeAlreadyRegisteredError(
                f"Node '{node.name}' is already registered in the local bus."
            )

        final_manifest = manifest if manifest is not None else build_default_node_manifest(node)

        try:
            self.registry.register(final_manifest)
        except NodeManifestAlreadyRegisteredError as exc:
            raise NodeAlreadyRegisteredError(str(exc)) from exc

        self.nodes[node.name] = node
        logger.info("Registered node '%s' in local bus and registry", node.name)

    def has_node(self, node_name: str) -> bool:
        """
        Check whether a node is registered in the runtime bus.
        """
        return node_name in self.nodes

    def get_node_manifest(self, node_name: str) -> dict[str, Any]:
        """
        Retrieve registered node metadata from the registry.

        Args:
            node_name:
                The node name to inspect.

        Returns:
            The registered node manifest.
        """
        return self.registry.get(node_name)

    def list_node_manifests(self) -> list[dict[str, Any]]:
        """
        List all registered node manifests.

        Returns:
            All manifests currently registered in the bus registry.
        """
        return self.registry.list_all()

    def send(self, message: dict[str, Any]) -> dict[str, Any]:
        """
        Friendlier alias for dispatch().
        """
        return self.dispatch(message)

    def dispatch(self, message: dict[str, Any]) -> dict[str, Any]:
        """
        Dispatch a validated message to its target node.

        Flow:
        1. validate incoming message
        2. resolve target node by name
        3. raise a clear error if target is missing
        4. call the target synchronously
        5. validate response envelope
        6. return response
        """
        validate_message_envelope(message)

        sender = message["sender"]
        target = message["target"]
        message_id = message["id"]
        task_id = message["task_id"]

        logger.info(
            "Dispatching message id=%s task_id=%s sender=%s target=%s",
            message_id,
            task_id,
            sender,
            target,
        )

        if target not in self.nodes:
            logger.error(
                "Dispatch failed for message id=%s: target node '%s' is not registered",
                message_id,
                target,
            )
            raise NodeNotFoundError(
                f"Target node '{target}' is not registered in the local bus."
            )

        response = self.nodes[target].handle_message(message)
        validate_message_envelope(response)

        logger.info(
            "Response generated for message id=%s by node=%s",
            message_id,
            target,
        )

        return response
    
    def get_node(self, node_name: str) -> BusNode:
        """
        Retrieve a registered runtime node object by name.

        Args:
            node_name:
                The runtime node name to retrieve.

        Returns:
            The runtime node object.

        Raises:
            RuntimeNodeNotFoundError:
                If the node is not registered in the local bus.
        """
        if node_name not in self.nodes:
            raise RuntimeNodeNotFoundError(
                f"Runtime node '{node_name}' is not registered in the local bus."
            )

        return self.nodes[node_name]


    def list_nodes(self) -> list[BusNode]:
        """
        List all registered runtime node objects.

        Returns:
            A list of registered runtime nodes.
        """
        return list(self.nodes.values())


    def get_node_summary(self, node_name: str) -> dict[str, Any]:
        """
        Build a CLI-friendly summary of a registered node.

        This combines:
        - runtime identity from the bus
        - metadata from the node registry

        Args:
            node_name:
                The node name to inspect.

        Returns:
            A summary dictionary suitable for CLI or docs output.
        """
        node = self.get_node(node_name)
        manifest = self.get_node_manifest(node_name)

        return {
            "name": node.name,
            "runtime_class": node.__class__.__name__,
            "manifest": manifest,
        }


    def format_node_summary(self, node_name: str) -> str:
        """
        Return a human-readable string summary of a registered node.

        Args:
            node_name:
                The node name to inspect.

        Returns:
            Pretty-printed JSON summary for future CLI use.
        """
        summary = self.get_node_summary(node_name)
        return json.dumps(summary, indent=2, ensure_ascii=False)


@dataclass
class EchoNode:
    """
    Minimal demo node used for local bus testing.
    """

    name: str

    def handle_message(self, message: dict[str, Any]) -> dict[str, Any]:
        """
        Return a simple response envelope.
        """
        return {
            "id": generate_message_id(),
            "task_id": message["task_id"],
            "parent_task_id": message.get("parent_task_id"),
            "sender": self.name,
            "target": message["sender"],
            "type": "response",
            "payload": {
                "received_by": self.name,
                "original_payload": message["payload"],
            },
            "metadata": {
                "source": "local_bus",
                "status": "ok",
            },
            "timestamp": message["timestamp"],
        }