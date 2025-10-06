from app.calculator_repl import run_repl, BANNER

def io(seq):
    it = iter(seq); out=[]
    def _in(_): return next(it)
    def _out(s): out.append(s)
    return _in,_out,out

def test_repl_flow(tmp_path, monkeypatch):
    monkeypatch.setenv("HISTORY_PATH", (tmp_path/"h.csv").as_posix())
    monkeypatch.setenv("AUTO_SAVE","true")
    _in,_out,out = io(["help","add 2 3","div 5 0","history","undo","history","redo","save","load","q"])
    run_repl(_in,_out)
    assert out[0] == BANNER
    assert any("Result: 5" in s for s in out)
    assert any("Error: Division by zero" in s for s in out)
    assert any("No calculations yet." in s for s in out) or any(". add(" in s for s in out)
    assert out[-1] == "Bye!"
