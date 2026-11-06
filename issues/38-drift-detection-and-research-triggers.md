# 38 — Detect market/model drift and schedule AI research only when warranted

**Track:** H · AI-guided improvement  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Complete issues 23–35 and 37 first.

## Why we're doing this

A market changes and old model relationships may weaken. That doesn't mean an agent should retrain or rewrite code every hour. Drift monitoring should identify changes worth investigating while avoiding churn and inference costs.

## Python and market concepts you'll practice

- Distribution shift versus prediction error
- Rolling windows and alert thresholds
- Scheduled jobs, cooldowns, and free-inference budgets

## Files to inspect or create

- `src/wallstreet/monitoring/drift.py` (new)
- `tests/test_drift.py` (new)
- `docs/AI_AGENT_RUNBOOK.md` (extend)

## Build it yourself — step by step

1. Choose a small set of monitored values: volatility regime frequency, feature missingness, model calibration drift, strategy drawdown, and recent turnover.
2. Define baseline windows and current windows using only data available at each time; use simple comparisons before advanced statistical drift tests.
3. Set explicit thresholds with a minimum sample size and a cooldown (for example no duplicate research request about the same event within seven days).
4. Separate `market changed` from `model degraded`: the first is a difference in data, while the second requires enough outcomes to evaluate predictions.
5. Record drift events, source evidence, severity, and suggested research topic. Do not interpret every alert as a trading signal.
6. Schedule a short GitHub Action that checks drift daily or less often. If quota is exhausted, stop and report, without buying inference.
7. Trigger an AI **proposal** only when sufficient data and risk thresholds justify review; the agent never edits the running strategy directly.
8. Require HOLD/rejection when essential data is stale, even if the drift detector itself fails.
9. Test a real shift, noisy temporary spike, missing data, repeated event, and insufficient sample.

## Worked example

Volatility doubles for two sessions, but only three observations are available. The system records a warning; it should not instantly rebuild the algorithm. After sufficient evidence and cooldown, it may request a research proposal.

## Tests to write

- [ ] Insufficient samples don't create confident drift claims.
- [ ] Cooldown prevents duplicate AI runs.
- [ ] No paid inference occurs beyond budget.
- [ ] A failed monitor doesn't permit unsafe trades.
- [ ] A drift alert is not an order or automatic model replacement.

## Acceptance criteria

- [ ] Drift records have timestamps, evidence, and severity.
- [ ] Research triggers are bounded and explainable.
- [ ] AI usage remains within the $0 plan.

## Common mistake to avoid

Overreacting to every change is itself a way to overfit. Frequent retraining can make the model chase noise.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

