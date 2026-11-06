# Learning roadmap

Do these in order. The **issue numbers are the intended learning sequence**, not a demand to finish everything immediately.

| Phase | Issues | Outcome |
| --- | --- | --- |
| A. Python foundations | 01–03 | Run a CLI, understand collections and functions, write tests |
| B. Build trusted datasets | 04–10 | Store price/news/filings data and refresh it safely |
| C. Think before trading | 11–15 | Analyze patterns, label news, test strategies honestly |
| D. Simulate safely | 16–19 | Risk rules, paper broker, portfolio and reports |
| E. Observe and assess | 20–22 | Dashboard, operations, international broker readiness |

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
