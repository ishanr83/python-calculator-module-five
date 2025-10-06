from __future__ import annotations
import pandas as pd
from datetime import datetime
from typing import List, Dict

class History:
    COLUMNS = ["op", "a", "b", "result", "ts"]

    def __init__(self) -> None:
        self._df = pd.DataFrame(columns=self.COLUMNS)

    def add(self, op: str, a: float, b: float, result: float) -> None:
        row = {"op": op, "a": a, "b": b, "result": result, "ts": datetime.utcnow().isoformat()}
        self._df = pd.concat([self._df, pd.DataFrame([row])], ignore_index=True)

    def clear(self) -> None:
        self._df = pd.DataFrame(columns=self.COLUMNS)

    def to_df(self) -> pd.DataFrame:
        return self._df.copy()

    def __len__(self) -> int:
        return len(self._df)

    def save_csv(self, path: str) -> None:
        self._df.to_csv(path, index=False)

    @classmethod
    def load_csv(cls, path: str) -> "History":
        h = cls()
        try:
            df = pd.read_csv(path)
            missing = [c for c in cls.COLUMNS if c not in df.columns]
            if missing:
                raise ValueError(f"Bad history file, missing: {missing}")
            h._df = df
        except FileNotFoundError:
            h._df = pd.DataFrame(columns=cls.COLUMNS)
        return h
