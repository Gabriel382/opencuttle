from __future__ import annotations

# Local imports
from core.message_ids import generate_message_id, generate_task_id


def test_generate_message_id_has_expected_prefix() -> None:
    """
    Message IDs should start with 'msg_'.
    """
    message_id = generate_message_id()
    assert message_id.startswith("msg_")


def test_generate_task_id_has_expected_prefix() -> None:
    """
    Task IDs should start with 'task_'.
    """
    task_id = generate_task_id()
    assert task_id.startswith("task_")


def test_generate_message_id_has_expected_length() -> None:
    """
    Message IDs should contain the prefix plus a 32-character hex UUID.
    """
    message_id = generate_message_id()
    assert len(message_id) == 4 + 32


def test_generate_task_id_has_expected_length() -> None:
    """
    Task IDs should contain the prefix plus a 32-character hex UUID.
    """
    task_id = generate_task_id()
    assert len(task_id) == 5 + 32


def test_generate_message_ids_are_unique_for_local_use() -> None:
    """
    Consecutively generated message IDs should differ.
    """
    first = generate_message_id()
    second = generate_message_id()
    assert first != second


def test_generate_task_ids_are_unique_for_local_use() -> None:
    """
    Consecutively generated task IDs should differ.
    """
    first = generate_task_id()
    second = generate_task_id()
    assert first != second


def test_generated_message_id_uses_lowercase_hex() -> None:
    """
    The UUID portion of the message ID should be lowercase hexadecimal.
    """
    message_id = generate_message_id()
    uuid_part = message_id.removeprefix("msg_")

    assert uuid_part == uuid_part.lower()
    assert all(char in "0123456789abcdef" for char in uuid_part)


def test_generated_task_id_uses_lowercase_hex() -> None:
    """
    The UUID portion of the task ID should be lowercase hexadecimal.
    """
    task_id = generate_task_id()
    uuid_part = task_id.removeprefix("task_")

    assert uuid_part == uuid_part.lower()
    assert all(char in "0123456789abcdef" for char in uuid_part)