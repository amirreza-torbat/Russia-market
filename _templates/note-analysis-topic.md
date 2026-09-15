---
type: template
template_for: analysis-note
created: 2026-09-15
last_updated: 1405-06-24
status: done
---

# قالب یادداشت تحلیل (تحلیل موضوع/جریان/محصول)

> این قالب برای یادداشت‌های تحلیلی `06-Analysis/` (ساخته‌شده در R4) استفاده می‌شود — الگوی `note-analysis-country.md` / `note-analysis-tariff.md` مرجع، با تطبیق روسیه.
> نام فایل: `kebab-case` (مثل `topic-machinery-imports.md` یا `flow-mirror-import-hs87.md`).
> قراردادها: سال میلادی، ISO3، Decimal با ۴ رقم اعشار در گزارش.

```markdown
---
type: analysis
title: [عنوان فارسی تحلیل]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft
tags:
  - analysis
  - topic/[slug]
related:
  - "[[R3-analyze-market]]"
  - "[[data-sources]]"
folder: 06-Analysis/[subfolder]
---

# [عنوان فارسی تحلیل]

## خلاصه
[۳-۵ جمله — جایگاه موضوع در بازار روسیه، روند کلی 2021–2025، عامل اصلی (تحریم/جایگزینی واردات/...)]

## داده‌ها
| سال | ارزش (USD FOB) | مبنا | کیفیت | سهم از کل (%) |
|-----|----------------|------|-------|----------------|
| 2021 | ... | official_fts / mirror_cif→fob | t/d/e | ... |
| 2022 | ... | ... | ... | ... |
| 2023 | ... | mirror_cif→fob | e | ... |
| 2024 | ... | mirror_cif→fob | e | ... |
| 2025 | ... | mirror_cif→fob (partial یا annualized) | e | ... |

> مبنا/کیفیت: طبق schema در [[data-sources]] — `value_basis` و `est_flag`.
> سال 2025 partial: روش مقایسه (YTD / annualized) مطابق مصوبه `decisions.md` ذکر شود.

## نمودار
![[charts/[slug]-trend.png]]

## شاخص‌ها
- **CAGR (2021–2025)**: X.XX٪
- **pct_change**: XX.XX٪ — **growth_multiplier**: X.XX
- **slope (OLS) / R²**: X.XX / 0.XX
- **Mann-Kendall p**: 0.XXXX (معنادار در ۹۵٪/۹۰٪: بله/خیر)
- **CV (نوسان)**: 0.XX — **trend_consistency**: X از ۴ بازه رشد مثبت
- **دسته روند (۷+۳)**: `strong_growth` | `moderate_growth` | `stable` | `volatile` | `declining` | `emerging` | `disappearing` | فرعی
- **mean_recent_3y**: X,XXX,XXX USD

## تحلیل کیفی
[۱۵۰-۲۰۰ کلمه — چرایی روند؛ اثر جنگ تجاری/تحریم‌ها/خروج برندها؛ نقش شرکای جدید (چین، ترکیه، ایران، EAEU)؛ مقایسه با موضوعات مشابه]

## پرچم‌های کیفیت و ریسک
- `partial_data`: [وضعیت 2025]
- `mirror_bias`: [bias factor دوره هم‌پوشان FTS، اگر محاسبه شده در R2]
- `sanctions_exposed`: [تقاطع با فهرست‌ها — در صورت relevans]
- `concentrated`: [تمرکز بر یک شریک/تأمین‌کننده > ۷۰٪]

## یافته‌های کلیدی
- **یافته ۱**: [۳-۵ جمله]
- **یافته ۲**: [۳-۵ جمله]
- **یافته ۳**: [۳-۵ جمله]

## توصیه‌ها
- [۳-۵ جمله توصیه عملی — با احتساب اصطکاک تحریمی و کانال پرداخت]

## مراجع
- [[R3-analyze-market]] · [[data-sources]] · [[conventions]]
- [[analysis/_MOC]] (MOC پوشه مربوط)
```
