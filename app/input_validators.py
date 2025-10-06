from .exceptions import ValidationError

def parse_two_numbers(parts: list[str]) -> tuple[float, float]:
    if len(parts) != 3:
        raise ValidationError("Usage: <op> <num1> <num2>")
    try:
        a = float(parts[1])
        b = float(parts[2])
    except ValueError as e:
        raise ValidationError("Numbers must be numeric") from e
    return a, b
