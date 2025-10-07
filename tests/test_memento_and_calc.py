from app.calculation import Calculator

def test_calc_compute():
    calc = Calculator()
    result = calc.compute("add", 2, 3)
    assert result == 5
    assert len(calc.history) == 1

def test_undo_redo():
    calc = Calculator()
    calc.compute("add", 2, 3)  # history: [add]
    assert len(calc.history) == 1

    # Undo - restores to empty state before first compute
    assert calc.undo() is True
    assert len(calc.history) == 0

    # Redo - restores the state with 1 entry
    assert calc.redo() is True
    assert len(calc.history) == 1
    
    # Undo again
    calc.undo()
    assert len(calc.history) == 0
    
    # New compute clears redo stack
    calc.compute("mul", 2, 4)
    assert len(calc.history) == 1
    assert calc.redo() is False  # redo stack cleared

def test_calc_save_load(tmp_path):
    calc = Calculator()
    calc.compute("sub", 10, 4)
    path = tmp_path / "calc_hist.csv"
    calc.save(path)

    calc2 = Calculator()
    calc2.load(path)
    assert len(calc2.history) == 1
    assert calc2.history.to_df().iloc[0]["result"] == 6

def test_clear():
    calc = Calculator()
    calc.compute("add", 1, 1)
    calc.clear()
    assert len(calc.history) == 0
