import pytest
from app.input_validators import parse_two_numbers
from app.exceptions import ValidationError

def test_parse_happy():
    assert parse_two_numbers(["add","2","3"]) == (2.0, 3.0)

@pytest.mark.parametrize("parts", [[],["add"],["add","2"],["add","a","3"]])
def test_parse_errors(parts):
    with pytest.raises(ValidationError):
        parse_two_numbers(parts)
