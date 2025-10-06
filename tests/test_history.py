import pandas as pd
from app.history import History

def test_add_clear_save_load(tmp_path):
    h = History()
    h.add("add", 2, 3, 5)
    assert len(h) == 1
    p = tmp_path/"h.csv"
    h.save_csv(p.as_posix())

    h2 = History.load_csv(p.as_posix())
    df = h2.to_df()
    assert len(df) == 1
    assert df.iloc[0]["result"] == 5

    h2.clear()
    assert len(h2) == 0

def test_load_missing_file(tmp_path):
    p = tmp_path/"missing.csv"
    h = History.load_csv(p.as_posix())
    assert len(h) == 0
