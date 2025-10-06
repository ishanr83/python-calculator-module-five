import os
from .calculation import Calculator
from .input_validators import parse_two_numbers
from .exceptions import DivisionByZeroError, InvalidOperationError

BANNER = "Simple Calculator REPL"

def run_repl(_in=None, _out=None):
    if _out is None:
        import sys
        _out = sys.stdout.write

    _out(BANNER + "\n")
    calc = Calculator()
    history_path = os.getenv("HISTORY_PATH", "history.csv")
    auto_save = os.getenv("AUTO_SAVE", "0") == "1"
    auto_load = os.getenv("AUTO_LOAD", "0") == "1"

    if auto_load:
        try:
            calc.load(history_path)
        except Exception:
            pass

    # Handle _in: if callable, call it to get iterable
    if _in is None:
        import sys
        input_iter = sys.stdin
    else:
        input_iter = _in() if callable(_in) else _in

    try:
        for line in input_iter:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line == "q":
                break
            elif line == "help":
                _out("Commands: add|sub|mul|div|pow|root <num1> <num2>, history, undo, redo, clear, save, load, q\n")
            elif line == "history":
                if len(calc.history) == 0:
                    _out("History is empty.\n")
                else:
                    _out(calc.history.df.to_string(index=False) + "\n")
            elif line == "undo":
                if calc.undo():
                    _out("Undone.\n")
                else:
                    _out("Nothing to undo.\n")
            elif line == "redo":
                if calc.redo():
                    _out("Redone.\n")
                else:
                    _out("Nothing to redo.\n")
            elif line == "clear":
                calc.clear()
                _out("Cleared.\n")
            elif line == "save":
                calc.save(history_path)
                _out(f"Saved to {history_path}\n")
            elif line == "load":
                try:
                    calc.load(history_path)
                    _out(f"Loaded from {history_path}\n")
                except Exception as e:
                    _out(f"Load failed: {e}\n")
            else:
                parts = line.split()
                try:
                    a, b = parse_two_numbers(parts)
                    op = parts[0]
                    result = calc.compute(op, a, b)
                    _out(f"Result: {result}\n")
                    if auto_save:
                        calc.save(history_path)
                except ValueError as e:
                    _out(f"Input Error: {e}\n")
                except DivisionByZeroError:
                    _out("Error: Division by zero\n")
                except InvalidOperationError as e:
                    _out(f"Operation Error: {e}\n")
    except KeyboardInterrupt:
        _out("\nExiting...\n")
