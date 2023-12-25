# ruff: noqa: A003, D100, D101, D102, D103, D104, D105, D107
from __future__ import annotations

from dataclasses import dataclass
from typing import (
    Any,
    Mapping,
    TypeVar,
    dataclass_transform,
)

_T = TypeVar("_T")


@dataclass_transform(kw_only_default=True, frozen_default=True)
def immutable(cls: type[_T]) -> type[_T]:
    return dataclass(frozen=True, kw_only=True)(cls)


@dataclass_transform(kw_only_default=True, frozen_default=True)
class Immutable:
    def __init_subclass__(
        cls: type[Immutable],
        **kwargs: Mapping[str, Any],
    ) -> None:
        super().__init_subclass__(**kwargs)
        immutable(cls)
