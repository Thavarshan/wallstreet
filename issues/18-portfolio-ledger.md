# 18 — Build an auditable portfolio ledger and reconcile with the paper broker

**Phase:** D · Safe simulation  
**Estimated learning time:** 6–9 hours  
**Prerequisite:** Finish issue 17 first.

## Why we're doing this

A dashboard showing the wrong cash balance is worse than no dashboard. Accounting must distinguish cash, positions, realized P&L, unrealized P&L, and pending orders while preserving a history of what happened.

## What you'll learn

- Transactions and event-style ledgers
- Average cost basis, cash flows, and valuation
- Reconciliation against an external authoritative source

## Files to inspect or create

- `src/wallstreet/portfolio.py` (new)
- `src/wallstreet/storage.py` (extend)
- `tests/test_portfolio.py` (new)

## Build it yourself — step by step

1. Define ledger events for deposit of *simulated* starting cash, filled buy, filled sell, fee, and dividend (only when data reliably exists). Events need IDs and timestamps.
2. Store every event once with a unique broker/execution ID. Avoid storing only a changing `total_balance` that loses history.
3. Implement position quantity and average purchase cost from fills. Decide and document the cost-basis rule (simple average cost for the educational version).
4. Calculate realized gains when a position is sold, net of applicable fees, and unrealized gain as marked market value minus remaining cost basis.
5. Separate broker-reported available cash from internally estimated cash, and handle open orders that reserve buying power.
6. Write `reconcile()` that compares stored cash, quantities, and order state with the paper broker and reports discrepancies rather than silently changing history.
7. Test sequential buys at different prices, a partial sale, fees, duplicate fill notifications, and a stock split scenario or explicit unsupported condition.
8. Expose a `portfolio` CLI command that prints cash, each holding, unrealized P&L, and discrepancy warnings.

## Concrete example

Buy 2 shares at $10 and 1 at $16 (ignore fees for this tiny example): average cost $12. Sell 1 at $15 → realized profit $3; remaining 2 shares cost $24.

## Tests to write

- [ ] Ledger events are applied once by unique ID.
- [ ] P&L agrees with hand-worked examples.
- [ ] Portfolio value = cash + market value of holdings.
- [ ] Unfilled orders do not create holdings.
- [ ] Reconciliation flags a broker mismatch.

## Acceptance checklist

- [ ] I can explain realized versus unrealized profit.
- [ ] A full portfolio is reconstructible from history.
- [ ] No P&L is presented as a guaranteed withdrawal balance.

## Common pitfall

Never silently overwrite ledger history to make it match the broker. Diagnose discrepancies and add correcting entries only with an explanation.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

