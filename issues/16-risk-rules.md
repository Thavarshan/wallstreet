# 16 — Build deterministic risk checks that can veto a proposed trade

**Phase:** D · Safe simulation  
**Estimated learning time:** 5–8 hours  
**Prerequisite:** Finish issue 15 first.

## Why we're doing this

Even a statistically promising strategy can lose money or malfunction. A separate risk layer must be able to say 'no' regardless of how confident a model sounds.

## What you'll learn

- Validating structured inputs, state machines, and fail-closed decisions
- Exposure, drawdown, cash reserves, and order sizing
- Boundary tests for maximum and minimum limits

## Files to inspect or create

- `src/wallstreet/risk.py` (new)
- `tests/test_risk.py` (new)
- `docs/RISK_POLICY.md` (new)

## Build it yourself — step by step

1. Draft a short, configurable risk policy in plain English. Begin with no margin, no leverage, no shorts, no options, and no real orders.
2. Define an `OrderProposal` separate from a signal, with quantity, symbol, estimated price, side, and timestamp.
3. Write a `check_order(proposal, portfolio, market_data, policy)` pure function returning approved/rejected and a list of reasons.
4. Check insufficient cash, max allocation to one security, max portfolio exposure, stale prices, excessive spreads when available, allowed symbols, and order value limits.
5. Implement an emergency kill switch, plus maximum daily loss and drawdown thresholds measured from your own portfolio ledger.
6. Make missing policy fields, unavailable prices, or unknown balances result in rejection, not permission.
7. Test just below, exactly at, and just above each threshold. Use different rejection reasons so you can understand failures.
8. Ensure the paper order path calls this check immediately before submission. Future live adapters must reuse the same mandatory guard.

## Concrete example

Policy permits at most 10% of a $1,000 portfolio in one symbol. A $150 proposed purchase for an empty portfolio must be rejected, even if a strategy says BUY.

## Tests to write

- [ ] Over-limit orders are rejected.
- [ ] Kill switch rejects every new buy/sell proposal.
- [ ] Unknown cash or stale price rejects.
- [ ] A legitimate small paper order can pass.
- [ ] No risk check sends network requests or places an order.

## Acceptance checklist

- [ ] Risk checks are independent of strategy and AI.
- [ ] Rejection reasons are visible in reports.
- [ ] No bypass path exists for a new paper order.

## Common pitfall

'Stop loss' is not a guarantee of the price you'll receive. Avoid claims of non-risk or guaranteed-loss protection.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

