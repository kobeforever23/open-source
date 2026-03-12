# UPDATE PROMPT — Persian Gulf Conflicts Full Dashboard (PersianGulfDashboard.html)

> **Purpose:** Give this prompt + the current `PersianGulfDashboard.html` file to your AI assistant. It will fetch live market data, determine the current date/time, and update the Epic Fury (2026) data layer while preserving all historical conflict data and the complete dashboard architecture. The output is a ready-to-open HTML file.

---

## ROLE

You are a CIB Risk Analytics desk analyst updating the full multi-conflict analytical dashboard. This dashboard covers 4 Persian Gulf conflicts (Tanker Wars 1987–88, Gulf War 1990–91, Iraq War 2003, Epic Fury 2026) with tabbed navigation. Your job is to:
1. **Determine the current date and time** (Step 0)
2. **Fetch live market data** from the web (Step 1)
3. **Update ONLY the Epic Fury data layer + shared timestamps** (Step 2)
4. **Never touch historical conflict data** (locked list below)
5. **Return the complete updated HTML file** (Step 3)

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

You MUST search the web for current prices. Do NOT reuse numbers from the existing HTML file — those are yesterday's data.

### Energy Prices
| Data Point | Search Query | Authoritative Sources |
|-----------|-------------|----------------------|
| Brent Crude | `"Brent crude oil price today"` | ICE, Bloomberg, TradingView, MarketWatch |
| WTI Crude | `"WTI crude oil price today"` | NYMEX/CME, Bloomberg, TradingView |
| Gasoline (retail) | `"AAA gas price today"` | AAA FuelGaugeReport |
| Diesel (retail) | `"AAA diesel price today"` | AAA FuelGaugeReport |
| Jet Fuel | `"jet fuel price today"` | IATA Jet Fuel Monitor, EIA |

### Equity Indexes
| Data Point | Search Query | Authoritative Sources |
|-----------|-------------|----------------------|
| S&P 500 | `"S&P 500 today"` | Yahoo Finance, Bloomberg, MarketWatch |
| DJIA | `"Dow Jones today"` | Yahoo Finance, Bloomberg |
| NASDAQ | `"NASDAQ composite today"` | Yahoo Finance |
| Nikkei 225 | `"Nikkei 225 today"` | Yahoo Finance, Nikkei.com |
| DAX | `"DAX index today"` | Yahoo Finance |
| Hang Seng | `"Hang Seng index today"` | Yahoo Finance, HKEX |
| KOSPI | `"KOSPI index today"` | Yahoo Finance, KRX |

### Risk & Situation
| Data Point | Search Query |
|-----------|-------------|
| VIX | `"VIX index today"` |
| SPR level | `"US strategic petroleum reserve level"` |
| Strait status | `"Strait of Hormuz shipping today"` |
| Conflict news | `"Operation Epic Fury latest"` or `"Iran US Gulf conflict today"` |
| Analyst views | `"oil price forecast Gulf conflict"` |
| IEA/OPEC | `"IEA oil reserve release"` or `"OPEC production update"` |
| Central bank | `"Federal Reserve interest rate"`, `"ECB rate decision"`, `"BOJ policy"` |

### Sector Performance
| Data Point | Search Query |
|-----------|-------------|
| Sector ETFs | `"XLE XLF XLK sector ETF performance today"` |
| Airlines | `"airline stocks today DAL UAL AAL"` |
| Defense | `"defense stocks today LMT RTX"` |

**If a market is closed**, use the most recent closing price.
**If you cannot find a data point**, keep the prior value prefixed with `~`.

---

## STEP 2 — UPDATE THE HTML (Epic Fury data layer ONLY)

### 2.1 Header Timestamp
Update `.tagline`:
```
INTERNAL — FOR SENIOR LEADERSHIP | Data as of {Month} {Day}, {Year}, {H:MM} AM/PM ET | Conflict Day {N}
```

### 2.2 `CONFLICTS.epicFury.kpi` (9 objects)
Update `v` values. These are **conflict-period peaks/maxima** — only update if today sets a new extreme:

| Index | Label | Logic |
|-------|-------|-------|
| 0 | Brent Peak Δ% | `(conflict_high_Brent - 70.12) / 70.12 × 100` |
| 1 | WTI Peak Δ% | `(conflict_high_WTI - 67.85) / 67.85 × 100` |
| 2 | Gasoline Peak Δ% | `(conflict_high_gas - 2.88) / 2.88 × 100` |
| 3 | S&P 500 Max DD | `(conflict_low_SPX - 6879) / 6879 × 100` — negative |
| 4 | Nikkei Max DD | `(conflict_low_Nikkei - 58885) / 58885 × 100` — negative |
| 5 | DAX Max DD | `(conflict_low_DAX - 23500) / 23500 × 100` — negative |
| 6 | VIX Peak | Highest VIX during conflict |
| 7 | Duration | `{N} days+` using today's conflict day number |
| 8 | Supply Risk | Update if EIA/analyst estimate has changed |

### 2.3 `CONFLICTS.epicFury.energy` (time-series array)
**Read the existing array.** Append one new entry:
```js
{day:N, brent:XX.XX, wti:XX.XX, gas:X.XX}
```
Never delete or modify existing entries.

### 2.4 `CONFLICTS.epicFury.heatmap`
Update `dd` only if today sets a new drawdown low for any index. Keep all `rec` as `"TBD"`.

Fixed pre-conflict baselines:
- sp500: 6,879 | djia: 48,978 | nasdaq: 22,668 | nikkei: 58,885 | dax: 23,500 | hangSeng: 26,450 | kospi: 6,131

### 2.5 `CONFLICTS.epicFury.sectors`
Update `r` (return %) values from SPDR sector ETF data if changed by ±2% or more since last update.

### 2.6 `CONFLICTS.epicFury.live` — Energy (5 items) + Equity (7 items)
For each item, update:
- `cur`: Today's price/level (fetched)
- `d`: `"{sign}{Δ%}%"` — from-pre-conflict delta
- `dod`: `"{sign}{DoD%}%"` — day-over-day
- `prev`: Yesterday's close (= the `cur` value from the OLD file)

**Pre-conflict baselines are the `pre` field — never change these.**

### 2.7 `CONFLICTS.epicFury.scenarios`
Update probability weights, price ranges, and impact estimates if analyst consensus has shifted based on today's news.

### 2.8 `NARRATIVE` object — Epic Fury entries ONLY

Update these sections based on today's fetched news:

| Section | What to update |
|---------|---------------|
| `briefings.epicFury.summary` | Rewrite 3-5 sentences with today's key developments |
| `briefings.epicFury.straitStatus` | Current Strait status |
| `briefings.epicFury.opec` | OPEC+ response |
| `briefings.epicFury.spr` | SPR level and release status |
| `briefings.epicFury.supplyNote` | Supply disruption estimate |
| `transmissionMechanisms.epicFury` | 6 strings — update if channels changed |
| `sectorAnnotations.epicFury` | Update with current ETF performance data |
| `strategicImplications` | 5 strings — today's key strategic takeaways |
| `keyVariables` | 9 strings — reorder/rewrite based on priority |
| `earningsImplications` | 5 sector entries — update if estimates changed |
| `centralBankMatrix` | 4 rows — update if policy stance shifted |

### 2.9 `compData` — Epic Fury entry only
```js
{name:"Epic Fury", ep:MIDPOINT_OF_BRENT_PEAK_RANGE, ed:SP500_MAX_DD}
```

### 2.10 Timeline bar — Epic Fury entry only
Update `peak` and `trough` strings if new extremes were set.

### 2.11 Footer timestamp
Must match header timestamp exactly.

---

## STEP 3 — SELF-VERIFICATION (MANDATORY BEFORE OUTPUT)

| # | Check | Rule |
|---|-------|------|
| 1 | Header date = Footer date | Timestamps must be identical |
| 2 | Conflict day calculation | `(today - Feb 28, 2026) + 1` in calendar days |
| 3 | KPI duration | Must show today's conflict day number |
| 4 | Live energy `cur` values | Must match the last entry in `energy` time-series array |
| 5 | Live `d` values | Must equal `(cur - pre) / pre × 100` for each item |
| 6 | Live `dod` values | Must equal `(cur - prev) / prev × 100` for each item |
| 7 | Heatmap DDs | Each must be ≤ the worst single-day close vs pre-conflict |
| 8 | KPI peak Δ% | Must use conflict-period highs, not today's spot |
| 9 | Energy array length | Must be exactly 1 entry longer than the old file |
| 10 | No historical data changed | Tanker Wars, Gulf War, Iraq War objects byte-identical |
| 11 | Pre-conflict baselines | All `pre` values unchanged from original |
| 12 | All Δ% recalculated | No copy-pasted percentages — all freshly computed |

If any check fails, fix it before outputting.

---

## HISTORICAL DATA — DO NOT MODIFY (LOCKED)

These objects are **permanently frozen**. Do not change a single character:

- `CONFLICTS.tankerWars` (entire object)
- `CONFLICTS.gulfWar` (entire object)
- `CONFLICTS.iraqWar` (entire object)
- `NARRATIVE.briefings.tankerWars / gulfWar / iraqWar`
- `NARRATIVE.transmissionMechanisms.tankerWars / gulfWar / iraqWar`
- `NARRATIVE.sectorAnnotations.tankerWars / gulfWar / iraqWar`
- `NARRATIVE.keyFindings` (cross-conflict — update only if truly warranted)
- `NARRATIVE.thisTimeIsDifferent` (update only if a structural factor materially changes)
- `NARRATIVE.historicalTimeline` (all rows except Epic Fury's oil/sp/dur fields)
- `NARRATIVE.methodology`
- `compData` entries for Tanker Wars, Gulf War, Iraq War
- `timelineEvts`, `indexNames`
- All CSS, all rendering functions, all HTML structure

---

## DO NOT CHANGE

- Any CSS (design system, colors, fonts, spacing, responsive breakpoints)
- HTML structure or element IDs
- Chart.js library version (`4.4.7`) or CDN URL
- Chart.js rendering options/config
- Tab system logic, collapse/expand system
- Any render function signatures or logic
- Badge styling or classification labels

---

## OUTPUT

Return the **complete** updated `PersianGulfDashboard.html` file. Not a diff, not a partial — the entire file, ready to save and open in a browser.
