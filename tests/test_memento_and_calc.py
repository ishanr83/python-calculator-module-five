# Author: Ishan Rehan
# Date: 10/6/2025

from app.calculation import Calculator
from app.calculator_memento import CalculatorCareTaker, CalculatorMemento
import pandas as pd

def test_calc_compute():
    calc = Calculator()
    result = calc.compute("add", 2, 3)
    assert result == 5
    assert len(calc.history) == 1

def test_undo_redo():
    calc = Calculator()
    calc.compute("add", 2, 3)
    assert len(calc.history) == 1

    assert calc.undo() is True
    assert len(calc.history) == 0

    assert calc.redo() is True
    assert len(calc.history) == 1
    
    calc.undo()
    assert len(calc.history) == 0
    
    calc.compute("mul", 2, 4)
    assert len(calc.history) == 1
    assert calc.redo() is False

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

def test_memento_direct():
    df = pd.DataFrame([{"operation": "add", "operand1": 1, "operand2": 2, "result": 3}])
    memento = CalculatorMemento(df)
    assert len(memento.history_df) == 1
    # Test that it's a deep copy
    df.iloc[0, 0] = "sub"
    assert memento.history_df.iloc[0]["operation"] == "add"
