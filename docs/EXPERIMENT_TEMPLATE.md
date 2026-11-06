# Trading strategy experiment template

Copy this structure into a pull request or a new research note **before** testing a new idea.

## Hypothesis

What specific market behavior are we testing? Why might it persist? What evidence would prove us wrong?

## Inputs and timing

- Symbols and exchanges:
- Data provider and permitted use:
- Data version / snapshot:
- Earliest availability of each feature:
- Training period:
- Validation period:
- Untouched evaluation period:
- Any missing data or known bias:

## Proposed strategy change

- Current strategy version:
- Candidate version:
- Exact parameters changed:
- Why these values were selected *before* evaluation:
- Cases in which the strategy must return HOLD:

## Risk and execution assumptions

- Initial simulated capital:
- Maximum per-position allocation:
- Fees, spread, FX, slippage:
- Fill timing (signal from day T, fill no earlier than an available later price):
- Handling of market closures, dividends, splits, and rejected orders:

## Comparison

| Metric | Current strategy | Candidate | Buy-and-hold | Cash |
| --- | ---: | ---: | ---: | ---: |
| Net return | TBD | TBD | TBD | TBD |
| Maximum drawdown | TBD | TBD | TBD | TBD |
| Trades / turnover | TBD | TBD | TBD | TBD |
| Costs | TBD | TBD | TBD | TBD |
| Forecast calibration (if applicable) | TBD | TBD | N/A | N/A |

## Failure cases and decision

- Market conditions where the candidate failed:
- Sensitivity to small parameter changes:
- Data or model drift concerns:
- Recommendation: `REJECT`, `MORE_PAPER_TESTING`, or `HUMAN_REVIEW`:
- Reviewer's decision and date:
- Rollback method:

**No profit result is guaranteed.** Never convert a backtest or AI forecast into live order authority.
