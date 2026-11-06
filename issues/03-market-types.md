# 03 — Practice Python dictionaries, lists, dataclasses, and validation

**Phase:** A · Python foundations  
**Estimated learning time:** 3–4 hours  
**Prerequisite:** Finish issue 02 first.

## Why we're doing this

Financial APIs return nested dictionaries and lists. Before storing or analyzing this data, you must know exactly what each field means. A lightweight Python model catches bad inputs before they corrupt your calculations.

## What you'll learn

- Lists versus dictionaries versus sets; indexing and iteration
- `@dataclass`, type hints, `datetime.date`, `Decimal`
- Exceptions (`ValueError`) and validation with tests

## Files to inspect or create

- `src/wallstreet/models.py` (new)
- `tests/test_models.py` (new)

## Build it yourself — step by step

1. Create an example dictionary with keys `symbol`, `date`, `open`, `high`, `low`, `close`, and `volume`. Print each key/value using `.items()`, not `for key, value in dictionary`.
2. Create a `PriceBar` dataclass holding a normalized uppercase ticker, a date, price fields, and integer volume. Research why `Decimal` is safer than binary floats for money-like values.
3. Add a classmethod or separate function converting a dictionary to a `PriceBar`. Make explicit decisions about string dates and numeric strings; don't guess silently.
4. Validate that prices are non-negative, volume is a non-negative integer, `high >= low`, and the open/close lie within the day's range. Raise a useful `ValueError` explaining the invalid field.
5. Create a list of two valid bars and loop over it to compute a simple min/max or average close. Use a separate set to discover which symbols are unique.
6. Write tests for valid construction and several invalid inputs. Learn pytest's `raises` helper.
7. Document which input formats you accept; no API calls are necessary.

## Concrete example

Valid: `{'symbol': 'AAPL', 'date': '2026-01-05', 'open': '100', 'high': '105', 'low': '99', 'close': '103', 'volume': 1000}`. Invalid: same record with `high: '98'` should raise an error.

## Tests to write

- [ ] Input symbol is normalized to uppercase.
- [ ] Invalid dates and negative volume are rejected.
- [ ] `high < low`, `open > high`, and missing required fields fail clearly.
- [ ] The original input dictionary is not unexpectedly modified.

## Hourly price extension (do this before issue 06)

The first toy example uses a **daily** `date` because it is easier to understand. The real API will also return **hourly** bars, so extend the same `PriceBar` model after your first tests pass.

1. Import `datetime` and `timezone` in addition to `date`. Define `bar_start_utc` as a **timezone-aware datetime**, `timeframe` as `1Hour` or `1Day`, and `provider`/`feed` as strings. A separate `trading_date` can help with daily display, but it cannot uniquely identify hourly bars.
2. Construct an hourly example for `AAPL` at `2026-10-05T14:00:00Z` and a daily example on the same date. They are *different* `PriceBar` records.
3. Make `from_dict` reject an unknown timeframe, a timestamp without a timezone, and impossible prices. Think of `datetime` as Python's equivalent of a date-time object you would normally handle with Carbon in Laravel.
4. Keep `Decimal` for prices; don't add unrelated stock prediction logic to the model.

### Extra tests

- [ ] `1Hour` and `1Day` records on the same date remain distinct.
- [ ] A naive `datetime` (missing timezone) is rejected.
- [ ] Unknown timeframes fail with a useful message.

## Acceptance checklist

- [ ] I understand why `for key, value in row.items()` works.
- [ ] I can explain what a dataclass gives me.
- [ ] Model tests cover both valid and invalid bars.

## Common pitfall

Avoid naming variables `list`, `dict`, or `set`; that shadows Python built-ins. Do not represent missing prices as zero.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.
