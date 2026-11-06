# 28 — Build and calibrate a simple market-direction prediction model

**Track:** G · Adaptive strategy lab  
**Estimated learning time:** 8–12 hours  
**Prerequisite:** Complete issues 15 and 23–25 first.

## Why we're doing this

An actual prediction model lets you test whether market features contain information about next-session movement. But a model saying '70% up' is useful only if events assigned about 70% probability really happen about 70% of the time.

## Python and market concepts you'll practice

- Features and labels for supervised learning
- Training/validation/test splits for time series
- Probability calibration and 'no prediction' states

## Files to inspect or create

- `src/wallstreet/analysis/direction_model.py` (new)
- `src/wallstreet/research/forecast_evaluation.py` (new)
- `tests/test_direction_model.py` (new)

## Build it yourself — step by step

1. Define one precise target, such as whether the **next completed session's close-to-close return** is positive. Record target horizon and the earliest time its truth becomes known.
2. Create training examples using only feature snapshots from issue 23. Every row needs its `as_of` and an outcome that occurs later.
3. Begin with a trivial baseline: predict the historical majority class. Then add a simple logistic regression model using scikit-learn; do not start with deep learning.
4. Split training, validation, and untouched test dates chronologically. Consider [scikit-learn's `TimeSeriesSplit`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) and its `gap` parameter if windows overlap. Never randomly shuffle rows.
5. Fit normalization/scaling on training data only. Applying scalers fitted on all data would leak future information.
6. Evaluate classification accuracy *and* a proper probability score such as Brier score. Make a reliability table of predicted probability ranges versus observed frequencies.
7. Add a minimum-data requirement and an `UNKNOWN` or abstain result when confidence or data quality is inadequate.
8. Record model version, feature version, data range, and prediction time. Compare with the majority baseline and a simple price-only rule.
9. Write a report showing losses, calibration errors, and why prediction accuracy is not the same as trading profit.

## Worked example

Across 100 untouched test cases where the model predicts about 0.70 probability of an up day, roughly 70 should actually be up for that bucket to be well calibrated. Ten examples are too few to establish this reliably.

## Tests to write

- [ ] Next-day label is never accessible to same-day features.
- [ ] Scaling uses training rows only.
- [ ] A constant predictor is included as a baseline.
- [ ] Prediction returns a bounded probability or UNKNOWN.
- [ ] Results can be reproduced from recorded data/model versions.

## Hourly price extension (optional advanced experiment)

Keep the **next-day** prediction task as your first model. Once your daily experiment is sound, test **next-completed-hour direction** as a *separate* experiment—not as a silent change to the original label.

1. Freeze one exact hourly horizon and feature availability time. All features must have been usable **before** the future outcome interval.
2. Split data chronologically by trading session; leave a gap where overlapping rolling windows could leak information.
3. Compare against an hourly majority-class/always-HOLD baseline and include fees, spreads and missing IEX bars.
4. Record `timeframe=1Hour`, `feed=iex`, coverage dates and model version. Explain that IEX-only coverage may bias apparent performance.
5. The AI can propose strategies for **review**, never edit risk rules or place real orders automatically.

**Extra tests:** next-hour labels cannot be read by current-hour features; a market-closed gap isn't labeled as a zero return; missing hourly data produces UNKNOWN.

## Acceptance criteria

- [ ] Model output is an uncertainty estimate, not a BUY instruction.
- [ ] Evaluation includes out-of-sample accuracy and calibration.
- [ ] No model prediction places a brokerage order.

## Common mistake to avoid

A confident probability from an uncalibrated model is not a measured likelihood. Most slight market moves may be overwhelmed by trading costs.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.
