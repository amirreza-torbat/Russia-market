---
type: task
task_id: R3
title: تحلیل روند، طبقه‌بندی و رتبه‌بندی بازار
status: draft
task_type: analyze
assignee: analyst
created: 2026-09-15
updated: 2026-09-15
depends_on: [R2]
blocks: [R4]
estimated_effort: 1-2 session
---

# R3 — تحلیل روند، طبقه‌بندی ۷+۳ و رتبه‌بندی ۶ وزنی

> ⚠️ **Placeholder (draft)** — نهایی‌سازی پس از R2. قلب پروژه (الگوی task-10/11/12 مرجع).
>
> 🆕 **Scope v2**: علاوه بر حلقه تجاری، ماتریس ظرفیت صادراتی ایران (M2)، پرچم‌های `war_opportunity`/`import_dependence` (M1) و سهم رقبا (M3) اضافه شد؛ خروجی اکسل 02 و 03 ([/07-Exports/_MOC](../07-Exports/_MOC.md)).

## 🎯 هدف
اجرای حلقه کامل تحلیل روی همه جفت‌های (کالا × جریان) در بازه مصوب، طبقه‌بندی روند، و رتبه‌بندی کاندیدها با فرمول ۶ وزنی شامل ضریب اصطکاک تحریمی.

## 📋 شرح کار (پیش‌نویس)

### مرحله ۱: شاخص‌های روند (الگوی task-10)
- محاسبه کامل شاخص‌ها برای **تمام** جفت‌ها بدون فیلتر: `cagr`, `slope(OLS)`, `r_squared`, `mk_p_value(Mann-Kendall با tie correction)`, `cv`, `trend_consistency`, `mean_recent_3y`, …
- مدیریت sparse data مطابق recipe-09 مرجع (صفر/NAN → Decimal(0)؛ همه-صفر → حذف؛ ناقص وسط سری → `insufficient_data`).
- خروجی: `05-Data/processed/trend-analysis.parquet`.

### مرحله ۲: طبقه‌بندی (الگوی task-11)
- اعمال تاکسونومی ۷+۳ با ترتیب اولویت recipe-09 و آستانه‌های مصوب R1.
- خروجی: `trend-classification.parquet` + تجمیع به سطح فصل.

### مرحله ۳: رتبه‌بندی (الگوی task-12)
- فرمول `market_score` ۶ وزنی (conventions بخش ۶) با وزن‌های مصوب Decision-004، شامل محاسبه `sanctions_friction` به تفکیک کالا/جریان.
- فیلتر اولیه + توصیه select/monitor/investigate + پرچم‌های ریسک.
- خروجی: `export-candidates-ranked.parquet` (Top N مصوب).

## ✅ معیار پذیرش (پیش‌نویس)
1. Sum consistency بین trend-analysis و Parquet ورودی < 0.0001٪.
2. هیچ NULL/مقدار نامعتبر در `trend_category`؛ `market_score ∈ [0,1]`؛ rank یکتا.
3. وزن‌ها و آستانه‌ها دقیقاً مطابق decisions.md (نه مقدار پیش‌فرض کد).
4. همه تست‌های recipe-09 (sections ۹) PASS و در qa-report.md ثبت.

## مراجع
[[conventions]] بخش ۵-۶ · `03-Recipes/recipe-09-trend-classification.md` · `/04-State/decisions.md`
