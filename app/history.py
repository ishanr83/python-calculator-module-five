import pandas as pd
from datetime import datetime

_COLUMNS = ["op","a","b","result","ts"]

class History:
    def __init__(self, df: pd.DataFrame | None = None) -> None:
        self._df = df.copy() if df is not None else pd.DataFrame(columns=_COLUMNS)

    def add(self, op: str, a: float, b: float, result: float) -> None:
        row = {"op":op, "a":a, "b":b, "result":result, "ts": datetime.utcnow().isoformat()}
        self._df = pd.concat([self._df, pd.DataFrame([row])], ignore_index=True)

    def clear(self) -> None: self._df = self._df.iloc[0:0].copy()
    def to_frame(self) -> pd.DataFrame: return self._df.copy()

    # persistence
    def save_csv(self, path: str) -> None: self._df.to_csv(path, index=False)
    @classmethod
    def load_csv(cls, path: str) -> "History":
        try: df = pd.read_csv(path)
        except FileNotFoundError: df = pd.DataFrame(columns=_COLUMNS)
        return cls(df)
