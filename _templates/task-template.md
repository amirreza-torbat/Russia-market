---
type: template
template_for: task-note
created: 2026-09-15
last_updated: 1405-06-24
status: done
---

# قالب یادداشت تسک (Task) — تطبیق‌یافته برای شناسه R#

> این قالب برای ساخت تسک جدید در `01-Tasks/` استفاده شود. نام فایل: `R#-task-slug.md`. انواع مجاز: `scan / validate / analyze / compile / review`.

```markdown
---
type: task
task_id: R#
title: عنوان کوتاه فارسی
status: draft|pending|in-progress|review|done|blocked
task_type: scan|validate|analyze|compile|review
assignee: research-agent|data-engineer|analyst|qa-validator|vault-writer|git-publisher
created: YYYY-MM-DD
updated: YYYY-MM-DD
depends_on: [R#]
blocks: [R#]
estimated_effort: N session(s)
---

# R# — عنوان تسک

## 🎯 هدف
[۱-۲ جمله — چرا این تسک]

## 📋 شرح کار
### مرحله ۱: ...
- ...
### مرحله ۲: ...
- ...

## ✅ معیار پذیرش (Acceptance)
1. ...
2. ... (شامل گیت QA در صورت وجود)

## 📦 خروجی‌ها
- مسیر فایل‌های خروجی

## مراجع
[[conventions]] · [[data-sources]] · فایل‌های مرتبط
```

## قراردادهای یادآوری (میراث مرجع)

- شروع تسک: STATUS.md → `in-progress` + شاخه `feature/R#-slug`.
- پایان تسک: progress.md سطر final + MOC و STATUS → `done`.
- محاسبات فقط Decimal؛ تلورانس < 0.0001٪.
- مسأله → `issues.md` (فقط افزودن).
