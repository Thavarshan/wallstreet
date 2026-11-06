# 12 — Classify news with a simple baseline before adding free AI inference

**Phase:** C · Analysis  
**Estimated learning time:** 5–7 hours  
**Prerequisite:** Finish issue 11 first.

## Why we're doing this

Language models can make headlines easier to read, but confident-sounding statements are not reliable trading signals. A measurable baseline gives you something honest to compare an AI model against.

## What you'll learn

- Text normalization, simple classification, accuracy
- Structured model responses and schema validation
- Free inference quotas, privacy, and reproducibility

## Files to inspect or create

- `src/wallstreet/analysis/sentiment.py` (new)
- `src/wallstreet/ai.py` (new, optional)
- `tests/test_sentiment.py` (new)

## Build it yourself — step by step

1. Create a tiny, openly licensed or self-authored fixture of financial headlines and manually label them positive, negative, neutral, or ambiguous.
2. Write a baseline classifier using a small transparent word list. Keep it separate from the news collector; data gathering must work without AI.
3. Define a result model containing label, reason, source article ID, inference timestamp, model name/version, and optional confidence. Distinguish confidence from measured accuracy.
4. Evaluate the baseline with a confusion matrix. Note how a phrase like `beats expectations but cuts guidance` challenges naive sentiment.
5. Investigate the current free allocation of Cloudflare Workers AI or a fully local small model, its terms, and whether your hourly workload fits. Do not enable paid inference.
6. If you implement remote inference, request strict JSON output and validate it. Reject malformed responses and cap retries, tokens, and daily requests.
7. Cache classification by article identity and model version so the same news isn't billed or processed repeatedly.
8. Compare AI labels with the fixture; include error cases, costs, and a deterministic fallback.

## Concrete example

Headline `Company beats estimates but cuts full-year guidance` should not become an automatic BUY. A sensible result can be `ambiguous` with a reason and original article ID.

## Tests to write

- [ ] Identical headline and model version return a cached label.
- [ ] AI timeout falls back to baseline or UNKNOWN.
- [ ] Invalid model output is rejected.
- [ ] No inferred label arrives before the headline's publication/collection timestamp.
- [ ] A mock quota exhaustion stops calls safely.

## Acceptance checklist

- [ ] I can explain accuracy versus model confidence.
- [ ] A no-AI mode works end-to-end.
- [ ] Every AI assessment links to the article and model version.

## Common pitfall

Don't copy entire copyrighted news stories into prompts or the repository. Avoid using an AI explanation as proof of future returns.

## Need help?

Ask your AI tutor to explain a concept or review **your attempt**. The goal is to learn Python, not to have the AI finish the ticket. Do not connect real money.

