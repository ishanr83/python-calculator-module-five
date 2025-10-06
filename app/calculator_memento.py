from dataclasses import dataclass
import pandas as pd

@dataclass(frozen=True)
class Memento:
    df: pd.DataFrame

class Caretaker:
    def __init__(self) -> None:
        self._undo: list[Memento] = []
        self._redo: list[Memento] = []

    def push_undo(self, m: Memento) -> None: self._undo.append(m)
    def pop_undo(self) -> Memento | None: return self._undo.pop() if self._undo else None
    def push_redo(self, m: Memento) -> None: self._redo.append(m)
    def pop_redo(self) -> Memento | None: return self._redo.pop() if self._redo else None
    def clear_redo(self) -> None: self._redo.clear()
