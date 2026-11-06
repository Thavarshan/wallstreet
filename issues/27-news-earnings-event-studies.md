# 27 — Study how markets move around news and earnings events

**Track:** F · Market movement analyzer  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Complete issues 07–09, 15, and 23 first.

## Why we're doing this

A headline alone doesn't prove it caused a price move. An event study asks what happened before and after a publicly timed event, compared with a benchmark, while avoiding hindsight.

## Python and market concepts you'll practice

- Event windows and benchmark-adjusted returns
- Publication time versus event time
- Confounding events and careful causal language

## Files to inspect or create

- `src/wallstreet/research/events.py` (new)
- `tests/test_event_studies.py` (new)
- `docs/EVENT_STUDIES.md` (new)

## Build it yourself — step by step

1. Select only a few clearly time-stamped events from licensed news or official company filings. Define how you identify an event without choosing it because its price result looks exciting.
2. Normalize event publication time and market-session calendar. A story after market close should generally be evaluated from the next tradable session.
3. Choose a window, such as two completed sessions before and five after. Specify the comparison benchmark and whether prices are adjusted.
4. Calculate the stock's return and the benchmark return across the same window, then compute their difference. Keep the calculation simple before considering statistical significance.
5. Group events by category (earnings beats, guidance cuts, product launches) only when labels are defensible and sample sizes are reported.
6. Record overlap: another earnings report or macro announcement within the window can make attribution weak.
7. Show both average results and individual event distributions, including losses and outliers.
8. Do not build a trading rule until enough events exist to evaluate out of sample and realistic execution delay is modeled.
9. Write a short conclusion saying what the data supports and what it cannot establish.

## Worked example

An announcement arrives Tuesday at 5:30 PM New York time. A backtest cannot place a hypothetical Tuesday 4:00 PM trade based on that later announcement.

## Tests to write

- [ ] After-hours events map to the next eligible session.
- [ ] Weekend events do not create fake trading days.
- [ ] Benchmark and stock return windows match.
- [ ] No event data appears in earlier decisions.
- [ ] Small sample size is prominently disclosed.

## Acceptance criteria

- [ ] A report demonstrates event-window calculations with sources.
- [ ] Conflicting events and missing data are visible.
- [ ] No causal or profit guarantee is asserted.

## Common mistake to avoid

A price move around an announcement does not establish causality; other market events may explain it.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

