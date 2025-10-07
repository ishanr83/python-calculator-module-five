# Author: Ishan Rehan
# Date: 10/6/2025

def parse_two_numbers(parts):
    if len(parts) != 3:
        raise ValueError("Usage: <op> <num1> <num2>")
    try:
        a = float(parts[1])
        b = float(parts[2])
    except ValueError as e:
        raise ValueError("Numbers must be numeric") from e
    return a, b
