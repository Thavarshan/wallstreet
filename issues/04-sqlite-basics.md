# 04 — Store market records in SQLite with unique keys

**Phase:** B · Trusted datasets  
**Estimated learning time:** 3–5 hours  
**Prerequisite:** Finish issue 03 first.

## Why we're doing this

A data collector is useless if it loses history or silently duplicates records. SQLite gives you persistent, queryable storage with no cloud account or monthly fee.

## What you'll learn

- Tables, primary keys, unique constraints, SQL parameters, transactions
- Python's built-in `sqlite3` module
- Repository functions that hide SQL from analysis code

## Files to inspect or create

- `src/wallstreet/storage.py` (new)
- `src/wallstreet/schema.sql` (new)
- `tests/test_storage.py` (new)

## Build it yourself — step by step

1. Sketch a `price_bars` table with `symbol`, `trading_date`, OHLCV, `source`, `collected_at`, and `published_at` (if available). Choose a unique key for one source/symbol/date combination.
2. Write `CREATE TABLE IF NOT EXISTS` SQL and a Python function that opens the configured database path. Do not store the DB itself in Git.
3. Insert a `PriceBar` from issue 03 using SQL parameter placeholders (`?`), never string interpolation for values.
4. Implement a function to list bars for one symbol between two dates in chronological order.
5. Insert the same record twice. Decide whether to keep the original or explicitly update it; document the policy and make the operation idempotent.
6. Use `sqlite3.Row` or another clear mechanism to convert database output back to a typed model.
7. Test against an in-memory or temporary database so the tests never depend on your personal data.
8. Add a small CLI command to show how many stored bars exist.

## Concrete example

Saving `AAPL / 2026-01-05` twice should leave exactly one row for the chosen source. Querying from 2026-01-01 to 2026-01-31 returns it once.

## Tests to write

- [ ] Database initialization can run twice safely.
- [ ] Insert then query reproduces symbol, date, and values.
- [ ] Duplicate inserts do not create duplicate rows.
- [ ] A SQL-looking symbol string is handled as data, not executed.
- [ ] A fresh temporary database starts empty.

## Acceptance checklist

- [ ] I can explain a unique constraint and an idempotent operation.
- [ ] No `.sqlite` database appears in `git status`.
- [ ] All storage tests pass without internet access.

## Common pitfall

Never save prices as numbers without documenting precision. SQLite isn't a substitute for validating the input model first.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

