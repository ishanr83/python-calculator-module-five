import pytest
from app.operations import get_operation
from app.exceptions import DivisionByZeroError, InvalidOperationError

@pytest.mark.parametrize("op,a,b,expected", [
    ("add", 2, 3, 5),
    ("sub", 5, 2, 3),
    ("mul", 3, 4, 12),
    ("div", 8, 2, 4),
    ("pow", 2, 3, 8),
    ("root", 9, 2, 3),
])
def test_strategies(op, a, b, expected):
    assert get_operation(op).execute(a,b) == pytest.approx(expected)

def test_div_zero():
    with pytest.raises(DivisionByZeroError):
        get_operation("div").execute(1,0)

def test_invalid_op():
    with pytest.raises(InvalidOperationError):
        get_operation("nope")
