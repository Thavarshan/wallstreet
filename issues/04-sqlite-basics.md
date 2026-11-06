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

1. Sketch a `price_bars` table with `symbol`, `trading_date` (for display), OHLCV, `source`, `collected_at`, and `published_at` (if available). Start simple, then add the hourly identity below **before** integrating the API in issue 06.
2. Write `CREATE TABLE IF NOT EXISTS` SQL and a Python function that opens the configured database path. Do not store the DB itself in Git.
3. Insert a `PriceBar` from issue 03 using SQL parameter placeholders (`?`), never string interpolation for values.
4. Implement a function to list bars for one symbol between two dates in chronological order.
5. Insert the same record twice. Decide whether to keep the original or explicitly update it; document the policy and make the operation idempotent.
6. Use `sqlite3.Row` or another clear mechanism to convert database output back to a typed model.
7. Test against an in-memory or temporary database so the tests never depend on your personal data.
8. Add a small CLI command to show how many stored bars exist.

## Concrete example

Saving `AAPL / 2026-01-05 / 1Day / alpaca / iex` twice should leave one row. Saving `AAPL / 2026-01-05T15:00:00Z / 1Hour / alpaca / iex` is a **different** row. Querying a timeframe returns just that timeframe.

## Tests to write

- [ ] Database initialization can run twice safely.
- [ ] Insert then query reproduces symbol, date, and values.
- [ ] Duplicate inserts do not create duplicate rows.
- [ ] A SQL-looking symbol string is handled as data, not executed.
- [ ] A fresh temporary database starts empty.

## Hourly price extension (part of this existing storage feature)

Before issue 06, make this database support **both** daily and hourly bars:

1. Add columns `provider`, `feed`, `timeframe` and `bar_start_utc` (ISO-8601 UTC text is fine for the beginner version) alongside OHLCV, `collected_at` and any known availability time.
2. Replace the date-only unique key with **`UNIQUE(provider, feed, symbol, timeframe, bar_start_utc)`**. Otherwise all bars from the same trading day collide! Never merge IEX with a different feed, or daily with hourly, under one ID.
3. Write `list_bars(symbol, timeframe, start, end)` and filter by `provider`/`feed` when querying data. Use bound SQL placeholders. Sort by `bar_start_utc`.
4. Choose an explicit *upsert* policy (`INSERT ... ON CONFLICT ...`): save a record once; on retries, either update a previously stored record with newer verified data or leave it unchanged. Document which policy you chose.
5. If you already made the original daily-only table, practice a small **migration** on a throwaway test database: create the replacement schema, copy valid rows with explicit `1Day` identity, and verify the old daily records remain queryable. Back up personal databases before schema changes.

### Extra tests

- [ ] Two hourly bars for AAPL on one day coexist.
- [ ] A daily bar on the same day also coexists.
- [ ] The same hourly insert repeated twice leaves one row.
- [ ] IEX and a hypothetical second feed cannot silently overwrite one another.
- [ ] A query for `1Hour` returns no `1Day` rows.

## Acceptance checklist

- [ ] I can explain a unique constraint and an idempotent operation.
- [ ] No `.sqlite` database appears in `git status`.
- [ ] All storage tests pass without internet access.

## Common pitfall

Never save prices as numbers without documenting precision. SQLite isn't a substitute for validating the input model first.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.
