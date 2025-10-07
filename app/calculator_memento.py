from .history import History

class CalculatorMemento:
    def __init__(self, history_df):
        self.history_df = history_df.copy()

class CalculatorCareTaker:
    def __init__(self):
        self._undos = []
        self._redos = []

    def save_for_undo(self, history_df):
        self._undos.append(CalculatorMemento(history_df))
        self._redos.clear()

    def undo(self, calc):
        if not self._undos:
            return False
        current = CalculatorMemento(calc.history.df)
        prev = self._undos.pop()
        calc.history = History(prev.history_df.copy())
        self._redos.append(current)
        return True

    def redo(self, calc):
        if not self._redos:
            return False
        current = CalculatorMemento(calc.history.df)
        redo_state = self._redos.pop()
        calc.history = History(redo_state.history_df.copy())
        self._undos.append(current)
        return True
