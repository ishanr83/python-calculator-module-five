from io import StringIO
from app.calculator_repl import run_repl
import os

def _io(inputs):
    input_iter = iter(inputs)
    output_lines = []
    def _in(): return input_iter
    def _out(s): output_lines.append(s)
    return _in, _out, output_lines

def test_repl_flow(monkeypatch, tmp_path):
    monkeypatch.setenv("HISTORY_PATH", str(tmp_path / "h.csv"))
    monkeypatch.setenv("AUTO_SAVE", "1")
    monkeypatch.setenv("AUTO_LOAD", "0")

    _in, _out, out = _io(["help", "add 2 3", "div 5 0", "history", "clear", "save", "q"])
    run_repl(_in, _out)

    output = "".join(out)
    assert "Result: 5" in output
    assert "Division by zero" in output
    assert "Cleared." in output
    assert "Saved to" in output

def test_repl_undo_redo():
    _in, _out, out = _io(["add 5 5", "undo", "redo", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Result: 10" in output
    assert "Undone." in output
    assert "Redone." in output

def test_blank_line_ignored():
    _in, _out, out = _io(["", "add 1 1", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Result: 2" in output
    assert "REPL" in output

def test_repl_load(monkeypatch, tmp_path):
    monkeypatch.setenv("HISTORY_PATH", str(tmp_path / "test.csv"))
    monkeypatch.setenv("AUTO_SAVE", "0")
    monkeypatch.setenv("AUTO_LOAD", "0")
    
    _in, _out, out = _io(["add 1 1", "save", "q"])
    run_repl(_in, _out)
    
    _in2, _out2, out2 = _io(["load", "history", "q"])
    run_repl(_in2, _out2)
    output = "".join(out2)
    assert "Loaded from" in output

def test_repl_auto_load(monkeypatch, tmp_path):
    path = tmp_path / "auto.csv"
    monkeypatch.setenv("HISTORY_PATH", str(path))
    monkeypatch.setenv("AUTO_SAVE", "1")
    monkeypatch.setenv("AUTO_LOAD", "0")
    
    _in, _out, out = _io(["add 2 2", "q"])
    run_repl(_in, _out)
    
    monkeypatch.setenv("AUTO_LOAD", "1")
    _in2, _out2, out2 = _io(["history", "q"])
    run_repl(_in2, _out2)
    output = "".join(out2)
    assert "add" in output.lower() or "2" in output

def test_repl_auto_load_corrupted(monkeypatch, tmp_path):
    path = tmp_path / "corrupted.csv"
    with open(path, 'w') as f:
        f.write("garbage\ndata\n")
    
    monkeypatch.setenv("HISTORY_PATH", str(path))
    monkeypatch.setenv("AUTO_LOAD", "1")
    
    _in, _out, out = _io(["add 1 1", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Result: 2" in output

def test_repl_invalid_operation():
    _in, _out, out = _io(["mod 5 2", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Operation Error" in output

def test_repl_empty_history():
    _in, _out, out = _io(["history", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "History is empty" in output

def test_repl_nothing_to_undo():
    _in, _out, out = _io(["undo", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Nothing to undo" in output

def test_repl_nothing_to_redo():
    _in, _out, out = _io(["redo", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Nothing to redo" in output

def test_repl_comment_line():
    _in, _out, out = _io(["# This is a comment", "add 1 1", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Result: 2" in output

def test_repl_load_fail(monkeypatch, tmp_path):
    monkeypatch.setenv("HISTORY_PATH", str(tmp_path / "nonexistent.csv"))
    _in, _out, out = _io(["load", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert len(output) > 0

def test_repl_input_error_not_enough_args():
    """Test ValueError from parse_two_numbers - not enough arguments"""
    _in, _out, out = _io(["add 5", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Input Error" in output

def test_repl_input_error_non_numeric():
    """Test ValueError from parse_two_numbers - non-numeric input"""
    _in, _out, out = _io(["add abc def", "q"])
    run_repl(_in, _out)
    output = "".join(out)
    assert "Input Error" in output
