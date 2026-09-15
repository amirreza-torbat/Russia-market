---
folder: 05-Data
type: moc
created: 2026-09-15
last_updated: 1405-06-25
status: done
---

# 🗺️ MOC داده (Data Map of Content)

> داده خام commit نمی‌شود (`.gitignore`) — اسکریپت‌های `scripts/` منبع حقیقت بازتولید هستند (قرارداد conventions بخش ۷).

## ساختار

| زیرپوشه | محتوا | وضعیت |
|---------|-------|--------|
| `raw/bac/` | BACI HS92 V202601 (zip کامل + فیلترهای R1: `bac__mirror_643__h6__2021-2024__20260916.csv`، `bac__iran-exports__h6__2021-2024__20260916.csv`، `qa-aggregates__20260916.json`، `src/` چهار فایل سالانه + کدها) | ✅ R1 |
| `raw/cbr/` | نرخ روزانه USD (۱٬۳۲۴ روز کاری) + checkpoint JSONL | ✅ R1 |
| `interim/` | فایل‌های میانی ETL | خالی — R2 |
| `processed/` | `countries.csv` (۲۳۸)، `cbr-rates-annual.csv`، `hs6-codes.csv` (۵٬۰۲۲) | ✅ R1 — Parquet در R2 |

## فایل‌های مرجع برنامه‌ریزی‌شده (R2–R3)

- `processed/mirror-russia-imports-2021-2024.parquet` — ستون فقرات mirror (از فیلتر R1؛ کالیبراسیون سالانه مطابق Issue-006)
- `processed/iran-side-*.parquet` — از IRICA (منبع اصلی M2 — Issue-007) + YTD-2026 با `partial_year`
- `processed/trend-analysis.parquet`، `trend-classification.parquet`، `market-candidates-ranked.parquet` — خروجی R3

## مراجع

- [[data-sources]] — کاتالوگ منابع و schema · [[conventions]] بخش ۴ و ۷ · `07-Exports/01-raw-consolidated.xlsx` (خلاصه R1 + qa-notes)
