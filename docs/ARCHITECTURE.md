# Architecture, gradually

Start with one Python package and a local SQLite file. This avoids learning cloud infrastructure before learning the programming concepts that make it useful.

### Phase 1: local only

```text
Python CLI -> collectors -> SQLite -> indicators -> backtest -> reports
```

This is a conceptual sequence, **not implemented code**. You will add each component by following its GitHub issue.

### Phase 2: scheduled research

GitHub Actions runs the same Python commands on a schedule. A database in an ephemeral Actions runner does not persist between runs, so you must choose safe persistent storage (later Cloudflare D1 or a well-defined artifact flow). Never assume the runner's local filesystem is durable.

### Phase 3: simulation

Add a narrow `PaperBroker` interface. The application keeps a separate ledger but the paper broker supplies the authoritative order state. All decisions pass through a deterministic risk check.

### Phase 4: dashboard

Use a read-only Cloudflare Worker or a static report first. Introduce D1 and authenticated interactive features only if the earlier learning stages need them. Never expose account credentials or personal financial data in a public page.

### Later: feasibility, not activation

Research international broker eligibility, Wise funding, banking, taxes, API sessions, and operational risk. The outcome is documentation and a decision. The app remains **paper-only** until a separate, explicit live-trading request.
