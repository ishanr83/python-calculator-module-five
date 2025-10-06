from __future__ import annotations
from typing import Callable, List
from .operations import get_operation
from .history import History
from .calculator_memento import Caretaker

Observer = Callable[[str, float, float, float], None]

class Calculator:
    def __init__(self, history: History | None = None) -> None:
        self.history = History() if history is None else history
        self._observers: List[Observer] = []
        self._memento = Caretaker()

    # Observer
    def subscribe(self, fn: Observer) -> None:
        if fn not in self._observers:
            self._observers.append(fn)

    def _notify(self, op: str, a: float, b: float, result: float) -> None:
        for fn in list(self._observers):
            fn(op, a, b, result)

    # Facade operation
    def compute(self, op: str, a: float, b: float) -> float:
        self._memento.snapshot(self.history.to_df())
        strategy = get_operation(op)
        result = strategy.execute(a, b)
        self.history.add(op, a, b, result)
        self._notify(op, a, b, result)
        return result

    # Persistence
    def save(self, path: str) -> None:
        self.history.save_csv(path)

    def load(self, path: str) -> None:
        self.history = History.load_csv(path)

    # Undo/Redo
    def undo(self) -> bool:
        df = self._memento.undo()
        if df is None:
            return False
        self.history._df = df
        return True

    def redo(self) -> bool:
        df = self._memento.redo()
        if df is None:
            return False
        self.history._df = df
        return True

    def clear(self) -> None:
        self._memento.snapshot(self.history.to_df())
        self.history.clear()
