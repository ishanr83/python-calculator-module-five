from dataclasses import dataclass, field
from typing import Protocol, Any
from .operations import operation_factory
from .history import History
from .calculator_memento import Memento, Caretaker

class Observer(Protocol):
    def update(self, event: str, payload: dict[str, Any]) -> None: ...

@dataclass
class Calculator:
    history: History
    observers: list[Observer] = field(default_factory=list)
    caretaker: Caretaker = field(default_factory=Caretaker)

    def notify(self, event: str, payload: dict[str, Any]) -> None:
        for obs in self.observers: obs.update(event, payload)

    # Memento helpers
    def snapshot(self) -> Memento: return Memento(self.history.to_frame())
    def restore(self, m: Memento | None) -> None:
        if m is None: return
        from .history import History
        self.history = History(m.df)

    def calculate(self, op: str, a: float, b: float) -> float:
        # Save state for undo, clear redo stack
        self.caretaker.push_undo(self.snapshot()); self.caretaker.clear_redo()
        func = operation_factory(op)
        result = func(a, b)
        self.history.add(op, a, b, result)
        self.notify("calculation", {"op":op,"a":a,"b":b,"result":result})
        return result

    def undo(self) -> bool:
        m = self.caretaker.pop_undo()
        if not m: return False
        self.caretaker.push_redo(self.snapshot())
        self.restore(m)
        self.notify("undo", {})
        return True

    def redo(self) -> bool:
        m = self.caretaker.pop_redo()
        if not m: return False
        self.caretaker.push_undo(self.snapshot())
        self.restore(m)
        self.notify("redo", {})
        return True
