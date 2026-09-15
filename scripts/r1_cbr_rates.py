#!/usr/bin/env python3
"""R1: daily RUB/USD (CBR via cbr-xml-daily mirror), 2021-01-01..2026-09-15.
Checkpointed + resumable (ck-cbr-daily.jsonl). Outputs:
  raw/cbr/cbr-daily__usd__2021-01-01_2026-09-15__<snap>.csv (not committed)
  processed/cbr-rates-annual.csv
"""
import csv, datetime as dt, json, os, threading, time, requests
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal, ROUND_HALF_UP

BASE = "/home/z/my-project/Russia-market/05-Data"
RAW = os.path.join(BASE, "raw", "cbr")
PROC = os.path.join(BASE, "processed")
os.makedirs(RAW, exist_ok=True); os.makedirs(PROC, exist_ok=True)
SNAP = dt.date.today().strftime("%Y%m%d")
START, END = dt.date(2021, 1, 1), dt.date(2026, 9, 15)
CK = os.path.join(RAW, "ck-cbr-daily.jsonl")
daily_csv = os.path.join(RAW, f"cbr-daily__usd__2021-01-01_2026-09-15__{SNAP}.csv")

have = {}
if os.path.exists(CK):
    with open(CK, encoding="utf-8") as fh:
        for line in fh:
            try:
                d, v = line.rstrip("\n").split("\t")
                have[d] = v
            except ValueError:
                pass

days = []
d = START
while d <= END:
    if d.weekday() < 5 and d.isoformat() not in have:
        days.append(d)
    d += dt.timedelta(1)
print(f"to fetch: {len(days)} (cached: {len(have)})", flush=True)

lock = threading.Lock()
ckf = open(CK, "a", encoding="utf-8")

def crawl(day, tries=3):
    url = f"https://www.cbr-xml-daily.ru/archive/{day:%Y/%m/%d}/daily_json.js"
    for a in range(tries):
        try:
            r = requests.get(url, timeout=(10, 25), headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
            if r.status_code == 200:
                usd = r.json().get("Valute", {}).get("USD")
                if usd:
                    v = str(Decimal(str(usd["Value"])) / Decimal(usd.get("Nominal", 1)))
                    with lock:
                        ckf.write(f"{day.isoformat()}\t{v}\n"); ckf.flush()
                        have[day.isoformat()] = v
                    return
            elif r.status_code == 404:
                return                     # holiday — no rate set
            elif r.status_code == 429:
                time.sleep(2 + 2 * a); continue
            time.sleep(0.5 + a)
        except Exception:
            time.sleep(0.5 + a)
    with lock:
        print(f"WARN: failed {day}", flush=True)

with ThreadPoolExecutor(max_workers=10) as ex:
    list(ex.map(crawl, days))
ckf.close()

rows = sorted(have.items())
with open(daily_csv, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["date", "usd_rub"])
    for dstr, v in rows:
        w.writerow([dstr, v])

by_year = {}
for dstr, v in rows:
    by_year.setdefault(dstr[:4], []).append(Decimal(v))
out = [["year", "usd_rub_avg", "days_counted", "period", "source", "snapshot_date"]]
for y in sorted(by_year):
    vals = by_year[y]
    avg = (sum(vals) / len(vals)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    out.append([y, f"{avg}", len(vals), "ytd" if y == "2026" else "full",
                "CBR official rate via cbr-xml-daily.ru mirror", SNAP])
with open(os.path.join(PROC, "cbr-rates-annual.csv"), "w", newline="", encoding="utf-8") as fh:
    csv.writer(fh).writerows(out)
for r in out[1:]:
    print(r)
