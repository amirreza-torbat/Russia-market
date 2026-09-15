---
folder: 04-State
type: status
created: 2026-09-15
last_updated: 1405-06-24
---

# 📊 وضعیت پروژه (STATUS)

> **این فایل نقطه شروع هر agent است.** قبل از هر کاری این فایل را بخوانید.

## 🎯 وضعیت کلی

| فیلد | مقدار |
|------|-------|
| **وضعیت کلی** | 🟢 `ready-for-R1` — موضوع و پارامترها مصوب (Decision-002/003) + **Scope v2** (چرخه کامل ورود به بازار — Decision-004) |
| **تسک فعلی** | bootstrap (فاز ۰–۳ مأموریت) تکمیل شد — گام بعدی `R1` |
| **agent مسئول** | research-agent (bootstrap) |
| **آخرین به‌روزرسانی** | ۱۴۰۵-۰۶-۲۴ |
| **بلوک‌ها** | — (Pending-001/002 با مصوبه کاربر رفع شد؛ Issue-001 امنیتی: revoke توکن توسط کاربر) |
| **قدم بعدی** | شروع `R1`: عملیاتی‌سازی Decision-002/003/004 (نگاشت M1–M8 از [[mental-model]])، رفع `TBD در R1`، دانلود داده پایه BAC-mirror + IRICA |

## 📋 وضعیت تسک‌ها

| Task ID | عنوان | وضعیت | Assignee | به‌روزرسانی |
|---------|-------|-------|----------|--------------|
| `R1` | اسکن اولیه + نهایی‌سازی قراردادها | 🟨 `draft` (پس از پاسخ کاربر: pending) | — | 1405-06-24 |
| `R2` | اعتبارسنجی و reconciliation | 🟨 `draft` | — | — |
| `R3` | روند + طبقه‌بندی + رتبه‌بندی | 🟨 `draft` | — | — |
| `R4` | تدوین گزارش‌ها و خروجی‌ها | 🟨 `draft` | — | — |
| `R5` | QA نهایی + closure + release | 🟨 `draft` | — | — |

**راهنما**: 🟨 draft → ⬜ pending → 🟡 in-progress → 🟠 review → 🟢 done | 🔴 blocked

## 🚦 مسیر فعلی

```
[bootstrap: اسکلت Vault + مصوبه موضوع] ✅ (فاز ۰–۳ مأموریت)
        ↓
[R1: scan] ⬜ → [R2: validate] ⬜ → [R3: analyze] ⬜ → [R4: compile] ⬜ → [R5: review/publish] ⬜
```

## 🆕 تغییرات اخیر

- ۱۴۰۵-۰۶-۲۴: bootstrap انجام شد — ساختار Vault از مرجع `Market-Research` الگوبرداری شد؛ conventions/گلاسری/data-sources با تطبیق روسیه (تقویم میلادی، mirror data، CIF→FOB، w6 تحریمی) نوشته شد؛ درس‌آموخته‌ها در `00-Overview/lessons.md`.
- ۱۴۰۵-۰۶-۲۴: راستی‌آزمایی مجدد bootstrap — مطالعه مستقل ۱۴ فایل مرجع تأیید شد؛ دو قالب یادداشت تحلیل/کاندید به `_templates/` افزوده شد (parity کامل با مرجع).
- ۱۴۰۵-۰۶-۲۴: فاز ۳ bootstrap — کاربر موضوع «فرصت صادرات ایران→روسیه» + پارامترها (2021–2025، HS6 کامل، BAC-mirror، مقایسه رقبا، وزن‌های پیش‌فرض، Obsidian، Top 100) را مصوب کرد (Decision-002/003) → پروژه `ready-for-R1`.
- ۱۴۰۵-۰۶-۲۴: **Scope v2 (Decision-004)** — روایت گسترش‌یافته کارفرما ثبت شد: ۸ ماژول M1–M8 ([[mental-model]])، بازه تا ماه ۹ ۲۰۲۶، ۵ ورک‌بوک Excel (`07-Exports/_MOC.md`)، Canvas نقشه پروژه (`project-flow.canvas`)، داشبورد و پلاگین‌های Obsidian ([[obsidian-setup]]).

## ⚠️ مسائل بحرانی

1. ~~Pending-001 (blocker)~~ — ✅ رفع شد (۱۴۰۵-۰۶-۲۴): موضوع مصوب = فرصت صادرات ایران→روسیه (Decision-002).
2. **Issue-001 (security)**: توکن دسترسی این مأموریت باید پس از پایان کار revoke شود (الگوی Issue-001 مرجع).

## 📝 یادداشت برای agentهای بعدی

- قبل از هر کاری: [[conventions]] + [[lessons]] را بخوان.
- مصوبات کاربر در `decisions.md` (Decision-002/003/004) ثبت شده — اولین کار R1، عملیاتی‌سازی همین مصوبات (از جمله نگاشت M1–M8 در [[mental-model]] بخش ۸) و رفع `TBD در R1` است.
- تسک‌های R1–R5 فعلاً **placeholder/draft** هستند و در ابتدای R1 نهایی می‌شوند.
- هیچ داده‌ای در مخزن نیست — raw با اسکریپت دانلود می‌شود و commit نمی‌گردد.

## 🔗 مراجع

- [/01-Tasks/_MOC](../01-Tasks/_MOC.md) · [/00-Overview/conventions](../00-Overview/conventions.md) · [/04-State/decisions](decisions.md) · [/04-State/issues](issues.md)
