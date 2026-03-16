from __future__ import annotations

# Local imports
from core.node_registry import (
    NodeManifestAlreadyRegisteredError,
    NodeManifestNotFoundError,
    NodeManifestValidationError,
    NodeRegistry,
)


def make_valid_manifest(name: str = "demo-echo-node") -> dict:
    """
    Return a valid OpenCuttle node manifest for registry tests.
    """
    return {
        "name": name,
        "type": "node",
        "description": "Minimal reference node that echoes received payloads",
        "skills": ["echo", "demo", "local-testing"],
        "tags": ["local", "demo", "reference"],
        "model": "none",
        "version": "0.1.0",
        "priority": 10,
        "persona": "friendly-demo",
        "memory_scope": "none",
    }


def test_register_valid_manifest_succeeds() -> None:
    """
    A valid manifest should register successfully.
    """
    registry = NodeRegistry()
    manifest = make_valid_manifest()

    registry.register(manifest)

    assert registry.has("demo-echo-node") is True


def test_duplicate_manifest_name_fails() -> None:
    """
    Registering the same node name twice should fail clearly.
    """
    registry = NodeRegistry()
    manifest = make_valid_manifest()

    registry.register(manifest)

    try:
        registry.register(manifest)
        assert False, "Expected duplicate node registration to fail"
    except NodeManifestAlreadyRegisteredError as exc:
        assert "already registered" in str(exc).lower()


def test_get_registered_manifest_by_name() -> None:
    """
    A registered manifest should be retrievable by name.
    """
    registry = NodeRegistry()
    manifest = make_valid_manifest(name="node-b")

    registry.register(manifest)
    stored = registry.get("node-b")

    assert stored["name"] == "node-b"
    assert stored["type"] == "node"
    assert "echo" in stored["skills"]


def test_get_missing_manifest_fails_clearly() -> None:
    """
    Looking up an unknown node name should fail clearly.
    """
    registry = NodeRegistry()

    try:
        registry.get("missing-node")
        assert False, "Expected missing node lookup to fail"
    except NodeManifestNotFoundError as exc:
        assert "missing-node" in str(exc)


def test_list_all_returns_registered_manifests() -> None:
    """
    Listing all manifests should return all registered entries.
    """
    registry = NodeRegistry()
    registry.register(make_valid_manifest(name="node-a"))
    registry.register(make_valid_manifest(name="node-b"))

    manifests = registry.list_all()
    names = {manifest["name"] for manifest in manifests}

    assert names == {"node-a", "node-b"}


def test_invalid_manifest_fails_validation() -> None:
    """
    Invalid manifests should fail before registration.
    """
    registry = NodeRegistry()
    manifest = make_valid_manifest()
    del manifest["description"]

    try:
        registry.register(manifest)
        assert False, "Expected invalid manifest registration to fail"
    except NodeManifestValidationError as exc:
        assert "description" in str(exc).lower()