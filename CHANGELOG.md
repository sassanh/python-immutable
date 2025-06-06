# Changelog

## Version 1.2.2

- refactor: make it play nicer with pyright's `reportUnhashable`
- chore: update setup-uv version in github actions to v6 to support `python-version` parameter

## Version 1.2.0

- chore: replace poetry with uv, make sure python3.9+ is supported and add tests for all supported python versions in github actions
- feat: add `__call__` method to `Immutable` class to allow replacing attributes with new values, basically a shorthand for `dataclasses.replace`

## Version 1.1.1

- fix: mark `Immutable` class as a dataclass to avoid `TypeError` when using `dataclasses.replace`,
  `dataclasses.fields`, etc.

## Version 1.1.0

- feat: instanced of subclasses of `Immutable` are now considered equal if they
  have the same attributes, in the same order, with the same values
- refactor: the return value of `make_immutable` now passes `issubclass(cls, Immutable)`
  check and has `__eq__` of `Immutable`
- test: add tests

## Version 1.0.6

- feat: add `make_immutable` to be on par with `make_dataclass`

## Version 1.0.5

- feat: add `is_immutable` to check whether an object is an instance of `Immutable`

## Version 1.0.4

- fix: support Python 3.9

## Version 1.0.3

- chore: add github actions for linting and type checking

## Version 1.0.2

- docs: improve `README.md`

## Version 1.0.1

- docs: add installation instructions for poetry in `README.md`

## Version 1.0.0

- feat: implement `Immutable` class and `immutable` class decorator
- docs: add `README.md`
- chore: initialize the repository
