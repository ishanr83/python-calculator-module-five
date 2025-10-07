from .exceptions import DivisionByZeroError, InvalidOperationError

class Add:
    def execute(self, a, b): return a + b

class Subtract:
    def execute(self, a, b): return a - b

class Multiply:
    def execute(self, a, b): return a * b

class Divide:
    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError()
        return a / b

class Power:
    def execute(self, a, b): return a ** b

class Root:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Root degree cannot be zero")  # pragma: no cover
        return a ** (1.0 / b)

_OPERATIONS = {
    "add": Add(),
    "sub": Subtract(),
    "mul": Multiply(),
    "div": Divide(),
    "pow": Power(),
    "root": Root(),
}

def get_operation(name):
    if name not in _OPERATIONS:
        raise InvalidOperationError(f"Unknown operation: {name}")
    return _OPERATIONS[name]
