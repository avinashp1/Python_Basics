# Advanced Python Examples — Overview

This document accompanies `examples/advanced_examples.py` and highlights
practical patterns useful for intermediate/experienced Python developers.

Topics included (see runnable file for code and small experiments):

- Dataclasses: concise domain models with type hints and immutability via `frozen=True`.
- Protocols & typing: structural typing with `typing.Protocol` and generic type examples.
- Context managers: `contextlib.contextmanager` and custom `__enter__/__exit__` for resource management.
- Decorators: function and class decorators (wrapping functions, preserving metadata with `functools.wraps`).
- Generators & iterators: streaming data with generators and using `itertools`.
- Async basics: `async def` + `asyncio` example for simple concurrency.
- Patterns: small in-memory repository (composition), simple dependency injection via constructor args, and logging usage.

How to use

1. Run the examples file and tweak small blocks to see behavior:

```powershell
python examples/advanced_examples.py
```

2. For tests, extract pure functions and classes and write `pytest` tests under `tests/`.

3. When refactoring: prefer small, focused examples from this file to guide production code.

If you want any topic expanded into a dedicated module, test suite, or an exercise, tell me which one.
