# 05 — Write a small HTTP client with timeouts, retries, and rate limits

**Phase:** B · Trusted datasets  
**Estimated learning time:** 3–4 hours  
**Prerequisite:** Finish issue 04 first.

## Why we're doing this

Free providers often reject excess requests or fail temporarily. Without proper handling, a scheduled job may save an error message as if it were a stock price.

## What you'll learn

- HTTP status codes, JSON decoding, exceptions
- `requests` or `urllib.request`—choose one and explain why
- Timeouts, exponential backoff, and quota-aware failure

## Files to inspect or create

- `src/wallstreet/http_client.py` (new)
- `tests/test_http_client.py` (new)

## Build it yourself — step by step

1. Read basic HTTP response concepts: 200 success, 429 rate-limited, 500+ provider failure, and 401/403 authentication issues.
2. Choose a minimal HTTP library. Write `fetch_json(url, *, timeout_seconds=...)` that returns decoded JSON or raises a clearly named error.
3. Send a real request only to a harmless publicly documented endpoint during manual exploration. Your automated tests must use mocked responses, not live internet.
4. Add a short timeout so the program cannot hang forever.
5. Implement at most a few retries for retryable errors with bounded waiting. Respect `Retry-After` when present; never retry invalid credentials indefinitely.
6. Return informative failures for malformed JSON and empty responses. Never pretend the returned data is valid.
7. Add a simple per-provider budget or counter and make exceeding the free quota a safe stop.
8. Hide tokens in environment variables and redact them from logs.

## Concrete example

Mock responses: `200` with `{'ok': true}` returns the parsed object; `429` with `Retry-After: 60` raises or backs off safely; `200` with broken JSON raises a parsing error.

## Tests to write

- [ ] Normal JSON is decoded.
- [ ] Timeout results in a meaningful failure.
- [ ] 429 and 500 can be retried only within a bounded policy.
- [ ] 401 is not blindly retried.
- [ ] No API key appears in exception messages or test output.

## Acceptance checklist

- [ ] I can explain why retries need a limit.
- [ ] Test fixtures use fake HTTP responses.
- [ ] The client cannot run forever or exceed a configured budget.

## Common pitfall

Do not write a generic networking framework. A tiny understandable wrapper is enough. Avoid scraping websites whose terms prohibit automation.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

