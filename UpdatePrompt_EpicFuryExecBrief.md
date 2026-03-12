# UPDATE PROMPT — Epic Fury Executive Brief (EpicFuryExecBrief.html)

> **Purpose:** Give this prompt + the current `EpicFuryExecBrief.html` file to your AI assistant. It will fetch live market data, determine the current date/time, and update every data point in place while preserving the design system exactly. The output is a ready-to-open HTML file with accurate, sourced, timestamped data.

---

## ROLE

You are a CIB Risk Analytics desk analyst updating the daily Executive Brief HTML dashboard for Operation Epic Fury. Your job is to:
1. **Determine the current date and time** (see Step 0)
2. **Fetch live market data** from authoritative sources (see Data Sourcing)
3. **Update every data point** in the HTML to reflect the latest available prices
4. **Return the complete updated HTML file**

Do NOT change any CSS, layout, HTML structure, Chart.js configuration, design tokens, or class names. Only update data values, text content, and the JS chart data array.

---

## STEP 0 — DETERMINE CURRENT DATE & TIME (MANDATORY FIRST STEP)

Before doing anything else, you MUST establish the current date and time. Use one or more of these methods:

1. **Check your system/tool time** — If your environment provides a current timestamp, use it.
2. **Search the web** for `"current time ET"` or check a financial news site (Bloomberg, CNBC, Reuters) — the dateline on their latest article gives you the time.
3. **Search for today's market data** — e.g., `"Brent crude oil price today"` — the results will confirm today's date.

From the current date, calculate:
- **Conflict Day Number:** Day 1 = February 28, 2026. Count calendar days (not trading days) from Feb 28 to today, inclusive. Example: Mar 1 = Day 2, Mar 15 = Day 16.
- **Timestamp string:** Format as `{Month} {Day}, {Year}, {H:MM} AM/PM ET`

**You must use the REAL current date/time, not the date from the existing file.** The existing file's date is stale — that's why you're running this update.

---

## STEP 1 — FETCH LIVE MARKET DATA (MANDATORY)

You MUST search the web for current prices. Do NOT reuse the numbers already in the HTML file — those are yesterday's data. Perform these searches:

### Energy Prices (search each individually if needed)
| Data Point | Search Query | Authoritative Sources |
|-----------|-------------|----------------------|
| Brent Crude | `"Brent crude oil price today"` | ICE, Bloomberg, TradingView, MarketWatch, CNBC |
| WTI Crude | `"WTI crude oil price today"` | NYMEX/CME, Bloomberg, TradingView, MarketWatch |
| Gasoline (retail) | `"AAA gas price today"` or `"average gas price US"` | AAA FuelGaugeReport (gasprices.aaa.com) |
| Diesel (retail) | `"AAA diesel price today"` | AAA FuelGaugeReport |
| Jet Fuel | `"jet fuel price today IATA"` or `"jet fuel spot price"` | IATA Jet Fuel Monitor, EIA |

### Equity Indexes (search each individually if needed)
| Data Point | Search Query | Authoritative Sources |
|-----------|-------------|----------------------|
| S&P 500 | `"S&P 500 today"` | Yahoo Finance, Bloomberg, MarketWatch |
| DJIA | `"Dow Jones today"` | Yahoo Finance, Bloomberg |
| NASDAQ | `"NASDAQ composite today"` | Yahoo Finance, Bloomberg |
| Nikkei 225 | `"Nikkei 225 today"` | Yahoo Finance, Nikkei.com |
| DAX | `"DAX index today"` | Yahoo Finance, Bloomberg |
| Hang Seng | `"Hang Seng index today"` | Yahoo Finance, HKEX |
| KOSPI | `"KOSPI index today"` | Yahoo Finance, KRX |

### Risk Indicators
| Data Point | Search Query |
|-----------|-------------|
| VIX | `"VIX index today"` |
| SPR level | `"US strategic petroleum reserve level"` |

### Situation / Developments
| Data Point | Search Query |
|-----------|-------------|
| Strait of Hormuz status | `"Strait of Hormuz shipping today"` |
| Latest conflict developments | `"Operation Epic Fury latest"` or `"Iran US Gulf conflict today"` |
| Analyst commentary | `"oil price forecast Gulf conflict"` |
| IEA / OPEC actions | `"IEA oil reserve release"` or `"OPEC production update"` |

**If a market is currently closed**, use the most recent closing price and note "(close)" in your reasoning.
**If you cannot find a specific data point**, use the prior value from the HTML file prefixed with `~` and add a note.

---

## STEP 2 — UPDATE THE HTML

### 2.1 Header Timestamp
Update `.hdr-sub` text with the current date/time and conflict day:
```
{Month} {Day}, {Year}, {H:MM} AM/PM ET  |  Day {N} of Conflict
```

### 2.2 KPI Strip (8 cards in `.kpi-grid`)
Update each card's `.val` and `.sub` with freshly fetched data:

| # | Label | Value = | Sub-text = |
|---|-------|---------|-----------|
| 1 | Brent Crude | Fetched Brent price | `+{Δ%}% from pre-conflict` |
| 2 | WTI Crude | Fetched WTI price | `+{Δ%}% from pre-conflict` |
| 3 | S&P 500 | Fetched S&P level | `{Δ%}% from pre-conflict` |
| 4 | Nikkei 225 | Fetched Nikkei level | `{Δ%}% from pre-conflict` |
| 5 | VIX | Fetched VIX | Descriptive (e.g., "Elevated", "Spiking", "Normalizing") |
| 6 | Strait of Hormuz | Status text | Brief detail |
| 7 | US SPR | Level in M bbl | Context (e.g., "Lowest since 1975") |
| 8 | Brent Day-over-Day | DoD% | `${yesterday} → ${today}` |

**Pre-conflict baselines (FIXED — never change):**
- Brent: $70.12 | WTI: $67.85 | S&P 500: 6,879 | Nikkei: 58,885

**Formula:** `Δ% = (current - pre) / pre × 100`, rounded to 1 decimal.

### 2.3 Situation Summary
Rewrite the `.summary` paragraph (3-5 sentences) based on what you found in your searches. Cover:
- Oil price level, direction, and magnitude of move
- Strait of Hormuz status and any shipping incidents
- IEA/SPR/OPEC response actions
- Key analyst quotes with attribution
- SPR level and implications

### 2.4 Energy Commodities Table (5 rows)
For each row, update all 4 data columns using fetched prices:
- **Current**: Today's price
- **Pre-conflict**: Fixed baseline (see above)
- **Δ%**: `(current - pre) / pre × 100`
- **DoD**: `(today - yesterday) / yesterday × 100`

To get yesterday's price: read it from the existing HTML file's table (the "Current" column in the old file = yesterday's current).

### 2.5 Global Equity Indexes Table (7 rows)
Same logic as energy — update all 4 columns using fetched data. Fixed pre-conflict baselines:
- S&P: 6,879 | DJIA: 48,978 | NASDAQ: 22,668 | Nikkei: 58,885 | DAX: 23,500 | Hang Seng: 26,450 | KOSPI: 6,131

### 2.6 Chart.js Data Array (`const D = [...]`)
**Read the existing array** from the file — it contains all prior days. **Append** today's data point:
```js
{day:N, b:BRENT_PRICE, w:WTI_PRICE}
```
Do NOT delete any existing points. Do NOT modify prior points.

### 2.7 Scenario Matrix
Update the 3 scenario rows (Quick Ceasefire / Extended Conflict / Prolonged War) if:
- Probability weights have shifted based on today's news
- Price range forecasts have changed based on analyst commentary
If no material change, keep existing values.

### 2.8 Top 5 Developments
Replace all 5 `<li>` items with today's top 5 developments from your searches. Format:
```html
<li><strong>{Headline}:</strong> {1-2 sentence detail with specific numbers}</li>
```

### 2.9 Key Variables to Watch
Update the 7 items if priorities have shifted based on today's news.

### 2.10 Footer
Update timestamp to match header. Keep source list unless new sources were used.

---

## STEP 3 — SELF-VERIFICATION (MANDATORY BEFORE OUTPUT)

Before returning the file, verify these cross-checks:

| Check | Rule |
|-------|------|
| KPI Brent value | Must exactly match Energy table Brent "Current" cell |
| KPI WTI value | Must exactly match Energy table WTI "Current" cell |
| KPI S&P value | Must exactly match Equity table S&P "Current" cell |
| KPI Nikkei value | Must exactly match Equity table Nikkei "Current" cell |
| KPI Brent Δ% | Must match Energy table Brent "Δ%" cell |
| KPI DoD% | Must match `(today Brent - yesterday Brent) / yesterday Brent × 100` |
| Header date | Must match footer date |
| Conflict day | Must equal `(today - Feb 28, 2026) + 1` in calendar days |
| Chart array | Must have exactly 1 more entry than the old file's array |
| All Δ% values | Must be recalculated from fixed baselines, not copied |

If any check fails, fix it before outputting.

---

## DO NOT CHANGE

- Any CSS (styles, colors, fonts, spacing, responsive breakpoints, print media query)
- HTML structure or class names
- Chart.js library version (`4.4.7`) or CDN URL
- Chart.js options/config (colors, tension, fill, tooltip format)
- Badge text ("LIVE", "Internal — Senior Leadership")
- The design system color tokens in `:root`

---

## OUTPUT

Return the **complete** updated `EpicFuryExecBrief.html` file. Not a diff, not a partial — the entire file, ready to save and open in a browser.
