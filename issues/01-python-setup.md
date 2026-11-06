# 01 — Set up Python, a virtual environment, and your first passing test

**Phase:** A · Python foundations  
**Estimated learning time:** 45–90 minutes  
**Prerequisite:** None

## Why we're doing this

Before asking the computer to analyze a market, you need a repeatable way to run Python code. A virtual environment keeps this project's packages separate from the rest of your Mac. Tests will later protect your calculations from accidental changes.

## What you'll learn

- `python` versus `python3`, packages, modules, virtual environments, and the terminal
- Why `python -m ...` runs a Python module and why `pytest` finds files named `test_*.py`
- How to interpret an error message instead of immediately changing code

## Files to inspect or create

- `README.md` (read)
- `src/wallstreet/__main__.py` (read)
- `tests/test_starter.py` (read)

## Build it yourself — step by step

1. Install Python 3.12+ and check the interpreter with `python3 --version`. If your machine has multiple versions, write down which one runs in the project.
2. Clone the repository, navigate into it, and run `python3 -m venv .venv`. Activate it with `source .venv/bin/activate` on macOS/Linux.
3. Explain to yourself why `.venv/` belongs in `.gitignore`. Run `python -m pip install -e '.[dev]'` and identify what `-e` means in the packaging documentation.
4. Run `python -m wallstreet`, then `python -m pytest -q`. Find the welcome message and a green passing test.
5. Open `test_starter.py`, change the expected version to a clearly wrong value temporarily, rerun tests, and study the assertion failure. Undo that temporary change.
6. Make a tiny documentation improvement describing your environment and commit it. Do not commit `.venv`.

## Concrete example

Expected terminal output includes `Welcome to Wallstreet. Start with GitHub Issue 01!` and `1 passed` from pytest. Exact formatting may vary.

## Tests to write

- [ ] The starter test passes on your machine.
- [ ] You can deliberately make the test fail and restore it.
- [ ] `git status` does not list `.venv` files.

## Acceptance checklist

- [ ] I can explain what a virtual environment does.
- [ ] I can run the package and tests without copying commands blindly.
- [ ] I committed only my own small documentation change.

## Common pitfall

If `python -m wallstreet` says `No module named wallstreet`, check the active environment and whether the editable install succeeded. Do not install random similarly named packages.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

