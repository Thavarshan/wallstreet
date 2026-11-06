# 09 — Validate data freshness, time zones, and market calendars

**Phase:** B · Trusted datasets  
**Estimated learning time:** 4–6 hours  
**Prerequisite:** Finish issue 08 first.

## Why we're doing this

A stock exchange has its own hours, holidays, and daylight-saving rules. An hourly script can run successfully but still analyze yesterday's prices. You need an explicit answer to 'Is this record usable now?'

## What you'll learn

- UTC versus exchange-local timestamps and `zoneinfo`
- Missing versus delayed versus invalid data
- Small, explicit validation reports

## Files to inspect or create

- `src/wallstreet/quality.py` (new)
- `tests/test_quality.py` (new)
- `docs/DATA_SOURCES.md` (extend)

## Build it yourself — step by step

1. Choose one target exchange, such as NYSE, and read its published calendar. Decide which trading sessions your initial application supports.
2. Make a function that converts a timezone-aware timestamp to UTC and rejects a naive timestamp unless the source's timezone is known.
3. Write a validator for a sequence of daily `PriceBar`s: unique symbol/date pairs, ascending dates, non-negative volume, positive prices, and non-impossible OHLC ranges.
4. Implement freshness rules: a daily bar isn't expected before the exchange closes, and weekends/holidays aren't missing bars. Make limits configurable rather than hard-coding assumptions.
5. Create a tiny `DataQualityReport` with counts of valid, missing, duplicate, stale, and rejected records, plus a short reason for each rejected record.
6. Add a `quality` CLI subcommand reading stored bars and printing a human-readable summary.
7. Make strategy code fail closed when a required price is stale or data quality is unknown.
8. Test a US daylight-saving transition, a weekend, a holiday, and a duplicated bar using explicit fixed timestamps.

## Concrete example

At 10:00 New York time on a normal Monday, the current day's closing price is not yet known. A completed Friday bar can still be valid; don't flag Saturday/Sunday as missing sessions.

## Tests to write

- [ ] Naive timestamps cannot sneak in as UTC.
- [ ] Valid holiday/weekend gaps are not treated as errors.
- [ ] A duplicate bar is reported clearly.
- [ ] A future-dated record is rejected.
- [ ] Quality report counts match the fixture.

## Acceptance checklist

- [ ] I can explain publication time, trading time, and collection time.
- [ ] A command prints useful quality checks.
- [ ] A strategy won't consume invalid or future data.

## Common pitfall

Never manually subtract five hours for New York time: daylight saving can change the offset. Use a timezone-aware library and exchange calendar.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

