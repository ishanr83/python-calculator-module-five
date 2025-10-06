from typing import Protocol, Dict, Callable
from math import sqrt
from .exceptions import DivisionByZeroError, ValidationError

class OperationStrategy(Protocol):
    def __call__(self, a: float, b: float) -> float: ...

def _add(a: float, b: float) -> float: return a + b
def _sub(a: float, b: float) -> float: return a - b
def _mul(a: float, b: float) -> float: return a * b
def _div(a: float, b: float) -> float:
    if b == 0: raise DivisionByZeroError("Division by zero")
    return a / b
def _pow(a: float, b: float) -> float: return a ** b
def _root(a: float, b: float) -> float:
    if b == 0: raise ValidationError("Root power cannot be zero")
    return a ** (1.0 / b)

_OPS: Dict[str, OperationStrategy] = {
    "add": _add, "sub": _sub, "mul": _mul, "div": _div, "pow": _pow, "root": _root,
}

def operation_factory(name: str) -> OperationStrategy:
    key = name.lower()
    if key not in _OPS: raise ValidationError(f"Unknown operation: {name}")
    return _OPS[key]

def operations_map() -> Dict[str, Callable[[float, float], float]]:
    return dict(_OPS)
