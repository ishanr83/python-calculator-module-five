from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Dict, Callable
from .exceptions import InvalidOperationError, DivisionByZeroError

class Operation(Protocol):
    def execute(self, a: float, b: float) -> float: ...

@dataclass(frozen=True)
class Add:
    def execute(self, a: float, b: float) -> float: return a + b

@dataclass(frozen=True)
class Sub:
    def execute(self, a: float, b: float) -> float: return a - b

@dataclass(frozen=True)
class Mul:
    def execute(self, a: float, b: float) -> float: return a * b

@dataclass(frozen=True)
class Div:
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Division by zero")
        return a / b

@dataclass(frozen=True)
class Pow:
    def execute(self, a: float, b: float) -> float: return a ** b

@dataclass(frozen=True)
class Root:
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise InvalidOperationError("Zero root not defined")
        return a ** (1.0 / b)

_FACTORY: Dict[str, Callable[[], Operation]] = {
    "add": Add,
    "sub": Sub,
    "mul": Mul,
    "div": Div,
    "pow": Pow,
    "root": Root,
}

def get_operation(name: str) -> Operation:
    key = name.lower()
    try:
        return _FACTORY[key]()
    except KeyError as e:
        raise InvalidOperationError(f"Unknown operation: {name}") from e
