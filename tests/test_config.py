import os, pytest
from app.calculator_config import load_config
from app.exceptions import ConfigError

def test_defaults(tmp_path, monkeypatch):
    monkeypatch.delenv("HISTORY_PATH", raising=False)
    monkeypatch.delenv("AUTO_SAVE", raising=False)
    cfg = load_config()
    assert cfg.history_path.endswith(".csv") and cfg.auto_save is True

def test_invalid_path(monkeypatch):
    monkeypatch.setenv("HISTORY_PATH", "bad.txt")
    with pytest.raises(ConfigError):
        load_config()
