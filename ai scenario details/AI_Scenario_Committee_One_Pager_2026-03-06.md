# AI Scenario One-Pager

**Purpose:** Give the committee the shortest defensible version of the scenario design, why it is baselined to Severe Rates Rally, and how to interpret the results.

## Core Message

This is **not** a brand-new macro scenario. It is **Severe Rates Rally plus an AI concentration overlay**.

That is the right design because:

1. the non-equity macro response still looks like risk-off / flight-to-quality,
2. the real incremental risk is concentrated in AI single names, AI-heavy indices, tech vol, and AI-linked credit,
3. and reusing the approved macro backbone is more defendable than re-underwriting every asset class from scratch.

## Why Now

1. S&P 500 trailing P/E was `29.34` on March 6, 2026 versus a long-run mean of `16.20`.
2. Shiller CAPE was `39.71` versus a long-run mean of `17.34`, or about `90%` of the December 1999 peak.
3. In the repo's February 27, 2026 constituent set, the top 10 names were `36.36%` of SPX proxy weight and `46.84%` of NDX proxy weight.
4. The 75 AI names used for calibration represent `34.24%` of SPX proxy weight and `50.88%` of NDX proxy weight.

## 60-Day Scenario Design

| Area | AI severe design | Why |
|---|---:|---|
| Rates / agency / muni / FX | Same as Severe Rates Rally | Macro transmission unchanged |
| AI single names | `-50%` | Direct valuation reset |
| SPX | `-26%` | Spillover beyond AI names |
| NDX / QQQ | `-35%` | AI-heavy benchmark should underperform |
| Remaining broad equity | `-15%` | Same as Severe Rates Rally |
| QQQ-aligned equity vol | April 2025 tariff-period QQQ / NDX surface | Best recent stressed tech-vol template |
| Remaining equity vol | April 2025 SPX surface | Best recent broad-market stressed template |
| Broad corporate spreads | AA / BBB / B = `100 / 250 / 750` | Same macro credit backbone |
| AI bond overlays | Tier 1 `+75 bps`, Tier 2 `+50 bps` | AI-specific credit differentiation |
| Credit indices | IG / HY `125 / 350` vs Rates Rally `125 / 450` | AI severe is less systemic for broad HY |

## Why The Equity Weighting Adjustment Matters

The main control issue is overlap.

If we shock AI single names at `-50%` and then also shock SPX / NDX at full headline levels without adjustment, we double count the same names through both the single-name and index layers. That creates false asymmetry in swaps, index hedges, and result attribution.

So we solve the residual baskets using constituent weights.

- NDX residual basket: `-19.43%`
- SPX residual basket, overlap-aware: `-10.89%`
- SPX-only fallback residual: `-13.47%`
- Implied NDX under fallback: `-32.07%`

**Committee line:** the weighting adjustment is an implementation control, not a scenario redesign.

## What Should Be Different Versus Severe Rates Rally

The incremental loss should show up in:

1. AI single names,
2. QQQ / NDX-linked books,
3. tech-heavy implied vol and skew,
4. and AI-linked credit.

The incremental loss should **not** primarily show up in rates, FX, agency, or muni, because those are intentionally unchanged.

## How To Explain Results

### If AI severe is worse than Rates Rally

The portfolio is carrying real AI concentration risk.

### If AI severe is similar to Rates Rally

The portfolio is more macro-beta driven than AI-concentration driven.

### If AI severe is lower than Rates Rally

The book is more exposed to broad credit / funding stress than to AI concentration, which is consistent with AI severe being narrower on systemic HY stress.

## Challenge Answers

### Why baseline to Rates Rally?

Because the macro direction is still risk-off / quality rally. Only the concentration overlay changes.

### Why not make everything worse?

Because that would be less defendable. We only increase severity where we have a strong causal and empirical basis.

### Why use April 2025 vol?

Because it is the cleanest recent stress analog for a concentrated tech-led de-risking episode.

### Why not go full 2008?

Because this is an equity-led valuation unwind, not a banking / funding collapse.

## Bottom Line

The scenario is defendable because it is:

1. coherent at the macro level,
2. targeted where AI concentration matters,
3. anchored to current valuation and concentration,
4. and implemented with a control that prevents index / single-name double counting.
