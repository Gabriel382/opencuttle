from __future__ import annotations

# Standard library imports
from copy import deepcopy

# Local imports
from core.message_validator import (
    MessageEnvelopeValidationError,
    validate_message_envelope,
)


def make_valid_message() -> dict:
    """
    Return a valid baseline OpenCuttle message for tests.
    """
    return {
        "id": "msg_0001",
        "task_id": "task_0001",
        "parent_task_id": None,
        "sender": "user",
        "target": "demo-node",
        "type": "invoke",
        "payload": {
            "text": "Hello from OpenCuttle"
        },
        "metadata": {
            "source": "cli",
            "priority": "normal"
        },
        "timestamp": "2026-03-15T18:00:00Z",
    }


def test_valid_message_passes() -> None:
    """
    A valid message should pass validation without raising an error.
    """
    message = make_valid_message()
    validate_message_envelope(message)


def test_missing_required_field_fails() -> None:
    """
    A message missing a required field should fail clearly.
    """
    message = make_valid_message()
    del message["target"]

    try:
        validate_message_envelope(message)
        assert False, "Expected validation to fail for missing 'target'"
    except MessageEnvelopeValidationError as exc:
        assert "target" in str(exc)


def test_invalid_type_field_fails() -> None:
    """
    A message with an invalid enum value for 'type' should fail clearly.
    """
    message = make_valid_message()
    message["type"] = "banana"

    try:
        validate_message_envelope(message)
        assert False, "Expected validation to fail for invalid 'type'"
    except MessageEnvelopeValidationError as exc:
        assert "type" in str(exc) or "banana" in str(exc)


def test_payload_must_be_an_object() -> None:
    """
    The payload field must be a JSON object, not a string.
    """
    message = make_valid_message()
    message["payload"] = "not-an-object"

    try:
        validate_message_envelope(message)
        assert False, "Expected validation to fail for invalid payload type"
    except MessageEnvelopeValidationError as exc:
        assert "payload" in str(exc)


def test_metadata_must_be_an_object() -> None:
    """
    The metadata field must be a JSON object.
    """
    message = make_valid_message()
    message["metadata"] = []

    try:
        validate_message_envelope(message)
        assert False, "Expected validation to fail for invalid metadata type"
    except MessageEnvelopeValidationError as exc:
        assert "metadata" in str(exc)


def test_parent_task_id_can_be_null() -> None:
    """
    parent_task_id is optional and may be null.
    """
    message = make_valid_message()
    message["parent_task_id"] = None
    validate_message_envelope(message)


def test_unknown_extra_field_fails_if_schema_is_strict() -> None:
    """
    If additionalProperties is false in the schema, unknown fields should fail.
    """
    message = make_valid_message()
    message["unexpected"] = "value"

    try:
        validate_message_envelope(message)
        assert False, "Expected validation to fail for unexpected field"
    except MessageEnvelopeValidationError as exc:
        assert "unexpected" in str(exc) or "Additional properties" in str(exc)