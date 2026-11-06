# 11 — Calculate simple indicators and a buy-and-hold benchmark

**Phase:** C · Analysis  
**Estimated learning time:** 4–6 hours  
**Prerequisite:** Finish issue 10 first.

## Why we're doing this

Before adding AI, learn what the market series says mathematically. A baseline shows whether your system is doing better than simply buying an index or holding cash.

## What you'll learn

- Means, percentages, rolling windows, missing values
- `pandas` basics introduced gradually
- Why the first rolling values may be unavailable

## Files to inspect or create

- `src/wallstreet/analysis/indicators.py` (new)
- `src/wallstreet/analysis/benchmark.py` (new)
- `tests/test_indicators.py` (new)

## Build it yourself — step by step

1. Begin with a five-day moving average using a plain Python loop. Write down the formula and work through five small numbers by hand.
2. Then implement the same calculation with `pandas` and compare the results. Learn `Series`, `.rolling()`, and how missing initial values appear.
3. Add a daily percentage return formula `(today / previous_day) - 1`. Validate that the previous price is positive.
4. Implement a longer moving average (such as 20 days) and document why a short dataset cannot produce it.
5. Create a buy-and-hold benchmark: start with an imaginary balance, buy a fixed quantity at a permitted historical date, and mark its value at each subsequent close. Account for dividends/corporate actions if the chosen dataset supports them.
6. Use unadjusted or adjusted prices consistently, and clearly document the return convention.
7. Print a small table containing date, close, moving average, daily return, and benchmark equity.
8. Test the calculations against an easy five-number series with manually known results.

## Concrete example

Closes `[10, 12, 14, 16, 18]` have a five-day mean of `14`; the fourth-to-fifth daily return is `18/16 - 1 = 0.125` (12.5%).

## Tests to write

- [ ] Hand-computed moving average matches code.
- [ ] Too few data points yield an explicit unavailable result.
- [ ] Zero or negative denominator cannot produce a nonsense return.
- [ ] Output dates match input dates with no future shift.
- [ ] Pandas and plain Python versions agree.

## Acceptance checklist

- [ ] I can explain a moving average without referring to a library.
- [ ] A small benchmark can be reproduced from fixture data.
- [ ] No inference model is involved.

## Common pitfall

Don't treat a moving average as a guarantee that the next price will rise. Indicators summarize history; they do not know the future.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

