# 10 — Schedule safe daily collection with GitHub Actions

**Phase:** B · Trusted datasets  
**Estimated learning time:** 3–5 hours  
**Prerequisite:** Finish issue 09 first.

## Why we're doing this

Research shouldn't depend on your Mac staying awake. GitHub Actions can run Python on a schedule, but runners are temporary and schedules can be delayed. You must plan where results actually persist.

## What you'll learn

- GitHub workflow YAML, cron expressions in UTC, job permissions
- Environment secrets and least privilege
- The difference between an ephemeral runner and persistent storage

## Files to inspect or create

- `.github/workflows/tests.yml` (review)
- `.github/workflows/collect.yml` (new)
- `docs/OPERATIONS.md` (new)

## Build it yourself — step by step

1. Read the official GitHub `schedule` event documentation and note that scheduled workflows may be delayed or disabled after inactivity on public repos.
2. Create a workflow with `workflow_dispatch` so you can run it manually. Initially schedule once daily, several minutes away from the top of an hour.
3. Install the Python package and run the same safe CLI collection command you already tested locally.
4. Start with dry-run mode. A successful job log must show which symbols would be collected without exposing secrets.
5. Document that `data/wallstreet.sqlite3` disappears when the runner ends. Choose and implement a permitted persistent storage path only after understanding the tradeoffs (e.g., a Cloudflare D1 adapter in a later task). Do not claim persistence before it works.
6. Add explicit minimal `permissions:` and secret names as environment variables. Do not print credentials to logs.
7. Make the job return a failure status on provider errors and record last success timestamps in durable storage when available.
8. Run the workflow manually and inspect its logs. Document the free-tier budget and missed-run recovery.

## Concrete example

A manual run on Tuesday prints a dry-run summary. A second run must not duplicate Tuesday's records in the persistent store, once configured.

## Tests to write

- [ ] YAML parses and the job passes locally equivalent tests.
- [ ] Secrets are referenced, never hardcoded.
- [ ] One failed provider call results in a visible failure state.
- [ ] Dry-run does not send an order or write fabricated prices.

## Acceptance checklist

- [ ] I can explain what cron does.
- [ ] Scheduled and manual paths use the same Python command.
- [ ] The documentation honestly describes persistence and schedule limitations.

## Common pitfall

A GitHub Actions cache or artifact isn't a replacement for a transactional database. Do not commit a constantly changing SQLite file to a public Git repo.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

