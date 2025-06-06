# ruff: noqa: D100, D101, D102, D103, D104, D107
from typing import Callable

from immutable import Immutable


def test_replace_with_call() -> None:
    class A(Immutable):
        x: int
        y: int

    instance = A(x=1, y=2)

    assert isinstance(instance, Callable)
    assert isinstance(instance(), A)
    assert instance().x == 1
    assert instance().y == 2
    assert instance(x=3).x == 3
    assert instance(y=5).y == 5
    assert instance(x=3, y=5).y == 5
    assert instance(x=3, y=5) == A(x=3, y=5)
