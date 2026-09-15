---
folder: 05-Data
type: moc
created: 2026-09-15
last_updated: 1405-06-24
status: draft
---

# 🗺️ MOC داده (Data Map of Content)

> داده خام commit نمی‌شود (`.gitignore`) — اسکریپت‌های `scripts/` منبع حقیقت بازتولید هستند (قرارداد conventions بخش ۷).

## ساختار

| زیرپوشه | محتوا | وضعیت |
|---------|-------|--------|
| `raw/` | خروجی مستقیم منابع (BAC bulk، Comtrade، IRICA، CBR) با الگوی نام `raw/<source>/<dataset>__<params>__YYYYMMDD.csv` | خالی — R1 پر می‌کند |
| `interim/` | فایل‌های میانی ETL | خالی — R2 |
| `processed/` | Parquet/CSV نهایی تحلیل (commit می‌شود) | خالی — R2 |

## فایل‌های مرجع برنامه‌ریزی‌شده (R1–R2)

- `processed/countries.csv` — جدول نگاشت iso3/m49/iso2/name_fa/name_en
- `processed/cbr-rates-annual.csv` — نرخ میانگین سالانه RUB/USD
- `processed/mirror-russia-imports-2021-2025.parquet` — ستون فقرات mirror
- `processed/trend-analysis.parquet`، `trend-classification.parquet`، `market-candidates-ranked.parquet` — خروجی R3

## مراجع

- [[data-sources]] — کاتالوگ منابع و schema · [[conventions]] بخش ۴ و ۷
