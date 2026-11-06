# 13 — Write explainable BUY, SELL, and HOLD signals without placing orders

**Phase:** C · Analysis  
**Estimated learning time:** 4–6 hours  
**Prerequisite:** Finish issue 12 first.

## Why we're doing this

Research results and money-moving actions should be separate. A signal is an opinion produced by a testable rule; an order is a request sent to a broker. Learning this separation prevents an AI response from placing a trade.

## What you'll learn

- Enums, pure functions, conditional logic
- Strategy inputs versus decisions versus execution
- Explicit reasons and minimum-data checks

## Files to inspect or create

- `src/wallstreet/strategies.py` (new)
- `src/wallstreet/models.py` (extend)
- `tests/test_strategies.py` (new)

## Build it yourself — step by step

1. Define a small `Action` enum with `BUY`, `SELL`, and `HOLD` and a `Signal` dataclass with symbol, decision time, action, reason, and the input data version/IDs.
2. Choose one beginner strategy, such as comparing a short and a long moving average. Write its rule as plain English before coding.
3. Implement the strategy as a pure function that receives already collected historical data. Do not fetch data or call a broker inside it.
4. If either average is unavailable, the timestamp is stale, or a quality check fails, return HOLD with a specific reason.
5. Make decisions only from bars known at the decision timestamp; never peek at the next price.
6. Add a second simple strategy only after the first has tests. Keep a clear interface so future experiments can be compared.
7. Log signals in a way that can be reproduced without an LLM.
8. Add `signals --symbol ... --as-of ...` CLI output showing action and human-readable reason.

## Concrete example

Five valid closes but a requested 20-day average → HOLD (`not enough historical data`). A valid bullish crossover → BUY signal, **not** a submitted order.

## Tests to write

- [ ] Missing and stale data result in HOLD.
- [ ] Known crossover fixture produces the expected action.
- [ ] Strategy never performs network I/O.
- [ ] A future price added to the fixture does not affect an earlier decision.
- [ ] Every result has a nonempty reason.

## Acceptance checklist

- [ ] I can explain what a pure function is.
- [ ] Signals are separate from orders.
- [ ] Tests prove the strategy can't use future data.

## Common pitfall

A strategy can appear correct on one example and still lose money. Do not optimize parameters on the same data used for evaluation.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

