---
folder: 04-State
type: status
created: 2026-09-15
last_updated: 1405-06-25
---

# 📊 وضعیت پروژه (STATUS)

> **این فایل نقطه شروع هر agent است.** قبل از هر کاری این فایل را بخوانید.

## 🎯 وضعیت کلی

| فیلد | مقدار |
|------|-------|
| **وضعیت کلی** | 🟢 `R1-done → ready-for-R2` — قراردادها نهایی، داده پایه BACI/CBR دانلود و QA اولیه شد (Decision-005) |
| **تسک فعلی** | `R1` تکمیل شد (۱۴۰۵-۰۶-۲۵) — گام بعدی `R2` (اعتبارسنجی و reconciliation) |
| **agent مسئول** | research-agent (R1) |
| **آخرین به‌روزرسانی** | ۱۴۰۵-۰۶-۲۵ |
| **بلوک‌ها** | — (Issue-001 امنیتی: revoke توکن توسط کاربر) |
| **قدم بعدی** | شروع `R2`: ETL → Parquet معتبر، CIF→FOB (κ=4.5٪ مصوب)، کالیبراسیون سالانه mirror با جمع‌های کلان FTS (Issue-006)، دانلود IRICA (منبع اصلی M2 — Issue-007)، اعتبارسنجی متقاطع Comtrade + QA gate |

## 📋 وضعیت تسک‌ها

| Task ID | عنوان | وضعیت | Assignee | به‌روزرسانی |
|---------|-------|-------|----------|--------------|
| `R1` | اسکن اولیه + نهایی‌سازی قراردادها | 🟢 `done` (۱۴۰۵-۰۶-۲۵) | research-agent | 1405-06-25 |
| `R2` | اعتبارسنجی و reconciliation | ⬜ `pending` (ورودی‌ها آماده: mirror/iran CSV، cbr-rates، لنگرهای کالیبراسیون) | data-engineer | 1405-06-25 |
| `R3` | روند + طبقه‌بندی + رتبه‌بندی | 🟨 `draft` | — | — |
| `R4` | تدوین گزارش‌ها و خروجی‌ها | 🟨 `draft` | — | — |
| `R5` | QA نهایی + closure + release | 🟨 `draft` | — | — |

**راهنما**: 🟨 draft → ⬜ pending → 🟡 in-progress → 🟠 review → 🟢 done | 🔴 blocked

## 🚦 مسیر فعلی

```
[bootstrap: اسکلت Vault + مصوبه موضوع] ✅
        ↓
[R1: scan] 🟢 ۱۴۰۵-۰۶-۲۵ — قراردادها نهایی + داده پایه BACI/CBR + Decision-005
        ↓
[R2: validate] ⬜ → [R3: analyze] ⬜ → [R4: compile] ⬜ → [R5: review/publish] ⬜
```

## 🆕 تغییرات اخیر

- ۱۴۰۵-۰۶-۲۴: bootstrap انجام شد — ساختار Vault از مرجع `Market-Research` الگوبرداری شد؛ conventions/گلاسری/data-sources با تطبیق روسیه (تقویم میلادی، mirror data، CIF→FOB، w6 تحریمی) نوشته شد؛ درس‌آموخته‌ها در `00-Overview/lessons.md`.
- ۱۴۰۵-۰۶-۲۴: راستی‌آزمایی مجدد bootstrap — مطالعه مستقل ۱۴ فایل مرجع تأیید شد؛ دو قالب یادداشت تحلیل/کاندید به `_templates/` افزوده شد (parity کامل با مرجع).
- ۱۴۰۵-۰۶-۲۴: فاز ۳ bootstrap — کاربر موضوع «فرصت صادرات ایران→روسیه» + پارامترها (2021–2025، HS6 کامل، BAC-mirror، مقایسه رقبا، وزن‌های پیش‌فرض، Obsidian، Top 100) را مصوب کرد (Decision-002/003) → پروژه `ready-for-R1`.
- ۱۴۰۵-۰۶-۲۵: **R1 اجرا و بسته شد** — Decision-005 (رفع همه TBDها: HS6، وزن‌ها، آستانه‌ها، κ=4.5٪، قاعده حاشیه، BACI V202601 لنگر، CBR-mirror، کالیبراسیون سالانه، IRICA محوری)؛ راستی‌آزمایی مستند FTS №312 / FTA لازم‌الاجرا ۲۰۲۵-۰۵-۱۵ / №506+№1532+№2701+№135 / №1721؛ تصحیح SLEI/RUICS (Issue-008)؛ داده پایه: mirror 2021–2024 (284.6G→201.8G$)، صادرات ایران، cbr-rates، countries.csv، hs6-codes؛ ورک‌بوک `01-raw-consolidated.xlsx` (شیت qa-notes)؛ قالب‌ها با پرچم‌های Scope v2 به‌روز؛ Issues-005..007 جدید.

## ⚠️ مسائل بحرانی

1. ~~Pending-001 (blocker)~~ — ✅ رفع شد (۱۴۰۵-۰۶-۲۴): موضوع مصوب = فرصت صادرات ایران→روسیه (Decision-002).
2. **Issue-001 (security)**: توکن دسترسی این مأموریت باید پس از پایان کار revoke شود (الگوی Issue-001 مرجع).
3. **Issue-006 (داده)**: کالیبراسیون سالانه mirror در R2 الزامی است (پوشش 2024 ≈۷۱٪).
4. **Issue-007 (داده)**: سمت ایران فقط با IRICA — BACI نامعتبر پس از ۲۰۲۲.

## 📝 یادداشت برای agentهای بعدی

- قبل از هر کاری: [[conventions]] (اکنون status: done) + [[lessons]] را بخوان.
- مصوبات: Decision-002/003/004/005 در `decisions.md` — پараметرهای اجرای R2 (κ، آستانه‌ها، کالیبراسیون، IRICA) همگی مصوب‌اند.
- R2 ورودی‌های آماده دارد: `raw/bac/bac__mirror_643__h6__2021-2024__20260916.csv`، `raw/bac/bac__iran-exports__h6__2021-2024__20260916.csv`، `processed/cbr-rates-annual.csv`، `processed/countries.csv`، `processed/hs6-codes.csv`، لنگرهای کالیبراسیون در شیت qa-notes ورک‌بوک.
- داده BACI فقط تا 2024 دارد — 2025/YTD-2026 در R2 از IRICA/شرکا با `partial_year`.
- raw هرگز commit نمی‌شود — اسکریپت‌های `scripts/` منبع بازتولید هستند.

## 🔗 مراجع

- [/01-Tasks/_MOC](../01-Tasks/_MOC.md) · [/00-Overview/conventions](../00-Overview/conventions.md) · [/04-State/decisions](decisions.md) · [/04-State/issues](issues.md)
