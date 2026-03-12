#!/usr/bin/env python3
"""
EQFIN Stress Shock Calibrator — Standalone Python GUI
Solves consistent stress shocks across SPX, NDX, and single-name positions.
Data as of 2026-02-27 (IVV/CNDX holdings + Yahoo Finance adj closes).

Run:  python3 calibrator_gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os, sys
import argparse
import importlib.util

# ---------------------------------------------------------------------------
#  Import constituent data
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

try:
    from spx_ndx_data import SPX_DATA, NDX_DATA
except ModuleNotFoundError as exc:
    if exc.name != "spx_ndx_data":
        raise
    data_path = os.path.join(SCRIPT_DIR, "spx_ndx_data.py")
    if not os.path.exists(data_path):
        raise ModuleNotFoundError(
            "spx_ndx_data.py not found. Keep calibrator_gui.py and spx_ndx_data.py "
            "in the same folder."
        )
    spec = importlib.util.spec_from_file_location("spx_ndx_data", data_path)
    if spec is None or spec.loader is None:
        raise ModuleNotFoundError("Unable to load spx_ndx_data.py from local folder.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    SPX_DATA = module.SPX_DATA
    NDX_DATA = module.NDX_DATA

# ---------------------------------------------------------------------------
#  The 75 fixed single-name tickers
# ---------------------------------------------------------------------------
THE_75_NAMES = [
    "ACN","ADBE","AEP","AI","AMAT","AMD","AMZN","ANET","ASML","AUR",
    "AVGO","BABA","BE","BIDU","BLDP","CART","CAT","CEG","CFLT","CMI",
    "CRM","CRWD","CSCO","DBX","DELL","DLR","EPAM","EQIX","ESTC","ETN",
    "FCEL","GPS","GLOB","GOOGL","HPE","IBM","INFY","INTC","IRBT","JCI",
    "KLAC","LRCX","MBLY","MDB","META","MRVL","MSFT","MU","MXL","NOW",
    "NVDA","OKLO","ORCL","PANW","PATH","PGY","PLTR","PLUG","RSKD","RXRX",
    "S","SHOP","SIEGY","SMCI","SNOW","SNPS","SOFI","TEAM","TSLA","TSM",
    "TT","UPST","VRT","ZM","ZS",
]

# ---------------------------------------------------------------------------
#  Helpers
# ---------------------------------------------------------------------------
SPX_MAP = {r["ticker"]: r["weight"] for r in SPX_DATA}
NDX_MAP = {r["ticker"]: r["weight"] for r in NDX_DATA}
SPX_NAME = {r["ticker"]: r["name"] for r in SPX_DATA}
NDX_NAME = {r["ticker"]: r["name"] for r in NDX_DATA}
ALL_NAMES = {**NDX_NAME, **SPX_NAME}  # SPX overrides if overlap


def fmt_usd(v):
    if v is None or not isinstance(v, (int, float)):
        return "n/a"
    sign = "-" if v < 0 else ""
    return f"{sign}${abs(v):,.0f}"


def fmt_pct(v):
    if v is None or not isinstance(v, (int, float)):
        return "n/a"
    return f"{v:.2f}%"


def parse_fixed_overrides(text, default_shock):
    overrides = {}
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t") if "\t" in line else line.split(",")
        ticker = parts[0].strip().upper()
        ticker = "".join(c for c in ticker if c.isalnum() or c == ".")
        if not ticker:
            continue
        shock = default_shock
        if len(parts) > 1 and parts[1].strip():
            try:
                shock = abs(float(parts[1].strip().replace(",", "").replace("%", "")))
            except ValueError:
                pass
        overrides[ticker] = shock
    return overrides


def parse_exposures(text):
    rows = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t") if "\t" in line else line.split(",")
        if len(parts) < 2:
            continue
        ticker = parts[0].strip().upper()
        ticker = "".join(c for c in ticker if c.isalnum() or c == ".")
        try:
            exp = float(parts[1].strip().replace("$", "").replace(",", ""))
        except ValueError:
            continue
        if ticker:
            rows.append({"ticker": ticker, "exp": exp})
    return rows


# ---------------------------------------------------------------------------
#  Core solver
# ---------------------------------------------------------------------------
def solve_residual(index_name, data, target_shock, override_map):
    total_w = sum(r["weight"] for r in data)
    fixed_w = 0.0
    fixed_contrib = 0.0
    fixed_count = 0
    for r in data:
        if r["ticker"] in override_map:
            fixed_count += 1
            fixed_w += r["weight"]
            fixed_contrib += r["weight"] * override_map[r["ticker"]]
    residual_w = total_w - fixed_w
    if residual_w < 1e-9:
        return {
            "index": index_name, "target": target_shock,
            "total_w": total_w, "fixed_count": fixed_count,
            "fixed_w": fixed_w, "residual_w": 0,
            "fixed_w_pct": 100.0, "residual_w_pct": 0.0,
            "residual_shock": None, "rebuilt": None, "fixed_contrib": fixed_contrib,
        }
    residual_shock = (target_shock * total_w - fixed_contrib) / residual_w
    rebuilt = (fixed_contrib + residual_w * residual_shock) / total_w if total_w > 1e-9 else None
    return {
        "index": index_name, "target": target_shock,
        "total_w": total_w, "fixed_count": fixed_count,
        "fixed_w": fixed_w, "residual_w": residual_w,
        "fixed_w_pct": (fixed_w / total_w) * 100 if total_w > 0 else 0,
        "residual_w_pct": (residual_w / total_w) * 100 if total_w > 0 else 0,
        "residual_shock": residual_shock, "rebuilt": rebuilt,
        "fixed_contrib": fixed_contrib,
    }


def generate_75_exposures():
    combined = {}
    for r in SPX_DATA:
        combined[r["ticker"]] = combined.get(r["ticker"], 0) + r["weight"]
    for r in NDX_DATA:
        combined[r["ticker"]] = combined.get(r["ticker"], 0) + r["weight"]
    entries = sorted(
        [(t, combined.get(t, 0)) for t in THE_75_NAMES],
        key=lambda x: -x[1]
    )
    lines = []
    for i, (t, w) in enumerate(entries):
        exp = round((1_200_000 - i * 9000) * (1 + w / 100))
        lines.append(f"{t},{exp}")
    return "\n".join(lines)


def run_self_test():
    """Run a lightweight deterministic validation without launching the GUI."""
    assert SPX_DATA and NDX_DATA, "Constituent datasets must be non-empty."
    assert abs(sum(r["weight"] for r in SPX_DATA) - 100.0) < 2.0, "SPX weights look invalid."
    assert abs(sum(r["weight"] for r in NDX_DATA) - 100.0) < 2.0, "NDX weights look invalid."

    sample_overrides = {"NVDA": 50.0, "MSFT": 50.0, "AAPL": 50.0}
    spx = solve_residual("SPX", SPX_DATA, 26.0, sample_overrides)
    ndx = solve_residual("NDX", NDX_DATA, 35.0, sample_overrides)

    assert spx["residual_shock"] is not None, "SPX residual shock should be solvable."
    assert ndx["residual_shock"] is not None, "NDX residual shock should be solvable."
    assert abs((spx["rebuilt"] or 0) - 26.0) < 1e-6, "SPX reconstruction failed."
    assert abs((ndx["rebuilt"] or 0) - 35.0) < 1e-6, "NDX reconstruction failed."
    assert len(generate_75_exposures().splitlines()) == 75, "75-name exposure template must have 75 rows."

    print("EQFIN self-test: PASS")


# ---------------------------------------------------------------------------
#  GUI Application
# ---------------------------------------------------------------------------
class CalibratorApp:
    def __init__(self, root):
        self.root = root
        root.title("EQFIN Stress Shock Calibrator")
        root.geometry("1020x820")
        root.minsize(800, 600)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook.Tab", padding=[14, 6], font=("Helvetica", 12, "bold"))
        style.configure("Run.TButton", font=("Helvetica", 13, "bold"), padding=[16, 8])
        style.configure("Treeview", font=("Menlo", 11), rowheight=22)
        style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

        # Header
        hdr = tk.Frame(root, bg="#edf3fa", padx=16, pady=10)
        hdr.pack(fill="x")
        tk.Label(hdr, text="EQFIN Stress Shock Calibrator", font=("Helvetica", 20, "bold"),
                 bg="#edf3fa", fg="#152238").pack(anchor="w")
        tk.Label(hdr, text="As-of 2026-02-27  |  SPX proxy: IVV (503)  |  NDX proxy: CNDX (101)",
                 font=("Helvetica", 11), bg="#edf3fa", fg="#5d6b80").pack(anchor="w")

        # Notebook tabs
        self.nb = ttk.Notebook(root)
        self.nb.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        self._build_quick_tab()
        self._build_advanced_tab()
        self._build_names75_tab()

    # ==================================================================
    #  TAB 1: Index Shock Solver
    # ==================================================================
    def _build_quick_tab(self):
        tab = ttk.Frame(self.nb, padding=10)
        self.nb.add(tab, text="Index Shock Solver")

        # --- Input frame ---
        inp = ttk.LabelFrame(tab, text="Inputs", padding=8)
        inp.pack(fill="x", pady=(0, 6))

        row1 = ttk.Frame(inp)
        row1.pack(fill="x", pady=2)
        ttk.Label(row1, text="Target SPX Shock %:").pack(side="left", padx=(0, 4))
        self.q_spx = ttk.Entry(row1, width=8)
        self.q_spx.insert(0, "26")
        self.q_spx.pack(side="left", padx=(0, 16))
        ttk.Label(row1, text="Target NDX Shock %:").pack(side="left", padx=(0, 4))
        self.q_ndx = ttk.Entry(row1, width=8)
        self.q_ndx.insert(0, "35")
        self.q_ndx.pack(side="left", padx=(0, 16))
        ttk.Label(row1, text="Fixed Shock %:").pack(side="left", padx=(0, 4))
        self.q_fixed = ttk.Entry(row1, width=8)
        self.q_fixed.insert(0, "50")
        self.q_fixed.pack(side="left")

        ttk.Label(inp, text="Fixed Names (one per line, optional: TICKER,SHOCK%):"
                  ).pack(anchor="w", pady=(6, 2))
        self.q_tickers = tk.Text(inp, height=8, width=60, font=("Menlo", 11))
        self.q_tickers.insert("1.0", "\n".join(THE_75_NAMES))
        self.q_tickers.pack(fill="x")

        btn_row = ttk.Frame(inp)
        btn_row.pack(fill="x", pady=(6, 0))
        ttk.Button(btn_row, text="Run Calibration", style="Run.TButton",
                   command=self._run_quick).pack(side="left", padx=(0, 8))
        ttk.Button(btn_row, text="Reset Defaults",
                   command=self._reset_quick).pack(side="left")

        # --- Output frame ---
        out = ttk.LabelFrame(tab, text="Results & Math Steps", padding=8)
        out.pack(fill="both", expand=True, pady=(0, 4))
        self.q_output = tk.Text(out, wrap="word", font=("Menlo", 11), state="disabled",
                                bg="#f8fafd", fg="#152238")
        q_scroll = ttk.Scrollbar(out, command=self.q_output.yview)
        self.q_output.configure(yscrollcommand=q_scroll.set)
        q_scroll.pack(side="right", fill="y")
        self.q_output.pack(fill="both", expand=True)

    def _reset_quick(self):
        self.q_spx.delete(0, "end"); self.q_spx.insert(0, "26")
        self.q_ndx.delete(0, "end"); self.q_ndx.insert(0, "35")
        self.q_fixed.delete(0, "end"); self.q_fixed.insert(0, "50")
        self.q_tickers.delete("1.0", "end")
        self.q_tickers.insert("1.0", "\n".join(THE_75_NAMES))

    def _run_quick(self):
        try:
            target_spx = abs(float(self.q_spx.get() or "26"))
            target_ndx = abs(float(self.q_ndx.get() or "35"))
            fixed_shock = abs(float(self.q_fixed.get() or "50"))
        except ValueError:
            messagebox.showerror("Input Error", "Shock values must be numbers.")
            return

        overrides = parse_fixed_overrides(self.q_tickers.get("1.0", "end"), fixed_shock)
        spx = solve_residual("SPX", SPX_DATA, target_spx, overrides)
        ndx = solve_residual("NDX", NDX_DATA, target_ndx, overrides)

        # Build output
        lines = []
        lines.append("=" * 60)
        lines.append("  EQFIN INDEX SHOCK CALIBRATION RESULTS")
        lines.append("=" * 60)

        # Warnings
        universe = set(r["ticker"] for r in SPX_DATA) | set(r["ticker"] for r in NDX_DATA)
        unmatched = [t for t in overrides if t not in universe]
        if unmatched:
            lines.append(f"\n  WARNING: {len(unmatched)} tickers not in SPX/NDX: "
                         f"{', '.join(unmatched[:8])}{'...' if len(unmatched)>8 else ''}")
        if not overrides:
            lines.append("\n  NOTE: No fixed names; residual = target.")

        lines.append(f"\n  KEY RESULTS:")
        lines.append(f"  Residual SPX Shock:  {fmt_pct(spx['residual_shock'])}")
        lines.append(f"  Residual NDX Shock:  {fmt_pct(ndx['residual_shock'])}")
        lines.append(f"  Fixed Wt (SPX/NDX):  {fmt_pct(spx['fixed_w_pct'])} / {fmt_pct(ndx['fixed_w_pct'])}")

        check_ok = (spx["rebuilt"] is not None and ndx["rebuilt"] is not None
                     and abs(spx["rebuilt"] - target_spx) < 1e-6
                     and abs(ndx["rebuilt"] - target_ndx) < 1e-6)
        status = "PASS" if check_ok else "MISMATCH"
        lines.append(f"  Rebuilt Check:       {fmt_pct(spx['rebuilt'])} / {fmt_pct(ndx['rebuilt'])}  [{status}]")

        # Math steps
        lines.append("\n" + "-" * 60)
        lines.append("  STEP 1: Parse Fixed Names")
        lines.append("-" * 60)
        lines.append(f"  Parsed {len(overrides)} fixed tickers (default shock = {fmt_pct(fixed_shock)}).")
        lines.append(f"  Matched in SPX: {spx['fixed_count']} ({fmt_pct(spx['fixed_w_pct'])} of weight)")
        lines.append(f"  Matched in NDX: {ndx['fixed_count']} ({fmt_pct(ndx['fixed_w_pct'])} of weight)")

        lines.append("\n" + "-" * 60)
        lines.append("  STEP 2: Weight Decomposition")
        lines.append("-" * 60)
        for s, label in [(spx, "SPX"), (ndx, "NDX")]:
            lines.append(f"\n  {label}:")
            lines.append(f"    Total Weight    = {s['total_w']:.2f}")
            lines.append(f"    Fixed Weight    = {s['fixed_w']:.2f} ({fmt_pct(s['fixed_w_pct'])})")
            lines.append(f"    Residual Weight = {s['residual_w']:.2f} ({fmt_pct(s['residual_w_pct'])})")

        lines.append("\n" + "-" * 60)
        lines.append("  STEP 3: Solve Residual Shock")
        lines.append("-" * 60)
        lines.append("  Formula:")
        lines.append("    residualShock = (target * totalWt - fixedContrib) / residualWt")
        for s, label, target in [(spx, "SPX", target_spx), (ndx, "NDX", target_ndx)]:
            lines.append(f"\n  {label}:")
            lines.append(f"    fixedContrib = {s['fixed_contrib']:.2f}")
            lines.append(f"    residualShock = ({target:.2f} * {s['total_w']:.2f} - {s['fixed_contrib']:.2f}) / {s['residual_w']:.2f}")
            lines.append(f"                 = {fmt_pct(s['residual_shock'])}")

        lines.append("\n" + "-" * 60)
        lines.append("  STEP 4: Verification (Rebuild Check)")
        lines.append("-" * 60)
        lines.append("  Formula:")
        lines.append("    rebuilt = (fixedContrib + residualWt * residualShock) / totalWt")
        for s, label, target in [(spx, "SPX", target_spx), (ndx, "NDX", target_ndx)]:
            lines.append(f"\n  {label}: rebuilt = {fmt_pct(s['rebuilt'])} (target = {fmt_pct(target)})"
                         f"  {'PASS' if s['rebuilt'] and abs(s['rebuilt']-target)<1e-6 else 'FAIL'}")

        lines.append("\n" + "-" * 60)
        lines.append("  SUMMARY TABLE")
        lines.append("-" * 60)
        lines.append(f"  {'Index':<6} {'Target':>8} {'Fixed#':>7} {'FixWt%':>8} {'ResWt%':>8} {'ResShock':>10} {'Rebuilt':>10}")
        for s in [spx, ndx]:
            lines.append(f"  {s['index']:<6} {fmt_pct(s['target']):>8} {s['fixed_count']:>7}"
                         f" {fmt_pct(s['fixed_w_pct']):>8} {fmt_pct(s['residual_w_pct']):>8}"
                         f" {fmt_pct(s['residual_shock']):>10} {fmt_pct(s['rebuilt']):>10}")

        self._set_output(self.q_output, "\n".join(lines))

    # ==================================================================
    #  TAB 2: PnL-Driven Solver
    # ==================================================================
    def _build_advanced_tab(self):
        tab = ttk.Frame(self.nb, padding=10)
        self.nb.add(tab, text="PnL-Driven Solver")

        inp = ttk.LabelFrame(tab, text="Inputs", padding=8)
        inp.pack(fill="x", pady=(0, 6))

        row1 = ttk.Frame(inp)
        row1.pack(fill="x", pady=2)
        for label, attr, default, col in [
            ("Single-Name Shock %:", "a_single", "50", 0),
            ("SPX Shock %:", "a_spx_shock", "26", 1),
            ("NDX Shock %:", "a_ndx_shock", "35", 2),
        ]:
            ttk.Label(row1, text=label).pack(side="left", padx=(0, 4))
            e = ttk.Entry(row1, width=8)
            e.insert(0, default)
            e.pack(side="left", padx=(0, 14))
            setattr(self, attr, e)

        row2 = ttk.Frame(inp)
        row2.pack(fill="x", pady=2)
        for label, attr, default in [
            ("Target PnL ($):", "a_target", "-3000000"),
            ("SPX Exp ($/1%):", "a_spx_exp", "0"),
            ("NDX Exp ($/1%):", "a_ndx_exp", "0"),
        ]:
            ttk.Label(row2, text=label).pack(side="left", padx=(0, 4))
            e = ttk.Entry(row2, width=12)
            e.insert(0, default)
            e.pack(side="left", padx=(0, 14))
            setattr(self, attr, e)

        ttk.Label(inp, text="Single-Name Exposures (TICKER,exposure_per_1pct):"
                  ).pack(anchor="w", pady=(6, 2))
        self.a_names = tk.Text(inp, height=6, width=60, font=("Menlo", 11))
        self.a_names.insert("1.0", generate_75_exposures())
        self.a_names.pack(fill="x")

        btn_row = ttk.Frame(inp)
        btn_row.pack(fill="x", pady=(6, 0))
        ttk.Button(btn_row, text="Run Calibration", style="Run.TButton",
                   command=self._run_advanced).pack(side="left", padx=(0, 8))
        ttk.Button(btn_row, text="Reset Defaults",
                   command=self._reset_advanced).pack(side="left")

        out = ttk.LabelFrame(tab, text="Results & Math Steps", padding=8)
        out.pack(fill="both", expand=True, pady=(0, 4))
        self.a_output = tk.Text(out, wrap="word", font=("Menlo", 11), state="disabled",
                                bg="#f8fafd", fg="#152238")
        a_scroll = ttk.Scrollbar(out, command=self.a_output.yview)
        self.a_output.configure(yscrollcommand=a_scroll.set)
        a_scroll.pack(side="right", fill="y")
        self.a_output.pack(fill="both", expand=True)

    def _reset_advanced(self):
        for attr, val in [("a_single", "50"), ("a_spx_shock", "26"), ("a_ndx_shock", "35"),
                          ("a_target", "-3000000"), ("a_spx_exp", "0"), ("a_ndx_exp", "0")]:
            w = getattr(self, attr)
            w.delete(0, "end"); w.insert(0, val)
        self.a_names.delete("1.0", "end")
        self.a_names.insert("1.0", generate_75_exposures())

    def _run_advanced(self):
        try:
            single_mag = abs(float(self.a_single.get() or "50"))
            spx_mag = abs(float(self.a_spx_shock.get() or "26"))
            ndx_mag = abs(float(self.a_ndx_shock.get() or "35"))
            target_net = float(self.a_target.get() or "-3000000")
            spx_exp = float(self.a_spx_exp.get() or "0")
            ndx_exp = float(self.a_ndx_exp.get() or "0")
        except ValueError:
            messagebox.showerror("Input Error", "All numeric fields must be valid numbers.")
            return

        rows = parse_exposures(self.a_names.get("1.0", "end"))

        # Step 1: Single-name PnL
        single_pnl = sum(r["exp"] * (-single_mag) for r in rows)

        # Step 2: Index PnL
        spx_pnl = spx_exp * (-spx_mag)
        ndx_pnl = ndx_exp * (-ndx_mag)
        index_pnl = spx_pnl + ndx_pnl
        net_pnl = single_pnl + index_pnl

        # Step 3: Solve
        solves = [("Current inputs", spx_mag, ndx_mag, net_pnl)]
        if index_pnl != 0:
            scale = (target_net - single_pnl) / index_pnl
            s, n = spx_mag * scale, ndx_mag * scale
            solves.append(("Scale both", s, n, single_pnl + spx_exp * (-s) + ndx_exp * (-n)))
        else:
            solves.append(("Scale both", None, None, None))
        if spx_exp != 0:
            s = -(target_net - single_pnl - ndx_pnl) / spx_exp
            solves.append(("Solve SPX only", s, ndx_mag, single_pnl + spx_exp * (-s) + ndx_pnl))
        else:
            solves.append(("Solve SPX only", None, ndx_mag, None))
        if ndx_exp != 0:
            n = -(target_net - single_pnl - spx_pnl) / ndx_exp
            solves.append(("Solve NDX only", spx_mag, n, single_pnl + spx_pnl + ndx_exp * (-n)))
        else:
            solves.append(("Solve NDX only", spx_mag, None, None))

        # Step 4: Basis risk
        basis_rows = []
        overlap_count = 0
        abs_exp = sum(abs(r["exp"]) for r in rows)
        abs_exp_overlap = 0
        basis_total = 0
        for r in rows:
            spx_w = SPX_MAP.get(r["ticker"], 0)
            ndx_w = NDX_MAP.get(r["ticker"], 0)
            is_overlap = (spx_w + ndx_w) > 0
            if is_overlap:
                overlap_count += 1
                abs_exp_overlap += abs(r["exp"])
            h_spx = abs(spx_exp) * spx_w
            h_ndx = abs(ndx_exp) * ndx_w
            if (h_spx + h_ndx) > 0:
                blended = (h_spx * spx_mag + h_ndx * ndx_mag) / (h_spx + h_ndx)
            elif (spx_w + ndx_w) > 0:
                blended = (spx_w * spx_mag + ndx_w * ndx_mag) / (spx_w + ndx_w)
            else:
                blended = 0
            delta = single_mag - blended
            extra = -r["exp"] * delta
            basis_total += extra
            basis_rows.append({
                "ticker": r["ticker"], "exp": r["exp"],
                "spx_w": spx_w, "ndx_w": ndx_w,
                "blended": blended, "delta": delta, "extra": extra,
            })
        basis_rows.sort(key=lambda x: -abs(x["extra"]))

        gap = net_pnl - target_net

        # Build output
        lines = []
        lines.append("=" * 60)
        lines.append("  EQFIN PnL-DRIVEN CALIBRATION RESULTS")
        lines.append("=" * 60)

        lines.append(f"\n  KEY METRICS:")
        lines.append(f"  Single-Name PnL:  {fmt_usd(single_pnl)}")
        lines.append(f"  Index Hedge PnL:  {fmt_usd(index_pnl)}")
        lines.append(f"  Net Portfolio PnL:{fmt_usd(net_pnl)}")
        lines.append(f"  Gap vs Target:    {fmt_usd(gap)}")

        # Step 1
        lines.append("\n" + "-" * 60)
        lines.append("  STEP 1: Single-Name PnL")
        lines.append("-" * 60)
        lines.append("  Formula: PnL = exposure_per_1pct * (-shock%)")
        for r in rows[:10]:
            pnl = r["exp"] * (-single_mag)
            lines.append(f"    {r['ticker']:>6}: {fmt_usd(r['exp']):>12} x (-{single_mag:.2f}%) = {fmt_usd(pnl)}")
        if len(rows) > 10:
            lines.append(f"    ... +{len(rows)-10} more names")
        lines.append(f"\n  Total Single-Name PnL = {fmt_usd(single_pnl)}")

        # Step 2
        lines.append("\n" + "-" * 60)
        lines.append("  STEP 2: Index Hedge PnL")
        lines.append("-" * 60)
        lines.append(f"  SPX PnL = {fmt_usd(spx_exp)} * (-{spx_mag:.2f}%) = {fmt_usd(spx_pnl)}")
        lines.append(f"  NDX PnL = {fmt_usd(ndx_exp)} * (-{ndx_mag:.2f}%) = {fmt_usd(ndx_pnl)}")
        lines.append(f"  Index PnL = {fmt_usd(index_pnl)}")

        # Step 3
        lines.append("\n" + "-" * 60)
        lines.append("  STEP 3: Net PnL & Gap")
        lines.append("-" * 60)
        lines.append(f"  Net PnL = {fmt_usd(single_pnl)} + {fmt_usd(index_pnl)} = {fmt_usd(net_pnl)}")
        lines.append(f"  Target  = {fmt_usd(target_net)}")
        lines.append(f"  Gap     = {fmt_usd(gap)}")

        # Step 4
        lines.append("\n" + "-" * 60)
        lines.append("  STEP 4: Shock Solver (3 Methods)")
        lines.append("-" * 60)
        lines.append(f"  {'Method':<20} {'SPX%':>10} {'NDX%':>10} {'Net PnL':>14}")
        lines.append(f"  {'-'*20} {'-'*10} {'-'*10} {'-'*14}")
        for method, s, n, p in solves:
            lines.append(f"  {method:<20} {fmt_pct(s):>10} {fmt_pct(n):>10} {fmt_usd(p):>14}")

        # Step 5: Basis
        lines.append("\n" + "-" * 60)
        lines.append("  STEP 5: Basis Risk Analysis")
        lines.append("-" * 60)
        lines.append(f"  Overlap: {overlap_count} of {len(rows)} names in indices"
                     f" ({(abs_exp_overlap/abs_exp*100) if abs_exp else 0:.1f}% of exposure)")
        lines.append(f"  Total Basis PnL: {fmt_usd(basis_total)}")
        lines.append(f"\n  {'Ticker':>6} {'Exposure':>12} {'SPXWt':>7} {'NDXWt':>7} {'Blend%':>8} {'Delta%':>8} {'BasisPnL':>12}")
        lines.append(f"  {'-'*6} {'-'*12} {'-'*7} {'-'*7} {'-'*8} {'-'*8} {'-'*12}")
        for b in basis_rows[:20]:
            lines.append(f"  {b['ticker']:>6} {fmt_usd(b['exp']):>12} {b['spx_w']:>6.2f}% {b['ndx_w']:>6.2f}%"
                         f" {b['blended']:>7.2f}% {b['delta']:>7.2f}% {fmt_usd(b['extra']):>12}")
        if len(basis_rows) > 20:
            lines.append(f"  ... +{len(basis_rows)-20} more")

        self._set_output(self.a_output, "\n".join(lines))

    # ==================================================================
    #  TAB 3: 75 Names Reference
    # ==================================================================
    def _build_names75_tab(self):
        tab = ttk.Frame(self.nb, padding=10)
        self.nb.add(tab, text="75 Names Reference")

        info = ttk.Frame(tab)
        info.pack(fill="x", pady=(0, 6))
        ttk.Label(info, text="The 75 single-name positions and their SPX/NDX membership.",
                  font=("Helvetica", 11)).pack(anchor="w")

        # Filter
        filt_row = ttk.Frame(tab)
        filt_row.pack(fill="x", pady=(0, 4))
        ttk.Label(filt_row, text="Filter:").pack(side="left", padx=(0, 4))
        self.n75_filter = ttk.Entry(filt_row, width=20)
        self.n75_filter.pack(side="left", padx=(0, 8))
        self.n75_filter.bind("<KeyRelease>", lambda e: self._populate_names75())
        ttk.Button(filt_row, text="Copy Table", command=self._copy_names75).pack(side="right")

        # Treeview
        cols = ("ticker", "name", "in_spx", "spx_wt", "in_ndx", "ndx_wt", "price")
        self.n75_tree = ttk.Treeview(tab, columns=cols, show="headings", height=22)
        for c, h, w, anchor in [
            ("ticker", "Ticker", 70, "w"), ("name", "Company", 260, "w"),
            ("in_spx", "In SPX", 60, "center"), ("spx_wt", "SPX Wt%", 80, "e"),
            ("in_ndx", "In NDX", 60, "center"), ("ndx_wt", "NDX Wt%", 80, "e"),
            ("price", "Price", 80, "e"),
        ]:
            self.n75_tree.heading(c, text=h)
            self.n75_tree.column(c, width=w, anchor=anchor)
        vsb = ttk.Scrollbar(tab, orient="vertical", command=self.n75_tree.yview)
        self.n75_tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.n75_tree.pack(fill="both", expand=True)

        # Summary
        self.n75_summary = ttk.Label(tab, text="", font=("Helvetica", 11))
        self.n75_summary.pack(anchor="w", pady=(4, 0))

        self._populate_names75()

    def _populate_names75(self):
        q = self.n75_filter.get().strip().upper()
        self.n75_tree.delete(*self.n75_tree.get_children())
        in_spx = in_ndx = in_both = in_neither = 0
        spx_wt_total = ndx_wt_total = 0

        for t in THE_75_NAMES:
            sw = SPX_MAP.get(t, 0)
            nw = NDX_MAP.get(t, 0)
            name = ALL_NAMES.get(t, "")
            price_rec = next((r for r in SPX_DATA if r["ticker"] == t),
                             next((r for r in NDX_DATA if r["ticker"] == t), None))
            price = f"${price_rec['price']:.2f}" if price_rec else "-"

            if q and q not in t and q not in name.upper():
                continue

            has_spx = sw > 0
            has_ndx = nw > 0
            if has_spx and has_ndx: in_both += 1
            elif has_spx: in_spx += 1
            elif has_ndx: in_ndx += 1
            else: in_neither += 1
            spx_wt_total += sw
            ndx_wt_total += nw

            self.n75_tree.insert("", "end", values=(
                t, name,
                "Yes" if has_spx else "No", f"{sw:.2f}%" if has_spx else "-",
                "Yes" if has_ndx else "No", f"{nw:.2f}%" if has_ndx else "-",
                price,
            ))

        if not q:
            self.n75_summary.config(
                text=f"Total: {len(THE_75_NAMES)}  |  SPX only: {in_spx}  |  "
                     f"NDX only: {in_ndx}  |  Both: {in_both}  |  Neither: {in_neither}  |  "
                     f"SPX coverage: {spx_wt_total:.2f}%  |  NDX coverage: {ndx_wt_total:.2f}%"
            )

    def _copy_names75(self):
        lines = ["Ticker\tCompany\tIn SPX\tSPX Wt%\tIn NDX\tNDX Wt%\tPrice"]
        for item in self.n75_tree.get_children():
            vals = self.n75_tree.item(item, "values")
            lines.append("\t".join(str(v) for v in vals))
        self.root.clipboard_clear()
        self.root.clipboard_append("\n".join(lines))

    # ==================================================================
    #  Utility
    # ==================================================================
    @staticmethod
    def _set_output(widget, text):
        widget.config(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", text)
        widget.config(state="disabled")
        widget.see("1.0")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="EQFIN Stress Shock Calibrator (standalone Python GUI)"
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run deterministic checks without opening the GUI.",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        run_self_test()
        return 0

    try:
        root = tk.Tk()
    except tk.TclError as exc:
        print(
            "Failed to start Tkinter GUI. Ensure your machine has a desktop "
            "environment and Tk support installed.\n"
            f"Details: {exc}"
        )
        return 1

    CalibratorApp(root)
    root.mainloop()
    return 0


# ---------------------------------------------------------------------------
#  Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    raise SystemExit(main())
