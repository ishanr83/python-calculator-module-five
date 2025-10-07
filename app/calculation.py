# Author: Ishan Rehan
# Date: 10/6/2025

from .history import History
from .operations import get_operation
from .calculator_memento import CalculatorCareTaker

class Calculator:
    def __init__(self):
        self.history = History()
        self.caretaker = CalculatorCareTaker()

    def compute(self, op, a, b):
        self.caretaker.save_for_undo(self.history.df)
        operation = get_operation(op)
        result = operation.execute(a, b)
        self.history.add(op, a, b, result)
        return result

    def undo(self):
        return self.caretaker.undo(self)

    def redo(self):
        return self.caretaker.redo(self)

    def save(self, path):
        self.history.save_csv(path)

    def load(self, path):
        self.history = History.load_csv(path)

    def clear(self):
        self.history.clear()
