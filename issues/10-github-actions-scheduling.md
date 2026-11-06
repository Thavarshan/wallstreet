# 10 — Schedule hourly stock-price collection with GitHub Actions

**Phase:** B · Trusted datasets  
**Estimated learning time:** 4–6 hours  
**Prerequisite:** Finish issue 09 first.

## Why we're doing this

You asked for **hourly prices without paying to run a server**. A scheduled GitHub Actions job can wake up, execute your Python collector and stop. Your Mac can stay off. But GitHub schedules are **best effort, not exact clocks**, and each runner has temporary storage, so success is more than seeing a green check.

## What you'll learn

- GitHub Actions `schedule` and `workflow_dispatch` triggers
- Cron fields, UTC, environment secrets, minimal workflow permissions
- Concurrency, idempotency, retry/backfill and persistent versus temporary files
- How to budget free API and CI minutes

## Files to inspect or create

- `.github/workflows/tests.yml` (review)
- `.github/workflows/collect.yml` (new; you write it)
- `docs/OPERATIONS.md` (new)
- `tests/test_collection_schedule.py` (new unit tests for calendar/clock decisions)

## Build it yourself — step by step

1. Read [GitHub's schedule event documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule). Scheduled runs use the default branch, and GitHub warns they can be delayed or dropped at busy times. **Do not base your algorithm on a promise of an exact hourly launch.**
2. Start with both a manual `workflow_dispatch` trigger and an hourly-ish weekday cron, for example `17 * * * 1-5`. This means “17 minutes after each hour on weekdays” in the default UTC interpretation. The schedule can fire outside US market hours; your **Python code** must check market sessions with `zoneinfo`/the calendar from issue 09.
3. Why minute 17? It avoids the highest-load first minute of an hour, and it lets completed hours settle. **It does not guarantee** that historical data is accessible: the free feed may limit access to the newest 15 minutes. Handle provider availability checks and retrieve only confirmed finalized intervals.
4. Reuse your one collector from issue 06: call `python -m wallstreet collect-prices --timeframe 1Hour --symbols AAPL MSFT` (adjust to the actual CLI you built). Run **`--dry-run` first**, then a read-only collection. Keep any optional daily refresh as a separate CLI mode or an additional scheduled invocation.
5. Add `permissions: contents: read` unless the workflow truly needs more. Configure `ALPACA_API_KEY_ID` and `ALPACA_SECRET_KEY` as GitHub Actions **secrets**. Never commit or print keys. This is market-data access, **not** brokerage order authorization.
6. Add `concurrency` with an explicit group and `cancel-in-progress: false` (or equivalent policy) so two jobs don't overwrite one another or race for a shared store. Keep requests sequential for the initial two-symbol watchlist.
7. Check the market calendar (including a **post-close window to fetch the final completed bar**), and **also look for missed completed bars** since the last durable checkpoint. GitHub may run late or skip an hour. Fetch a small overlapping range and upsert by `provider/feed/symbol/timeframe/start`, with a bounded historical backfill window. Do not depend on “exactly one bar per run.”
8. **Solve persistence honestly.** GitHub runner files (including a local SQLite DB) disappear when the job ends. A cache or temporary artifact is not your live database. In `docs/OPERATIONS.md`, choose a permitted persistent option (potential later Cloudflare D1 adapter, after verifying current free-tier limits), or state clearly that this stage runs in dry-run/report-only mode without history surviving.
9. If credentials are missing, a provider fails, data is stale, the free quota is exceeded or durable storage is unavailable, **stop or report `unavailable`**. Don't fabricate prices and don't submit paper/live orders.
10. Test manually through the Actions UI, inspect logs for missing bar recovery, and document the free-tier minutes/API-call estimates. Revisit usage before increasing watchlist size or frequency.
11. Add an operations note: how to re-run a failed collection safely, how to disable the schedule, and how to verify the most recent stored completed bar.

## Example scheduling snippet (illustration, not the full workflow)

```yaml
on:
  workflow_dispatch:
  schedule:
    - cron: "17 * * * 1-5"
```

**Important:** GitHub may delay the run. A normal Monday trading session is based on **New York local time**, which changes its UTC offset seasonally. Your Python market calendar decides what should be collected; cron doesn't know US market holidays.

## Tests to write

- [ ] Workflow YAML is valid and can be triggered manually.
- [ ] The Python session guard skips a fixed holiday or market-closed timestamp.
- [ ] A missed scheduled hour is recovered by overlapping, deduplicated collection.
- [ ] Running twice doesn't duplicate the same saved `1Hour` bar.
- [ ] No run consumes an unfinished bar as historical input.
- [ ] Provider failure is visible; secrets never appear in logs.
- [ ] `--dry-run` neither writes prices nor places orders.

## Acceptance checklist

- [ ] I can explain what `17 * * * 1-5` means.
- [ ] Hourly collection is configured using the **existing** collector, not a separate trading bot.
- [ ] Documentation states exactly where data persists (or that it does not yet).
- [ ] Missed runs, provider delays and quota exhaustion fail safely.
- [ ] No live-trading workflow exists.

## Common pitfall

Polling hourly is **not a real-time streaming feed**. Even if the underlying free IEX feed is real-time, the collector only stores whatever completed historical bars are accessible when the job runs.

## Need help?

Ask your AI tutor to explain each YAML line or review your first workflow and logs. Implement it yourself, one step at a time.
