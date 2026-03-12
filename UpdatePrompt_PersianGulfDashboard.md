# UPDATE PROMPT — Persian Gulf Conflicts Full Dashboard (PersianGulfDashboard.html)

> **Purpose:** Give this prompt + the current `PersianGulfDashboard.html` file to your AI assistant. It will update the Epic Fury (2026) live data while preserving the complete 4-conflict analytical dashboard — historical data, design system, layout, tabs, and all rendering logic. Run this each morning to refresh the current-event data layer.

---

## ROLE

You are a CIB Risk Analytics desk analyst updating the full multi-conflict analytical dashboard. This dashboard covers 4 Persian Gulf conflicts (Tanker Wars 1987-88, Gulf War 1990-91, Iraq War 2003, Epic Fury 2026) with tabbed navigation. **Only the Epic Fury data and shared elements (header timestamp, footer) need updating.** Historical conflict data is fixed and must never be modified.

---

## WHAT TO UPDATE (Checklist)

### 1. Header Timestamp
Update the `.tagline` text:
```
INTERNAL — FOR SENIOR LEADERSHIP | Data as of {Month} {Day}, 2026, {H:MM} AM/PM ET | Conflict Day {N}
```
Day 1 = Feb 28, 2026.

### 2. Epic Fury KPI Array (`CONFLICTS.epicFury.kpi`)
Update these 9 KPI objects. Only change `v` (value) fields:

| Index | Label | Current Value | Source |
|-------|-------|--------------|--------|
| 0 | Brent Peak Δ% | +70–80% | ICE Brent intraday high vs $70.12 |
| 1 | WTI Peak Δ% | +52–70% | NYMEX WTI intraday high vs $67.85 |
| 2 | Gasoline Peak Δ% | +24% | AAA vs $2.88 |
| 3 | S&P 500 Max DD | -3.1% | Max intraday drawdown from 6,879 |
| 4 | Nikkei Max DD | -11.9% | Max drawdown from 58,885 |
| 5 | DAX Max DD | -5.4% | Max drawdown from 23,500 |
| 6 | VIX Peak | ~30 | CBOE VIX conflict-period high |
| 7 | Duration | 13 days+ | Update day count |
| 8 | Supply Risk | 5–20 mbpd | EIA / analyst estimates |

**Important:** These are **peak/max** values across the entire conflict, not today's spot. Only update if today sets a new extreme.

### 3. Epic Fury Energy Time-Series (`CONFLICTS.epicFury.energy`)
Append today's data point to the array:
```js
{day:N, brent:XX.XX, wti:XX.XX, gas:X.XX}
```
- `day` = conflict day number
- Keep ALL existing data points — only append

### 4. Epic Fury Heatmap (`CONFLICTS.epicFury.heatmap`)
Update `dd` (max drawdown) values only if today sets a new low for any index:

| Index Key | Current DD | Pre-conflict |
|-----------|-----------|--------------|
| sp500 | -3.1% | 6,879 |
| djia | -2.9% | 48,978 |
| nasdaq | -4.0% | 22,668 |
| nikkei | -11.9% | 58,885 |
| ftse | -2.7% | (use pre-conflict close) |
| dax | -5.4% | 23,500 |
| cac40 | -4.0% | (use pre-conflict close) |
| hangSeng | -3.2% | 26,450 |
| kospi | -16.9% | 6,131 |
| shanghai | -1.2% | (use pre-conflict close) |
| asx200 | -7.2% | (use pre-conflict close) |
| sensex | -2.6% | (use pre-conflict close) |

All `rec` fields stay `"TBD"` while conflict is ongoing.

### 5. Epic Fury Sectors (`CONFLICTS.epicFury.sectors`)
Update percentage returns if meaningfully changed (±2% threshold):
```js
{n:"Energy",r:15},{n:"Utilities",r:2}, ...
```
Source: SPDR sector ETF performance from Feb 27 close.

### 6. Epic Fury Live Data (`CONFLICTS.epicFury.live`)

#### Energy (5 items):
Update `cur`, `d` (delta%), `dod` (day-over-day%), and `prev` (yesterday's close):

| Label | Current fields | Pre-conflict (fixed) |
|-------|---------------|---------------------|
| Brent Crude | cur, d, dod, prev | pre: 70.12 |
| WTI Crude | cur, d, dod, prev | pre: 67.85 |
| Gasoline (AAA) | cur, d, dod, prev | pre: 2.88 |
| Diesel (Retail) | cur, d, dod, prev | pre: 3.89 |
| Jet Fuel | cur, d, dod, prev | pre: 2.15 |

#### Equity (7 items):
Update `cur`, `d` (delta%), `dod`, and `prev`:

| Label | Pre-conflict (fixed) |
|-------|---------------------|
| S&P 500 | pre: 6879 |
| DJIA | pre: 48978 |
| NASDAQ | pre: 22668 |
| Nikkei 225 | pre: 58885 |
| DAX | pre: 23500 |
| Hang Seng | pre: 26450 |
| KOSPI | pre: 6131 |

### 7. Scenario Probabilities (`CONFLICTS.epicFury.scenarios`)
Update Brent/WTI/gasoline ranges and S&P/global impact if analyst consensus has shifted. Update the scenario color-coded probabilities if the situation has materially changed.

### 8. Narrative Data (`NARRATIVE` object) — Epic Fury entries only

#### `NARRATIVE.briefings.epicFury`
- `summary`: Rewrite to reflect today's situation (3-5 sentences)
- `straitStatus`: Update (e.g., "Effectively closed", "Partially reopened", "Open under escort")
- `opec`: Update OPEC+ response status
- `spr`: Update SPR level and release status
- `supplyNote`: Update disruption estimate

#### `NARRATIVE.transmissionMechanisms.epicFury`
Update the 6 bullet strings if transmission channels have materially changed.

#### `NARRATIVE.sectorAnnotations.epicFury`
Update the annotation string with current sector performance data.

#### `NARRATIVE.strategicImplications`
Update the 5 bullet strings with today's key strategic takeaways.

#### `NARRATIVE.keyVariables`
Update the 9 monitoring variables if priorities have shifted.

#### `NARRATIVE.earningsImplications`
Update the 5 sector earnings impact entries if materially changed.

#### `NARRATIVE.centralBankMatrix`
Update the 4 central bank rows if policy stance has shifted.

### 9. Comparative Chart Data (`compData`)
Update Epic Fury entry only:
```js
{name:"Epic Fury", ep:XX, ed:-X.X}
```
- `ep` = peak Brent Δ% (midpoint of range)
- `ed` = S&P 500 max drawdown %

### 10. Timeline Bar Data (in `renderTimeline`)
Update Epic Fury bar's `peak` and `trough` text if new extremes were set:
```js
{name:"Epic Fury", start:92, width:7, cls:"bar-epic", peak:"Brent: $119–126", trough:"S&P: -3.1%"}
```

### 11. Footer Timestamp
Update the footer date string to match the header.

---

## HISTORICAL DATA — DO NOT MODIFY

The following data objects are **locked** and must never be changed:

- `CONFLICTS.tankerWars` (entire object)
- `CONFLICTS.gulfWar` (entire object)
- `CONFLICTS.iraqWar` (entire object)
- `NARRATIVE.briefings.tankerWars`
- `NARRATIVE.briefings.gulfWar`
- `NARRATIVE.briefings.iraqWar`
- `NARRATIVE.transmissionMechanisms.tankerWars`
- `NARRATIVE.transmissionMechanisms.gulfWar`
- `NARRATIVE.transmissionMechanisms.iraqWar`
- `NARRATIVE.sectorAnnotations.tankerWars / gulfWar / iraqWar`
- `NARRATIVE.keyFindings` (cross-conflict analysis — update only if new finding emerges)
- `NARRATIVE.thisTimeIsDifferent` (structural comparison — update only if a factor materially changes)
- `NARRATIVE.historicalTimeline` (all rows except Epic Fury)
- `NARRATIVE.methodology` (sources, phases, caveats)
- `compData` entries for Tanker Wars, Gulf War, Iraq War
- `timelineEvts` array
- `indexNames` object
- All CSS
- All rendering functions
- All HTML structure

---

## ACCURACY RULES

1. **Every number must be sourced.** Use `~` prefix for estimates.
2. **Percentages must be recalculated:** `(current - baseline) / baseline × 100`, rounded to 1 decimal.
3. **Pre-conflict baselines are fixed** (Feb 27, 2026 close). Never change them.
4. **Cross-check consistency:**
   - KPI `v` values must match live data `d` values
   - Heatmap `dd` must equal or exceed any single-day drawdown
   - Chart data array must include every prior day (never delete points)
   - Footer date must match header date
5. **Peak/max values are cumulative** — only update if today sets a new extreme.
6. **DoD = Day-over-Day:** `(today - yesterday) / yesterday × 100`.

---

## DO NOT CHANGE

- Any CSS (design system, colors, fonts, spacing, responsive breakpoints)
- HTML structure or element IDs
- Chart.js library version or CDN URL
- Chart.js rendering options/config
- Tab system logic
- Collapse/expand system
- Any render function signatures or logic
- Badge styling or classification labels
- Historical conflict data (see locked list above)

---

## OUTPUT

Return the complete updated `PersianGulfDashboard.html` file. Do not return a diff or partial file — return the entire file so it can be saved and opened directly in a browser.
