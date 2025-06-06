# ruff: noqa: D100, D101, D102, D103, D104, D107
from immutable import Immutable, immutable


def test_subclasses_with_same_order_of_fields() -> None:
    class A(Immutable):
        x: int
        y: int

    class B(Immutable):
        x: int
        y: int

    a = A(x=1, y=2)
    b = B(x=1, y=2)

    assert a == b

    a = A(x=2, y=2)
    b = B(x=1, y=2)

    assert a != b

    a = A(y=2, x=1)
    b = B(x=1, y=2)

    assert a == b


def test_nested_subclasses() -> None:
    class C(Immutable):
        z: int

    class D(Immutable):
        z: int

    class A(Immutable):
        x: int
        y: C

    class B(Immutable):
        x: int
        y: D

    a = A(x=1, y=C(z=3))
    b = B(x=1, y=D(z=3))

    assert a == b

    a = A(x=1, y=C(z=3))
    b = B(x=1, y=D(z=2))

    assert a != b


def test_subclasses_with_different_order_of_fields() -> None:
    class A(Immutable):
        x: int
        y: int

    class B(Immutable):
        y: int
        x: int

    a = A(x=1, y=2)
    b = B(x=1, y=2)

    assert a != b


def test_decorator() -> None:
    @immutable
    class A:
        x: int
        y: int

    @immutable
    class B:
        x: int
        y: int

    a = A(x=1, y=2)
    b = B(x=1, y=2)

    assert a != b


def test_with_other_types() -> None:
    class A(Immutable):
        x: int

    class B:
        x: int

    b_instance = B()
    b_instance.x = 1

    assert A(x=1) != b_instance
