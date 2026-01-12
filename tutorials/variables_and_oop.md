# Python Variables and OOP — Quick Guide

This short guide shows Python variable basics and a recommended Object-Oriented
approach for learners. Use the paired runnable example at
`examples/variables_and_oop.py` to experiment.

## Variables — core ideas
- Names: use `snake_case` for variables (e.g., `user_name`).
- Dynamic typing: a variable holds a reference; its type can change.
- Common types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`.
- Mutable vs immutable: `list`/`dict` are mutable; `str`/`tuple`/`int` are immutable.
- Scope: local (inside function), global (module-level). Prefer passing values rather than using globals.
- Type hints: use `name: str = "Alice"` to document types.

Example patterns:

- Multiple assignment: `a, b = 1, 2`
- Unpacking: `x, *rest = [1,2,3]`
- Constants (convention): `MAX_RETRIES = 3`

## When to use OOP
- Use functions for small tasks and utilities.
- Use classes when you need to group state + behavior into logical units (domain models, services with state).
- Prefer composition over deep inheritance for clarity.

Recommended OOP topics to learn (demonstrated in example file):
- Class definition and `__init__` (constructor)
- Instance attributes vs class attributes
- Methods (behavior) and `self`
- Encapsulation: single leading underscore `_private` (convention), properties for managed access
- Inheritance and method overriding
- `__repr__` / `__str__` for readable debugging output

## Which is better — simple variables/functions or OOP?
- For tiny scripts and one-off tasks: simple variables + functions are simpler and clearer.
- For domain logic that groups data and operations (e.g., `Student`, `Invoice`), OOP gives structure and testability.
- Start with functions. When you notice grouped state and repeated behavior, refactor into classes.

## Learning path / exercises
1. Experiment with the `examples/variables_and_oop.py` file: change values, run it.
2. Convert a pair of related functions that share state into a class.
3. Add unit tests (use `pytest`) for methods on the class.

If you want, I can:
- add inline exercises and test stubs, or
- convert one of your existing modules into a small OOP-based refactor and show diff.
