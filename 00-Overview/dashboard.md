---
folder: 00-Overview
type: dashboard
title: داشبورد زنده پروژه
created: 2026-09-15
last_updated: 1405-06-24
status: review
tags: [dashboard, dataview, scope-v2]
related: ["[[mental-model]]", "[[obsidian-setup]]"]
---

# 📊 داشبورد زنده پروژه

> ⚠️ **نیازمند پلاگین Dataview** — نصب مطابق [[obsidian-setup]]. این داشبورد خودکار از frontmatter نوت‌ها تغذیه می‌شود؛ با پیشرفت R1–R5 جداول زیر پر می‌شوند.

## وضعیت تسک‌ها (R1–R5)

```dataview
TABLE task_id AS "Task", status AS "وضعیت", task_type AS "نوع", assignee AS "Agent", updated AS "به‌روزرسانی"
FROM "01-Tasks"
WHERE type = "task"
SORT task_id ASC
```

## همه وظایف باز (checkboxها)

```dataview
TASK
FROM "01-Tasks"
WHERE !completed
```

## کاندیدهای صادراتی (در R3 پر می‌شود — Top 20)

```dataview
TABLE status AS "وضعیت", trend_category AS "دسته روند", market_score AS "امتیاز", recommendation AS "توصیه"
FROM "06-Analysis"
WHERE type = "candidate"
SORT market_score DESC
LIMIT 20
```

## یادداشت‌های تحلیلی به تفکیک دسته روند

```dataview
TABLE trend_category AS "دسته ۷+۳", hs6 AS "HS6", war_opportunity AS "فرصت جنگی"
FROM "06-Analysis"
WHERE type = "analysis-topic"
SORT file.name ASC
```

## آخرین تغییرات State

```dataview
TABLE file.mtime AS "زمان", status AS "وضعیت"
FROM "04-State"
SORT file.mtime DESC
LIMIT 10
```

## منابع اکسل (در R1+ پر می‌شود)

```dataview
TABLE status AS "وضعیت", sheets AS "شیت‌ها"
FROM "07-Exports"
WHERE type = "excel-output"
SORT file.name ASC
```

## مراجع

[[mental-model]] · [[obsidian-setup]] · [/01-Tasks/_MOC](../01-Tasks/_MOC.md) · [/07-Exports/_MOC](../07-Exports/_MOC.md)
