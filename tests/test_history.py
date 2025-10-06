import os, pandas as pd
from app.history import History

def test_add_clear_save_load(tmp_path):
    h = History()
    h.add("add", 2, 3, 5)
    assert not h.to_frame().empty
    p = tmp_path/"hist.csv"
    h.save_csv(p.as_posix())
    h2 = History.load_csv(p.as_posix())
    df = h2.to_frame()
    assert df.iloc[0]["result"] == 5
    h2.clear()
    assert h2.to_frame().empty
