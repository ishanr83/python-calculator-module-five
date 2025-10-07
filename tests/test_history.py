import pandas as pd
from app.history import History

def test_history_init_empty():
    h = History()
    assert len(h) == 0
    assert list(h.to_df().columns) == ["operation", "operand1", "operand2", "result"]

def test_history_add():
    h = History()
    h.add("add", 2, 3, 5)
    assert len(h) == 1
    df = h.to_df()
    assert df.iloc[0]["operation"] == "add"
    assert df.iloc[0]["result"] == 5

def test_history_clear():
    h = History()
    h.add("add", 1, 1, 2)
    h.clear()
    assert len(h) == 0

def test_history_save_load(tmp_path):
    h = History()
    h.add("mul", 2, 3, 6)
    path = tmp_path / "history.csv"
    h.save_csv(path)

    h2 = History.load_csv(path)
    assert len(h2) == 1
    assert h2.to_df().iloc[0]["result"] == 6

def test_history_load_missing_file(tmp_path):
    path = tmp_path / "missing.csv"
    h = History.load_csv(path)
    assert len(h) == 0
