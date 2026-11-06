# 15 — Measure out-of-sample performance and challenge your own strategy

**Phase:** C · Analysis  
**Estimated learning time:** 5–8 hours  
**Prerequisite:** Finish issue 14 first.

## Why we're doing this

An impressive historical return can arise by accident, especially after testing many parameter combinations. Honest evaluation requires reserved dates, realistic costs, and comparison with doing nothing or buying an index.

## What you'll learn

- Train/test chronology and walk-forward evaluation
- Max drawdown, volatility, win rate, and benchmark returns
- Distinguishing evidence from overfitting

## Files to inspect or create

- `src/wallstreet/evaluation.py` (new)
- `tests/test_evaluation.py` (new)
- `docs/RESEARCH_RULES.md` (new)

## Build it yourself — step by step

1. Divide historical dates into an earlier development period and later untouched evaluation period. Never shuffle a time series at random.
2. Write clear definitions for total return, percentage drawdown, maximum drawdown, number of trades, win rate, and transaction costs.
3. Calculate these from the actual backtest ledger. Decide how to treat open positions when computing win rate rather than guessing.
4. Compare strategies against buy-and-hold and cash, using the same starting capital and dates.
5. Run a simple walk-forward exercise: choose parameters on one historical window and evaluate on the next without tuning them using that future window.
6. Test bad scenarios, including a fast drop, no price movement, high fees, and a long period where HOLD is optimal.
7. Write an honest one-page report: what worked, what did not, data gaps, hidden assumptions, and reasons not to deploy.
8. Record every strategy parameter set tried to reduce selective reporting.

## Concrete example

A strategy returns +8% but its benchmark returns +12% over the same period. The strategy did **not** outperform just because it made money.

## Tests to write

- [ ] Flat equity produces zero drawdown.
- [ ] A known peak-to-trough fixture produces the correct max drawdown.
- [ ] Chronological split never overlaps evaluation dates.
- [ ] Fees are deducted consistently.
- [ ] A test can intentionally demonstrate a strategy losing to HOLD.

## Acceptance checklist

- [ ] I can explain what out-of-sample means.
- [ ] Reports show losses and limitations, not just wins.
- [ ] Performance is compared to appropriate benchmarks.

## Common pitfall

Do not keep tuning to the evaluation period until the chart looks good. That turns the 'test' into another training set.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

