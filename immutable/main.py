# ruff: noqa: A003, D100, D101, D102, D103, D104, D105, D107
from __future__ import annotations

import sys
from dataclasses import dataclass, make_dataclass
from typing import Any, Iterable, TypeGuard, TypeVar

from typing_extensions import dataclass_transform

_T = TypeVar('_T')


@dataclass_transform(kw_only_default=True, frozen_default=True)
def immutable(cls: type[_T]) -> type[_T]:
    if sys.version_info < (3, 10):
        return dataclass(frozen=True)(cls)  # pragma: no cover
    return dataclass(frozen=True, kw_only=True, eq=False, unsafe_hash=True)(cls)


@dataclass_transform(kw_only_default=True, frozen_default=True)
class Immutable:
    def __init_subclass__(
        cls: type[Immutable],
        *,
        _immutable_applied: bool = False,
        **kwargs: object,
    ) -> None:
        super().__init_subclass__(**kwargs)
        if not _immutable_applied:
            immutable(cls)

    def __eq__(self: Immutable, other: object) -> bool:
        if not isinstance(other, Immutable):
            return NotImplemented
        return tuple(self.__dict__.values()) == tuple(other.__dict__.values())


class _Immutable(Immutable):
    def __init_subclass__(
        cls: type[_Immutable],
        **kwargs: object,
    ) -> None:
        super().__init_subclass__(_immutable_applied=True, **kwargs)


def is_immutable(obj: object) -> TypeGuard[Immutable]:
    return (
        hasattr(obj, '__dataclass_fields__')
        and hasattr(obj, '__dataclass_params__')
        and getattr(getattr(obj, '__dataclass_params__', None), 'frozen', False)
    )


@dataclass_transform(kw_only_default=True, frozen_default=True)
def make_immutable(
    cls_name: str,
    fields: Iterable[str | tuple[str, Any] | tuple[str, Any, Any]],
) -> type:
    return make_dataclass(
        cls_name,
        fields,
        frozen=True,
        kw_only=True,
        bases=(_Immutable,),
    )
