# Changelog

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
