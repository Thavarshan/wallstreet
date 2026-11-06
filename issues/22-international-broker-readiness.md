# 22 — Research international live-trading feasibility, Wise, and withdrawal rules — no activation

**Phase:** E · Observe and assess  
**Estimated learning time:** 4–8 hours research  
**Prerequisite:** Finish issue 21 first.

## Why we're doing this

Being able to write a broker adapter does not prove that you can legally fund it, maintain authentication on $0 hosting, or withdraw proceeds. This issue is a careful go/no-go assessment, not a request to put capital at risk.

## What you'll learn

- Reading official broker and payments documentation
- Distinguishing residence, citizenship, tax residency, and banking eligibility
- Listing operational blockers without inventing shortcuts

## Files to inspect or create

- `docs/BROKER_RESEARCH.md` (new)
- `docs/LIVE_READINESS_CHECKLIST.md` (new)
- `tests/` (no live-order tests)

## Build it yourself — step by step

1. List actual markets you want (US, UK, possibly Europe), your desired account type (cash-only to start), supported order types, fee limits, and acceptable trade frequency.
2. Research current official eligibility for UK-resident accounts, noting that citizenship and tax status may have separate requirements. Record date and source links. Don't publish your full home address or ID documents.
3. Compare regulated brokers with an API, paper trading, documented authentication, US/UK security access, and permitted automated order entry.
4. Investigate IBKR's official Wise integration for deposits and withdrawals, and verify actual features enabled on your Wise account and possible UK-bank fallback. Record any entity-dependent restrictions.
5. Evaluate whether an API needs a continuously running authenticated gateway or human login. GitHub Actions and Workers may not be a viable replacement; mark the blocker honestly.
6. Estimate realistic commission, spread, FX conversion, withholding/tax, withdrawal and account costs. The infrastructure may be $0 while investing still costs money.
7. Evaluate Stripe only as a separately permitted financial service; never assume a brokerage can pay trading profits into a Stripe payments balance.
8. Require documentary proof of paper results, risk controls, operator alerts, brokerage terms, privacy/security review, and separate written approval before any future live integration.
9. Conclude `GO for more paper testing`, `NEEDS MORE EVIDENCE`, or `STOP`, with clear reasons. Do **not** activate live trading or automate withdrawals.

## Concrete example

If a broker supports UK residents and Wise funding but requires a continuously authenticated local gateway, the zero-cost stateless deployment requirement is currently **not satisfied**. Report that mismatch rather than ignoring it.

## Tests to write

- [ ] No live API endpoint or key is added.
- [ ] No real order/withdrawal operation is executed.
- [ ] Research links point to current official documentation.
- [ ] Every unsupported assumption is marked unresolved.
- [ ] Personal address and account numbers remain out of Git.

## Acceptance checklist

- [ ] A human can understand broker choices and restrictions.
- [ ] A go/no-go report exists with cost estimates and blockers.
- [ ] Paper-only mode remains the sole executable trading mode.

## Common pitfall

A verified Wise/Stripe account and UK bank account do not automatically establish brokerage approval or tax status. Never use identity or residency misrepresentation.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

