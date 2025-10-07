from .history import History
from .operations import get_operation
from .calculator_memento import CalculatorCareTaker, CalculatorMemento

class Calculator:
    def __init__(self):
        self.history = History()
        self.caretaker = CalculatorCareTaker()

    def compute(self, op, a, b):
        self.caretaker.save(CalculatorMemento(self.history.df))
        operation = get_operation(op)
        result = operation.execute(a, b)
        self.history.add(op, a, b, result)
        return result

    def undo(self):
        memento = self.caretaker.undo()
        if memento is not None:
            self.history = History(memento.history_df)
            return True
        return False

    def redo(self):
        memento = self.caretaker.redo()
        if memento is not None:
            self.history = History(memento.history_df)
            return True
        return False

    def save(self, path):
        self.history.save_csv(path)

    def load(self, path):
        self.history = History.load_csv(path)

    def clear(self):
        self.history.clear()
