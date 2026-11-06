# 17 — Connect a paper-only broker adapter and handle order states

**Phase:** D · Safe simulation  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Finish issue 16 first.

## Why we're doing this

Your backtester assumes fills; a real paper broker can reject orders, partially fill them, or lose connectivity. You need to learn broker-specific behavior without risking real capital.

## What you'll learn

- Python protocols/interfaces and dependency injection
- Order states and idempotency keys
- Safe API authentication and mock testing

## Files to inspect or create

- `src/wallstreet/brokers/base.py` (new)
- `src/wallstreet/brokers/paper.py` (new)
- `tests/test_paper_broker.py` (new)

## Build it yourself — step by step

1. Read official free paper-trading documentation from one provider. Alpaca paper-only accounts are a candidate; verify current availability, permissions, and data limitations.
2. Define a tiny broker interface: `account()`, `positions()`, `submit_order()`, `get_order()`. Keep it independent from a specific HTTP library.
3. Create a fake in-memory broker first so every test can run offline. Model NEW, ACCEPTED, PARTIALLY_FILLED, FILLED, REJECTED, and CANCELED where supported.
4. Implement the provider adapter with a dedicated paper endpoint and paper credentials only. Never include a live endpoint in the app's default settings.
5. Route every proposed order through risk checks from issue 16, and use a unique client order ID to avoid duplicate execution when jobs retry.
6. When an API call times out after submission, query the existing order by ID; never blindly resubmit an unknown order.
7. Reconcile filled quantities and broker-reported prices rather than assuming every order fills immediately.
8. Write a CLI `paper-status` and `paper-order --dry-run` that show what would happen before any simulated submission.

## Concrete example

First submission times out, but the broker actually accepted `order-123`. Retry should retrieve `order-123`, not create a second order.

## Tests to write

- [ ] Risk-rejected proposals never reach the adapter.
- [ ] Paper endpoint is used; production endpoint is never present in tests.
- [ ] Duplicate client order ID doesn't generate a second order.
- [ ] Partial fills update correctly.
- [ ] Timeout and rejection produce visible states.

## Acceptance checklist

- [ ] A fake broker can pass all tests without credentials.
- [ ] An official paper account can be queried manually, if eligible.
- [ ] Every order is clearly marked `PAPER`.

## Common pitfall

Paper fill models can be optimistic and may omit actual market impact, slippage, or regulatory fees. Never treat simulated profit as withdrawable.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

