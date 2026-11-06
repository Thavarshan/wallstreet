# 20 — Publish a read-only dashboard without exposing secrets

**Phase:** E · Observe and assess  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Finish issue 19 first.

## Why we're doing this

A small dashboard helps you review the research from any device, but it should not become an excuse to introduce paid infrastructure or unsafe public account endpoints.

## What you'll learn

- Separating private data from public presentation
- Simple JSON API responses and access control
- Cloudflare Workers, D1 quotas, and deploy checks

## Files to inspect or create

- `web/` (new; only when you reach this issue)
- `docs/DEPLOYMENT.md` (new)
- `tests/test_dashboard_data.py` (new)

## Build it yourself — step by step

1. Start by designing a read-only page on paper: last run, source freshness, paper equity, benchmark, risk state, and recent signals. No trade buttons.
2. Decide whether a static, manually published sample report already satisfies your needs. Introduce Cloudflare Workers only if it adds meaningful value.
3. Verify current Workers/D1 free limits, account requirements, authentication options, and whether data egress/storage can unexpectedly incur charges.
4. Create a minimal endpoint returning a synthetic JSON portfolio. The page must label all figures as simulated and make no authenticated broker calls from the browser.
5. Keep any personal portfolio data behind real authentication and authorization. If you cannot protect it on the free plan, publish only synthetic/demo data.
6. Add graceful handling for missing report data, stale last runs, and API errors.
7. Make page size and database queries small enough for the verified free quotas.
8. Test on a phone, verify no secret is embedded in frontend JavaScript, and document how to deploy/revert.

## Concrete example

Dashboard shows `PAPER / last sync 2 hours ago / data status stale`, and refuses to display an invented current price.

## Tests to write

- [ ] No credential appears in generated assets or responses.
- [ ] Unauthorized request cannot read personal portfolio data.
- [ ] No data results in an honest empty state.
- [ ] All figures are visibly marked paper/demo.
- [ ] Quota limits lead to a safe failure, not a paid upgrade.

## Acceptance checklist

- [ ] A small dashboard renders correctly on desktop/mobile.
- [ ] Privacy and free-tier budget are documented.
- [ ] No feature can place an order or withdraw money.

## Common pitfall

Cloudflare Workers are not a free unlimited compute cluster. Keep expensive analysis in short, scheduled Python tasks and avoid storing sensitive balances on an open endpoint.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

