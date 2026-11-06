# 25 — Classify market regimes and explain why a label changed

**Track:** F · Market movement analyzer  
**Estimated learning time:** 6–9 hours  
**Prerequisite:** Complete issues 23–24 first.

## Why we're doing this

Strategies often behave differently in rising, falling, sideways, calm, and turbulent conditions. A regime label lets you compare those environments explicitly, but changing labels too frequently can produce excessive trading.

## Python and market concepts you'll practice

- Finite-state decisions and thresholds
- Hysteresis: requiring stronger evidence to change a state than to keep it
- UNKNOWN handling, confidence, and explainability

## Files to inspect or create

- `src/wallstreet/analysis/regimes.py` (new)
- `tests/test_regimes.py` (new)
- `docs/REGIMES.md` (new)

## Build it yourself — step by step

1. Define a small regime vocabulary: `TREND_UP`, `TREND_DOWN`, `RANGE`, `UNKNOWN`, and a separate `HIGH_VOLATILITY` flag. Avoid too many overlapping labels.
2. Write a plain-English rule using features from issue 24. Example: trend above a threshold for a minimum number of *completed* sessions, with volatility separately classified.
3. Build the first deterministic classifier with fixed thresholds chosen **before** looking at evaluation results.
4. Implement hysteresis or a minimum holding period for a label so one borderline day does not flip `TREND_UP` to `RANGE` and back.
5. Attach `as_of`, input features, rule version, and a human-readable explanation to each regime decision.
6. Make stale, missing, contradictory, or incomplete data return `UNKNOWN`. A strategy later treats UNKNOWN as HOLD.
7. Create a transition table (previous label, new evidence, next label) and test it using synthetic sequences.
8. Plot or print regime transitions over historical data without overlaying future labels on earlier dates.
9. Compare different threshold settings only using an explicit training window; reserve later dates for honest evaluation.

## Worked example

If the trend score oscillates just above and below 0.01, hysteresis should avoid daily label changes. If the newest bars disappear, result becomes UNKNOWN rather than assuming yesterday's regime continues forever.

## Tests to write

- [ ] Synthetic rising/falling/flat sequences produce expected labels.
- [ ] State switching respects minimum persistence.
- [ ] Missing data yields UNKNOWN.
- [ ] Earlier regime labels do not change when future bars are added.
- [ ] Explanation includes the actual threshold and input values.

## Acceptance criteria

- [ ] I can explain what a regime is and isn't.
- [ ] A deterministic classifier produces reproducible labels.
- [ ] No market regime directly triggers an order.

## Common mistake to avoid

A label about the market *today* isn't a confident forecast about *tomorrow*. Avoid naming regimes `SAFE_TO_BUY` or `GUARANTEED_PROFIT`.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

