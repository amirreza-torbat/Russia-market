---
type: template
template_for: candidate-note
created: 2026-09-15
last_updated: 1405-06-24
status: done
---

# قالب یادداشت کاندید رتبه‌بندی‌شده (Ranked Candidate)

> برای یادداشت‌های `06-Analysis/candidates/rank-NN-*.md` (ساخته‌شده در R4) — الگوی `export-candidates` مرجع با فرمول ۶ وزنی تطبیق‌یافته روسیه (w6 = ضریب اصطکاک تحریمی).
> نام فایل: `rank-NN-<slug>.md` (NN = رتبه، دو رقمی).

```markdown
---
type: analysis
title: کاندید رتبه NN — [نام فارسی محصول/فرصت]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft
tags:
  - candidate
  - rank/NN
  - hs2/[chapter]
related:
  - "[[R3-analyze-market]]"
  - "[[conventions]]"
folder: 06-Analysis/candidates
---

# کاندید رتبه NN — [نام فارسی محصول/فرصت]

## شناسه‌ها
- **HS6 / ТН ВЭД**: `NNNNNN` (string — پیش‌صفر حفظ شود) — فصل: `NN`
- **جریان تحلیل**: mirror_import (واردات روسیه از دید شرکا) / official_export_ir
- **بازه**: 2021–2025 (میلادی) — روش 2025 partial: [YTD / annualized]

## نمره ترکیبی (market_score)
```
market_score = w1*norm(size) + w2*norm(growth) + w3*norm(competition)
             + w4*norm(access) + w5*norm(stability) - w6*norm(sanctions_friction)
```
| مؤلفه | مقدار خام | نرمال‌شده | وزن | سهم |
|-------|-----------|-----------|-----|-----|
| size (اندازه بازار) | ... | 0.XX | w1=0.30 | 0.XXX |
| growth (CAGR) | ... | 0.XX | w2=0.20 | 0.XXX |
| competition (رقابت/شکاف) | ... | 0.XX | w3=0.20 | 0.XXX |
| access (تعرفه/FTA ایران–اوراسیا) | ... | 0.XX | w4=0.10 | 0.XXX |
| stability (trend_consistency) | ... | 0.XX | w5=0.10 | 0.XXX |
| sanctions_friction (جریمه) | ... | 0.XX | w6=0.10 | −0.XXX |
| **market_score** | | | | **0.XX** |

> وزن‌ها طبق مصوبه `decisions.md` (پیش‌فرض 0.30/0.20/0.20/0.10/0.10/0.10 — قابل تغییر با re-run R3).

## توصیه (مطابق recipe-09)
- [ ] `select` — score > 0.7 و دسته رشد معنادار
- [ ] `monitor` — score بین 0.4 و 0.7
- [ ] `investigate` — score < 0.4 یا نوسان بالا

## روند و طبقه‌بندی
- **دسته (۷+۳)**: `...` — CAGR: X.XX٪ | MK p: 0.XXXX | CV: 0.XX | R²: 0.XX
- **شرکای تأمین اصلی 2025**: [کشور ISO3 + سهم ٪ — top 3]
- **خلأ/فرصت**: [جای خالی برندهای خروج‌کرده / رشد تقاضا / کاهش رقابت — ۲-۳ جمله]

## پرچم‌های ریسک
- [ ] `volatile` (CV > 0.7) — [توضیح]
- [ ] `concentrated` (تمرکز شریک اول > 70٪) — [توضیح]
- [ ] `declining_recent` (2025 < 2024) — [توضیح]
- [ ] `partial_data` — [توضیح]
- [ ] `sanctions_exposed` (تقاطع فهرست‌ها / ریسک پرداخت و حمل) — [توضیح]
- [ ] `war_opportunity` (شکاف عرضه پس از ۲۰۲۲ / خروج برندهای غربی — تحلیل M1) — [توضیح]
- [ ] `unfriendly_surcharge_advantage` (مزیت تعرفه‌ای ایران مقابل کشورهای «غیردوست» — مصوبه № 1721) — [توضیح]
- [ ] `import_dependence` (وابستگی ساختاری روسیه به واردات — Rosstat) — [توضیح]
- [ ] `ir_coverage_gap` (داده سمت ایران از BACI نامعتبر — Issue-007؛ مبنای IRICA) — [توضیح]
- [ ] `low_margin` (حاشیه خالص برآوردی < 10٪ — قاعده Decision-005) — [توضیح]

## تحلیل کیفی
[۱۵۰-۲۰۰ کلمه — چرایی جذابیت؛ ساختار رقابت؛ کانال‌های ورود (چه کسی تأمین می‌کند)؛ ملاحظات پرداخت ایران–روسیه (SPFS/ریال-روبل) و لجستیک (کریدور اینشتس/دریای خزر)]

## مراجع
- [[R3-analyze-market]] · [[conventions]] بخش ۶ · [[data-sources]]
- [[candidates/_MOC]] · [[candidates/_executive-ranking]]
```
