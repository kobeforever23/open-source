# AI Scenario Committee Report

**Prepared for:** Traded Products Stress Business Committee  
**Date:** March 6, 2026  
**Scenario horizon:** 3 months / 60 trading days  
**Scenario design intent:** Severe but plausible AI-led valuation correction with a rates-rally / flight-to-quality macro backbone

## Executive Summary

This AI scenario is intentionally built on top of the existing Severe Rates Rally scenario rather than as a fully independent macro event. That is the right design choice because the non-equity transmission channel still looks like a classic risk-off / flight-to-quality episode: Treasury yields rally, USD strengthens versus major developed-market currencies, and risk assets outside the AI complex de-rate. The point of differentiation is not the macro backbone. The point of differentiation is the concentration of the equity, volatility, and sector-credit shock in AI-linked names and AI-heavy benchmarks.

The scenario is designed to capture a sharp unwind in elevated AI valuations and crowded positioning without assuming a 2008-style balance-sheet seizure. The economic hit is meaningful through weaker earnings expectations, slower capex follow-through, and tighter credit conditions for AI-dependent sectors, but the scenario remains smaller than the Global Financial Crisis on broad credit and funding stress. That is why rates, agency, muni, and FX stay aligned to Severe Rates Rally, while equities, equity vol, and AI-linked credit receive targeted overlays.

The calibration is also operationally controlled. Because the system shocks names through index and single-name drivers with limited granularity, we cannot simply apply `-50%` to AI single names and also apply full headline SPX / NDX shocks without creating asymmetry in equity swaps, index hedges, and overlapping constituents. We therefore solve residual index baskets using constituent weights so the implemented shock set reproduces the intended SPX and NDX headline outcomes instead of double counting the AI names.

## Committee Takeaway

The cleanest message is:

1. We reused Severe Rates Rally wherever the causal chain is the same.
2. We only changed factors where AI concentration materially changes the loss distribution.
3. We anchored the equity and volatility calibration to observable market stress, not to a hand-waved narrative.
4. We corrected system implementation asymmetry through constituent weighting, which is a control enhancement rather than a change in scenario severity.

## Why This Scenario Is Needed Now

Three facts make the scenario timely:

1. **Valuation is rich.** As captured on March 6, 2026, Multpl showed the S&P 500 trailing P/E at `29.34`, versus a long-run mean of `16.20`, or about `1.81x` the historical mean. Multpl showed the Shiller CAPE at `39.71`, versus a long-run mean of `17.34`, or about `2.29x` the historical mean and roughly `89.9%` of the December 1999 CAPE peak of `44.19`.
2. **Index concentration is high.** In the local IVV / CNDX constituent data set dated February 27, 2026, the top 10 names were `36.36%` of the SPX proxy and `46.84%` of the NDX proxy. The 75 AI names already identified for the scenario account for `34.24%` of SPX proxy weight and `50.88%` of NDX proxy weight.
3. **The recent market analog was already severe.** Using Yahoo Finance daily closes, the April 8, 2025 tariff episode saw SPX fall `-18.90%` from the February 19, 2025 peak to trough, while NDX fell `-22.93%`. VIX peaked at `52.33` on April 8, 2025 and VXN peaked at `43.25` on April 10, 2025. That is a valid modern stress analog for a concentrated de-risking episode, especially for QQQ / NDX skew and vol shape.

## Why We Baseline To Severe Rates Rally

The rationale for reusing Severe Rates Rally as the backbone is straightforward.

1. **Macro transmission is still risk-off.** A sharp AI correction should still drive a Treasury rally, USD strength, wider credit spreads, and weaker commodity demand expectations.
2. **We have less evidence for reinventing the non-equity side.** We have a defensible view on how AI-heavy equities and related credit should reprice. We have much less evidence that agency, muni, major FX, or rates should move in a fundamentally different direction than in a standard growth scare / quality rally.
3. **It preserves governance continuity.** Reusing an approved macro backbone reduces model risk and challenge risk. The committee can focus on the incremental AI overlay rather than reopening every asset-class assumption.
4. **It avoids over-fitting.** A bespoke cross-asset AI scenario that changes everything would look less defendable, not more, because it would imply high conviction about relationships we cannot observe directly.

In short, the scenario is **Rates Rally plus an AI concentration overlay**, not a wholly new macro regime.

## Scenario Narrative

The scenario assumes that AI-linked valuations correct sharply after investors reassess the durability of revenue growth, monetization, margins, and capex intensity. The immediate market response is led by AI-exposed single names and AI-heavy benchmarks. That first-order equity shock then propagates through the usual macro channels: weaker risk sentiment, lower Treasury yields on flight-to-quality, stronger USD, softer commodities on weaker forward demand expectations, and wider corporate spreads.

The scenario is **not** meant to represent:

1. a bank funding crisis,
2. a sovereign stress event,
3. or a 2008-scale systemic default cycle.

It **is** meant to represent:

1. an equity-led valuation reset,
2. concentrated downside in AI-linked single names,
3. a spike in tech-heavy implied volatility and skew,
4. and a measurable but more moderate deterioration in broad credit and the economy.

## Shock Framework Summary

### Asset-Class Design

| Asset class | AI scenario design | Relative to Severe Rates Rally | Rationale |
|---|---|---:|---|
| Rates | Same as Severe Rates Rally | Unchanged | Flight-to-quality remains the correct backbone |
| Agency | Same as Severe Rates Rally | Unchanged | Macro transmission unchanged |
| Muni | Same as Severe Rates Rally | Unchanged | Macro transmission unchanged |
| FX | Same as Severe Rates Rally | Unchanged | USD strength remains the base case in risk-off |
| Broad equities outside AI concentration | `-15%` | Same as Severe Rates Rally | Reuse approved broad-market severity |
| AI-exposed single names | `-50%` | More severe | Direct valuation unwind |
| SPX index headline | `-26%` | More severe than broad `-15%` | Captures spillover from AI concentration |
| NDX / QQQ headline | `-35%` | More severe | AI-heavy benchmark should underperform SPX |
| Equity vol for QQQ-aligned names | April 2025 QQQ / NDX tariff-period vol surface | Changed | Best recent stressed shape for tech-heavy de-risking |
| Equity vol for remaining names | April 2025 SPX vol surface | Changed | Preserves stressed market skew outside QQQ alignment |
| Credit broad corporates | AA / BBB / B = `100 / 250 / 750` | Same as Severe Rates Rally | Macro credit backbone preserved |
| AI-specific bond overlays | Tier 1 `+75 bps`, Tier 2 `+50 bps` | Changed | Direct and indirect AI spread effects |
| HY / CDS overlays | AI severe `50 / 100 / 250`; Rates Rally `50 / 100 / 500` | AI severe less systemic | AI correction is narrower than a full macro credit washout |
| Credit indices | AI severe IG / HY = `125 / 350`; Rates Rally IG / HY = `125 / 450` | AI HY less severe | Broad HY stress is material but below Rates Rally |
| Commodities | Roughly same as Severe Rates Rally; oil about `-20%` | Near unchanged | Weaker demand channel, not supply shock |

### Important Labeling Note

For credit, the committee deck should label the numbers consistently as either **shocked spread levels** or **spread widens**. The current working language mixes the two. Before final committee distribution, make sure the shock sheet uses one convention only.

## Equity Design And Implementation Control

### Headline Equity Intent

The headline intent is:

1. Shock AI-exposed single names by `-50%`.
2. Hold SPX at a `-26%` headline shock.
3. Hold NDX / QQQ at a `-35%` headline shock.
4. Keep broad non-AI equities on the existing `-15%` Severe Rates Rally backbone.

### Why A Simple Index Overlay Fails

A simple implementation would shock the single names and then also shock SPX and NDX at their full headline levels. That is not correct in a system where index drivers and single-name drivers overlap.

That approach would:

1. double count the AI names already fixed at `-50%`,
2. create asymmetry between cash / swap / index hedge positions,
3. and distort result attribution by overstating the contribution of index drivers.

### Constituent-Weighting Control

Using the local February 27, 2026 IVV / CNDX proxy data already stored in the repo:

1. The 75-name AI list covers `50.88%` of NDX proxy weight.
2. The same list covers `34.24%` of SPX proxy weight.
3. The NDX residual basket therefore has to be solved, not guessed.

The residual calculations already documented in the existing calibration note are:

- **NDX residual basket:** `-19.43%`
- **SPX residual basket, overlap-aware implementation:** `-10.89%`
- **SPX residual basket, fallback SPX-only implementation:** `-13.47%`
- **Implied NDX under SPX-only fallback:** `-32.07%`

### The Math

For NDX:

`(50.88 x 50.00) + (49.02 x 19.43) = 34.97`, which reconstructs the `-35%` NDX headline.

For SPX under the overlap-aware implementation:

`(34.24 x 50.00) + (19.77 x 19.43) + (45.79 x 10.89) = 25.95`, which reconstructs the `-26%` SPX headline.

### Committee Message On The Weighting Adjustment

Use this exact framing:

> The constituent-weighting adjustment is not a softer scenario and it is not a harder scenario. It is an implementation control that ensures the delivered index shock matches the intended headline once AI single names have already been fixed at `-50%`.

That sentence usually diffuses the main challenge.

## Volatility Calibration

The volatility design uses the April 2025 tariff period as the calibration anchor because it is the most recent observable episode with the right qualitative shape:

1. concentrated downside in growth / tech,
2. sharp repricing of index downside protection,
3. higher tech vol relative to broad-market vol,
4. and stress that lasted long enough to generate realistic skew rather than a one-day air pocket.

Supporting market context from public price history:

- SPX trough on April 8, 2025: `-18.90%` from the February 19, 2025 peak
- NDX trough on April 8, 2025: `-22.93%` from the February 19, 2025 peak
- VIX peak: `52.33` on April 8, 2025
- VXN peak: `43.25` on April 10, 2025
- 20-day realized vol on April 10, 2025: SPX `48.25%`, NDX `57.36%`

That is why the design uses:

1. QQQ-aligned names to the April 2025 QQQ / NDX surface,
2. remaining equity to the April 2025 SPX surface,
3. and then applies those stressed shapes over the 60-day scenario horizon.

The key defense point is that we are **using the observed stressed surface shape**, not assuming that the event itself only lasts a few days.

## Credit Design

The credit calibration keeps the broad corporate spread backbone stable while adding AI-specific overlays where the fundamental link is strongest.

### Broad Credit Backbone

Use the same broad corporate spread grid as Severe Rates Rally:

- AA: `100 bps`
- BBB: `250 bps`
- B: `750 bps`

That keeps the scenario anchored to the same macro deterioration assumption on the broad economy and credit cycle.

### AI-Specific Sector Overlays

On top of that broad grid, apply AI-specific overlays:

- Tier 1 direct AI bond impact: `+75 bps`
- Tier 2 indirect AI bond impact: `+50 bps`
- HY / CDS direct-indirect buckets under AI severe: `50 / 100 / 250 bps`
- HY / CDS direct-indirect buckets under Rates Rally: `50 / 100 / 500 bps`
- Credit index endpoints under AI severe: IG / HY `125 / 350`
- Credit index endpoints under Rates Rally: IG / HY `125 / 450`

### Credit Rationale

This says the following:

1. broad macro credit risk is real in both scenarios,
2. AI-sensitive credits underperform their broad peers,
3. but AI severe is still not as systemic for broad HY as a fuller macro / funding stress episode.

That is a coherent position. It is consistent with an equity-led correction that weakens earnings and confidence without assuming mass refinancing failure across the entire speculative-grade universe.

## Other Asset Classes

### Rates

Keep U.S. Treasury shocks the same as Severe Rates Rally. The message is simple: in an AI unwind, money still moves into duration and liquidity, so Treasuries rally on flight-to-quality.

### FX

Keep FX the same as Severe Rates Rally. The working assumption is stronger USD versus major European and Asian currencies as capital moves toward U.S. liquidity and safety.

### Commodities

Keep the commodity complex roughly aligned to Severe Rates Rally. The scenario logic is weaker forward demand, not a supply shock. Oil around `-20%` remains directionally consistent with that narrative. Preserve the existing commodity sheet implementation for the remaining curve points.

### Securitized Products And Structured Books

The scenario should not be sold as a securitized-products story. Those books move mainly because the macro backbone is still risk-off. The differentiated loss should show up primarily in:

1. AI single names,
2. NDX / QQQ-linked books,
3. equity vol and correlation-sensitive products,
4. and AI-linked credit.

If the result set instead shows the biggest incremental stress in rates or securitized books, that is more likely a portfolio mapping or hedge-basis question than a scenario-design question.

## How To Rationalize The Results In Committee

### If AI Scenario Loss Is Worse Than Severe Rates Rally

Say:

> That is the expected outcome if the book carries concentrated AI single-name, QQQ / NDX, or AI-linked volatility risk. The scenario is built precisely to isolate that concentration risk on top of the same macro risk-off backbone.

### If AI Scenario Loss Is Similar To Severe Rates Rally

Say:

> That tells us the portfolio is driven more by macro beta than by AI concentration. Since rates, FX, agency, and muni are intentionally unchanged, similar losses indicate the incremental AI overlay is not the dominant driver of this portfolio.

### If AI Scenario Loss Is Lower Than Severe Rates Rally

Say:

> That can happen if the portfolio is more exposed to broad HY, general spread beta, or macro funding risk than to AI concentration. The AI scenario is intentionally narrower on systemic broad-credit severity than Severe Rates Rally.

### If Equity Vol Dominates The Incremental Loss

Say:

> That is also expected. The scenario is not just a spot shock. It is also a tech-heavy vol and skew shock, using the April 2025 tariff period as the empirical anchor.

## What We Should Expect To Notice

The expected qualitative pattern is:

1. Loss concentration should migrate toward AI single names, QQQ / NDX exposures, and equity vol.
2. Results on rates, FX, agency, and muni should look broadly similar to Severe Rates Rally because those shocks are intentionally unchanged.
3. AI-linked credit should underperform broad credit, but broad HY should still look less catastrophic than in Severe Rates Rally.
4. Books that appear unexpectedly benign despite known AI exposure should be reviewed for mapping gaps, hedge offsets, or missed basis.
5. Books that show very large incremental losses from broad index hedges should be checked for index / single-name overlap implementation.

## Key Defensibility Points

When challenged, the strongest defenses are:

1. **Narrative coherence:** the scenario is an AI valuation unwind, not a funding crisis.
2. **Governance coherence:** unchanged asset classes inherit from an already-approved severe macro scenario.
3. **Empirical anchor:** valuation, concentration, and April 2025 market stress all support a severe AI correction narrative.
4. **Implementation control:** constituent weighting prevents double counting and hedge asymmetry.
5. **Severity discipline:** the scenario is clearly harsher than a normal correction but intentionally below a full 2008-scale systemic event.

## Likely Committee Questions And Tight Answers

### Why not just use Severe Rates Rally and stop there?

Because Severe Rates Rally does not isolate the concentration risk in AI single names, AI-heavy benchmarks, and tech-heavy implied volatility. The macro direction is similar, but the loss distribution is different.

### Why are rates and FX unchanged if this is an AI scenario?

Because the first-order macro reaction still looks like a growth scare and flight-to-quality. The scenario differentiates where AI changes the shock, not where it does not.

### Why `-50%` on AI single names?

Because the scenario is meant to capture a genuine valuation unwind in crowded names rather than a mild de-rating. The `-50%` level is the direct concentration overlay that makes the scenario meaningfully different from the broad market backbone.

### Why is NDX `-35%` but broad remaining equities only `-15%`?

Because NDX is the index expression of AI concentration. Broad remaining equity is intentionally kept on the approved Severe Rates Rally backbone.

### Why is broad HY less severe than Rates Rally?

Because this is not designed as a full-systemic default wave. The broad economy weakens, but the stress remains centered on AI valuations and AI-linked earnings expectations.

### Why use April 2025 volatility as the calibration basis for a 60-day horizon?

Because we need the stressed shape and skew from a recent, observable, tech-heavy drawdown. We are not assuming the event lasts only a week. We are using that stressed surface as the empirical template for the 60-day horizon implementation.

### Why is the constituent-weighting adjustment necessary?

Because otherwise the system double counts AI names through both the single-name and index layers, which creates false asymmetry in swaps and hedge positions.

## Model And System Limitations

1. The exact inherited rates, agency, muni, FX, and commodity curve point shocks are assumed unchanged from the existing Severe Rates Rally sheet and are not reproduced here line-by-line.
2. Credit labeling needs one final control pass to ensure all numbers are tagged as levels or widens consistently.
3. If the system cannot support mutually exclusive residual baskets, the fallback implementation must disclose that the effective NDX headline drifts to about `-32.07%` rather than the intended `-35%`.
4. The commodity curve notation supplied in working discussions should be carried over exactly from the approved sheet to avoid translation errors.

## Recommendation

Take the scenario forward as the committee version of an **AI severe but non-systemic valuation correction** with the following framing:

1. Severe Rates Rally remains the approved macro backbone.
2. AI single names, AI-heavy benchmarks, AI vol, and AI-linked credit carry the incremental stress.
3. Constituent weighting is the key implementation control that makes the delivered shock set internally consistent.

## Sources And Evidence

### External

1. Multpl, S&P 500 P/E Ratio: <https://www.multpl.com/s-p-500-pe-ratio>
2. Multpl, Shiller PE Ratio: <https://www.multpl.com/shiller-pe>
3. OECD, *OECD Economic Outlook, Volume 2025 Issue 2*: <https://www.oecd.org/en/publications/oecd-economic-outlook-volume-2025-issue-2_9f653ca1-en.html>
4. Yahoo Finance ticker history used for public market context calculations: <https://finance.yahoo.com/quote/%5EGSPC/>, <https://finance.yahoo.com/quote/%5ENDX/>, <https://finance.yahoo.com/quote/%5EVIX/>, <https://finance.yahoo.com/quote/%5EVXN/>

### Internal / Repo

1. Existing detailed equity calibration note: `open-source/artifacts/reports/ai_severe_equity_calibration_full.docx`
2. IVV / CNDX constituent basis in repo tool: `open-source/tools/eqfin-shock-calibrator/spx_ndx_data.py`
3. 75-name AI list and calibration logic: `open-source/tools/eqfin-shock-calibrator/calibrator_gui.py`
