from __future__ import annotations
from typing import List
from .operations import execute
from .history import History
from .exceptions import InvalidOperationError, DivisionByZeroError

class Calculator:
    def __init__(self, history: History | None = None):
        self.history = history or History.empty()
        self._undo_stack: List = []
        self._redo_stack: List = []

    def compute(self, op: str, a: float, b: float) -> float:
        # Snapshot for undo before mutating history
        self._undo_stack.append(self.history.snapshot())
        self._redo_stack.clear()
        result = execute(op, a, b)
        self.history.add(op, a, b, result)
        return result

    def undo(self) -> None:
        if not self._undo_stack:
            return
        self._redo_stack.append(self.history.snapshot())
        self.history.restore(self._undo_stack.pop())

    def redo(self) -> None:
        if not self._redo_stack:
            return
        self._undo_stack.append(self.history.snapshot())
        self.history.restore(self._redo_stack.pop())
