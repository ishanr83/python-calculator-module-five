# Author: Ishan Rehan
# Date: 10/6/2025

import pandas as pd

class History:
    def __init__(self, df=None):
        if df is None:
            df = pd.DataFrame(columns=["operation", "operand1", "operand2", "result"])
        self.df = df.copy()

    def __len__(self):
        return len(self.df)

    def add(self, op, a, b, result):
        new_row = pd.DataFrame([{
            "operation": op,
            "operand1": float(a),
            "operand2": float(b),
            "result": float(result)
        }], columns=["operation", "operand1", "operand2", "result"])
        self.df = pd.concat([self.df, new_row], ignore_index=True)

    def clear(self):
        self.df = pd.DataFrame(columns=self.df.columns)

    def to_df(self):
        return self.df.copy()

    def save_csv(self, path):
        self.df.to_csv(path, index=False)

    @classmethod
    def load_csv(cls, path):
        try:
            df = pd.read_csv(path)
            expected = ["operation", "operand1", "operand2", "result"]
            if not all(col in df.columns for col in expected):
                df = pd.DataFrame(columns=expected)
            return cls(df)
        except (FileNotFoundError, pd.errors.EmptyDataError):
            return cls()
