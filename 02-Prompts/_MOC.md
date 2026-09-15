---
folder: 02-Prompts
type: moc
created: 2026-09-15
last_updated: 1405-06-24
status: draft
---

# 🗺️ MOC پرامپت‌ها (Prompts Map of Content)

> ⚠️ اسکلت bootstrap — پرامپت‌های نقش‌محور در R1 بر اساس الگوی `02-Prompts/` پروژه مرجع نوشته می‌شوند.

## نقش‌های برنامه‌ریزی‌شده (الگوی مرجع)

| نقش | وظیفه | فایل (در R1) | وضعیت |
|-----|--------|--------------|--------|
| Research Agent | اسکن منابع، دانلود داده، راستی‌آزمایی | `prompt-research-agent.md` | ⬜ planned |
| Data Engineer | ETL، نرمال‌سازی، mirror reconciliation | `prompt-data-engineer.md` | ⬜ planned |
| Analyst | روند، طبقه‌بندی ۷+۳، رتبه‌بندی ۶ وزنی | `prompt-analyst.md` | ⬜ planned |
| QA Validator | تلورانس < 0.0001٪، کامل‌بودن | `prompt-qa-validator.md` | ⬜ planned |
| Vault Writer | نگارش یادداشت‌های تحلیلی با backlink | `prompt-vault-writer.md` | ⬜ planned |
| Git Publisher | commit/push/release/closure | `prompt-git-publisher.md` | ⬜ planned |

## قرارداد مشترک همه پرامپت‌ها (میراث مرجع)

هر پرامپت باید این بندها را به agent یادآوری کند:
1. قبل از شروع: خواندن `04-State/STATUS.md` و `00-Overview/conventions.md`.
2. محاسبات فقط `decimal.Decimal`؛ تلورانس < 0.0001٪.
3. پس از پایان: ثبت در `progress.md` و به‌روزرسانی `STATUS.md` (طبق recipe-08 مرجع).
4. مسائل → `issues.md` (فقط افزودن).
5. هیچ توکن/محرمانه‌ای در فایل‌ها.

## مراجع

- [/01-Tasks/_MOC](../01-Tasks/_MOC.md) · [/03-Recipes/_MOC](../03-Recipes/_MOC.md) · [/04-State/STATUS](../04-State/STATUS.md)
