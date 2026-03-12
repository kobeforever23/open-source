# AI Scenario Speaking Script

**Audience:** Traded Products Stress Business Committee  
**Use:** Spoken narrative for presenting the AI scenario, rationalizing the result pattern, and handling challenge questions  
**Time:** 7 to 10 minutes plus Q&A

## Opening Script

I want to frame this scenario very clearly up front.

This is not a completely separate macro world from Severe Rates Rally. It is Severe Rates Rally as the macro backbone, plus a targeted AI concentration overlay where we believe the loss distribution should materially differ. We kept rates, agency, muni, and FX aligned to the existing Severe Rates Rally scenario because the first-order transmission channel still looks like a standard risk-off, flight-to-quality event. Where we changed the scenario is where AI concentration matters: AI-exposed single names, AI-heavy indices, tech-heavy equity vol, and AI-linked credit.

The reason we built it that way is to be more defendable, not less. We are reusing the approved macro framework where the causal chain is unchanged, and only introducing differentiation where current valuation, index concentration, and recent stressed-market behavior give us a strong basis to do so.

## Why This Scenario Exists

The core risk we are trying to capture is an AI valuation correction.

Current valuation and concentration support that concern. As of March 6, 2026, the S&P 500 trailing P/E was about 29.34 versus a long-run mean of 16.20. The Shiller CAPE was about 39.71 versus a long-run mean of 17.34, which is about 90% of the dot-com peak. At the same time, the market is highly concentrated. In our February 27, 2026 proxy data, the top 10 names are over 36% of SPX and almost 47% of NDX. Our own 75 AI names are already 34.24% of SPX proxy weight and 50.88% of NDX proxy weight.

So the scenario is designed to answer a very specific question: if the AI complex materially re-rates, what happens to the book once that repricing spills into broader equity, volatility, and AI-linked credit, while the macro backdrop still behaves like a quality rally?

## Why We Baseline To Severe Rates Rally

The answer here is simple and I would keep it simple in the room.

We baseline to Severe Rates Rally because the non-equity shock direction is still the same. In a sharp AI correction, investors still move into Treasuries. The dollar still strengthens. Risk assets still cheapen. Commodity demand expectations soften. The difference is that equity and equity-vol losses should be much more concentrated in AI-sensitive exposures than in a standard macro de-risking event.

So this is not an attempt to reinvent rates or FX for the sake of novelty. It is an attempt to isolate the incremental concentration risk that the existing Rates Rally scenario does not fully express.

## Shock Walkthrough

Here is the short version of the shock framework.

1. Rates, agency, muni, and FX are unchanged from Severe Rates Rally.
2. Broad non-AI equity remains on the same `-15%` backbone.
3. AI-exposed single names are shocked `-50%`.
4. SPX is held to a `-26%` headline outcome.
5. NDX / QQQ is held to a `-35%` headline outcome.
6. QQQ-aligned vol uses the April 2025 tariff-period QQQ / NDX surface.
7. Remaining equity vol uses the April 2025 SPX surface.
8. Broad corporate credit stays on the same AA / BBB / B grid as Severe Rates Rally, but AI-specific names receive additional tier overlays.
9. Broad HY is intentionally less severe than in Severe Rates Rally because this scenario is not meant to be a full-systemic credit break.

If anyone asks why the scenario is not even harsher, the answer is that we are deliberately distinguishing between an AI-led valuation unwind and a 2008-scale credit collapse. This scenario absolutely pressures earnings, risk appetite, and parts of the credit cycle, but it does not assume a generalized banking or refinancing event.

## The Most Important Technical Point: Index / Single-Name Consistency

This is the point I would spend the most time on if the room is technical.

We cannot just shock AI single names at `-50%` and then also slap full `-26%` SPX and `-35%` NDX shocks on top of them without adjustment. If we do that, we double count overlapping names through both the single-name and index layers, and that creates asymmetry in equity swaps, hedges, and index-linked positions.

So what we did is solve the residual index baskets using constituent weights.

The key solved numbers are:

- NDX residual basket: `-19.43%`
- SPX residual basket, overlap-aware implementation: `-10.89%`
- SPX-only fallback residual: `-13.47%`
- Implied NDX if only the SPX fallback is available: about `-32.07%`

The message to the committee is that this weighting adjustment is not a change in scenario severity. It is an implementation control that makes the delivered index shock internally consistent once the AI single names are already fixed at `-50%`.

If someone challenges that, the response is: if we do not do this, we are not preserving scenario intent; we are creating a system artifact.

## Why April 2025 Is The Volatility Anchor

The volatility calibration is anchored to the April 2025 tariff period because it is the best recent observable analog for a concentrated, policy-driven, tech-heavy de-risking event.

In that episode, SPX fell about `-18.9%` peak to trough and NDX fell about `-22.9%`. VIX peaked above `52` and VXN peaked above `43`. That gives us an observed stressed vol and skew shape for a modern concentrated selloff.

We are not saying the AI scenario lasts only a few trading days. We are saying that the April 2025 surface gives us the right stressed shape to apply over a 60-day scenario horizon. That is a much stronger defense than inventing a theoretical vol surface.

## How To Explain The Credit Design

The broad corporate spread grid is intentionally the same as Severe Rates Rally. That keeps the scenario anchored to the same macro deterioration assumption.

The difference is in the overlays.

Tier 1 direct AI names get a larger bond spread overlay than Tier 2 indirect names. HY and CDS overlays are also differentiated, but broad HY index stress is still less severe than in Severe Rates Rally. That is because this is supposed to be an equity-led and valuation-led correction with real economic follow-through, not a generalized funding seizure.

So if the committee asks why broad HY is not as wide as Rates Rally, the answer is: because that would imply a much more systemic credit event than the narrative supports.

## How To Rationalize The Results

If the scenario is working properly, the incremental loss relative to Severe Rates Rally should primarily show up in four places.

1. AI single names.
2. QQQ / NDX and related basis exposures.
3. Equity vol and skew-sensitive books.
4. AI-linked credit names and sectors.

If the incremental loss is instead mostly showing up in rates, FX, or securitized books, I would treat that as a mapping or portfolio-composition discussion, not as proof that the scenario is wrong.

Here is the quick interpretation framework.

### If AI severe is materially worse than Severe Rates Rally

That means the portfolio genuinely carries AI concentration risk. That is the scenario doing its job.

### If AI severe is roughly the same as Severe Rates Rally

That means the book is more macro-beta driven than AI-concentration driven. Since the macro backbone is mostly unchanged, that outcome is coherent.

### If AI severe is lower than Severe Rates Rally

That usually means the portfolio is more exposed to broad HY, spread beta, or other macro channels that are intentionally harsher in Severe Rates Rally than in AI severe.

### If vol explains most of the incremental move

That is not a bug. It is expected. The scenario deliberately adds a tech-heavy vol and skew overlay.

## Closing Script

So the way I would summarize the scenario is this.

We are not trying to tell the committee that an AI correction changes every asset class. We are saying it changes the concentration of risk. The macro backbone still looks like a quality rally. The real incremental stress should sit in AI single names, AI-heavy indices, tech-heavy vol, and AI-linked credit. We anchored the scenario to current valuation and concentration, used a recent real-world stress analog for the vol shape, and corrected the implementation so the index and single-name layers are internally consistent.

That is why the scenario is both intuitive and defendable.

## Q&A Bank

### Why not just make SPX and NDX equal to the broad `-15%` equity shock?

Because that would miss the spillover from AI concentration into the major benchmarks. The whole point is that the benchmark impact should be materially worse where AI weight is concentrated.

### Why not use a dot-com-sized market shock everywhere?

Because that would imply a much broader macro and credit collapse than the current narrative supports. We want a severe AI correction, not a catch-all catastrophe scenario.

### Why are you comfortable keeping rates and FX unchanged?

Because those are governed by the same flight-to-quality channel we already use in Severe Rates Rally. We changed the scenario only where AI concentration gives us a reason to.

### Why should the committee trust the weighting adjustment?

Because without it, the scenario engine overstates the index effect by double counting names already fixed at `-50%`. The adjustment is a control to preserve the intended headline shock.

### If the system only supports the fallback implementation, what do we say?

We say clearly that the design intent is NDX `-35%`, but the implemented fallback delivers an effective NDX of about `-32.07%` because of system hierarchy constraints. That is a limitation disclosure, not a hidden assumption.

### How do we defend the `-50%` single-name shock?

It is the direct expression of the AI valuation unwind. Without that overlay, the scenario would collapse back into a generic macro correction and would fail to capture the concentration risk we are specifically trying to test.

### Why is broad HY less severe than Rates Rally?

Because the scenario assumes a meaningful earnings and confidence hit, but not a full refinancing or liquidity crisis across the entire speculative-grade market.

### What would make us revisit the calibration?

If valuation, concentration, or market structure changes enough that the scenario is no longer clearly harsher on AI concentration than Severe Rates Rally, or if the committee wants the design to migrate from a valuation correction toward a broader systemic stress event.
