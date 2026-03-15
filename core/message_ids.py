from __future__ import annotations

# Standard library imports
import uuid


def generate_message_id() -> str:
    """
    Generate a unique OpenCuttle message ID for local v0 usage.

    Returns:
        A string in the format: msg_<32 lowercase hex chars>
    """
    return f"msg_{uuid.uuid4().hex}"


def generate_task_id() -> str:
    """
    Generate a unique OpenCuttle task ID for local v0 usage.

    Returns:
        A string in the format: task_<32 lowercase hex chars>
    """
    return f"task_{uuid.uuid4().hex}"