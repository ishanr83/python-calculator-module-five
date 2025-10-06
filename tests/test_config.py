import os
from app.calculator_config import Config

def test_config_defaults(monkeypatch):
    for k in ("HISTORY_PATH","AUTO_SAVE","AUTO_LOAD"):
        monkeypatch.delenv(k, raising=False)
    c = Config.load()
    assert c.history_path == "history.csv"
    assert c.auto_save is False
    assert c.auto_load is True

def test_config_env(monkeypatch, tmp_path):
    monkeypatch.setenv("HISTORY_PATH", (tmp_path/"x.csv").as_posix())
    monkeypatch.setenv("AUTO_SAVE", "true")
    monkeypatch.setenv("AUTO_LOAD", "0")
    c = Config.load()
    assert c.auto_save is True
    assert c.auto_load is False
