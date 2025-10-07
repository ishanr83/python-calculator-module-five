class CalculatorMemento:
    def __init__(self, history_df):
        self.history_df = history_df.copy()

class CalculatorCareTaker:
    def __init__(self):
        self._undos = []
        self._redos = []

    def save(self, memento):
        self._undos.append(memento)
        self._redos.clear()

    def undo(self):
        if self._undos:
            memento = self._undos.pop()
            self._redos.append(memento)
            return memento
        return None

    def redo(self):
        if self._redos:
            memento = self._redos.pop()
            self._undos.append(memento)
            return memento
        return None
