# ruff: noqa: A003, D100, D101, D102, D103, D104, D105, D107
from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Any, Mapping, TypeGuard, TypeVar

from typing_extensions import dataclass_transform

_T = TypeVar('_T')


@dataclass_transform(kw_only_default=True, frozen_default=True)
def immutable(cls: type[_T]) -> type[_T]:
    if sys.version_info < (3, 10):
        return dataclass(frozen=True)(cls)
    return dataclass(frozen=True, kw_only=True)(cls)


@dataclass_transform(kw_only_default=True, frozen_default=True)
@immutable
class Immutable:
    def __init_subclass__(
        cls: type[Immutable],
        **kwargs: Mapping[str, Any],
    ) -> None:
        super().__init_subclass__(**kwargs)
        immutable(cls)


def is_immutable(obj: object) -> TypeGuard[Immutable]:
    return (
        hasattr(obj, '__dataclass_fields__')
        and hasattr(obj, '__dataclass_params__')
        and getattr(getattr(obj, '__dataclass_params__', None), 'frozen', False)
    )
