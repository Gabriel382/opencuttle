from __future__ import annotations

# Standard library imports
from dataclasses import dataclass
from typing import Protocol, Any

# Local imports
from core.message_ids import generate_message_id, generate_task_id
from core.message_validator import validate_message_envelope


class LocalBusError(Exception):
    """Raised when the local bus cannot complete an operation."""


class NodeAlreadyRegisteredError(LocalBusError):
    """Raised when trying to register a node name that already exists."""


class NodeNotFoundError(LocalBusError):
    """Raised when the target node is not registered in the bus."""


class BusNode(Protocol):
    """
    Protocol for a minimal OpenCuttle node.

    A node must expose:
    - a unique name
    - a synchronous message handler
    """

    name: str

    def handle_message(self, message: dict[str, Any]) -> dict[str, Any]:
        """Handle an incoming message and return a response message."""


@dataclass
class LocalBus:
    """
    Minimal in-memory OpenCuttle bus.

    This v0 bus:
    - stores nodes in memory
    - dispatches synchronously
    - does not use network access
    - does not persist state
    """

    nodes: dict[str, BusNode]

    def __init__(self) -> None:
        """Initialize an empty local bus."""
        self.nodes = {}

    def register_node(self, node: BusNode) -> None:
        """
        Register a node in the local bus.

        Args:
            node:
                The node to register.

        Raises:
            NodeAlreadyRegisteredError:
                If another node with the same name is already registered.
        """
        if node.name in self.nodes:
            raise NodeAlreadyRegisteredError(
                f"Node '{node.name}' is already registered in the local bus."
            )

        self.nodes[node.name] = node

    def has_node(self, node_name: str) -> bool:
        """
        Check whether a node is registered.

        Args:
            node_name:
                The node name to look up.

        Returns:
            True if the node exists, otherwise False.
        """
        return node_name in self.nodes

    def dispatch(self, message: dict[str, Any]) -> dict[str, Any]:
        """
        Dispatch a validated message to its target node.

        Args:
            message:
                The message envelope to dispatch.

        Returns:
            The target node's response envelope.

        Raises:
            NodeNotFoundError:
                If the target node is not registered.
        """
        validate_message_envelope(message)

        target = message["target"]

        if target not in self.nodes:
            raise NodeNotFoundError(
                f"Target node '{target}' is not registered in the local bus."
            )

        response = self.nodes[target].handle_message(message)
        validate_message_envelope(response)
        return response


@dataclass
class EchoNode:
    """
    Minimal demo node used for local bus testing.

    It returns a simple response containing the incoming payload.
    """

    name: str

    def handle_message(self, message: dict[str, Any]) -> dict[str, Any]:
        """
        Return a simple response envelope.

        Args:
            message:
                The incoming validated message.

        Returns:
            A response envelope.
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