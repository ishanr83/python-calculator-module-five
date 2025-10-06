from app.calculator_repl import run_repl, BANNER

def _io(lines):
    it = iter(lines)
    outs = []
    def _in(_):
        return next(it)
    def _out(s):
        outs.append(s)
    return _in, _out, outs

def test_repl_flow(tmp_path, monkeypatch):
    monkeypatch.setenv("HISTORY_PATH", (tmp_path/"h.csv").as_posix())
    monkeypatch.setenv("AUTO_SAVE", "1")
    monkeypatch.setenv("AUTO_LOAD", "0")

    _in,_out,out = _io(["help","add 2 3","div 5 0","history","undo","redo","save","load","clear","q"])
    run_repl(_in, _out)

    assert BANNER in out[0]
    assert any("Result: 5" in s for s in out)
    assert any("Error: Division by zero" in s for s in out)
    assert any("Cleared." in s for s in out)
    assert out[-1] == "Bye!"

def test_blank_line_goes_to_help(monkeypatch):
    monkeypatch.setenv("AUTO_LOAD","0")
    _in,_out,out = _io(["","q"])
    run_repl(_in,_out)
    assert any("Type 'help' for usage." in s for s in out)
