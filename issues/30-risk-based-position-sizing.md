# 30 — Size portfolio positions using a fixed risk budget

**Track:** G · Adaptive strategy lab  
**Estimated learning time:** 6–9 hours  
**Prerequisite:** Complete issues 16, 18, and 29 first.

## Why we're doing this

Even a promising signal can be a bad trade if it uses too much capital. Position sizing asks how much to buy while preserving cash, diversification, and maximum exposure limits.

## Python and market concepts you'll practice

- Percentages and portfolio allocation arithmetic
- Rounding order quantities and price precision
- Separation of risk budget from predicted returns

## Files to inspect or create

- `src/wallstreet/sizing.py` (new)
- `tests/test_position_sizing.py` (new)
- `docs/RISK_POLICY.md` (extend)

## Build it yourself — step by step

1. Define a small risk budget in configuration: maximum single-position percentage, maximum sector exposure, minimum cash reserve, and a strict no-leverage rule.
2. Write a pure function that receives current cash, portfolio equity, existing holdings, estimated execution price, and the approved signal. It returns a proposed quantity or an abstention reason.
3. Begin with deterministic fixed-fraction sizing (e.g., at most 5% equity per position in a toy example), not leveraged volatility targeting.
4. Apply concentration limits and cash reserve checks to existing plus proposed exposure, not just the new purchase.
5. Handle exchange lot sizes, whole/fractional share availability, rounding down, currency differences, and unknown prices.
6. Test high-volatility regimes with a smaller *configured* maximum exposure, but do not silently change the risk ceiling based on AI advice.
7. Route proposals through the independent risk checker; it remains authoritative.
8. Compare turnover and concentration of fixed-size versus size-aware strategies in backtests with fees.
9. Document how a prediction can be correct but still fail to justify a costly trade.

## Worked example

Portfolio equity $1,000, 5% position cap, one stock already worth $30, estimated purchase price $10. The most you may add under the cap is $20 (2 shares) before other constraints.

## Tests to write

- [ ] Size never exceeds remaining cash or concentration cap.
- [ ] Quantity rounds down, never up beyond the budget.
- [ ] Unknown or non-positive price returns no trade.
- [ ] Higher volatility policy cannot accidentally raise exposure.
- [ ] Risk engine rejects a proposal regardless of sizing output.

## Acceptance criteria

- [ ] I can work through sizing math by hand.
- [ ] No borrowing or shorting is possible.
- [ ] Allocation limits hold across multiple positions.

## Common mistake to avoid

Risk budgets reduce some losses; they do not eliminate market risk or guarantee that the account can't fall sharply.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

