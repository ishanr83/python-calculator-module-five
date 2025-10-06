from __future__ import annotations
from dataclasses import dataclass
import pandas as pd
from typing import List

@dataclass
class _Memento:
    df: pd.DataFrame

class Caretaker:
    def __init__(self) -> None:
        self._undo: List[_Memento] = []
        self._redo: List[_Memento] = []

    def snapshot(self, df: pd.DataFrame) -> None:
        self._undo.append(_Memento(df.copy()))
        self._redo.clear()

    def undo(self) -> pd.DataFrame | None:
        if not self._undo:
            return None
        m = self._undo.pop()
        self._redo.append(_Memento(m.df.copy()))
        return m.df.copy()

    def redo(self) -> pd.DataFrame | None:
        if not self._redo:
            return None
        m = self._redo.pop()
        self._undo.append(_Memento(m.df.copy()))
        return m.df.copy()
