from .history import History
from .operations import get_operation
from .calculator_memento import CareTaker, Memento

class Calculator:
    def __init__(self):
        self.history = History()
        self.caretaker = CareTaker()

    def compute(self, op: str, a: float, b: float) -> float:
        self.caretaker.save(Memento(self.history.df.copy()))
        operation = get_operation(op)
        result = operation.execute(a, b)
        self.history.add(op, a, b, result)
        return result

    def undo(self) -> bool:
        memento = self.caretaker.undo()
        if memento is not None:
            self.history = History(memento.state)
            return True
        return False

    def redo(self) -> bool:
        memento = self.caretaker.redo()
        if memento is not None:
            self.history = History(memento.state)
            return True
        return False

    def save(self, path: str):
        self.history.save_csv(path)

    def load(self, path: str):
        self.history = self.history.load_csv(path)

    def clear(self):
        self.history.clear()
