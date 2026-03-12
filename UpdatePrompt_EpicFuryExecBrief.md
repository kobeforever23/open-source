# UPDATE PROMPT — Epic Fury Executive Brief (EpicFuryExecBrief.html)

> **Purpose:** Give this prompt + the current `EpicFuryExecBrief.html` file to your AI assistant. It will update every data point in place while preserving the design system, layout, and chart structure exactly. Run this each morning before 8 AM ET to produce the day's brief.

---

## ROLE

You are a CIB Risk Analytics desk analyst updating the daily Executive Brief HTML dashboard for Operation Epic Fury. You must update **every data point** listed below to reflect today's market open / overnight close. Do NOT change any CSS, layout, HTML structure, Chart.js configuration, design tokens, or class names. Only update data values, text content, and the JS chart data array.

---

## WHAT TO UPDATE (Checklist)

### 1. Header Timestamp
- `.hdr-sub` text: Update the date, time (ET), and conflict day number.
  - Current: `March 12, 2026, 7:20 AM ET | Day 13 of Conflict`
  - Format: `{Month} {Day}, 2026, {H:MM} AM/PM ET | Day {N} of Conflict`
  - Day 1 = Feb 28, 2026.

### 2. KPI Strip (8 cards in `.kpi-grid`)
Update each card's `.val` and `.sub`:

| # | Label | Current Value | Current Sub-text | Where to source |
|---|-------|--------------|------------------|-----------------|
| 1 | Brent Crude | $98.19 | +40.0% from pre-conflict | ICE Brent front-month |
| 2 | WTI Crude | $93.79 | +38.2% from pre-conflict | NYMEX WTI front-month |
| 3 | S&P 500 | 6,733 | -2.1% from pre-conflict | SPX futures or prior close |
| 4 | Nikkei 225 | 52,191 | -11.4% from pre-conflict | Nikkei close (Tokyo) |
| 5 | VIX | ~30 | Elevated | CBOE VIX |
| 6 | Strait of Hormuz | Effectively Closed | 3 ships attacked overnight | UKMTO / Navy reports |
| 7 | US SPR | ~243M bbl | Lowest since 1975 | DOE Weekly Petroleum Status |
| 8 | Brent Day-over-Day | +6.8% | $91.98 → $98.19 | Yesterday close → today |

**Pre-conflict baselines (do NOT change unless correcting):**
- Brent pre-conflict: $70.12
- WTI pre-conflict: $67.85
- S&P 500 pre-conflict: 6,879
- Nikkei pre-conflict: 58,885

**Formula:** `Δ% = (current - pre) / pre × 100`, rounded to 1 decimal.

### 3. Situation Summary (`.summary` paragraph)
Rewrite the narrative paragraph to reflect today's top developments. Keep it to 3-5 sentences. Must mention:
- Oil price level and overnight direction
- Any IEA/SPR/OPEC actions
- Strait status and any shipping attacks
- Key analyst quotes (JPMorgan, Goldman, Macquarie, etc.)
- SPR level after releases

### 4. Energy Commodities Table (5 rows)
Update all 4 numeric columns per row:

| Commodity | Fields to update |
|-----------|-----------------|
| Brent Crude | Current $/bbl, Pre-conflict, Δ%, DoD% |
| WTI Crude | Current $/bbl, Pre-conflict, Δ%, DoD% |
| Gasoline (AAA) | Current $/gal, Pre-conflict, Δ%, DoD% |
| Diesel (Retail) | Current $/gal, Pre-conflict, Δ%, DoD% |
| Jet Fuel | Current $/gal, Pre-conflict, Δ%, DoD% |

**Sources:** EIA, AAA FuelGaugeReport, IATA Jet Fuel Monitor.

### 5. Global Equity Indexes Table (7 rows)
Update all 4 numeric columns per row:

| Index | Fields to update |
|-------|-----------------|
| S&P 500 | Current, Pre-conflict (6,879), Δ%, DoD% |
| DJIA | Current, Pre-conflict (48,978), Δ%, DoD% |
| NASDAQ | Current, Pre-conflict (22,668), Δ%, DoD% |
| Nikkei 225 | Current, Pre-conflict (58,885), Δ%, DoD% |
| DAX | Current, Pre-conflict (23,500), Δ%, DoD% |
| Hang Seng | Current, Pre-conflict (26,450), Δ%, DoD% |
| KOSPI | Current, Pre-conflict (6,131), Δ%, DoD% |

### 6. Chart.js Data Array (`const D = [...]`)
Append today's data point and keep all prior points. Format:
```js
{day:N, b:BRENT, w:WTI}
```
- `N` = conflict day (Day 1 = Feb 28)
- `b` = Brent price
- `w` = WTI price

**Do NOT remove any existing data points.** Only append the new day.

Also update the x-axis title text if the day range changes (currently says "Days from Conflict Onset (Feb 28)").

### 7. Scenario Matrix (3 rows)
Update probability percentages and price ranges if analyst consensus has shifted:

| Scenario | Current Prob | Brent Range | WTI Range | S&P Impact | Global |
|----------|-------------|-------------|-----------|------------|--------|
| Quick Ceasefire | 25% | $65–$75 | $62–$72 | Recover 2–4 wks | Full recovery <1 mo |
| Extended Conflict | 50% | $90–$110 | $85–$105 | -5 to -10% | Asia -10–15% |
| Prolonged War | 25% | $110–$130+ | $105–$125+ | -10 to -20% | Bear market risk |

Update the italic footnote below the table if the key signal has changed.

### 8. Top 5 Developments
Replace all 5 `<li>` items in `.dev-list` with today's top 5 developments. Each item format:
```html
<li><strong>{Headline}:</strong> {1-2 sentence detail with numbers}</li>
```

### 9. Key Variables to Watch
Update the 7 items in `.var-list` if priorities have shifted. These should be the 7 most important forward-looking variables.

### 10. Footer
Update the timestamp in `.footer`:
```
Data as of {Month} {Day}, 2026, {H:MM} AM/PM ET
```
Keep the source list unless new sources were added.

---

## ACCURACY RULES

1. **Every number must be sourced.** If you cannot verify a price, use `~` prefix (e.g., `~$99.50`).
2. **Percentages must be recalculated**, not copy-pasted. Use the formula: `(current - baseline) / baseline × 100`.
3. **Pre-conflict baselines are fixed** (Feb 27, 2026 close). Never change them.
4. **Cross-check:** KPI strip values must exactly match the corresponding table row values.
5. **DoD = Day-over-Day:** `(today - yesterday) / yesterday × 100`.

---

## DO NOT CHANGE

- Any CSS (styles, colors, fonts, spacing, responsive breakpoints, print media query)
- HTML structure or class names
- Chart.js library version or CDN URL
- Chart.js options/config (colors, tension, fill, tooltip format)
- Badge text ("LIVE", "Internal — Senior Leadership")
- The design system color tokens in `:root`

---

## OUTPUT

Return the complete updated `EpicFuryExecBrief.html` file. Do not return a diff or partial file — return the entire file so it can be saved and opened directly in a browser.
