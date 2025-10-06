# Enhanced Python Calculator (Module 5)

**Author:** Ishan Rehan  
**Date:** 2025-10-xx

A modular command-line calculator using Strategy, Factory, Memento, Observer, and a Facade-style Calculator API. History is stored in a pandas DataFrame and auto-saved to CSV. Tests run locally and in GitHub Actions with a 100% coverage gate.

## Run
```bash
python -m venv .venv
# Windows Git Bash
source .venv/Scripts/activate
pip install -r requirements.txt
export PYTHONPATH=.
python -c "from app.calculator_repl import run_repl; run_repl()"

