#!/usr/bin/env python3
"""R1: Filter BACI 2021-2024 for (a) Russia mirror imports (j=643, all exporters)
and (b) Iran global exports (i=364). Build countries.csv (m49/iso3/iso2/name_en/
name_fa/role) and copy HS6 product codes. Compute QA aggregates.
Outputs (raw not committed; processed & aggregates committed):
  raw/bac/bac__mirror_643__h6__2021-2024__<snap>.csv
  raw/bac/bac__iran-exports__h6__2021-2024__<snap>.csv
  processed/countries.csv
  processed/hs6-codes.csv
  raw/bac/qa-aggregates__20260916.json
"""
import csv, json, os
from decimal import Decimal

BAC = "/home/z/my-project/Russia-market/05-Data/raw/bac"
SRC = os.path.join(BAC, "src")
PROC = "/home/z/my-project/Russia-market/05-Data/processed"
os.makedirs(PROC, exist_ok=True)
SNAP = "20260916"
YEARS = [2021, 2022, 2023, 2024]
RUS, IRN = "643", "364"

# Persian names for key countries (R1: core + comparators + major partners)
NAME_FA = {
    "RUS": "روسیه", "IRN": "ایران", "CHN": "چین", "TUR": "ترکیه",
    "IND": "هند", "BLR": "بلاروس", "KAZ": "قزاقستان", "ARM": "ارمنستان",
    "AZE": "جمهوری آذربایجان", "ARE": "امارات متحده عربی", "DEU": "آلمان",
    "USA": "ایالات متحده", "BRA": "برزیل", "VNM": "ویتنام", "THA": "تایلند",
    "ITA": "ایتالیا", "FRA": "فرانسه", "NLD": "هلند", "POL": "لهستان",
    "KOR": "کره جنوبی", "JPN": "ژاپن", "MYS": "مالزی", "IDN": "اندونزی",
    "SAU": "عربستان سعودی", "IRQ": "عراق", "Afg": "", "AFG": "افغانستان",
    "PAK": "پاکستان", "IRQ ": "", "TKM": "ترکمنستان", "UZB": "ازبکستان",
    "KGZ": "قرقیزستان", "TJK": "تاجیکستان", "GRC": "یونان", "ESP": "اسپانیا",
    "GBR": "بریتانیا", "CHE": "سوئیس", "SWE": "سوئد", "AUT": "اتریش",
    "BEL": "بلژیک", "CZE": "چک", "SVK": "اسلواکی", "HUN": "مجارستان",
    "ROU": "رومانی", "BGR": "بلغارستان", "UKR": "اوکراین", "GEO": "گرجستان",
    "ISR": "اسرائیل", "EGY": "مصر", "MAR": "مراکش", "TUN": "تونس",
    "ZAF": "آفریقای جنوبی", "NGA": "نیجریه", "ETH": "اتیوپی", "KEN": "کنیا",
    "CAN": "کانادا", "MEX": "مکزیک", "ARG": "آرژانتین", "CHL": "شیلی",
    "COL": "کلمبیا", "PER": "پرو", "ECU": "اکوادور", "AUS": "استرالیا",
    "NZL": "نیوزیلند", "SGP": "سنگاپور", "HKG": "هنگ‌کنگ", "TWN": "تایوان",
    "BGD": "بنگلادش", "LKA": "سری‌لانکا", "NPL": "نپال", "SYR": "سوریه",
    "JOR": "اردن", "LBN": "لبنان", "KWT": "کویت", "QAT": "قطر",
    "OMN": "عمان", "BHR": "بحرین", "YEM": "یمن", "MDA": "مولداوی",
    "SRB": "صربستان", "FIN": "فنلاند", "NOR": "نروژ", "DNK": "دانمارک",
    "LTU": "لیتوانی", "LVA": "لتونی", "EST": "استونی", "CYP": "قبرس",
    "MLT": "مالت", "IRL": "ایرلند", "PRT": "پرتغال", "ESP ": "", "ISL": "ایسلند",
}
COMPARATORS = {"CHN", "TUR", "IND", "BLR"}
CORE = {"RUS", "IRN"}

# ---- countries.csv ----
cc_in = os.path.join(SRC, "country_codes_V202601.csv")
rows = list(csv.DictReader(open(cc_in, encoding="utf-8")))
out = [["iso3", "m49", "iso2", "name_en", "name_fa", "role"]]
for r in rows:
    iso3 = r["country_iso3"]
    role = "core" if iso3 in CORE else ("comparator" if iso3 in COMPARATORS else "other")
    out.append([iso3, r["country_code"], r["country_iso2"], r["country_name"],
                NAME_FA.get(iso3, ""), role])
with open(os.path.join(PROC, "countries.csv"), "w", newline="", encoding="utf-8") as fh:
    csv.writer(fh).writerows(out)
print(f"countries.csv: {len(out)-1} rows")

# ---- product codes ----
prod = list(csv.DictReader(open(os.path.join(SRC, "product_codes_HS92_V202601.csv"), encoding="utf-8")))
with open(os.path.join(PROC, "hs6-codes.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["hs6", "description_en"])
    for p in prod:
        w.writerow([p.get("code") or p.get("product_code"), p.get("description") or p.get("product_description")])
print(f"hs6-codes.csv: {len(prod)} rows")

# ---- filter year files ----
agg = {"mirror_by_year": {}, "iran_to_rus_by_year": {}, "iran_total_exports_by_year": {},
       "mirror_rows": 0, "iran_rows": 0}
mirror_path = os.path.join(BAC, f"bac__mirror_643__h6__2021-2024__{SNAP}.csv")
iran_path = os.path.join(BAC, f"bac__iran-exports__h6__2021-2024__{SNAP}.csv")
fm = open(mirror_path, "w", newline="", encoding="utf-8")
fi = open(iran_path, "w", newline="", encoding="utf-8")
wm, wi = csv.writer(fm), csv.writer(fi)
wm.writerow(["t", "i_m49", "k_hs6", "v_kusd", "q"])
wi.writerow(["t", "j_m49", "k_hs6", "v_kusd", "q"])

for y in YEARS:
    src = os.path.join(SRC, f"BACI_HS92_Y{y}_V202601.csv")
    n_m = n_i = 0
    with open(src, encoding="utf-8") as fh:
        rd = csv.reader(fh)
        hdr = next(rd)
        # columns: t,i,j,k,v,q
        for row in rd:
            t, i, j, k, v, q = row[0], row[1], row[2], row[3], row[4], row[5]
            if j == RUS:
                wm.writerow([t, i, k, v, q]); n_m += 1
                agg["mirror_by_year"][t] = agg["mirror_by_year"].get(t, Decimal(0)) + Decimal(v)
                if i == IRN:
                    agg["iran_to_rus_by_year"][t] = agg["iran_to_rus_by_year"].get(t, Decimal(0)) + Decimal(v)
            if i == IRN:
                wi.writerow([t, j, k, v, q]); n_i += 1
                agg["iran_total_exports_by_year"][t] = agg["iran_total_exports_by_year"].get(t, Decimal(0)) + Decimal(v)
    agg["mirror_rows"] += n_m
    agg["iran_rows"] += n_i
    print(f"{y}: mirror rows {n_m:,} | iran-exports rows {n_i:,}", flush=True)
fm.close(); fi.close()

# QA note: v is in thousand USD in BACI → convert aggregates to USD for readability
for key in ("mirror_by_year", "iran_to_rus_by_year", "iran_total_exports_by_year"):
    agg[key] = {y: f"{(v * 1000):.4f}" for y, v in sorted(agg[key].items())}
meta = {"snapshot": SNAP, "source": "BACI HS92 V202601 (CEPII), released 2026-01-20, coverage 1995-2024",
        "units": "v = thousand USD (aggregates below in USD); q = metric tons",
        "mirror_definition": "partner-reported exports to Russia (j=643), CIF basis → FOB adj. κ in R2",
        "analysis_window_note": "BACI coverage ends 2024 → 2025 must come from est sources (IRICA/partner monthly) per mental-model §9",
        **agg}
with open(os.path.join(BAC, f"qa-aggregates__{SNAP}.json"), "w", encoding="utf-8") as fh:
    json.dump(meta, fh, indent=2)
print(json.dumps({k: meta[k] for k in ("mirror_by_year", "iran_to_rus_by_year", "iran_total_exports_by_year")}, indent=1))
print("DONE")
