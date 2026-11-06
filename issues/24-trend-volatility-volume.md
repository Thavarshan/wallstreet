# 24 — Analyze trend, volatility, and abnormal trading volume

**Track:** F · Market movement analyzer  
**Estimated learning time:** 5–8 hours  
**Prerequisite:** Complete issue 23 first.

## Why we're doing this

A single price change tells very little about market behavior. Trend describes direction, volatility describes the size of changes, and unusual volume can show that a move happened with more participation than normal. Each measure can still be noisy.

## Python and market concepts you'll practice

- Log/simple returns, rolling standard deviation, and rolling baselines
- The difference between a price movement and a prediction
- Normalizing features so values can be compared across securities

## Files to inspect or create

- `src/wallstreet/analysis/movement.py` (new)
- `tests/test_movement.py` (new)

## Build it yourself — step by step

1. Take a tiny synthetic sequence of daily closes and calculate simple daily returns by hand. Decide whether you will use percentage or decimal return consistently.
2. Implement a trend measure such as close relative to 20-day moving average and a short/long moving average slope; don't add ten indicators just to look sophisticated.
3. Implement realized volatility from a rolling standard deviation of daily returns. State your lookback window and whether values are annualized.
4. Compute a relative volume measure: today's observed volume divided by average volume over a **prior** window. Exclude today's volume from the baseline to avoid changing the comparison after the fact.
5. Optionally add average true range once you understand high/low/previous-close relationships; do not depend on undocumented indicator packages.
6. Normalize numbers and keep units in output (`0.02` return means 2%, not 0.02%).
7. Produce a small readable report for a few dates containing trend, volatility, volume ratio, and unavailable warnings.
8. Test constant prices, one big jump, missing trading days, zero volume baseline, and a rolling window shorter than requested.
9. Explain how each metric could become an input to a regime detector, without turning it into a BUY signal yet.

## Worked example

If recent closes are `[100, 102, 101, 105]`, daily returns are approximately +2%, −0.98%, +3.96%. Higher volatility describes the variation; it does not prove the next return.

## Tests to write

- [ ] Known hand-calculated returns match.
- [ ] Constant-price series has zero realized volatility where defined.
- [ ] Volume ratio uses the correct prior window.
- [ ] Short series returns unavailable, not fabricated values.
- [ ] No external network calls occur.

## Hourly price extension

After daily movement calculations work, allow a `1Hour` data series **separately**. A `20-bar` trend will then mean 20 **completed market-hour bars**, not 20 days. Do not use 24 clock hours to mean one US trading day.

1. Require the same `provider`, `feed` and `timeframe` throughout each calculation.
2. Check quality flags from issue 09 and refuse stale, incomplete or fabricated hours.
3. Report intraday volume ratios only against comparable windows; IEX volume represents activity on **one exchange**, not all US trading.
4. Label output units (`hourly return`, `per-hour volatility`) and avoid applying daily annualization rules to hourly results.

**Extra tests:** no weekend placeholders enter rolling windows; `1Hour` and `1Day` outputs differ when fed different fixtures; an absent IEX bar returns unavailable.

## Acceptance criteria

- [ ] A movement report explains direction, turbulence, and volume separately.
- [ ] All formulas and lookback periods are documented.
- [ ] Edge cases have unit tests.

## Common mistake to avoid

Don't equate high volatility with an opportunity to profit. High volatility can increase losses and execution costs.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.
