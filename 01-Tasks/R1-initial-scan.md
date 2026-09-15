---
type: task
task_id: R1
title: اسکن اولیه — نهایی‌سازی قراردادها و دانلود داده پایه
status: draft
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

## مراجع
[[conventions]] · [[data-sources]] · [[lessons]] · `/04-State/decisions.md`
