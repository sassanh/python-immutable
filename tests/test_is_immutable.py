# ruff: noqa: D100, D101, D102, D103, D104, D107
from immutable import Immutable, immutable, is_immutable


def test_sub_classes() -> None:
    class A(Immutable):
        x: int

    assert is_immutable(A(x=1))


def test_decorator() -> None:
    @immutable
    class A:
        x: int

    assert is_immutable(A(x=1))


def test_negative() -> None:
    class A: ...

    assert not is_immutable(A)
