# 31 — Select strategy parameters with walk-forward testing and no future leakage

**Track:** G · Adaptive strategy lab  
**Estimated learning time:** 8–12 hours  
**Prerequisite:** Complete issues 15, 28, and 29 first.

## Why we're doing this

If you try hundreds of parameter combinations and celebrate the best historical chart, you are likely fitting noise. Walk-forward testing is a disciplined way to choose settings using past data and then test on later untouched data.

## Python and market concepts you'll practice

- Rolling/expanding time windows
- Hyperparameter search and nested chronological evaluation
- Search budgets and experiment reproducibility

## Files to inspect or create

- `src/wallstreet/research/walk_forward.py` (new)
- `tests/test_walk_forward.py` (new)
- `docs/EXPERIMENT_TEMPLATE.md` (use)

## Build it yourself — step by step

1. Draw a timeline with separate training, validation, and final evaluation periods. Make the periods explicit in code and report them.
2. Define a small, pre-declared set of candidate parameters (for example 3 moving-average pairs), not an unbounded grid search.
3. For each walk-forward fold, select parameters using only its earlier training/validation window, then evaluate once on the next unseen interval.
4. If labels or features overlap boundaries, leave a gap appropriate to the observation horizon. Read the official scikit-learn `TimeSeriesSplit` documentation.
5. Include a strategy with no tuning as a baseline and ensure all variants use the same prices and cost assumptions.
6. Record *every* attempted configuration, not only the winner. Add a fixed random seed if you use any stochastic model.
7. Aggregate fold results by return, drawdown, volatility, trade count, fees, and number of failed folds. Don't average percentages incorrectly.
8. Reserve a final untouched holdout that cannot be used to adjust parameters.
9. Report whether the tuned strategy remains better after costs and whether results are stable across windows.

## Worked example

Fit on January–June, choose settings using July, evaluate August; then roll forward. A choice made using August outcomes cannot be credited to a strategy that supposedly traded in August.

## Tests to write

- [ ] Training dates precede evaluation dates in every fold.
- [ ] No labels cross a split gap when horizon overlaps.
- [ ] Parameter search is bounded.
- [ ] Replaying a fixed seed reproduces the same result.
- [ ] A toy dataset designed to overfit is caught by the holdout.

## Acceptance criteria

- [ ] Every result includes its fold date ranges.
- [ ] Untouched test performance is reported separately.
- [ ] The chosen settings can be reproduced from logs.

## Common mistake to avoid

Don't rerun the 'untouched' evaluation repeatedly and keep tuning until it looks good. You have then converted it into another validation set.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

