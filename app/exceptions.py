class CalculatorError(Exception):
    """Base error for calculator problems."""

class InvalidOperationError(CalculatorError):
    """Raised when an unsupported operation is requested."""

class DivisionByZeroError(CalculatorError):
    """Raised on division by zero."""
