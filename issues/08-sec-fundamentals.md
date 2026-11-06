# 08 — Read company fundamentals from SEC EDGAR without guessing

**Phase:** B · Trusted datasets  
**Estimated learning time:** 4–7 hours  
**Prerequisite:** Finish issue 07 first.

## Why we're doing this

Price charts alone don't explain a business. Official filings help you learn the difference between revenue, profit, and cash flow, while teaching you to handle irregular real-world data.

## What you'll learn

- Nested JSON and company identifiers (CIK versus ticker)
- Financial periods, units, filing dates, and revisions
- Official API etiquette (User-Agent, request pacing)

## Files to inspect or create

- `src/wallstreet/collectors/fundamentals.py` (new)
- `tests/test_fundamentals.py` (new)
- `docs/DATA_SOURCES.md` (extend)

## Build it yourself — step by step

1. Read SEC EDGAR companyfacts documentation and access rules, including the required descriptive User-Agent. Do not send unnecessary requests.
2. Map one ticker to its official company identifier (CIK); validate it rather than guessing CIK from a symbol.
3. For one company, extract a limited set of facts such as revenue and net income. Keep original taxonomy name and units alongside the values.
4. Understand `start`, `end`, `filed`, fiscal year, and form type (10-K versus 10-Q). Explain why they are not interchangeable.
5. Store both financial period end and filing publication date. An earnings figure must not enter a backtest before it was publicly filed.
6. Handle restatements and multiple facts for the same reporting period by retaining enough version information to reproduce what was known then.
7. Write tests using a miniature synthetic companyfacts fixture and one intentionally missing concept.
8. Add a CLI view that prints a short facts table, including the filing date.

## Concrete example

A fact covers the quarter ending March 31 but was filed May 7. A hypothetical April 15 strategy run must not see that fact.

## Tests to write

- [ ] Missing concepts are reported as unavailable, not zero.
- [ ] USD and shares units remain distinct.
- [ ] Filing date is preserved and gates point-in-time usage.
- [ ] Duplicate facts or amended filings are deterministic.
- [ ] HTTP failures don't erase previously stored facts.

## Acceptance checklist

- [ ] I can explain the difference between a report period and its public filing date.
- [ ] One company's facts can be inspected from the CLI.
- [ ] Source and EDGAR access rules are documented.

## Common pitfall

Don't confuse yearly and quarterly values. A new fiscal period or restatement can change the meaning of apparently identical numbers.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

