from app.exceptions import DivisionByZeroError, InvalidOperationError

def test_exceptions_exist():
    e1 = DivisionByZeroError()
    e2 = InvalidOperationError("test")
    assert str(e2) == "test"
