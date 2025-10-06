from app.calculation import Calculator

def test_calc_compute_undo_redo_and_save_load(tmp_path):
    calc = Calculator()
    r = calc.compute("add", 2, 3)
    assert r == 5
    assert len(calc.history) == 1

    # undo
    assert calc.undo() is True
    assert len(calc.history) == 0
    # redo
    assert calc.redo() is True
    assert len(calc.history) == 0  # redo returns to last snapshot; then compute again
    calc.compute("mul", 2, 4)
    assert len(calc.history) == 1

    # save/load
    p = tmp_path/"hist.csv"
    calc.save(p.as_posix())
    calc.clear()
    assert len(calc.history) == 0
    calc.load(p.as_posix())
    assert len(calc.history) == 1
