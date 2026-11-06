# Learning roadmap

Do these in order. The **issue numbers are the intended learning sequence**, not a demand to finish everything immediately.

| Phase | Issues | Outcome |
| --- | --- | --- |
| A. Python foundations | 01–03 | Run a CLI, understand collections and functions, write tests |
| B. Build trusted datasets | 04–10 | Store price/news/filings data and refresh it safely |
| C. Think before trading | 11–15 | Analyze patterns, label news, test strategies honestly |
| D. Simulate safely | 16–19 | Risk rules, paper broker, portfolio and reports |
| E. Observe and assess | 20–22 | Dashboard, operations, international broker readiness |

## Issue index

### A. Python foundations

1. [#1 — Set up Python and tests](https://github.com/Thavarshan/wallstreet/issues/1)
2. [#2 — Build your first command-line interface](https://github.com/Thavarshan/wallstreet/issues/2)
3. [#3 — Learn dictionaries, lists, dataclasses, and validation](https://github.com/Thavarshan/wallstreet/issues/3)

### B. Trusted datasets

4. [#4 — Store records in SQLite](https://github.com/Thavarshan/wallstreet/issues/4)
5. [#5 — Fetch HTTP data safely](https://github.com/Thavarshan/wallstreet/issues/5)
6. [#6 — Collect daily stock prices](https://github.com/Thavarshan/wallstreet/issues/6)
7. [#7 — Collect financial news with RSS](https://github.com/Thavarshan/wallstreet/issues/7)
8. [#8 — Read fundamentals from SEC filings](https://github.com/Thavarshan/wallstreet/issues/8)
9. [#9 — Check data quality and market calendars](https://github.com/Thavarshan/wallstreet/issues/9)
10. [#10 — Schedule collection with GitHub Actions](https://github.com/Thavarshan/wallstreet/issues/10)

### C. Analysis and honest backtesting

11. [#11 — Calculate indicators and a buy-and-hold baseline](https://github.com/Thavarshan/wallstreet/issues/11)
12. [#12 — Analyze headlines with a baseline and optional free AI](https://github.com/Thavarshan/wallstreet/issues/12)
13. [#13 — Create explainable BUY/SELL/HOLD signals](https://github.com/Thavarshan/wallstreet/issues/13)
14. [#14 — Build a realistic backtesting engine](https://github.com/Thavarshan/wallstreet/issues/14)
15. [#15 — Evaluate out-of-sample performance](https://github.com/Thavarshan/wallstreet/issues/15)

### D. Paper trading

16. [#16 — Add independent risk controls](https://github.com/Thavarshan/wallstreet/issues/16)
17. [#17 — Connect a paper-only broker](https://github.com/Thavarshan/wallstreet/issues/17)
18. [#18 — Track portfolio positions and profit accurately](https://github.com/Thavarshan/wallstreet/issues/18)
19. [#19 — Generate daily reports](https://github.com/Thavarshan/wallstreet/issues/19)

### E. Operations and feasibility

20. [#20 — Make a read-only Cloudflare dashboard](https://github.com/Thavarshan/wallstreet/issues/20)
21. [#21 — Monitor reliability, security, and $0 usage](https://github.com/Thavarshan/wallstreet/issues/21)
22. [#22 — Research broker, Wise, and withdrawal readiness](https://github.com/Thavarshan/wallstreet/issues/22)

### Progress tracking

- [ ] Phase A — Python foundations
- [ ] Phase B — trusted datasets
- [ ] Phase C — analysis and backtesting
- [ ] Phase D — paper trading
- [ ] Phase E — dashboard and readiness review

**Suggested pace:** one or two issues per week. Take longer when a Python concept is new. The goal is *skill gained*, not tickets closed.

### Milestone gates

After Phase B, you should be able to answer where every data point came from and whether it was available at the time.

After Phase C, your strategy must beat a naive baseline on honest out-of-sample tests to justify paper experiments; if it does not, improve the research, not the claims.

After Phase D, run paper trading for long enough to observe different market conditions. Keep results separate from backtests and include fees/slippage assumptions. A positive paper result is not proof of future live profits.

Phase E is an **investigate-and-document** milestone. It never switches live trading on by itself.
