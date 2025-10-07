# Author: Ishan Rehan
# Date: 10/6/2025

import pytest
from app.operations import get_operation, Add, Subtract, Multiply, Divide, Power, Root
from app.exceptions import DivisionByZeroError, InvalidOperationError

@pytest.mark.parametrize("op,a,b,expected", [
    ("add", 2, 3, 5),
    ("sub", 5, 2, 3),
    ("mul", 3, 4, 12),
    ("div", 8, 2, 4),
    ("pow", 2, 3, 8),
    ("root", 9, 2, 3),
])
def test_operations_execute(op, a, b, expected):
    operation = get_operation(op)
    assert operation.execute(a, b) == pytest.approx(expected)

def test_div_zero():
    with pytest.raises(DivisionByZeroError):
        get_operation("div").execute(1, 0)

def test_invalid_operation():
    with pytest.raises(InvalidOperationError, match="Unknown operation"):
        get_operation("mod")

def test_root_zero():
    with pytest.raises(ValueError, match="Root degree cannot be zero"):
        get_operation("root").execute(4, 0)
