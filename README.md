< Author: Ishan Rehan -->
< Date: 10/6/2025 -->

```markdown
# Enhanced Python Calculator (Module 5)

Author: Ishan Rehan  
Date: 2025-10-06  

A professional-grade modular calculator built in Python, featuring advanced OOP design patterns, persistent history via pandas, and automated CI testing with 100 percent coverage enforcement on GitHub Actions.

-------------------------------------------------------------------------------

## Overview

This calculator demonstrates advanced software engineering concepts:
- REPL Interface for continuous user interaction (add|sub|mul|div|pow|root <a> <b>, plus commands like help, history, undo, redo, save, load, and exit).
- Design Patterns:  
  Strategy (operations)  
  Factory (operation creation)  
  Memento (undo/redo)  
  Observer (auto-saving history)  
  Facade (unified calculator interface)
- Data Management: Uses pandas to manage and persist history (history.csv).
- Configuration: Uses dotenv and environment variables for flexible settings (HISTORY_PATH, AUTO_SAVE, AUTO_LOAD).
- Error Handling: Demonstrates both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission) paradigms.
- CI/CD: GitHub Actions enforces 100 percent coverage and runs automated pytest checks on every commit.

-------------------------------------------------------------------------------

## Project Structure

python-calculator-module-five/
├── app/
│   ├── calculator_repl.py          # REPL main entry
│   ├── calculation.py              # Facade and Observer integration
│   ├── calculator_config.py        # dotenv configuration
│   ├── calculator_memento.py       # undo and redo via Memento pattern
│   ├── exceptions.py               # custom error classes
│   ├── history.py                  # pandas-based persistent history
│   ├── input_validators.py         # LBYL parsing and validation
│   └── operations.py               # Factory and Strategy patterns
├── tests/                          # pytest and parameterized tests (100 percent coverage)
├── .github/workflows/python-app.yml# GitHub Actions CI config
├── pytest.ini                      # pytest config (coverage enforcement)
└── requirements.txt                # dependencies

-------------------------------------------------------------------------------

## Setup and Run

Setup:
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt

Run the Calculator:
python - <<'PY'
from app.calculator_repl import run_repl
run_repl()
PY

Example interaction:
> add 2 3
Result: 5
> div 5 0
Error: Division by zero
> history
1. add(2, 3) = 5
> undo
Undone.
> redo
Redone.
> exit
Bye!

-------------------------------------------------------------------------------

## Testing and Coverage

Run all tests locally:
python -m pytest

-------------------------------------------------------------------------------

## Continuous Integration (GitHub Actions)

Every push automatically runs tests and enforces 100 percent coverage.  
If coverage drops, the build fails.

Workflow file: .github/workflows/python-app.yml

Key steps:
1. Checkout repo  
2. Set up Python 3.x  
3. Install dependencies (pytest, pytest-cov, pandas, python-dotenv)  
4. Run all tests with coverage enforcement
