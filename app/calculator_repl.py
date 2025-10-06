from __future__ import annotations
from typing import Callable
from .calculation import Calculator
from .calculator_config import Config
from .input_validators import parse_two_numbers
from .exceptions import CalculatorError

BANNER = "Commands: add|sub|mul|div|pow|root <a> <b> | history | help | clear | undo | redo | save | load | exit"

def _print_history(calc: Calculator, out: Callable[[str], None]) -> None:
    df = calc.history.to_df()
    if df.empty:
        out("No history.")
    else:
        for i, r in df.iterrows():
            out(f"{i+1}. {r['op']}({r['a']}, {r['b']}) = {r['result']}")

def run_repl(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print
) -> None:
    cfg = Config.load()
    calc = Calculator()
    if cfg.auto_load:
        calc.load(cfg.history_path)

    def logger(op: str, a: float, b: float, result: float) -> None:
        if cfg.auto_save:
            calc.save(cfg.history_path)

    calc.subscribe(logger)

    output_fn(BANNER)
    while True:
        try:
            line = input_fn("> ").strip()
        except (EOFError, KeyboardInterrupt):
            output_fn("Bye!")
            break

        if not line:
            output_fn("Type 'help' for usage.")
            continue

        cmd = line.split()[0].lower()

        if cmd in {"exit", "quit", "q"}:
            output_fn("Bye!")
            break
        if cmd == "help":
            output_fn(BANNER); continue
        if cmd == "history":
            _print_history(calc, output_fn); continue
        if cmd == "clear":
            calc.clear(); output_fn("Cleared."); continue
        if cmd == "undo":
            output_fn("Undone." if calc.undo() else "Nothing to undo."); continue
        if cmd == "redo":
            output_fn("Redone." if calc.redo() else "Nothing to redo."); continue
        if cmd == "save":
            calc.save(cfg.history_path); output_fn("Saved."); continue
        if cmd == "load":
            calc.load(cfg.history_path); output_fn("Loaded."); continue

        # operations
        try:
            a, b = parse_two_numbers(line.split())
            result = calc.compute(cmd, a, b)
            output_fn(f"Result: {result}")
        except ValueError as e:
            output_fn(f"Error: {e}")
        except CalculatorError as e:
            output_fn(f"Error: {e}")
