# 06 — Collect daily OHLCV from one legitimate free provider

**Phase:** B · Trusted datasets  
**Estimated learning time:** 4–6 hours  
**Prerequisite:** Finish issue 05 first.

## Why we're doing this

Daily prices are the foundation for charting, indicators, and backtests. Starting with just two symbols protects free API quotas and keeps debugging manageable.

## What you'll learn

- Parsing third-party JSON into your `PriceBar` model
- Date sorting, adjusted versus unadjusted prices
- Upserts and data provenance

## Files to inspect or create

- `src/wallstreet/collectors/prices.py` (new)
- `tests/test_price_collector.py` (new)
- `docs/DATA_SOURCES.md` (new)

## Build it yourself — step by step

1. Compare official free documentation for at least two providers (for example Alpha Vantage and eligible broker market data). Select one with permitted non-commercial use and enough daily quota.
2. Define a very small watchlist such as AAPL and MSFT. Store provider name, endpoint, limits, coverage, whether prices are delayed, and the last verification date in `DATA_SOURCES.md`.
3. Write a collector function taking a symbol and a client, returning validated `PriceBar` objects. Keep the network call separate from response parsing.
4. Account for reverse chronological responses, decimal strings, missing days, splits, and the difference between raw and adjusted values.
5. Call your SQLite storage layer; re-running collection must not add duplicates.
6. Record the source timestamp and your collection timestamp. If only end-of-day prices are available, don't mark them real-time.
7. Add `python -m wallstreet collect-prices` with a safe default watchlist and a dry-run option.
8. Write fixtures from a *small synthetic* provider response; never depend on the live API in CI.

## Concrete example

Provider returns two dates in reverse order. Your output saves them in chronological order, and the second run still shows two records.

## Tests to write

- [ ] Parser accepts valid daily bars.
- [ ] Rate-limit or provider error leaves existing database records untouched.
- [ ] Malformed prices are rejected.
- [ ] Duplicate collection is idempotent.
- [ ] Collection time and published/trading date aren't confused.

## Acceptance checklist

- [ ] Two symbols can be refreshed within the verified free quota.
- [ ] Source/license/delay are documented.
- [ ] Tests are deterministic and run offline.

## Common pitfall

Don't rely on an unofficial Yahoo endpoint without reviewing its terms. Avoid assuming a market holiday is a missing-data error.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

