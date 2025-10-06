from __future__ import annotations
import os
import pandas as pd
from dataclasses import dataclass
from typing import Optional
from .exceptions import HistoryError

COLUMNS = ["op", "a", "b", "result", "ts"]

@dataclass
class History:
    df: pd.DataFrame

    @classmethod
    def empty(cls) -> "History":
        return cls(pd.DataFrame(columns=COLUMNS))

    @classmethod
    def load_csv(cls, path: str) -> "History":
        try:
            if not path or not os.path.exists(path):
                return cls.empty()
            df = pd.read_csv(path)
            missing = [c for c in COLUMNS if c not in df.columns]
            if missing:
                # normalize columns if someone edited the csv
                for c in missing: df[c] = None
                df = df[COLUMNS]
            return cls(df)
        except Exception as e:
            raise HistoryError(f"load_csv failed: {e}") from e

    def save_csv(self, path: str) -> None:
        try:
            self.df.to_csv(path, index=False)
        except Exception as e:
            raise HistoryError(f"save_csv failed: {e}") from e

    def add(self, op: str, a: float, b: float, result: float, ts: Optional[str] = None) -> None:
        row = {"op": op, "a": a, "b": b, "result": result, "ts": ts or pd.Timestamp.utcnow().isoformat()}
        self.df.loc[len(self.df)] = row

    def clear(self) -> None:
        self.df = self.df.iloc[0:0].copy()

    def snapshot(self) -> pd.DataFrame:
        return self.df.copy(deep=True)

    def restore(self, snapshot: pd.DataFrame) -> None:
        self.df = snapshot.copy(deep=True)

    def to_df(self) -> pd.DataFrame:
        return self.df
