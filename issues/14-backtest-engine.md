# 14 — Build a tiny historical backtesting engine with realistic costs

**Phase:** C · Analysis  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Finish issue 13 first.

## Why we're doing this

A strategy must be tested on data it could have known at the time. Backtesting helps reject poor ideas before paper trading, but only if fills, cash, and fees are modeled honestly.

## What you'll learn

- State updated across chronological events
- Cash, shares, fees, and next-bar execution
- Deterministic simulations and invariants

## Files to inspect or create

- `src/wallstreet/backtest.py` (new)
- `tests/test_backtest.py` (new)

## Build it yourself — step by step

1. Choose a simple simulation rule: at close of day T calculate a signal using data through T; any simulated buy/sell executes no earlier than a price available on the next trading session. Document your assumption.
2. Start with `cash=1000`, `shares=0`, and a fixed fee/slippage configuration. Model cash and whole shares before adding fractional shares.
3. Loop through historical bars in time order. For each bar, apply a pending order from a previous signal, charge realistic configurable costs, then update equity.
4. Refuse a buy that exceeds available cash. Refuse a sale larger than current holdings. The engine should never invent funds.
5. Record every simulated decision, fill, fee, cash balance, share balance, and equity observation.
6. Add corporate action handling or explicitly block datasets without consistent split/dividend adjustments; never silently combine conflicting price conventions.
7. Compare the simulation with a HOLD-only strategy and a naive buy-and-hold benchmark.
8. Create a five-day hand-worked example and verify each line of the ledger matches calculations.

## Concrete example

Start with $100, buy 1 share at next-session $20 with a $1 fee → cash $79, shares 1. If later marked at $22, equity = $101 before a sell fee (not $102).

## Tests to write

- [ ] Cash never becomes negative without explicitly enabled borrowing (which is forbidden here).
- [ ] No orders execute on the same bar whose close created the signal.
- [ ] Fees reduce equity exactly once.
- [ ] Duplicate input bars don't create duplicate trades.
- [ ] Final equity equals cash plus marked holdings.

## Hourly price extension

Finish the simple daily backtester first. You may later run it on hourly bars collected in issue 06, but an hourly strategy needs **hourly timing rules**:

1. A signal generated from an hour's completed closing bar may fill **no earlier than a later available bar**, never inside the hour it measured.
2. A one-exchange IEX bar is a **research approximation**, not proof that your simulated quantity could have traded at that price. Explain the resulting execution uncertainty.
3. Don't carry `next bar` directly across a weekend or holiday as if markets ran continuously. Use issue 09's trading calendar and refuse unavailable fills.
4. Measure assumed spread, slippage and fees; intraday turnover can make a “profitable” backtest lose money.
5. Keep separate daily versus hourly experiment results, with `timeframe`, `feed`, data ranges and price-adjustment policy in each report.

**Extra tests:** an hourly signal cannot fill on its own bar; missing next-hour data means no invented fill; an overnight/weekend gap does not produce a synthetic trade.

## Acceptance checklist

- [ ] A tiny example can be verified by hand.
- [ ] Backtest results are reproducible.
- [ ] A HOLD strategy submits zero orders.

## Common pitfall

Don't use the day's closing price to generate a signal and pretend you already filled at that same close. That is a common look-ahead error.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.
