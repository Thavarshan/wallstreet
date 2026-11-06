# How to learn with Wallstreet

Welcome, Jerome. You already know how applications fit together; here you will build the same instincts in Python, one small feature at a time.

## Your working rhythm

1. **Read** the issue and highlight unfamiliar words. The [glossary](GLOSSARY.md) is there for you.
2. **Predict** what your code should do, using the issue's example input/output.
3. **Write one tiny function** or class. Don't try to finish the entire issue in one attempt.
4. **Run it manually** with a harmless sample (not a live brokerage account).
5. **Write a test** for a normal case and an error case.
6. **Refactor** only when the tests pass. Give variables and functions clear names.
7. **Commit** your work and describe in your own words what you learned.

An AI assistant is allowed to explain a traceback, ask guiding questions, review your proposed solution, or show a separate toy example. Try asking:

> I'm learning Python. Please **do not implement the issue for me**. Explain the concepts and give me the smallest hint needed. Review my code after I try.

## Small translation guide for a JavaScript/PHP developer

| Familiar concept | Python example |
| --- | --- |
| JavaScript array / PHP list | `symbols = ["AAPL", "MSFT"]` |
| JS object / associative array | `quote = {"symbol": "AAPL", "close": 100.0}` |
| Loop through array | `for symbol in symbols:` |
| Function | `def normalize_symbol(value: str) -> str:` |
| No value | `None` |
| Truthiness | `if quotes:` |
| Run a module | `python -m wallstreet` |
| Python unit tests | `pytest` |

Python indentation is syntax. Four spaces inside a function or loop is conventional. Prefer a readable loop over a clever one-liner when learning.

## What to do when stuck

- Read the *last line* of the traceback first, then the highlighted file/line.
- Print or inspect a small variable rather than the whole dataset.
- Isolate the failing case in a test.
- Look at the official Python documentation for `pathlib`, `datetime`, `sqlite3`, or the relevant module.
- Ask what assumption was wrong. Do not blindly paste a suggested replacement.

## Definition of done

Every issue has its own checklist. In general, you are finished when:

- The example works locally.
- The automated tests pass.
- The code handles the specific bad-input case mentioned in the issue.
- No secret, personal detail, or copyrighted full-text article was committed.
- You can explain **why** your solution works, in two or three sentences.

## Safety boundary

The lessons create local data, tests, research signals, backtests, and simulated orders. They do **not** instruct you to trade with real capital. There is a separate, later review for broker feasibility and account authorization.
