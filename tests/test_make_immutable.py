# ruff: noqa: D100, D101, D102, D103, D104, D107

from immutable.main import Immutable, is_immutable, make_immutable


def test_make_immutable() -> None:
    A: type = make_immutable('B', [('x', int)])  # noqa: N806

    assert issubclass(A, Immutable)


def test_is_immutable() -> None:
    A: type = make_immutable('B', [('x', int)])  # noqa: N806

    assert is_immutable(A(x=1))


def test_equality() -> None:
    class A(Immutable):
        x: int

    B: type = make_immutable('B', [('x', int)])  # noqa: N806

    assert B(x=1) == B(x=1)
    assert B(x=1) != B(x=2)
    assert B(x=1) == A(x=1)
    assert B(x=1) != A(x=2)
    assert B(x=1) != A
