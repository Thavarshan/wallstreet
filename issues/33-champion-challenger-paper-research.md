# 33 — Compare the current strategy with a paper-only challenger

**Track:** G · Adaptive strategy lab  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Complete issues 17–19 and 29–32 first.

## Why we're doing this

When you discover a promising new algorithm, replacing the existing one immediately would erase the evidence of which actually performs better. A champion–challenger setup runs both over the same market period with separate simulated ledgers.

## Python and market concepts you'll practice

- Experiment identity and versioned configurations
- Controlled comparisons and forward testing
- Metrics, sample size, and human review

## Files to inspect or create

- `src/wallstreet/research/experiments.py` (new)
- `src/wallstreet/paper/challenger.py` (new)
- `tests/test_champion_challenger.py` (new)

## Build it yourself — step by step

1. Define `champion` (currently approved paper strategy) and `challenger` (candidate) with immutable version IDs and configurations.
2. Create separate simulated portfolios for both, with the same starting capital, permitted symbols, market data timestamps, fee rules, and period.
3. Route both strategies through independent but identical risk checks. Neither may place real orders.
4. Record each candidate's signals, intended orders, fills, equity series, drawdowns, fees, and missed data points.
5. Generate a daily side-by-side report and include cash and buy-and-hold benchmarks for the same dates.
6. Decide the comparison criteria in an experiment note *before* the forward run. Include minimum observation count and reasons to reject.
7. Keep a challenger that underperforms visible instead of deleting its record.
8. Add a review state: `PROPOSED`, `PAPER_TESTING`, `NEEDS_MORE_EVIDENCE`, `REJECTED`, `APPROVED_FOR_PAPER`. Approval is a manual action.
9. Simulate promoting a challenger to paper champion and reversing it without touching real brokerage accounts.

## Worked example

Both strategies start with $1,000 virtual cash on the same date. One ends with $1,040 and 15% drawdown, the other with $1,030 and 3% drawdown. The decision is not simply 'pick $1,040'; compare risk and costs.

## Tests to write

- [ ] Champion and challenger ledgers never mix.
- [ ] Both see identical data availability cutoffs.
- [ ] Approval state cannot be set by AI output alone.
- [ ] A rollback restores previous paper configuration.
- [ ] No real-order endpoint is reachable.

## Acceptance criteria

- [ ] I can compare candidate algorithms fairly over the same interval.
- [ ] Every strategy has a version and human review history.
- [ ] No automatic live-strategy replacement occurs.

## Common mistake to avoid

A few weeks of paper outperformance may be luck. Never imply a small sample validates persistent income.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

