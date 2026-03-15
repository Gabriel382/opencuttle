from __future__ import annotations

# Local imports
from core.message_serializer import (
    MessageEnvelopeSerializationError,
    deserialize_message_envelope,
    serialize_message_envelope,
)


def make_valid_message() -> dict:
    """
    Return a valid baseline OpenCuttle message for serializer tests.
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


def test_serialize_valid_message_returns_json_string() -> None:
    """
    Serializing a valid message should return a JSON string.
    """
    message = make_valid_message()
    raw_json = serialize_message_envelope(message)

    assert isinstance(raw_json, str)
    assert '"id":"msg_0001"' in raw_json


def test_deserialize_valid_json_returns_message_dict() -> None:
    """
    Deserializing a valid JSON envelope should return a dictionary.
    """
    raw_json = (
        '{"id":"msg_0001","task_id":"task_0001","parent_task_id":null,'
        '"sender":"user","target":"demo-node","type":"invoke",'
        '"payload":{"text":"Hello from OpenCuttle"},'
        '"metadata":{"source":"cli","priority":"normal"},'
        '"timestamp":"2026-03-15T18:00:00Z"}'
    )

    message = deserialize_message_envelope(raw_json)

    assert isinstance(message, dict)
    assert message["id"] == "msg_0001"
    assert message["metadata"]["source"] == "cli"


def test_round_trip_preserves_all_fields() -> None:
    """
    Serializing and then deserializing a valid message should preserve all fields.
    """
    original = make_valid_message()

    raw_json = serialize_message_envelope(original)
    restored = deserialize_message_envelope(raw_json)

    assert restored == original


def test_deserialize_invalid_json_fails_clearly() -> None:
    """
    Invalid JSON should raise a readable serialization error.
    """
    raw_json = '{"id": "msg_0001", invalid json}'

    try:
        deserialize_message_envelope(raw_json)
        assert False, "Expected deserialization to fail"
    except MessageEnvelopeSerializationError as exc:
        assert "deserialize" in str(exc).lower()


def test_deserialize_non_object_json_fails() -> None:
    """
    The top-level JSON value must be an object.
    """
    raw_json = '["not", "an", "object"]'

    try:
        deserialize_message_envelope(raw_json)
        assert False, "Expected deserialization to fail for non-object JSON"
    except MessageEnvelopeSerializationError as exc:
        assert "top-level" in str(exc).lower()


def test_serialize_invalid_message_fails() -> None:
    """
    Invalid message objects should fail before serialization.
    """
    invalid_message = make_valid_message()
    del invalid_message["target"]

    try:
        serialize_message_envelope(invalid_message)
        assert False, "Expected serialization to fail for invalid message"
    except Exception as exc:
        assert "target" in str(exc).lower()