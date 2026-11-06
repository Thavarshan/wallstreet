# 29 — Create a strategy algorithm that adapts its rules to market regimes

**Track:** G · Adaptive strategy lab  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Complete issues 13–16 and 25 first.

## Why we're doing this

Instead of blindly using one rule in every market, a strategy router can select among already-tested behaviors based on the current regime. It must decide before seeing the future result and must sometimes do nothing.

## Python and market concepts you'll practice

- Python Protocol or a small common function interface
- Configuration-driven behavior versus rewriting code
- Separate strategy, regime analysis, and risk checks

## Files to inspect or create

- `src/wallstreet/strategy_router.py` (new)
- `src/wallstreet/strategy_config.py` (new)
- `tests/test_strategy_router.py` (new)
- `docs/STRATEGY_CATALOG.md` (new)

## Build it yourself — step by step

1. Define the smallest common strategy interface: input `FeatureSnapshot`, `RegimeResult`, and current positions; output `Signal` with action/reason. It must be a pure computation.
2. Register only previously tested strategies, e.g., a trend-following candidate and an all-cash HOLD fallback. Do not invent a large strategy catalog yet.
3. Write an explicit mapping of regime to strategy in a versioned JSON/YAML configuration, including an `UNKNOWN -> HOLD` rule.
4. Validate configuration against an allowlist of strategy names and bounded parameters. Reject unknown keys and out-of-range risk parameters.
5. Implement the router so each decision records the selected strategy version, regime label, input snapshot ID, and reason.
6. Make sure the router has no capability to submit orders or bypass the existing risk engine. It produces a proposal only.
7. Backtest fixed and regime-routed variants over identical dates and costs. Compare not just return but drawdown and trade count.
8. Test regime transitions, stale features, conflicting labels, and invalid configurations; fail closed with HOLD.
9. Document that switching algorithms can increase overfitting and turnover; don't assume adaptivity improves results.

## Worked example

Regime = `TREND_UP`, configuration selects a tested trend strategy; Regime = `UNKNOWN` selects HOLD. A BUY proposal still fails if the risk engine says exposure is too high.

## Tests to write

- [ ] Every label maps to an allowed strategy or HOLD.
- [ ] Invalid config cannot select unknown code.
- [ ] Risk checks remain mandatory.
- [ ] Decision log contains strategy/config versions.
- [ ] Future regime observations cannot affect earlier selections.

## Acceptance criteria

- [ ] A readable configuration describes the strategy policy.
- [ ] Tests show safe fallback behavior.
- [ ] Backtests compare fixed and adaptive choices honestly.

## Common mistake to avoid

The router should not pick whichever strategy performed best *after* the market moved. That is hindsight, not adaptation.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

