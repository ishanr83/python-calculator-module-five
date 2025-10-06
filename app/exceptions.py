class CalculatorError(Exception):
    """Base error for calculator problems."""

class ValidationError(CalculatorError):
    """Bad or malformed user input."""

class ConfigError(CalculatorError):
    """Configuration/env error."""

class OperationError(CalculatorError):
    """Base for operation issues."""

class InvalidOperationError(OperationError):
    """Unknown or unsupported operation."""

class DivisionByZeroError(OperationError):
    """Division by zero attempt."""

class HistoryError(CalculatorError):
    """History storage/IO errors."""
    
__all__ = [
    "CalculatorError",
    "ValidationError",
    "ConfigError",
    "OperationError",
    "InvalidOperationError",
    "DivisionByZeroError",
    "HistoryError",
]

class InvalidOperationError(Exception):
    pass
