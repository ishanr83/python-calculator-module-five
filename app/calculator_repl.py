from __future__ import annotations
from typing import Callable
import os
from .calculation import Calculator
from .history import History
from .exceptions import DivisionByZeroError, InvalidOperationError

BANNER = "Calculator REPL. Commands: add|sub|mul|div|pow|root <a> <b> | history | help | clear | undo | redo | save | load | exit"

def run_repl(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
) -> None:
    hist_path = os.getenv("HISTORY_PATH", "history.csv")
    auto_load = os.getenv("AUTO_LOAD", "false").lower() in {"1", "true", "yes"}
    auto_save = os.getenv("AUTO_SAVE", "false").lower() in {"1", "true", "yes"}

    calc = Calculator(History.load_csv(hist_path) if auto_load else History.empty())
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

        parts = line.split()
        cmd = parts[0].lower()

        if cmd in {"q", "quit", "exit"}:
            output_fn("Bye!")
            break

        if cmd == "help":
            output_fn(BANNER)
            continue

        if cmd == "history":
            df = calc.history.to_df()
            if df.empty:
                output_fn("No calculations yet.")
            else:
                for _, r in df.iterrows():
                    output_fn(f"{r['op']}({r['a']}, {r['b']}) = {r['result']}")
            continue

        if cmd == "clear":
            calc.history.clear()
            output_fn("History cleared.")
            continue

        if cmd == "undo":
            calc.undo(); output_fn("OK"); continue
        if cmd == "redo":
            calc.redo(); output_fn("OK"); continue
        if cmd == "save":
            calc.history.save_csv(hist_path); output_fn("Saved."); continue
        if cmd == "load":
            calc.history = History.load_csv(hist_path); output_fn("Loaded."); continue

        if cmd in {"add", "sub", "mul", "div", "pow", "root"}:
            if len(parts) != 3:
                output_fn("Usage: <op> <a> <b>")
                continue
            try:
                a = float(parts[1]); b = float(parts[2])
            except ValueError:
                output_fn("Error: numbers must be numeric")
                continue
            try:
                result = calc.compute(cmd, a, b)
                output_fn(f"Result: {result}")
                if auto_save:
                    calc.history.save_csv(hist_path)
            except DivisionByZeroError:
                output_fn("Error: Division by zero")
            except InvalidOperationError as e:
                output_fn(f"Error: {e}")
            continue

        output_fn("Unknown command. Type 'help'.")
