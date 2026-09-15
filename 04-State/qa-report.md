---
folder: 04-State
type: qa-report
status: pending
created: 2026-09-15
last_updated: 1405-06-24
---

# 🧪 گزارش QA (Placeholder)

> این فایل در `R2` (گیت اولیه) و `R5` (QA نهایی) پر می‌شود. تا آن زمان placeholder (الگوی مرجع).

## وضعیت فعلی

🟡 **در انتظار اجرای R1/R2** — bootstrap هیچ داده‌ای ندارد که QA شود.

## کاتالوگ تست‌های برنامه‌ریزی‌شده

### تست‌های عددی (تلورانس < 0.0001٪)
- [ ] Test 1.1: مجموع value (raw vs processed) — < 0.0001٪
- [ ] Test 1.2: مجموع value (trend-analysis vs parquet ورودی)
- [ ] Test 1.3: مجموع value (classification vs trend-analysis)
- [ ] Test 1.4: consistency تبدیل CIF→FOB (κ مصوب، بازه حساسیت مستند)

### تست‌های کامل‌بودن
- [ ] Test 2.1: همه سال‌های بازه مصوب موجود (partial بودن سال پایانی مستند)
- [ ] Test 2.2: پوشش شرکای اصلی mirror (حداقل Top-10 گزارش‌دهنده)
- [ ] Test 2.3: پوشش کالاها در دانه‌بندی مصوب
- [ ] Test 2.4: بدون null در فیلدهای کلیدی

### تست‌های فرمت
- [ ] Test 3.1: hs6 به‌صورت string با پیش‌صفر حفظ‌شده
- [ ] Test 3.2: ISO3 معتبر (`IRN`, `RUS`, …)؛ M49 (364, 643) در ستون مربوطه
- [ ] Test 3.3: value > 0 برای رکوردهای واقعی؛ est_flag برای تخمینی‌ها

### تست‌های تحلیل
- [ ] Test 4.1: همه جفت‌های (کالا × جریان) در classification دسته‌بندی شده
- [ ] Test 4.2: trend_category بدون مقدار invalid
- [ ] Test 4.3: market_score ∈ [0,1]؛ rank یکتا

### تست‌های متقابل (Mirror)
- [ ] Test 5.1: دوره هم‌پوشان 2021–Q1-2022 — mirror vs FTS رسمی (bias per partner)
- [ ] Test 5.2: سمت ایران — IRICA vs mirror صادرات ایران→روسیه
