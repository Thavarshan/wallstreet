# 06 — Collect hourly and daily OHLCV from Alpaca's free IEX API

**Phase:** B · Trusted datasets  
**Estimated learning time:** 6–9 hours  
**Prerequisite:** Finish issues 03–05 first.

## Why we're doing this

We already planned a price collector; we are **extending that existing collector to retrieve hourly bars as well as daily bars**, not creating a second unrelated subsystem. Hourly data allows Wallstreet to ask what changed *during the trading day*. Daily data remains useful for beginner-friendly charts and long-term comparisons.

Our first official source is [Alpaca's US stock historical-bars API](https://docs.alpaca.markets/us/reference/stockbars) on the free **IEX** feed. **IEX covers one US exchange, not all US trades**, so its prices and volumes may differ from a consolidated US market feed. The free plan has rate/history restrictions: verify them before use. This is research and paper trading only.

## What you'll learn

- API JSON with lists nested inside dictionaries: `data["bars"]["AAPL"]`
- Functions with parameters, `for` loops, `datetime` and timezone-aware timestamps
- An **OHLCV bar**: open, high, low, close and traded volume for a fixed time window
- Historical API pagination, deduplication and incremental updates
- The difference between `1Hour`, `1Day`, an instant trade/quote and a still-forming bar

## Files to inspect or create

- `src/wallstreet/collectors/prices.py` (new)
- `src/wallstreet/models.py` (extend the `PriceBar` from issue 03)
- `src/wallstreet/storage.py` and `schema.sql` (extend issue 04 storage)
- `tests/test_price_collector.py` (new)
- `docs/DATA_SOURCES.md` (new: provider, URL, feed, terms, quotas, delays, verified date)

## Build it yourself — step by step

1. **Read the official endpoint:** `GET https://data.alpaca.markets/v2/stocks/bars`. It accepts `symbols`, `timeframe`, `start`, `end`, `feed`, `adjustment`, and `page_token`. Read [the stock-bars reference](https://docs.alpaca.markets/us/reference/stockbars), especially pagination. Select just **AAPL and MSFT** to begin.
2. **Start with one completed historical hour.** Request `timeframe=1Hour`, `feed=iex`, `adjustment=raw`, and a **bounded RFC-3339 UTC** start/end range in the past. Use the authenticated HTTP client from issue 05. Do not begin with a WebSocket or continuous live connection.
3. **Understand the response.** For each symbol, the `bars` dictionary contains a list. A bar typically has `t` (bar timestamp), `o`, `h`, `l`, `c`, `v`, and possibly `n` (trade count) and `vw` (volume-weighted price). The timestamp describes the *bar*, not when your collector ran. Validate required fields; tolerate documented optional fields.
4. **Keep parsing pure.** Implement one function to retrieve raw JSON and another like `parse_bars(payload, *, provider, feed, timeframe)` to convert JSON to `PriceBar` objects. The parser should be testable from local fixture dictionaries without an HTTP connection.
5. **Represent both intervals clearly.** Extend your `PriceBar` with `timeframe` (exactly `1Hour` or `1Day`), a timezone-aware `bar_start_utc`, `provider` (Alpaca), `feed` (`iex`), source availability/collection time when known, and OHLCV. For daily bars, retain the trading date for human display; **do not store a daily bar as if it were the 9:30–10:30 hourly bar**.
6. **Extend SQLite's unique key** from issue 04 to include at least `provider, feed, symbol, timeframe, bar_start_utc`. This permits one daily AAPL bar and multiple hourly AAPL bars on the same day while making repeated collection safe. Explain *upsert*: inserting the same identity again updates or ignores that row according to your documented policy.
7. **Handle pagination.** Alpaca may group/sort data by symbol, so a page may contain AAPL but no MSFT. Keep requesting with the returned `next_page_token` until none remains. Set a safety limit on number of pages and never claim a missing symbol is delisted just because it was not on page one.
8. **Collect a second timeframe.** Request `timeframe=1Day` through the **same collector** with a different parameter. Store daily and hourly records separately. Do not manufacture hourly bars by repeating daily closing prices.
9. **Reject unfinished or unavailable bars.** A bar that has not finished must not enter historical strategy features as a final close. The free plan's newest historical bars may be restricted/delayed; do not pretend your result is live when the provider says otherwise. Use a conservative completion/availability cutoff and let issue 09 validate it.
10. **Make refresh incremental.** On a repeat run, request a small overlap before the last saved completed bar, then upsert by unique identity. Use bounded backfill to fill genuinely missed hours. Market closures, holidays and sparse IEX activity can produce legitimate gaps.
11. **Expose one safe command** such as `python -m wallstreet collect-prices --timeframe 1Hour --symbols AAPL MSFT --dry-run`; support `1Day` too. A dry run shows the request and validation plan without writing data. Keep real authentication out of console output.
12. **Record limitations.** In `docs/DATA_SOURCES.md` state exactly which market feed you use, that `iex` is a subset of market trades, which prices are raw/adjusted, historical availability, quota checks, API terms and the date you verified them. Do not mix data from `iex` and other feeds under one key.

## Example to work through

Request (dates deliberately historical; replace with a valid completed market session):

```text
GET https://data.alpaca.markets/v2/stocks/bars
    ?symbols=AAPL,MSFT
    &timeframe=1Hour
    &start=2026-10-05T13:00:00Z
    &end=2026-10-05T20:00:00Z
    &feed=iex
    &adjustment=raw
```

Illustrative **fake** JSON (do not treat these as market observations):

```json
{
  "bars": {
    "AAPL": [
      {"t": "2026-10-05T13:00:00Z", "o": 100, "h": 102, "l": 99, "c": 101, "v": 1200}
    ],
    "MSFT": []
  },
  "next_page_token": null
}
```

The AAPL record must retain its exact UTC timestamp and `1Hour` interval. An empty MSFT list means **no bar in this response**, not a zero-dollar price. If a `next_page_token` exists, fetch remaining pages first.

## Tests to write (all offline)

- [ ] Parse a valid 1Hour fixture, including timezone, symbol, price precision and volume.
- [ ] Parse a 1Day fixture without confusing it with 1Hour.
- [ ] Missing/malformed prices and impossible OHLC ranges fail visibly.
- [ ] Two response pages are merged without dropping a symbol.
- [ ] Insert the same hourly bar twice: still one row; a separate daily row remains.
- [ ] A still-forming or future bar never enters the “completed bars” result.
- [ ] An empty IEX window is recorded as unavailable, **not** as a zero-volume fabricated bar.
- [ ] 429, timeout or bad JSON does not corrupt previously saved prices.
- [ ] Tests use synthetic fixtures and need neither real credentials nor internet access.

## Acceptance checklist

- [ ] I can explain what hourly OHLCV measures and what it **doesn't** measure.
- [ ] One collector handles `1Hour` and `1Day` for AAPL/MSFT on the IEX feed.
- [ ] Both intervals store without clashing; retries are idempotent.
- [ ] `DATA_SOURCES.md` explains IEX coverage, source timestamps, limits and caveats.
- [ ] No paper or live trade is placed by this collector.

## Common pitfalls

The “latest bar” endpoint provides a **minute** bar, not a finalized one-hour history. Don't use it as a shortcut for `1Hour`. Market-hours boundaries and daylight saving require issue 09; don't implement trading-calendar guesses inside your HTTP parser.

## Need help?

Ask your AI tutor to review **your function and fixture tests** after you attempt them. Your goal is to implement the feature yourself, with understanding.
