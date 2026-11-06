# 23 — Build point-in-time market feature snapshots

**Track:** F · Market movement analyzer  
**Estimated learning time:** 5–8 hours  
**Prerequisite:** Complete issues 06, 09, 11, 12, and 15 first.

## Why we're doing this

A market analyzer needs inputs such as returns, volume, and news sentiment. The hardest part is making sure every input really existed when a historical decision was made. Without this rule, the analyzer can appear almost magically accurate because it secretly knows the future.

## Python and market concepts you'll practice

- Feature engineering: transforming observations into measurable inputs
- As-of timestamps, event time versus collection time, and reproducible snapshots
- Pure functions and lightweight typed models

## Files to inspect or create

- `src/wallstreet/analysis/features.py` (new)
- `src/wallstreet/models.py` (extend)
- `tests/test_features.py` (new)
- `docs/ADVANCED_RESEARCH.md` (read)

## Build it yourself — step by step

1. Define a `FeatureSnapshot` model with symbol, `as_of`, calculation version, input IDs, feature values, and validity warnings. Begin with no machine learning.
2. Choose three simple features: previous-day percentage return, rolling average volume, and distance from a moving average. Write their formulas in a comment or documentation.
3. Implement a function that receives an ordered sequence of already validated price bars and an `as_of` time. It must **not** call the internet.
4. Select only bars whose information was published or available by `as_of`. Exclude bars whose timestamps are after the requested decision time.
5. Return an explicit `unavailable` or `UNKNOWN` state when too few bars exist; do not replace missing values with zero.
6. Attach the source record IDs, their availability timestamps, and calculation version. This is how you reproduce old research after the dataset changes.
7. Add a second function that serializes the snapshot into small JSON suitable for a report or later AI prompt.
8. Build fixed-time tests where an extra future price exists in storage; prove it cannot influence a snapshot from an earlier date.
9. Document why a feature snapshot belongs between data collection and strategy decisions.

## Worked example

If the analyzer runs `as_of=2026-10-01` and the dataset also contains a bar dated October 2, the October 1 snapshot must be identical whether October 2 exists or not.

## Tests to write

- [ ] All output features have a documented calculation and units.
- [ ] Future observations do not affect earlier snapshots.
- [ ] Missing lookback history returns unavailable with a reason.
- [ ] Same inputs and version produce exactly the same result.
- [ ] Malformed timestamps are rejected rather than guessed.

## Hourly price extension

A feature snapshot at **10:17 New York time** may only include a particular hourly closing bar if that bar was **fully completed, validated and accessible** by 10:17. Its `bar_start_utc` is **not** necessarily its availability time.

1. Include `timeframe` and `feed` in every hourly feature and source-record ID.
2. Require `available_at <= as_of` when known; otherwise apply the documented conservative availability policy from issues 06 and 09.
3. Keep daily and hourly lookbacks separate; use explicit units like `5 completed hourly bars` rather than ambiguous `5 periods`.

**Extra tests:** a record published after `as_of` is excluded even if its bar timestamp is earlier; mixing daily and hourly source IDs is rejected.

## Acceptance criteria

- [ ] I can explain `as_of` in my own words.
- [ ] Every snapshot records source IDs and freshness.
- [ ] Unit tests demonstrate no future-data leakage.

## Common mistake to avoid

Don't confuse the timestamp of a price bar with the time an API made it available. For filings and news these can differ by hours or days.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.
