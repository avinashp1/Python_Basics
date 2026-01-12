"""Advanced runnable examples for intermediate/experienced learners.

Run: python examples/advanced_examples.py

Each section prints a short demonstration you can tinker with.
"""

from dataclasses import dataclass
from typing import Protocol, Iterable, List, Iterator, runtime_checkable
from contextlib import contextmanager
from functools import wraps
import asyncio
import logging

logging.basicConfig(level=logging.INFO)


# -----------------------
# Dataclass example
# -----------------------

@dataclass(frozen=True)
class Invoice:
    id: str
    amount: float


def dataclass_demo():
    print("-- Dataclass (frozen) --")
    inv = Invoice("I100", 199.99)
    print(inv)
    try:
        # frozen dataclass prevents attribute assignment
        inv.amount = 1.0
    except Exception as e:
        print("immutable test ->", type(e).__name__)
    print()


# -----------------------
# Protocol / structural typing
# -----------------------

@runtime_checkable
class HasName(Protocol):
    name: str


class Named:
    def __init__(self, name: str):
        self.name = name


def protocol_demo(obj: HasName):
    print("-- Protocol demo --")
    print(f"Hello, {obj.name}")
    print(isinstance(obj, HasName))
    print()


# -----------------------
# Context manager example
# -----------------------

@contextmanager
def open_and_log(path: str, mode: str = "r"):
    logging.info("Opening %s", path)
    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()
        logging.info("Closed %s", path)


def context_demo():
    print("-- Context manager demo --")
    # write a temp file then read it via context manager
    tmp = "tmp_demo.txt"
    with open(tmp, "w", encoding="utf-8") as w:
        w.write("hello\n")
    with open_and_log(tmp) as r:
        print(r.read().strip())
    print()


# -----------------------
# Decorator example
# -----------------------

def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        import time

        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            end = time.perf_counter()
            logging.info("%s took %.6fs", fn.__name__, end - start)

    return wrapper


@timeit
def compute(n: int) -> int:
    s = 0
    for i in range(n):
        s += i
    return s


# -----------------------
# Generator / iterator
# -----------------------

def chunked(iterable: Iterable, size: int) -> Iterator[List]:
    it = iter(iterable)
    while True:
        chunk = []
        try:
            for _ in range(size):
                chunk.append(next(it))
        except StopIteration:
            if chunk:
                yield chunk
            break
        yield chunk


def generator_demo():
    print("-- Generator demo --")
    for c in chunked(range(10), 3):
        print(c)
    print()


# -----------------------
# Async example
# -----------------------

async def say_after(delay: float, what: str):
    await asyncio.sleep(delay)
    print(what)


async def async_demo():
    print("-- Async demo --")
    await asyncio.gather(say_after(0.2, "first"), say_after(0.1, "second"))
    print()


# -----------------------
# Small in-memory repository pattern
# -----------------------

class StudentRepo:
    def __init__(self):
        self._items = {}

    def add(self, id: str, obj):
        self._items[id] = obj

    def get(self, id: str):
        return self._items.get(id)

    def list(self):
        return list(self._items.values())


def repo_demo():
    print("-- In-memory repo demo --")
    repo = StudentRepo()
    repo.add("s1", {"name": "A"})
    repo.add("s2", {"name": "B"})
    print(repo.list())
    print()


if __name__ == "__main__":
    dataclass_demo()
    protocol_demo(Named("Zoe"))
    context_demo()
    print("-- Decorator / timing --")
    compute(100000)
    print()
    generator_demo()
    asyncio.run(async_demo())
    repo_demo()
