# Learning roadmap

Do these in order. The **issue numbers are the intended learning sequence**, not a demand to finish everything immediately.

| Phase | Issues | Outcome |
| --- | --- | --- |
| A. Python foundations | 01–03 | Run a CLI, understand collections and functions, write tests |
| B. Build trusted datasets | 04–10 | Learn to store hourly/daily IEX price bars, news and filings; validate and refresh them safely |
| C. Think before trading | 11–15 | Analyze patterns, label news, test strategies honestly |
| D. Simulate safely | 16–19 | Risk rules, paper broker, portfolio and reports |
| E. Observe and assess | 20–22 | Dashboard, operations, international broker readiness |
| F. Market movement analyzer | 23–27 | Time-aware features, trends, volatility, regimes, breadth, and events |
| G. Adaptive strategy lab | 28–33 | Prediction experiments, regime-based rules, sizing, robustness, and paper challengers |
| H. AI-guided improvement | 34–39 | Safe AI proposals, candidate code PRs, evaluation, drift, approval and rollback |

## Issue index

### A. Python foundations

1. [#1 — Set up Python and tests](https://github.com/Thavarshan/wallstreet/issues/1)
2. [#2 — Build your first command-line interface](https://github.com/Thavarshan/wallstreet/issues/2)
3. [#3 — Learn dictionaries, lists, dataclasses, and validation](https://github.com/Thavarshan/wallstreet/issues/3)

### B. Trusted datasets

4. [#4 — Store records in SQLite](https://github.com/Thavarshan/wallstreet/issues/4)
5. [#5 — Fetch HTTP data safely](https://github.com/Thavarshan/wallstreet/issues/5)
6. [#6 — Collect hourly and daily stock bars from Alpaca IEX](https://github.com/Thavarshan/wallstreet/issues/6)
7. [#7 — Collect financial news with RSS](https://github.com/Thavarshan/wallstreet/issues/7)
8. [#8 — Read fundamentals from SEC filings](https://github.com/Thavarshan/wallstreet/issues/8)
9. [#9 — Check data quality and market calendars](https://github.com/Thavarshan/wallstreet/issues/9)
10. [#10 — Schedule hourly collection with GitHub Actions](https://github.com/Thavarshan/wallstreet/issues/10)

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

### F. Market movement analyzer (advanced)

23. [#23 — Build point-in-time feature snapshots](https://github.com/Thavarshan/wallstreet/issues/23)
24. [#24 — Analyze trend, volatility, and unusual volume](https://github.com/Thavarshan/wallstreet/issues/24)
25. [#25 — Classify market regimes and transitions](https://github.com/Thavarshan/wallstreet/issues/25)
26. [#26 — Measure market breadth and sector strength](https://github.com/Thavarshan/wallstreet/issues/26)
27. [#27 — Study news and earnings price reactions](https://github.com/Thavarshan/wallstreet/issues/27)

### G. Adaptive strategy lab (advanced)

28. [#28 — Predict market direction with calibrated probabilities](https://github.com/Thavarshan/wallstreet/issues/28)
29. [#29 — Route strategy rules by market regime](https://github.com/Thavarshan/wallstreet/issues/29)
30. [#30 — Size positions with a strict risk budget](https://github.com/Thavarshan/wallstreet/issues/30)
31. [#31 — Choose parameters using walk-forward tests](https://github.com/Thavarshan/wallstreet/issues/31)
32. [#32 — Stress-test strategies under bad conditions](https://github.com/Thavarshan/wallstreet/issues/32)
33. [#33 — Compare champion and challenger paper strategies](https://github.com/Thavarshan/wallstreet/issues/33)

### H. AI-guided improvement (advanced)

34. [#34 — Prepare a safe evidence pack for AI](https://github.com/Thavarshan/wallstreet/issues/34)
35. [#35 — Have AI suggest testable strategy changes](https://github.com/Thavarshan/wallstreet/issues/35)
36. [#36 — Let AI draft algorithm changes in isolated PRs](https://github.com/Thavarshan/wallstreet/issues/36)
37. [#37 — Evaluate candidate strategies independently](https://github.com/Thavarshan/wallstreet/issues/37)
38. [#38 — Detect model drift and trigger research](https://github.com/Thavarshan/wallstreet/issues/38)
39. [#39 — Approve or roll back paper strategies with an audit trail](https://github.com/Thavarshan/wallstreet/issues/39)

### Hourly market-data path

The first price-data lessons now explicitly support **hourly and daily bars** without duplicating the collector:

1. [#3](https://github.com/Thavarshan/wallstreet/issues/3) and [#4](https://github.com/Thavarshan/wallstreet/issues/4): extend the Python bar model and SQLite unique key so hourly records do not overwrite daily records.
2. [#5](https://github.com/Thavarshan/wallstreet/issues/5) and [#6](https://github.com/Thavarshan/wallstreet/issues/6): connect to Alpaca's free **IEX** feed and parse `1Hour` / `1Day` records from its documented historical-bars endpoint.
3. [#9](https://github.com/Thavarshan/wallstreet/issues/9) and [#10](https://github.com/Thavarshan/wallstreet/issues/10): check bar completion, US market calendars and data freshness; schedule hourly collection with a way to catch up after missed runs.
4. [#11](https://github.com/Thavarshan/wallstreet/issues/11), [#14](https://github.com/Thavarshan/wallstreet/issues/14), [#23](https://github.com/Thavarshan/wallstreet/issues/23), [#24](https://github.com/Thavarshan/wallstreet/issues/24), and [#28](https://github.com/Thavarshan/wallstreet/issues/28): explicitly separate hourly research from daily research and prevent future-price leakage.

**What this does not mean:** the API integration or workflow is implemented already. Wallstreet is a Python learning scaffold: **Jerome writes the collector himself** following the issues. GitHub Actions is periodic polling rather than continuously streaming real-time quotes. Alpaca's Basic feed covers **IEX only**, not the consolidated US market. Validate its current pricing, historical access, terms and free quotas before enabling requests. Historical availability may lag; the safest strategy output remains `HOLD`.

### Progress tracking

- [ ] Phase A — Python foundations
- [ ] Phase B — trusted datasets
- [ ] Phase C — analysis and backtesting
- [ ] Phase D — paper trading
- [ ] Phase E — dashboard and readiness review
- [ ] Phase F — advanced market movement analyzer
- [ ] Phase G — adaptive strategy lab
- [ ] Phase H — AI-guided improvements with human review

**Suggested pace:** one or two issues per week. Take longer when a Python concept is new. The goal is *skill gained*, not tickets closed.

### Milestone gates

After Phase B, you should be able to answer where every data point came from and whether it was available at the time.

After Phase C, your strategy must beat a naive baseline on honest out-of-sample tests to justify paper experiments; if it does not, improve the research, not the claims.

After Phase D, run paper trading for long enough to observe different market conditions. Keep results separate from backtests and include fees/slippage assumptions. A positive paper result is not proof of future live profits.

Phase E is an **investigate-and-document** milestone. It never switches live trading on by itself.

Phases F–H are advanced, optional extensions. The AI agent is a research assistant that can propose changes and open pull requests. It cannot merge itself, relax the risk policy, or trade with real capital. Follow the [adaptive-strategy policy](ADAPTIVE_STRATEGY_POLICY.md) and [experiment template](EXPERIMENT_TEMPLATE.md).
