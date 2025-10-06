import pytest
from app.input_validators import parse_two_numbers

def test_parse_happy():
    assert parse_two_numbers(["add","2","3"]) == (2.0, 3.0)

@pytest.mark.parametrize("parts", [[], ["add"], ["add","2"], ["add","x","y"]])
def test_parse_errors(parts):
    with pytest.raises(ValueError):
        parse_two_numbers(parts)
