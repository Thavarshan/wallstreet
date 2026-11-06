# 26 — Measure market breadth and relative sector strength

**Track:** F · Market movement analyzer  
**Estimated learning time:** 5–9 hours  
**Prerequisite:** Complete issues 23–25 first.

## Why we're doing this

A major index can rise while only a few large companies do well. Breadth asks how many stocks participate; relative strength asks which sectors are leading or lagging. These help describe broad market movement without making unfounded trades.

## Python and market concepts you'll practice

- Aggregating multiple symbols over aligned dates
- Equal-weighted measures versus market-cap-weighted indexes
- Universe changes and survivorship bias

## Files to inspect or create

- `src/wallstreet/analysis/breadth.py` (new)
- `tests/test_breadth.py` (new)
- `docs/DATA_SOURCES.md` (extend)

## Build it yourself — step by step

1. Start with a tiny, explicitly fixed universe of 5–10 synthetic symbols. Document the universe selection date and limitations.
2. For each completed trading session, count symbols with close above their own moving average; divide by the number of symbols with enough valid data.
3. Track the numerator and denominator, not just the percentage. Make missing prices visible so breadth doesn't silently improve when bad performers disappear.
4. Choose a small set of sector ETFs only if a free licensed data source supports them. Calculate their returns relative to a broad benchmark over the same calendar window.
5. Normalize dates across symbols; handle holidays, halted symbols, and different listing dates explicitly.
6. Create a report with breadth, sector relative strength, data coverage, and uncertainty warnings. No automatic orders.
7. Test the effect of a single giant stock move and a missing symbol; breadth should count participation, not dollar contribution.
8. Explain survivorship bias: historical results using only today's surviving stocks can be too optimistic.
9. Decide whether the free API quota supports the universe. Keep it small if it doesn't.

## Worked example

If 7 of 10 eligible stocks are above their 20-day average, breadth is 70%. If data exists for only 7 of the 10, do not report 7/7 as 100% without showing the coverage change.

## Tests to write

- [ ] Numerator and denominator are correct.
- [ ] Missing symbols are reported, not silently dropped.
- [ ] Duplicate symbols aren't double-counted.
- [ ] Sector comparisons use aligned dates.
- [ ] A too-small universe yields insufficient-data warnings.

## Acceptance criteria

- [ ] Breadth reports show coverage and uncertainty.
- [ ] Sector results are benchmark-relative rather than just absolute.
- [ ] The analysis fits verified free-data quotas.

## Common mistake to avoid

A sector ETF is an approximation of sector performance, not a definitive list of constituent stock movements. Document that shortcut.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

