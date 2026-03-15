from __future__ import annotations

# Standard library imports
import logging
from dataclasses import dataclass
from typing import Protocol, Any

# Local imports
from core.message_ids import generate_message_id
from core.message_validator import validate_message_envelope


logger = logging.getLogger(__name__)


class LocalBusError(Exception):
    """Raised when the local bus cannot complete an operation."""


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
        """
        if node.name in self.nodes:
            raise NodeAlreadyRegisteredError(
                f"Node '{node.name}' is already registered in the local bus."
            )

        self.nodes[node.name] = node
        logger.info("Registered node '%s'", node.name)

    def has_node(self, node_name: str) -> bool:
        """
        Check whether a node is registered.
        """
        return node_name in self.nodes

    def send(self, message: dict[str, Any]) -> dict[str, Any]:
        """
        Friendlier alias for dispatch().

        Args:
            message:
                The validated message envelope to send.

        Returns:
            The response envelope returned by the target node.
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