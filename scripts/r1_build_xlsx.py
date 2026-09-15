#!/usr/bin/env python3
"""R1: Build initial 07-Exports/01-raw-consolidated.xlsx skeleton.
Sheets: readme / countries / cbr-rates-annual / mirror-russia-imports-annual /
iran-exports-annual / iran-to-russia-bilateral / qa-notes.
Aggregates computed from raw filtered BACI CSVs with Decimal precision."""
import csv, json, os
from collections import defaultdict
from decimal import Decimal
import pandas as pd

BASE = "/home/z/my-project/Russia-market/05-Data"
BAC = os.path.join(BASE, "raw", "bac")
PROC = os.path.join(BASE, "processed")
OUT = "/home/z/my-project/Russia-market/07-Exports/01-raw-consolidated.xlsx"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
SNAP = "20260916"

# ---- aggregates ----
mp = defaultdict(lambda: defaultdict(Decimal))   # year -> m49 -> kUSD (mirror)
ip = defaultdict(lambda: defaultdict(Decimal))   # year -> m49 -> kUSD (iran exports)
ir = defaultdict(Decimal)                        # year -> kUSD (iran->rus)
mir_hs6 = defaultdict(lambda: defaultdict(Decimal))  # year -> hs2 -> kUSD
with open(os.path.join(BAC, f"bac__mirror_643__h6__2021-2024__{SNAP}.csv")) as fh:
    for r in csv.DictReader(fh):
        v = Decimal(r["v_kusd"]); y = r["t"]
        mp[y][r["i_m49"]] += v
        mir_hs6[y][r["k_hs6"][:2]] += v
        if r["i_m49"] == "364":
            ir[y] += v
with open(os.path.join(BAC, f"bac__iran-exports__h6__2021-2024__{SNAP}.csv")) as fh:
    for r in csv.DictReader(fh):
        ip[r["t"]][r["j_m49"]] += Decimal(r["v_kusd"])

cc = {r["m49"]: (r["iso3"], r["name_en"], r["name_fa"]) for r in csv.DictReader(open(os.path.join(PROC, "countries.csv")))}

def wide(d, val_label="value_kusd_mirror_cif"):
    years = ["2021", "2022", "2023", "2024"]
    partners = sorted(set().union(*[set(d[y]) for y in years]), key=lambda p: -(max((d[y].get(p, Decimal(0)) for y in years))))
    rows = []
    for p in partners:
        iso3, en, fa = cc.get(p, ("", "", ""))
        rows.append({"partner_m49": p, "iso3": iso3, "name_en": en, "name_fa": fa,
                     **{y: float(d[y].get(p, Decimal(0))) for y in years}})
    return pd.DataFrame(rows), years

def style_sheet(ws):
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    fill = PatternFill("solid", fgColor="1F4E79")
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF"); c.fill = fill
        c.alignment = Alignment(horizontal="center", vertical="center")
    ws.freeze_panes = "A2"
    for col in ws.columns:
        letter = get_column_letter(col[0].column)
        width = max((len(str(c.value)) if c.value is not None else 0) for c in col[:50]) + 2
        ws.column_dimensions[letter].width = min(max(width, 9), 46)
    for row in ws.iter_rows(min_row=2):
        for c in row:
            if isinstance(c.value, float):
                c.number_format = "#,##0"

with pd.ExcelWriter(OUT, engine="openpyxl") as xw:
    readme = pd.DataFrame([
        ["workbook", "01-raw-consolidated.xlsx (R1 skeleton)"],
        ["project", "Russia-market — Iran→Russia export opportunity (Scope v2, Decision-004)"],
        ["snapshot", "2026-09-16 (1405-06-25)"],
        ["trade source", "BACI HS92 V202601 (CEPII, released 2026-01-20, coverage 1995–2024); partner-reported exports to Russia = mirror imports (CIF basis)"],
        ["analysis window", "2021–2025 full years + YTD 2026 to September (partial_year) — BACI supplies 2021–2024; 2025/2026 from IRICA & partner monthly releases in R2 (est_flag)"],
        ["fx source", "CBR official daily USD rate via cbr-xml-daily.ru mirror → annual averages (days_counted per year)"],
        ["sheets", "countries; cbr-rates-annual; mirror-russia-imports-annual (year×partner); iran-exports-annual (year×partner); iran-to-russia-bilateral; qa-notes"],
        ["flags in force", "mirror_cif basis (FOB adj κ in R2); est_flag for all 3rd-party estimates; partial_year for 2026"],
        ["qa tolerance", "|calc − ref|/ref < 0.0001% vs source files (R2 cross-source reconciliation)"],
        ["reproducibility", "scripts/: baci_parallel_download.py → r1_build_baci.py → r1_cbr_rates.py → r1_build_xlsx.py (raw never committed)"],
    ], columns=["field", "value"])
    readme.to_excel(xw, sheet_name="readme", index=False)

    pd.read_csv(os.path.join(PROC, "countries.csv")).to_excel(xw, sheet_name="countries", index=False)
    pd.read_csv(os.path.join(PROC, "cbr-rates-annual.csv")).to_excel(xw, sheet_name="cbr-rates-annual", index=False)

    mdf, years = wide(mp)
    mdf = mdf.rename(columns={y: f"import_{y}_kusd" for y in years})
    total = {"partner_m49": "TOTAL", "iso3": "", "name_en": "(all partners, sum)", "name_fa": "جمع کل"}
    for y in years:
        total[f"import_{y}_kusd"] = float(sum(mp[y].values()))
    mdf = pd.concat([mdf, pd.DataFrame([total])], ignore_index=True)
    mdf.to_excel(xw, sheet_name="mirror-russia-imports-annual", index=False)

    idf, years = wide(ip)
    idf = idf.rename(columns={y: f"export_{y}_kusd" for y in years})
    total = {"partner_m49": "TOTAL", "iso3": "", "name_en": "(all partners, sum)", "name_fa": "جمع کل"}
    for y in years:
        total[f"export_{y}_kusd"] = float(sum(ip[y].values()))
    idf = pd.concat([idf, pd.DataFrame([total])], ignore_index=True)
    idf.to_excel(xw, sheet_name="iran-exports-annual", index=False)

    bi = pd.DataFrame([{"year": y,
                        "iran_to_russia_kusd_mirror": float(ir.get(y, Decimal(0))),
                        "flag": "baci_gap" if y in ("2023", "2024") else ""} for y in ["2021", "2022", "2023", "2024"]])
    bi.to_excel(xw, sheet_name="iran-to-russia-bilateral", index=False)

    qa = pd.DataFrame([
        ["Q1", "Mirror total vs official FTS", "2021 mirror = 284.59 G$ (CIF, partner-reported) vs FTS official imports ≈ 296.1 G$ (789.4 turnover − 493.3 exports) → mirror/official ≈ 0.961", "R2: per-year bias factor on overlap window; sensitivity 3–6%"],
        ["Q2", "Mirror under-coverage grows post-2022", "mirror: 2021=284.6G, 2022=196.6G, 2023=216.3G, 2024=201.8G; partner count 210→112. FTS official aggregates (published since 2023-03): 2024 turnover 716.9G$; 2025 turnover −2.8% → ≈696.8G$, surplus 139.3G$ → imports ≈278.8G$ vs mirror 2024=201.8G → coverage ≈0.71", "R2: calibrate HS6 mix by official annual totals (per-year factor); IMF DOTS cross-check"],
        ["Q3", "BACI Iran export coverage collapse", "Iran total exports per BACI: 2021=52.7G, 2022=57.4G, 2023=13.4G, 2024=13.3G — Iran stopped reporting + oil relabeling (Malaysia/UAE). China 2023=4.6G vs real ≈14G+", "M2 uses IRICA as Iran-side primary source (Decision-003); BACI Iran flows flagged ir_coverage_gap"],
        ["Q4", "Iran→Russia bilateral gap in BACI", "2021=578.5M$, 2022=691.5M$, 2023/2024 = no rows (neither side reports)", "IRICA monthly official data fills 2023–2025; est_flag"],
        ["Q5", "Cross-check China 2021", "mirror CHN→RUS 2021 = 73.17G$ vs FTS official 72.0G$ (CIF) → +1.6%", "consistent; recorded as calibration anchor"],
        ["Q6", "CBR source note", "cbr.ru XML endpoint blocked from this host (Issue-005) → cbr-xml-daily.ru mirror of official CBR rate used; annual avgs: 2021=73.6654, 2022=68.1790, 2023=85.8155, 2024=92.5771, 2025=83.1750, 2026YTD=77.9127", "R2: spot-verify vs official CBR statistical bulletin"],
        ["Q7", "Verified legal/regulatory anchors (R1 research)", "FTS statistics classification: Gov. Decree 09.03.2022 № 312 (amends 289-FZ art.278); partial resumption of AGGREGATE publication from 2023-03. Iran–EAEU full FTA in force 15 May 2025 (≈90% tariff lines preferential). Parallel import: Gov. Decree 29.03.2022 № 506 + Minpromtorg lists № 1532 (19.04.2022) → № 2701 (21.07.2023) → № 135 (16.01.2024). Unfriendly-country import surcharge: Gov. Decree 21.10.2023 № 1721 (from 2023-12-01, rates up to 35–50%)", "R4: re-verify scope/dates of surcharge & parallel-import list (fast-moving policy)"],
        ["Q8", "2025 & 2026 data plan", "BACI ends at 2024 → 2025 annual + 2026 YTD from IRICA (Iran side) + partner-monthly (China/Turkey customs, EU) with partial_year + annualization per conventions §4.1", "R2 build YTD panel; flag per-record"],
    ], columns=["id", "finding", "evidence (from R1 data & verified sources)", "mitigation / next step"])
    qa.to_excel(xw, sheet_name="qa-notes", index=False)

    for name in ("readme", "cbr-rates-annual", "mirror-russia-imports-annual",
                 "iran-exports-annual", "iran-to-russia-bilateral", "qa-notes"):
        style_sheet(xw.book[name])

print("written:", OUT, os.path.getsize(OUT), "bytes")
