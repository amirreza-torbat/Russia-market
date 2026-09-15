---
type: task
task_id: R2
title: اعتبارسنجی داده و reconciliation آینه‌ای
status: draft
task_type: validate
assignee: data-engineer + qa-validator
created: 2026-09-15
updated: 2026-09-15
depends_on: [R1]
blocks: [R3]
estimated_effort: 1 session
---

# R2 — اعتبارسنجی داده و Mirror Reconciliation

> ⚠️ **Placeholder (draft)** — نهایی‌سازی پس از R1.

## 🎯 هدف
تضمین کیفیت داده mirror و داده رسمی قبل از تحلیل: اعتبارسنجی متقابل، تنظیم CIF→FOB، و تولید Parquet پردازش‌شده با دقت Decimal.

## 📋 شرح کار (پیش‌نویس)

### مرحله ۱: ETL و نرمال‌سازی
- پارس raw → schema مصوب (`flow`, `reporter_iso3`, `hs6`, `value_usd_fob`, `est_flag`, …).
- نگاشت نام شرکا → ISO3/M49 (فایل مرجع `countries.csv`)؛ موارد مبهم → `issues.md` (الگوی Issue-004 مرجع).
- خروجی: `05-Data/processed/mirror-russia-imports-2021-2025.parquet` (+ فایل سمت ایران IRICA).

### مرحله ۲: تنظیم CIF→FOB
- اعمال `FOB = CIF × (1 − κ)`؛ حساسیت‌سنجی κ ∈ {3%, 4%, 4.5%, 5%, 6%} و ثبت κ مصوب در `decisions.md`.

### مرحله ۳: اعتبارسنجی متقابل (گیت اصلی این تسک)
- دوره هم‌پوشان 2021–Q1-2022: مقایسه mirror با FTS رسمی → bias factor به تفکیک شریک بزرگ (چین، بلاروس، ترکیه، …).
- مقایسه سمت ایران: IRICA vs mirror صادرات ایران به روسیه.
- تلورانس QA < 0.0001٪ روی sum ها؛ شکست → `issues.md` + برگشت به R1.

## ✅ معیار پذیرش (پیش‌نویس)
1. Parquet با schema مصوب، بدون null در فیلدهای کلیدی.
2. گزارش reconciliation (bias per partner) در `05-Data/processed/` + یادداشت در `06-Analysis` (پس از ساخت).
3. همه تست‌های عددی < 0.0001٪ و در `qa-report.md` ثبت شده.
4. `est_flag` برای همه رکوردهای تخمینی پر شده باشد.

## مراجع
[[conventions]] بخش ۴ · [[data-sources]] · `/04-State/qa-report.md`
