---
type: task
task_id: R5
title: بازبینی نهایی، QA و انتشار
status: draft
task_type: review
assignee: qa-validator + git-publisher
created: 2026-09-15
updated: 2026-09-15
depends_on: [R4]
blocks: []
estimated_effort: 0.5-1 session
---

# R5 — بازبینی نهایی، QA و انتشار (Closure + Release)

> ⚠️ **Placeholder (draft)** — نهایی‌سازی پس از R4.
>
> 🆕 **Scope v2**: R5 علاوه بر QA/closure، حاشیه سود (M6: ماشین‌حساب landed cost) و نقشه راه ورود (M8: تقویم ۱۲ ماهه) را تولید می‌کند → خروجی `05-margin-roadmap.xlsx` ([[mental-model]] بخش ۸).

## 🎯 هدف
اجرای QA نهایی کل حلقه، تکمیل placeholderهای State، و انتشار نسخه نهایی (release tag) مطابق الگوی task-06/09 مرجع.

## 📋 شرح کار (پیش‌نویس)

### مرحله ۱: QA نهایی (الگوی qa-report مرجع)
- تست‌های عددی (sum consistency در هر سطح)، کامل‌بودن، فرمت (hs6 string، iso3)، تحلیل (پوشش همه جفت‌ها)، متقابل (مقایسه با منبع دوم).
- تلورانس کل < 0.0001٪ — شکست → issues.md + برگشت به تسک مربوطه.

### مرحله ۲: بستن پروژه
- تکمیل `04-State/closure.md` (خروجی‌ها، آمار کلیدی، یافته‌های اصلی، درس‌آموخته‌ها، پیشنهادها برای پروژه بعدی).
- به‌روزرسانی `executive-summary.md` و STATUS نهایی.

### مرحله ۳: انتشار
- مرور نهایی diff، merge همه feature branches، tag نسخه (`v1.0.0-YYYYMMDD`)، و یادآوری revoke توکن به کاربر (الگوی Issue-001).

## ✅ معیار پذیرش (پیش‌نویس)
1. qa-report.md کامل با نتیجه همه تست‌ها (PASS/FAIL).
2. closure.md تکمیل و STATUS = done.
3. Release tag ایجاد شده؛ تاریخچه git تمیز (`type(scope): subject`).
4. هیچ راز/توکنی در تاریخچه مخزن وجود ندارد (بررسی نهایی).

## مراجع
`/04-State/qa-report.md` · `/04-State/closure.md` · [[lessons]] بخش ۴
