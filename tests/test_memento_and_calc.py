from app.calculation import Calculator
from app.history import History

def test_calc_undo_redo():
    c = Calculator(History())
    c.calculate("add", 2, 3)
    assert not c.history.to_frame().empty
    assert c.undo() is True
    assert c.history.to_frame().empty
    assert c.redo() is True
    assert not c.history.to_frame().empty
