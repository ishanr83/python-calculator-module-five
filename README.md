# Enhanced Python Calculator (Module 5)

**Author:** Ishan Rehan  
**Date:** 2025-09-29

- REPL: `add|sub|mul|div|pow|root <a> <b>`; `history`, `help`, `clear`, `undo`, `redo`, `save`, `load`, `exit`
- Patterns: Strategy + Factory (operations), Facade (Calculator), Observer (auto-save), Memento (undo/redo)
- pandas history saved/loaded from CSV
- Config via `.env` or environment (`HISTORY_PATH`, `AUTO_SAVE`, `AUTO_LOAD`)
- CI: GitHub Actions fails if coverage < 100%

## Run
```bash
python - <<'PY'
from app.calculator_repl import run_repl
run_repl()
PY
