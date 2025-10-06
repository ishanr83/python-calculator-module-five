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
            raise DivisionByZeroError("Division by zero")
        return a / b

class Power:
    def execute(self, a, b): return a ** b

class Root:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Root degree cannot be zero")
        if a < 0 and b % 2 == 0:
            raise ValueError("Cannot compute even root of negative number")
        return a ** (1 / b)

_OPERATIONS = {
    "add": Add(),
    "sub": Subtract(),
    "mul": Multiply(),
    "div": Divide(),
    "pow": Power(),
    "root": Root(),
}

def get_operation(name: str):
    if name not in _OPERATIONS:
        raise InvalidOperationError(f"Unknown operation: {name}")
    return _OPERATIONS[name]
