---
type: task
task_id: R1
title: اسکن اولیه — نهایی‌سازی قراردادها و دانلود داده پایه
status: done
task_type: scan
assignee: research-agent
created: 2026-09-15
updated: 2026-09-15
depends_on: [bootstrap]
blocks: [R2]
estimated_effort: 1-2 session
---

# R1 — اسکن اولیه (نهایی‌سازی conventions + دانلود داده پایه)

> ✅ **موضوع و پارامترها مصوب شد (۱۴۰۵-۰۶-۲۴)**: فرصت صادرات ایران→روسیه + پارامترهای ۷گانه (Decision-002/003 در `04-State/decisions.md`). این تسک مصوبات را عملیاتی می‌کند.
>
> 🆕 **Scope v2 (Decision-004)**: بازه 2021–2025 + YTD تا ماه ۹ ۲۰۲۶؛ ماژول‌های M1–M8 ([[mental-model]])؛ خروجی ۵ ورک‌بوک Excel + Vault (Canvas/داشبورد). پرچم‌های جدید schema برای افزودن در R1: `war_opportunity`، `unfriendly_surcharge_advantage`، `import_dependence`، `partial_year`.

## 🎯 هدف
تبدیل اسکلت bootstrap به سند مصوب عملیاتی: ثبت موضوع تحلیل، نهایی‌سازی پارامترهای TBD در `conventions.md`، مصوبه منابع، و دانلود/بازتولید داده پایه.

## 📋 شرح کار (پیش‌نویس)

### مرحله ۱: ثبت موضوع و پارامترها
- پاسخ‌های bootstrap کاربر → `decisions.md` (Decision-001: موضوع؛ Decision-002: بازه زمانی؛ Decision-003: دانه‌بندی؛ Decision-004: وزن‌های فرمول؛ Decision-005: منابع).
- به‌روزرسانی `project-overview.md` (scope نهایی) و رفع همه `TBD در R1` از `conventions.md`.

### مرحله ۲: راستی‌آزمایی‌های مستندشده
- شماره مصوبه محرمانگی آمار FTS (مارس ۲۰۲۲) — در `issues.md` نتیجه ثبت شود.
- وضعیت لازم‌الاجرا بودن FTA کامل ایران–اوراسیا (۲۰۲۵).
- تعریف دقیق SLEI/RUICS-IPS و افزودن به `glossary.md`.

### مرحله ۳: دانلود داده پایه (تکرارپذیر)
- اسکریپت `scripts/download_mirror_data.py` → BAC/CEPII bulk (partner=RUS) + Comtrade (اعتبارسنجی متقاط) → `05-Data/raw/` (بدون commit).
- نرخ‌های سالانه CBR → `05-Data/processed/cbr-rates-annual.csv`.
- ساخت `05-Data/processed/countries.csv`.

## ✅ معیار پذیرش (پیش‌نویس)
1. همه TBDهای conventions مصوب و در decisions.md ثبت شده‌اند.
2. داده پایه 2021–2025 در raw موجود و با اسکریپت بازتولید می‌شود.
3. countries.csv و cbr-rates-annual.csv با QA اولیه (sum/tol < 0.0001٪ نسبت به منبع) ساخته شده‌اند.
4. STATUS.md و progress.md به‌روز.

## ✅ صورت‌جلسه اجرا (۱۴۰۵-۰۶-۲۵ — وضعیت: done)
| معیار | نتیجه |
|-------|-------|
| ۱. رفع TBDها | ✅ Decision-005 (بند‌های ۱–۵، ۱۰) — conventions → status: done |
| ۲. داده پایه در raw | ✅ BACI HS92 V202601 (2.4GB؛ پوشش واقعی تا **2024** — مستند شد) + فیلترهای mirror/iran (۳۷MB)؛ 2025/YTD-2026 طبق Decision-005 از IRICA/شرکا در R2 |
| ۳. QA اولیه | ✅ countries.csv (۲۳۸)، cbr-rates-annual.csv (۱٬۳۲۴ روز کاری)، hs6-codes.csv (۵٬۰۲۲)؛ جمع TOTAL ورک‌بوک = qa-aggregates JSON (تطابق کامل < 0.0001٪) |
| ۴. State به‌روز | ✅ STATUS/progress/qa-report/issues (Issue-005..008)/decisions (Decision-005) |

**راستی‌آزمایی‌های مرحله ۲**: FTS №312 (2022-03-09) ✅؛ FTA کامل ایران–اوراسیا لازم‌الاجرا 2025-05-15 ✅؛ واردات موازی №506/№1532/№2701/№135 ✅؛ surcharge №1721 ✅؛ SLEI/RUICS-IPS نامعتبر → حذف و تصحیح (Issue-008) ✅ — تعاریف در [[glossary]].

**یافته‌های کلیدی داده** (جزئیات در `01-raw-consolidated.xlsx` شیت qa-notes): mirror 2021 = 284.6G$ (≈۰٫۹۶۱× رسمی)؛ افت پوشش پس از ۲۰۲۲ → کالیبراسیون سالانه (Issue-006)؛ پوشش BACI سمت ایران فروپاشیده → IRICA منبع اصلی M2 (Issue-007).

## مراجع
[[conventions]] · [[data-sources]] · [[lessons]] · `/04-State/decisions.md`
