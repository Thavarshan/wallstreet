# 19 — Produce a daily research and paper-portfolio report

**Phase:** D · Safe simulation  
**Estimated learning time:** 4–7 hours  
**Prerequisite:** Finish issue 18 first.

## Why we're doing this

You need to learn whether the bot is working without staring at logs. A short evidence-backed report is more useful than a flashy chart that hides bad data or losses.

## What you'll learn

- Formatting tables and dates, separation of calculation and display
- Readable Markdown/JSON output
- Warnings for missing inputs and reporting accuracy

## Files to inspect or create

- `src/wallstreet/reporting.py` (new)
- `tests/test_reporting.py` (new)
- `docs/REPORT_EXAMPLE.md` (new)

## Build it yourself — step by step

1. Define the intended report sections: date/timezone, data freshness, market summary, benchmark, signals, rejected orders, paper fills, portfolio cash/holdings, P&L, and known gaps.
2. Build a report model from previously stored data. Reports should never fetch live prices unpredictably while formatting.
3. Output Markdown first, optionally JSON later. Show both amounts and percentages with consistent currency symbols and rounding.
4. Include links or identifiers for source records and explain why every BUY/SELL/HOLD signal was produced.
5. Distinguish realized, unrealized, and total equity changes. If something is unavailable, print `unavailable` with a reason rather than zero.
6. Display provider/API outages, stale data, AI inference fallback, and quota exhaustion in a prominent warning section.
7. Create a `report --date YYYY-MM-DD --output report.md` CLI option with explicit date handling.
8. Write snapshot-like tests for a small synthetic portfolio and a deliberately incomplete data day.

## Concrete example

`Paper portfolio: cash $800, holdings $210, total equity $1,010; realized P&L $0, unrealized P&L $10` plus a warning if the latest price is stale.

## Tests to write

- [ ] Same frozen inputs produce the same report.
- [ ] Missing prices are visible warnings.
- [ ] A losing day shows a negative sign correctly.
- [ ] Markdown escapes external article text safely.
- [ ] Paper money is never described as cash available for real withdrawal.

## Acceptance checklist

- [ ] I can read one report and explain every number.
- [ ] Report generation works offline.
- [ ] A sample report includes a loss or failure case.

## Common pitfall

Do not send personal financial data to a public GitHub issue, public artifact, or publicly accessible dashboard.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

