---
type: task
task_id: R4
title: تدوین گزارش‌ها و خروجی‌ها
status: draft
task_type: compile
assignee: vault-writer + data-engineer
created: 2026-09-15
updated: 2026-09-15
depends_on: [R3]
blocks: [R5]
estimated_effort: 1 session
---

# R4 — تدوین گزارش‌ها و خروجی‌ها (Obsidian + Excel)

> ⚠️ **Placeholder (draft)** — نهایی‌سازی پس از R3.

## 🎯 هدف
تبدیل خروجی‌های تحلیل R3 به یادداشت‌های Obsidian و فایل Excel نهایی، با ساخت پوشه‌های `06-Analysis/` و `07-Exports/` مطابق ساختار Vault.

## 📋 شرح کار (پیش‌نویس)

### مرحله ۱: ساخت 06-Analysis و 07-Exports
- درخت مطابق مرجع: `06-Analysis/{by-country, by-tariff, trend, export-candidates}` هر یک با `_MOC.md` و `charts/`؛ `07-Exports/` با `_MOC.md`.

### مرحله ۲: یادداشت‌های تحلیلی
- `executive-summary.md`، `methodology.md`، `key-findings.md` در ریشه 06-Analysis (سه فایلی که مرجع در وضعیت فعلی ندارد — ما از ابتدا می‌سازیم).
- یادداشت‌های به تفکیک دسته روند و به تفکیک کالا/بخش با backlink به تسک و منبع (قرارداد ۷.۲ conventions).
- همه اعداد با حداکثر ۴ رقم اعشار و از خروجی R3 (دست‌نویس ممنوع).

### مرحله ۳: خروجی Excel
- فایل `07-Exports/russia-market-<scope>-YYYYMMDD.xlsx` با شیت‌های مصوب (الگوی ۱۸ شیت مرجع: خلاصه، روند، طبقه‌بندی، کاندیدها، QA، …).

## ✅ معیار پذیرش (پیش‌نویس)
1. هر عدد در گزارش‌ها == مقدار Parquet (تست نمونه‌ای < 0.0001٪).
2. همه یادداشت‌ها frontmatter کامل و status: review دارند.
3. Excel با فرمول‌بندی استاندارد و فهرست شیت‌ها مطابق مصوبه.
4. MOCهای جدید به‌روز.

## مراجع
[[conventions]] بخش ۳ و ۸ · `05-Data/processed/` خروجی‌های R3
