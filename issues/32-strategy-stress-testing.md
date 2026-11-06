# 32 — Stress-test strategies against crashes, costs, and broken data

**Track:** G · Adaptive strategy lab  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Complete issues 14–16 and 29–31 first.

## Why we're doing this

A strategy that performs beautifully on an average day may fail in a gap-down market, a delayed feed, or an unusually wide spread. Stress testing deliberately explores those bad situations before you trust a paper-trading result.

## Python and market concepts you'll practice

- Scenario-based tests and sensitivity analysis
- Execution assumptions, drawdown, and risk tail events
- Fail-closed handling of infrastructure failures

## Files to inspect or create

- `src/wallstreet/research/stress.py` (new)
- `tests/test_strategy_stress.py` (new)
- `docs/STRESS_SCENARIOS.md` (new)

## Build it yourself — step by step

1. Define synthetic scenarios: sudden price gap down, prolonged downtrend, sideways whipsaw, high spreads, missing candles, news arriving late, and broker partial fills.
2. Run each scenario through the *same* strategy/risk/backtest interfaces. Don't add a special code path that makes stress results look good.
3. Vary costs across reasonable illustrative values and show when a strategy becomes unprofitable. Distinguish assumptions from actual broker quotes.
4. Stress position sizing and maximum loss thresholds. Check that orders are rejected when data quality is unknown.
5. Measure maximum drawdown, largest one-day loss, time spent underwater, worst scenario, and whether the kill switch activated.
6. Record if a strategy wins only under a narrow parameter value; test small neighboring values for sensitivity.
7. Introduce a simulated provider outage and verify the system stops new orders without losing ledger state.
8. Write a report ranking failure modes and engineering fixes separately from strategy research questions.
9. Do not label a worst-case synthetic test as an absolute maximum possible loss.

## Worked example

If average estimated spread grows from 0.02% to 0.50%, a frequent-trading strategy may move from profit to loss. Show both outcomes instead of hiding the higher-cost scenario.

## Tests to write

- [ ] A large gap does not create negative cash through leveraged execution.
- [ ] Stale-data scenario returns HOLD/rejection.
- [ ] Fees are accounted for once per simulated fill.
- [ ] No missing price is filled with a made-up favorable value.
- [ ] Every scenario is deterministic and repeatable.

## Acceptance criteria

- [ ] The strategy has a visible failure-case report.
- [ ] Risk controls are tested under stress.
- [ ] The report does not claim all future crashes have been simulated.

## Common mistake to avoid

No historical or synthetic scenario set can prove that losses are bounded under every future market condition.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

