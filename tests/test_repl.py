from io import StringIO
from app.calculator_repl import run_repl

def _io(inputs):
    input_iter = iter(inputs)
    output_lines = []
    def _in(): return input_iter
    def _out(s): output_lines.append(s)
    return _in, _out, output_lines

def test_repl_flow(monkeypatch, tmp_path):
    monkeypatch.setenv("HISTORY_PATH", str(tmp_path / "h.csv"))
    monkeypatch.setenv("AUTO_SAVE", "0")
    monkeypatch.setenv("AUTO_LOAD", "0")

    _in, _out, out = _io(["add 2 3", "div 5 0", "history", "clear", "q"])
    run_repl(_in, _out)

    output = "".join(out)
    assert "Result: 5" in output
    assert "Division by zero" in output
    assert "Cleared." in output

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
    assert "REPL" in output  # banner printed
