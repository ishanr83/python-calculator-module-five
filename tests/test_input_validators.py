import pytest
from app.input_validators import parse_two_numbers

@pytest.mark.parametrize("parts", [
    [],
    ["add"],
    ["add", "2"],
    ["add", "a", "3"]
])
def test_parse_errors(parts):
    with pytest.raises(ValueError):
        parse_two_numbers(parts)

def test_parse_valid():
    a, b = parse_two_numbers(["add", "2.5", "3"])
    assert a == 2.5
    assert b == 3.0
