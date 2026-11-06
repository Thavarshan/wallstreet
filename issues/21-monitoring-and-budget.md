# 21 — Make the $0 system observable, secure, and safe to stop

**Phase:** E · Observe and assess  
**Estimated learning time:** 5–8 hours  
**Prerequisite:** Finish issue 20 first.

## Why we're doing this

Free automation can fail silently or use up quotas. A project you can trust needs to know when it last ran, whether results are valid, and how to stop itself safely.

## What you'll learn

- Operational logs, retry-safe jobs, failure reporting
- Least-privilege GitHub tokens and dependency hygiene
- Usage limits and emergency stop policies

## Files to inspect or create

- `src/wallstreet/operations.py` (new)
- `tests/test_operations.py` (new)
- `docs/OPERATIONS.md` (extend)
- `.github/workflows/` (review)

## Build it yourself — step by step

1. Create a job-run record with unique run ID, task name, start/end time, outcome, rows collected, provider budget, and error summary.
2. Make repeated runs idempotent and ensure no two overlapping runs can create duplicate paper orders. Explore GitHub Actions concurrency groups.
3. Introduce configuration for maximum HTTP requests/day, inference calls/day, storage budget, and task timeouts. Stop before exceeding a verified free allocation.
4. Add a health summary CLI command: last successful run, last failure, stale sources, risk kill switch, and next expected market session.
5. Restrict workflow permissions to what each job needs, pin trusted dependencies where practical, and avoid executing untrusted PR code with secrets.
6. Add an emergency environment/config flag that disables new simulated orders while allowing read-only reports.
7. Set up an appropriate zero-cost notification option only if available; otherwise make a clear failure report in GitHub Actions.
8. Write a runbook describing what to do if a provider rate-limits, a workflow stops, the DB is unavailable, or a secret is exposed.

## Concrete example

If a free API quota is 25 requests/day and 25 were used, request 26 must be skipped with `quota exhausted`, not attempted or billed.

## Tests to write

- [ ] Failed job has a failure status, not success.
- [ ] Repeated run ID doesn't create duplicate results.
- [ ] Kill switch blocks paper orders.
- [ ] No secret is logged.
- [ ] Usage counters stop at the configured threshold.

## Acceptance checklist

- [ ] I can tell if the latest scheduled run failed.
- [ ] Documented limits keep the infrastructure at $0.
- [ ] Recovery steps are understandable to a beginner.

## Common pitfall

Don't enable paid fallback services automatically. Scheduled GitHub workflows are best-effort, not a reliable clock for high-frequency trading.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

