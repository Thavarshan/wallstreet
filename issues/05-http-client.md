# 05 — Write a small HTTP client with timeouts, retries, and rate limits

**Phase:** B · Trusted datasets  
**Estimated learning time:** 4–6 hours  
**Prerequisite:** Finish issue 04 first.

## Why we're doing this

Wallstreet needs a dependable way to request **hourly stock-price bars** from an official API. A request can time out, return bad JSON, or hit a free-plan limit. If you mistake an error response for a price, every indicator and paper trade built on it is unreliable.

We'll use [Alpaca's Market Data API](https://docs.alpaca.markets/us/docs/about-market-data-api) as the first concrete provider. Its free Basic plan supplies real-time **IEX exchange** data—not a complete consolidated feed of every US exchange. You are learning to *read prices*, not to place brokerage orders.

## Python concepts you'll practice

- HTTP GET requests and headers (similar to Laravel's `Http::withHeaders(...)->get(...)`)
- Dictionaries, JSON decoding, custom exceptions and type hints
- Environment variables with `os.environ`, timeouts and limited retries
- Dependency injection: pass a fake HTTP transport in tests instead of calling the real internet

## Files to inspect or create

- `src/wallstreet/http_client.py` (new)
- `tests/test_http_client.py` (new)
- `docs/DATA_SOURCES.md` (document the provider in issue 06)

## Build it yourself — step by step

1. Read what HTTP status codes mean: **200** success; **400** invalid query; **401/403** authentication or access; **429** rate limit; **500+** temporary server trouble. Never interpret an error body as a stock price.
2. Choose either Python `requests` (easy to learn) or `urllib.request` (standard library). Explain your choice in a short comment; do not install a large broker SDK just to fetch JSON.
3. Design a small `fetch_json(url, *, params=None, headers=None, timeout_seconds=10)` function. Its only job is to make a request and return decoded JSON or a clear exception. In `requests`, `params` is a Python dictionary turned into URL query parameters.
4. Read credentials from **`ALPACA_API_KEY_ID`** and **`ALPACA_SECRET_KEY`** environment variables, *not* from Python source or committed YAML. Alpaca's request headers are **`APCA-API-KEY-ID`** and **`APCA-API-SECRET-KEY`**. Never print headers or complete exception URLs containing secrets. If either variable is missing, fail with a helpful setup message.
5. Make a single manual, read-only test against **`https://data.alpaca.markets/v2/stocks/bars`** using `symbols=AAPL`, `timeframe=1Hour`, `feed=iex`, a small historical `start`/`end` range, and `adjustment=raw`. Do not use a live order/trading endpoint. Issue 06 will turn this experiment into a collector.
6. Use a **finite** timeout; catch connection and decoding errors separately. Retry only transient network errors, 429 and appropriate 5xx responses. Limit retries (for example, at most 3 attempts total), use increasing wait times, and respect a documented `Retry-After` header when present. Never infinitely retry 401/403.
7. Keep a simple request counter and stop safely when your chosen quota budget is exhausted. Re-check Alpaca's [current plan limits](https://docs.alpaca.markets/us/docs/about-market-data-api) rather than hardcoding a forever-true allowance.
8. Separate the generic client from the Alpaca-specific settings: the client sends HTTP, while the collector in issue 06 knows which endpoint and parameters to request.
9. Write fake HTTP responses for all automated tests. No real API calls or credentials are needed for `pytest` or GitHub CI.

## Small example to reason through

```python
params = {
    "symbols": "AAPL,MSFT",
    "timeframe": "1Hour",  # A completed 60-minute OHLCV bar, not an instant quote
    "feed": "iex",
    "adjustment": "raw",
}
```

For a `200` response, decode the JSON. For `429`, either wait within your strict limit or raise `RateLimitError`. For `401`, stop and explain that the credentials need checking—never silently use a fake value.

## Tests to write

- [ ] A valid JSON response becomes a Python dictionary.
- [ ] Parameters and both authentication headers are sent to the **data** endpoint, using fake credentials in tests.
- [ ] Missing credentials fail clearly without leaking their values.
- [ ] Timeout, invalid JSON and 401/403 produce understandable errors.
- [ ] 429 and temporary 5xx stop after the configured maximum attempts.
- [ ] The retry policy respects `Retry-After` without sleeping in unit tests (inject a fake wait function).
- [ ] No HTTP calls happen during the test suite.

## Acceptance checklist

- [ ] I can explain `params`, `headers`, a timeout and a retry using plain Python.
- [ ] I can fetch a small historical IEX sample manually with my own key.
- [ ] Secrets never appear in code, a GitHub commit, logs or test output.
- [ ] The reusable HTTP client knows nothing about trading or strategies.

## Common pitfalls

- **Hourly bars aren't quotes.** A bar summarizes prices during an hour; it is not the price at this instant.
- **IEX isn't the whole market.** Do not label the free feed “consolidated real-time US stocks.”
- Do not turn a network failure into a zero-value price or fall back to a different feed without recording the change.

## Need help?

Ask your AI tutor to explain one HTTP concept or review **your code attempt**. Implement it yourself to learn Python. Wallstreet remains research/paper-only; no real orders.
