"""Tests for the hashability of Immutable instances."""

from immutable import Immutable


def test_is_hashable() -> None:
    """Test that Immutable instances are hashable."""

    class A(Immutable):
        x: int = 0

    some_hash = hash(A())
    some_set = {A(), A(x=2)}
    assert A() in some_set
    assert A(x=2) in some_set
    assert hash(A()) == some_hash
    assert any(hash(instance) == some_hash for instance in some_set)
