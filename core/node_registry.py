from __future__ import annotations

# Standard library imports
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# Third-party imports
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError


SCHEMA_PATH = Path(__file__).with_name("node_manifest_schema.json")


class NodeRegistryError(Exception):
    """Base exception for node registry errors."""


class NodeManifestValidationError(NodeRegistryError):
    """Raised when a node manifest is invalid."""


class NodeManifestAlreadyRegisteredError(NodeRegistryError):
    """Raised when a node name is already registered."""


class NodeManifestNotFoundError(NodeRegistryError):
    """Raised when a node name cannot be found."""


def load_node_manifest_schema() -> dict[str, Any]:
    """
    Load the node manifest JSON Schema from disk.

    Returns:
        The parsed schema as a Python dictionary.
    """
    with SCHEMA_PATH.open("r", encoding="utf-8") as schema_file:
        return json.load(schema_file)


def validate_node_manifest(manifest: dict[str, Any]) -> None:
    """
    Validate a node manifest against the OpenCuttle node manifest schema.

    Args:
        manifest:
            The manifest object to validate.

    Raises:
        NodeManifestValidationError:
            If the manifest does not match the schema.
    """
    schema = load_node_manifest_schema()
    validator = Draft202012Validator(schema)

    errors = sorted(validator.iter_errors(manifest), key=lambda err: list(err.path))

    if not errors:
        return

    readable_errors = [_format_validation_error(error) for error in errors]

    raise NodeManifestValidationError(
        "Invalid OpenCuttle node manifest:\n- " + "\n- ".join(readable_errors)
    )


def _format_validation_error(error: ValidationError) -> str:
    """
    Convert a jsonschema ValidationError into a readable string.

    Args:
        error:
            The validation error returned by jsonschema.

    Returns:
        A readable error string.
    """
    if error.path:
        field_path = ".".join(str(part) for part in error.path)
        return f"{field_path}: {error.message}"

    return error.message


@dataclass
class NodeRegistry:
    """
    In-memory registry for OpenCuttle node manifests.

    This registry:
    - stores validated node metadata
    - supports registration and lookup by name
    - prevents duplicate names
    - is independent of CLI and bus logic
    """

    _manifests: dict[str, dict[str, Any]] = field(default_factory=dict)

    def register(self, manifest: dict[str, Any]) -> None:
        """
        Validate and register a node manifest.

        Args:
            manifest:
                The node manifest to register.

        Raises:
            NodeManifestValidationError:
                If the manifest is invalid.
            NodeManifestAlreadyRegisteredError:
                If the node name is already registered.
        """
        validate_node_manifest(manifest)

        node_name = manifest["name"]

        if node_name in self._manifests:
            raise NodeManifestAlreadyRegisteredError(
                f"Node manifest '{node_name}' is already registered."
            )

        # Store a shallow copy to avoid accidental external mutation.
        self._manifests[node_name] = dict(manifest)

    def has(self, node_name: str) -> bool:
        """
        Check whether a node manifest is registered.

        Args:
            node_name:
                The node name to check.

        Returns:
            True if registered, otherwise False.
        """
        return node_name in self._manifests

    def get(self, node_name: str) -> dict[str, Any]:
        """
        Retrieve a registered node manifest by name.

        Args:
            node_name:
                The node name to retrieve.

        Returns:
            The registered node manifest.

        Raises:
            NodeManifestNotFoundError:
                If the node name is not registered.
        """
        if node_name not in self._manifests:
            raise NodeManifestNotFoundError(
                f"Node manifest '{node_name}' is not registered."
            )

        return dict(self._manifests[node_name])

    def list_all(self) -> list[dict[str, Any]]:
        """
        List all registered node manifests.

        Returns:
            A list of manifest dictionaries.
        """
        return [dict(manifest) for manifest in self._manifests.values()]