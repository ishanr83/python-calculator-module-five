import pandas as pd

class Memento:
    def __init__(self, state: pd.DataFrame):
        self.state = state

class CareTaker:
    def __init__(self):
        self._undos = []
        self._redos = []

    def save(self, memento: Memento):
        self._undos.append(memento)
        self._redos.clear()

    def undo(self) -> Memento | None:
        if self._undos:
            memento = self._undos.pop()
            self._redos.append(memento)
            return memento
        return None

    def redo(self) -> Memento | None:
        if self._redos:
            memento = self._redos.pop()
            self._undos.append(memento)
            return memento
        return None
