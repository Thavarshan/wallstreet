# 02 — Build a tiny command-line interface with Python arguments

**Phase:** A · Python foundations  
**Estimated learning time:** 2–3 hours  
**Prerequisite:** Finish issue 01 first.

## Why we're doing this

You need an easy, reproducible way to run collectors and reports both locally and later inside GitHub Actions. A command-line program is simpler to build and test than a website.

## What you'll learn

- Functions, `if` statements, `return`, strings, lists, and command-line arguments
- `argparse` in the Python standard library
- Separating parsing from business logic

## Files to inspect or create

- `src/wallstreet/__main__.py`
- `src/wallstreet/cli.py` (new)
- `tests/test_cli.py` (new)

## Build it yourself — step by step

1. Read the `argparse` tutorial. Create a `main()` function that constructs an argument parser with a useful description.
2. Add subcommands `hello`, `status`, and `help` (or use argparse's built-in help). Keep them non-financial for now.
3. Make `python -m wallstreet hello --name Jerome` print a friendly greeting, and `python -m wallstreet status` print `research mode; no live trading`.
4. Move the greeting into a small pure function returning a string. The CLI should print the returned value; this makes testing easier.
5. Handle a missing name with a sensible default. Verify that unknown commands exit with a helpful usage message rather than a cryptic traceback.
6. Write tests for the pure greeting function and the CLI output. Explore pytest's `capsys` or call the program via `subprocess`.
7. Document the new commands in the README with copy-pasteable examples.

## Concrete example

`python -m wallstreet hello --name Jerome` → `Hello, Jerome!` and `python -m wallstreet status` → `Wallstreet mode: research (no real orders)`.

## Tests to write

- [ ] A provided name appears exactly once in the greeting.
- [ ] Omitting the optional name still works.
- [ ] Invalid command prints usage or an error and returns a non-zero exit status.

## Acceptance checklist

- [ ] I can explain the difference between a function returning text and the CLI printing it.
- [ ] All commands have help text and tests.
- [ ] No broker API or network dependency has been introduced.

## Common pitfall

Avoid putting everything inside one long `if` block. Keep parsing, input validation, and output formatting in small functions.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

