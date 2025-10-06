import math, pytest
from app.operations import operation_factory, operations_map
from app.exceptions import DivisionByZeroError, ValidationError

@pytest.mark.parametrize("name,a,b,expected", [
    ("add",2,3,5), ("sub",2,3,-1), ("mul",2,3,6),
    ("div",6,3,2), ("pow",2,3,8), ("root",9,2,3),
])
def test_ops(name,a,b,expected):
    f = operation_factory(name)
    assert math.isclose(f(a,b), expected)

def test_div_zero():
    with pytest.raises(DivisionByZeroError): operation_factory("div")(1,0)

def test_root_zero_power():
    with pytest.raises(ValidationError): operation_factory("root")(9,0)

def test_unknown_op():
    with pytest.raises(ValidationError): operation_factory("nope")
    
def test_operations_map_copy():
    ops = operations_map(); assert "add" in ops and callable(ops["add"])
    ops["add"] = None
    assert operations_map()["add"] is not None
