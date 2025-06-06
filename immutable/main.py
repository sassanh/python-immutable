# ruff: noqa: A003, D100, D101, D102, D103, D104, D105, D107
from __future__ import annotations

import sys
from dataclasses import dataclass, make_dataclass, replace
from typing import TYPE_CHECKING, Any, TypeVar, cast

from typing_extensions import Self, TypeGuard, dataclass_transform

if TYPE_CHECKING:
    from collections.abc import Iterable

    from _typeshed import DataclassInstance

_T = TypeVar('_T')

# These values should be written explicitly in the dataclass for pyright to recognize
# them.
dataclass_decorator = (
    dataclass(frozen=True, eq=False, unsafe_hash=True, kw_only=True)
    if sys.version_info >= (3, 10)
    else dataclass(frozen=True, eq=False, unsafe_hash=True)
)


@dataclass_transform(kw_only_default=True, frozen_default=True, eq_default=False)
def immutable(cls: type[_T]) -> type[_T]:
    return dataclass_decorator(cls)


@dataclass_transform(kw_only_default=True, frozen_default=True)
@dataclass_decorator
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

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Immutable):
            return NotImplemented
        return tuple(self.__dict__.values()) == tuple(other.__dict__.values())

    def __call__(self, **kwrags: object) -> Self:
        return cast('Self', replace(cast('DataclassInstance', self), **kwrags))


class _Immutable(Immutable):
    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(_immutable_applied=True, **kwargs)


dataclass_kwargs = {
    'frozen': True,
    'eq': False,
    'unsafe_hash': True,
    **({'kw_only': True} if sys.version_info >= (3, 10) else {}),
}


def is_immutable(obj: object) -> TypeGuard[Immutable]:
    return (
        hasattr(obj, '__dataclass_fields__')
        and hasattr(obj, '__dataclass_params__')
        and all(
            getattr(getattr(obj, '__dataclass_params__', None), key, None)
            is dataclass_kwargs[key]
            for key in dataclass_kwargs
            if (sys.version_info >= (3, 12) or key != 'kw_only')
        )
    )


@dataclass_transform(kw_only_default=True, frozen_default=True)
def make_immutable(
    cls_name: str,
    fields: Iterable[str | tuple[str, Any] | tuple[str, Any, Any]],
) -> type:
    return make_dataclass(
        cls_name,
        fields,
        bases=(_Immutable,),
        **dataclass_kwargs,  # pyright: ignore[reportArgumentType]
    )
