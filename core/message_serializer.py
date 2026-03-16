from __future__ import annotations

# Standard library imports
import json
from typing import Any

# Local imports
from core.message_validator import (
    MessageEnvelopeValidationError,
    validate_message_envelope,
)


class MessageEnvelopeSerializationError(Exception):
    """Raised when an OpenCuttle message cannot be serialized or deserialized."""


def serialize_message_envelope(message: dict[str, Any]) -> str:
    """
    Validate and serialize an OpenCuttle message envelope to JSON text.

    Args:
        message:
            The message envelope as a Python dictionary.

    Returns:
        The serialized JSON string.

    Raises:
        MessageEnvelopeValidationError:
            If the message does not match the schema.
        MessageEnvelopeSerializationError:
            If JSON serialization fails.
    """
    validate_message_envelope(message)

    try:
        return json.dumps(message, ensure_ascii=False, separators=(",", ":"))
    except (TypeError, ValueError) as exc:
        raise MessageEnvelopeSerializationError(
            f"Failed to serialize message envelope: {exc}"
        ) from exc


def deserialize_message_envelope(raw_json: str) -> dict[str, Any]:
    """
    Parse JSON text into an OpenCuttle message envelope and validate it.

    Args:
        raw_json:
            The raw JSON string.

    Returns:
        The deserialized message envelope as a Python dictionary.

    Raises:
        MessageEnvelopeSerializationError:
            If JSON parsing fails or the parsed value is not an object.
        MessageEnvelopeValidationError:
            If the parsed object does not match the schema.
    """
    try:
        parsed = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise MessageEnvelopeSerializationError(
            f"Failed to deserialize message envelope: {exc}"
        ) from exc

    if not isinstance(parsed, dict):
        raise MessageEnvelopeSerializationError(
            "Failed to deserialize message envelope: top-level JSON value must be an object"
        )

    validate_message_envelope(parsed)
    return parsed