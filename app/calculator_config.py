import os
from dataclasses import dataclass
from dotenv import load_dotenv
from .exceptions import ConfigError

@dataclass(frozen=True)
class AppConfig:
    history_path: str
    auto_save: bool

def load_config() -> AppConfig:
    load_dotenv()
    path = os.getenv("HISTORY_PATH", "history.csv").strip() or "history.csv"
    auto = os.getenv("AUTO_SAVE", "true").lower() in {"1","true","yes","y"}
    if not path.endswith(".csv"):
        raise ConfigError("HISTORY_PATH must end with .csv")
    return AppConfig(history_path=path, auto_save=auto)
