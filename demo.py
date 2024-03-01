# ruff: noqa: A003, D100, D101, D102, D103, D104, D105, D107
from dataclasses import FrozenInstanceError

from immutable import Immutable
from immutable.main import immutable


class InheritedClass(Immutable):
    field: int


@immutable
class DecoratedClass:
    field: int


def main() -> None:
    first_instance = InheritedClass(field=1)
    try:
        first_instance.field = 2  # pyright: ignore [reportAttributeAccessIssue]
        raise AssertionError
    except FrozenInstanceError as error:
        assert isinstance(error, FrozenInstanceError)  # noqa: S101, PT017

    second_instance = DecoratedClass(field=1)
    try:
        second_instance.field = 2  # pyright: ignore [reportAttributeAccessIssue]
        raise AssertionError
    except FrozenInstanceError as error:
        assert isinstance(error, FrozenInstanceError)  # noqa: S101, PT017
