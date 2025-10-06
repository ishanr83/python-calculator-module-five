from __future__ import annotations
import os
from dataclasses import dataclass
from dotenv import load_dotenv

def _to_bool(v: str | None, default: bool) -> bool:
    if v is None:
        return default
    return v.strip().lower() in {"1", "true", "yes", "y", "on"}

@dataclass(frozen=True)
class Config:
    history_path: str
    auto_save: bool
    auto_load: bool

    @classmethod
    def load(cls) -> "Config":
        load_dotenv(override=False)
        path = os.getenv("HISTORY_PATH", "history.csv")
        autosave = _to_bool(os.getenv("AUTO_SAVE"), False)
        autoload = _to_bool(os.getenv("AUTO_LOAD"), True)
        return cls(history_path=path, auto_save=autosave, auto_load=autoload)
