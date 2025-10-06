"""
Exception hierarchy for the calculator.

Tests import ValidationError from app.exceptions, so it must exist.
We also provide a few specific types used across the app.
"""

class CalculatorError(Exception):
    """Base error for calculator problems."""

class ValidationError(CalculatorError):
    """Bad or malformed user input (parsing, type, range)."""

class ConfigError(CalculatorError):
    """Configuration or environment related error."""

class OperationError(CalculatorError):
    """Operation lookup or execution failure."""

class DivisionByZeroError(OperationError):
    """Division by zero attempt."""
    
# Make star-imports and explicit imports predictable in tests
__all__ = [
    "CalculatorError",
    "ValidationError",
    "ConfigError",
    "OperationError",
    "DivisionByZeroError",
]
