from typing import Callable
from .calculation import Calculator
from .history import History
from .input_validators import parse_two_numbers
from .exceptions import CalculatorError, ValidationError
from .calculator_config import load_config

PROMPT = "> "
BANNER = "Enhanced Calculator | Commands: add|sub|mul|div|pow|root <a> <b> | history | clear | undo | redo | save | load | help | exit"

class AutoSaver:
    def __init__(self, path: str): self.path = path
    def update(self, event: str, payload: dict) -> None:
        if event == "calculation": payload.get("history")  # placeholder

def run_repl(input_fn: Callable[[str], str] = input, output_fn: Callable[[str], None] = print) -> None:
    cfg = load_config()
    calc = Calculator(History.load_csv(cfg.history_path))
    if cfg.auto_save:
        class _Auto:
            def update(self, event, payload): calc.history.save_csv(cfg.history_path)
        calc.observers.append(_Auto())

    output_fn(BANNER)
    while True:
        try:
            line = input_fn(PROMPT).strip()
        except (EOFError, KeyboardInterrupt):
            output_fn("Bye!"); break
        if not line: output_fn("Type 'help' for usage."); continue

        cmd, *rest = line.split()
        if cmd.lower() in {"exit","quit","q"}: output_fn("Bye!"); break
        if cmd.lower() == "help":
            output_fn(BANNER); continue
        if cmd.lower() == "history":
            df = calc.history.to_frame()
            if df.empty: output_fn("No calculations yet.")
            else:
                for i,row in df.reset_index().iterrows():
                    output_fn(f"{i+1}. {row['op']}({row['a']}, {row['b']}) = {row['result']}")
            continue
        if cmd.lower() == "clear": calc.caretaker.push_undo(calc.snapshot()); calc.history.clear(); output_fn("Cleared."); continue
        if cmd.lower() == "undo": output_fn("Undone." if calc.undo() else "Nothing to undo."); continue
        if cmd.lower() == "redo": output_fn("Redone." if calc.redo() else "Nothing to redo."); continue
        if cmd.lower() == "save": calc.history.save_csv(cfg.history_path); output_fn("Saved."); continue
        if cmd.lower() == "load":
            from .history import History
            calc.caretaker.push_undo(calc.snapshot())
            calc.history = History.load_csv(cfg.history_path)
            output_fn("Loaded."); continue

        # Operation path (Strategy via factory)
        try:
            a,b = parse_two_numbers([cmd]+rest)
            result = calc.calculate(cmd, a, b)
            output_fn(f"Result: {result}")
        except CalculatorError as e:
            output_fn(f"Error: {e}")
