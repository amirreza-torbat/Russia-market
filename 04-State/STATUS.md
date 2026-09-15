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
| **وضعیت کلی** | 🟡 `bootstrap-done` — در انتظار انتخاب موضوع توسط کاربر |
| **تسک فعلی** | bootstrap (فاز ۰–۲ مأموریت) تکمیل شد |
| **agent مسئول** | research-agent (bootstrap) |
| **آخرین به‌روزرسانی** | ۱۴۰۵-۰۶-۲۴ |
| **بلوک‌ها** | Pending-001: موضوع تحلیل مصوب نشده |
| **قدم بعدی** | پاسخ کاربر به سؤالات bootstrap → شروع `R1` (نهایی‌سازی conventions و دانلود داده پایه) |

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
[bootstrap: اسکلت Vault] ✅ (این کامیت)
        ↓
[انتظار: پاسخ کاربر به سؤالات bootstrap — موضوع تحلیل] 🔴 blocker
        ↓
[R1: scan] ⬜ → [R2: validate] ⬜ → [R3: analyze] ⬜ → [R4: compile] ⬜ → [R5: review/publish] ⬜
```

## 🆕 تغییرات اخیر

- ۱۴۰۵-۰۶-۲۴: bootstrap انجام شد — ساختار Vault از مرجع `Market-Research` الگوبرداری شد؛ conventions/گلاسری/data-sources با تطبیق روسیه (تقویم میلادی، mirror data، CIF→FOB، w6 تحریمی) نوشته شد؛ درس‌آموخته‌ها در `00-Overview/lessons.md`.
- ۱۴۰۵-۰۶-۲۴: راستی‌آزمایی مجدد bootstrap — مطالعه مستقل ۱۴ فایل مرجع تأیید شد؛ دو قالب یادداشت تحلیل/کاندید به `_templates/` افزوده شد (parity کامل با مرجع).

## ⚠️ مسائل بحرانی

1. **Pending-001 (blocker)**: موضوع دقیق تحلیل بازار روسیه توسط کاربر تأیید نشده — بدون آن R1 شروع نمی‌شود (الگوی Issue-002 مرجع).
2. **Issue-001 (security)**: توکن دسترسی این مأموریت باید پس از پایان کار revoke شود (الگوی Issue-001 مرجع).

## 📝 یادداشت برای agentهای بعدی

- قبل از هر کاری: [[conventions]] + [[lessons]] را بخوان.
- تسک‌های R1–R5 فعلاً **placeholder/draft** هستند؛ اولین کار R1، نهایی‌سازی همین فایل‌ها بر اساس موضوع مصوب است.
- هیچ داده‌ای در مخزن نیست — raw با اسکریپت دانلود می‌شود و commit نمی‌گردد.

## 🔗 مراجع

- [/01-Tasks/_MOC](../01-Tasks/_MOC.md) · [/00-Overview/conventions](../00-Overview/conventions.md) · [/04-State/decisions](decisions.md) · [/04-State/issues](issues.md)
