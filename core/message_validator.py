from __future__ import annotations

# Standard library imports
import json
from pathlib import Path
from typing import Any

# Third-party imports
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError


# Resolve the schema path relative to this file.
SCHEMA_PATH = Path(__file__).with_name("message_schema.json")


class MessageEnvelopeValidationError(Exception):
    """Raised when an OpenCuttle message envelope is invalid."""


def load_message_schema() -> dict[str, Any]:
    """
    Load the OpenCuttle message envelope schema from disk.

    Returns:
        The parsed JSON schema as a Python dictionary.
    """
    with SCHEMA_PATH.open("r", encoding="utf-8") as schema_file:
        return json.load(schema_file)


def validate_message_envelope(message: dict[str, Any]) -> None:
    """
    Validate a message envelope against the OpenCuttle JSON Schema.

    Args:
        message:
            The message object to validate.

    Raises:
        MessageEnvelopeValidationError:
            If the message does not match the schema.
    """
    schema = load_message_schema()
    validator = Draft202012Validator(schema)

    # Collect all validation errors instead of failing on only the first one.
    errors = sorted(validator.iter_errors(message), key=lambda err: list(err.path))

    if not errors:
        return

    # Convert structured validation errors into readable text.
    readable_errors = [_format_validation_error(error) for error in errors]

    raise MessageEnvelopeValidationError(
        "Invalid OpenCuttle message envelope:\n- " + "\n- ".join(readable_errors)
    )


def _format_validation_error(error: ValidationError) -> str:
    """
    Convert a jsonschema ValidationError into a more readable string.

    Args:
        error:
            The validation error returned by jsonschema.

    Returns:
        A user-friendly error string.
    """
    # Build a readable field path like "payload.text" if possible.
    if error.path:
        field_path = ".".join(str(part) for part in error.path)
        return f"{field_path}: {error.message}"

    return error.message