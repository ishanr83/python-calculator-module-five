from typing import Callable, Dict
from .exceptions import InvalidOperationError, DivisionByZeroError

def _add(a: float, b: float) -> float: return a + b
def _sub(a: float, b: float) -> float: return a - b
def _mul(a: float, b: float) -> float: return a * b
def _div(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("division by zero")
    return a / b
def _pow(a: float, b: float) -> float: return a ** b
def _root(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("root with zero exponent")
    return a ** (1.0 / b)

_OPS: Dict[str, Callable[[float, float], float]] = {
    "add": _add, "sub": _sub, "mul": _mul, "div": _div, "pow": _pow, "root": _root,
}

def get_operation(name: str) -> Callable[[float, float], float]:
    func = _OPS.get(name.lower())
    if func is None:
        raise InvalidOperationError(f"unknown operation: {name}")
    return func

def execute(name: str, a: float, b: float) -> float:
    return get_operation(name)(a, b)

__all__ = ["get_operation", "execute"]
