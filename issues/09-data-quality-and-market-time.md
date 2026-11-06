# 09 — Validate data freshness, time zones, and market calendars

**Phase:** B · Trusted datasets  
**Estimated learning time:** 5–7 hours  
**Prerequisite:** Finish issue 08 first; use the hourly records from issue 06.

## Why we're doing this

An hourly data collector can run successfully and still return **yesterday's** bar, a **bar that hasn't finished**, or **no trade on the IEX venue**. Wallstreet must know the difference. A missing bar outside market hours should not raise the same alarm as an outdated bar during a normal session.

## What you'll learn

- Aware `datetime` objects, UTC and `zoneinfo.ZoneInfo("America/New_York")`
- Difference between exchange session time, bar timestamp, API availability time and our `collected_at`
- Valid OHLCV fields, duplicate detection, missing data and freshness checks
- Why trading calendars include holidays, shortened sessions and daylight-saving changes

## Files to inspect or create

- `src/wallstreet/quality.py` (new)
- `tests/test_quality.py` (new)
- `docs/DATA_SOURCES.md` (extend with hourly freshness/coverage policy)

## Build it yourself — step by step

1. Read the official NYSE calendar, then choose **regular US stock market hours** for the first version. A typical session is **09:30–16:00 New York local time**; it is not 24/7, and some days have early closes. Use an official/reliable exchange calendar and record your source; do not build a never-ending hardcoded holiday list.
2. Practice `datetime.now(timezone.utc)`, `datetime.fromisoformat(...)` and `ZoneInfo("America/New_York")`. Convert aware timestamps to UTC. Reject naive timestamps (no timezone) until you explicitly know how to interpret them.
3. Add an explicit `timeframe` parameter to your validator: `1Hour` and `1Day` have **different** expectations. Never compare an hourly 10:00 bar to the daily closing bar as if they were the same measurement.
4. Validate each bar: normalized symbol, exact interval/feed, chronological order, unique `(provider, feed, symbol, timeframe, bar_start_utc)`, finite positive OHLC prices, `low <= open/close <= high`, and nonnegative volume. Reject an impossible or future timestamp.
5. Distinguish **completed** from **forming** bars. An hour's open/high/low/close can change while trading continues. Do not use it as finalized history until the interval is over **and any provider availability/delay policy is satisfied**. Learn whether Alpaca timestamps indicate the start of a window; document how you determine its end. Do not simply add a UTC hour across exchange breaks without checking the provider's documented boundaries.
6. Determine what bar is actually **expected** for a timestamp using the trading session calendar. The session opens at **09:30 local**, not 09:00, and may end early. IEX is one venue and might provide **no bar for a sparse symbol/window**. Mark that observation `missing_or_unavailable`; do not invent a price or assume the market was closed.
7. Define freshness separately for **hourly** and **daily**: e.g., can you use the most recent *fully completed and available* interval? After closing or on weekends, the last completed trading bar may be old in clock hours but still the latest valid session. Make thresholds configurable.
8. Create a plain `DataQualityReport` holding counts of `valid`, `duplicates`, `stale`, `rejected`, `unavailable`, plus short reasons. Keep this report separate from the collection code.
9. Make a `quality` CLI command for one symbol and timeframe. Strategy code must return `HOLD`/unavailable when required data quality fails, not invent a prediction.
10. Write tests using fixed known timestamps around a market open/close, weekend, US DST shift, holiday and early close. Use a fake clock so tests never depend on the current date.

## Worked example

At 10:05 a.m. New York time, the hour currently underway is **not a final bar**. A completed prior bar may be usable; a Friday final bar might be the freshest valid result on Saturday. Conversely, if Wallstreet expected a completed intraday IEX bar and receives no data, report that explicitly.

## Tests to write

- [ ] Naive or future timestamps are rejected.
- [ ] `1Hour` and `1Day` use separate freshness rules and identities.
- [ ] A forming hourly bar is never accepted as complete.
- [ ] Holidays, weekends and early closes don't generate fake expected bars.
- [ ] Fixed tests pass across a US daylight-saving transition.
- [ ] Missing IEX data is not converted to zero, nor silently replaced by another feed.
- [ ] A duplicate or malformed bar is reported with a useful reason.

## Acceptance checklist

- [ ] I can explain bar time versus the time our job downloaded it.
- [ ] A quality report tells me whether I can safely run **hourly** analysis.
- [ ] A missing or unfinished bar results in no new signal rather than a made-up one.
- [ ] Automated tests use no provider requests.

## Common pitfall

Don't subtract a fixed 5 hours to get New York time. Its UTC offset changes with daylight saving. Also don't assume a US trading day consists of six or seven perfect wall-clock hour bars: verify how your chosen provider constructs buckets.

## Need help?

Ask your AI tutor to draw a **single day's timeline** and critique your freshness function after you write it. Keep all activity paper-only.
