# 07 — Collect financial headlines from permitted RSS feeds

**Phase:** B · Trusted datasets  
**Estimated learning time:** 3–5 hours  
**Prerequisite:** Finish issue 06 first.

## Why we're doing this

News sentiment is only useful if you know what was published and when. Storing headlines and links—not copied full articles—makes the dataset auditable and less likely to infringe licensing terms.

## What you'll learn

- RSS/Atom parsing, timestamps, URLs, hashes
- Deduplication and source attribution
- Testing date parsing with known time zones

## Files to inspect or create

- `src/wallstreet/collectors/news.py` (new)
- `src/wallstreet/storage.py` (extend)
- `tests/test_news_collector.py` (new)

## Build it yourself — step by step

1. Find two legitimate sources with RSS/Atom terms that allow your intended personal usage. Document their licenses and feed URLs.
2. Create a `news_items` table containing a stable ID, source, title, canonical URL, published time, collected time, and optional tickers. Do not store whole copyrighted articles.
3. Parse a small saved XML fixture first, before making live requests. Use a standard XML parser or a maintained RSS library.
4. Normalize timestamps to UTC and keep the original timezone or source-provided string for debugging.
5. Deduplicate by canonical URL or a normalized source-specific identifier. Decide how you handle edited titles.
6. Write a conservative ticker matching function that starts with explicit symbols/tags. Don't assume an ordinary word matching a ticker means the article is about the company.
7. Use the HTTP client from issue 05 and ensure failures never delete existing news.
8. Expose `collect-news --dry-run` and a `news --limit 10` command.

## Concrete example

Two feed entries with the same canonical URL but different tracking query strings should resolve to one article. A third genuinely different article remains separate.

## Tests to write

- [ ] Duplicate headlines with the same identity aren't stored twice.
- [ ] Missing publication timestamp is marked unknown, not guessed.
- [ ] Malformed XML fails safely.
- [ ] Only the intended short metadata is persisted.
- [ ] UTC conversion behaves correctly.

## Acceptance checklist

- [ ] I can fetch and inspect at least one allowed feed locally.
- [ ] News has both publication and collection timestamps.
- [ ] Offline fixture tests pass.

## Common pitfall

A headline's publication time is not the time your system first *knew* about it. Backtests must avoid using stories collected later.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

