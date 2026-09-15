---
folder: 03-Recipes
type: recipe
recipe_id: recipe-09
title: طبقه‌بندی روند و رتبه‌بندی کاندیدها (port از مرجع — تطبیق روسیه)
related_tasks: [R3]
created: 2026-09-15
last_updated: 1405-06-24
status: draft
priority: critical
---

# 📖 Recipe-09 — طبقه‌بندی روند و رتبه‌بندی کاندیدها (Port پیش‌نویس)

> **نقش**: Analyst · **تسک مرتبط**: [[R3-analyze-market]]
> **منبع**: port مستقیم از `recipe-09` پروژه مرجع + تطبیق روسیه. این نسخه draft است؛ پس از مصوبه آستانه‌ها در R1، به `done` می‌رود.

## ۱. معماری pipeline

```
processed/mirror-russia-imports-2021-2025.parquet  (+ official IRICA)
        ↓
[R3-مرحله۱] trend-analysis.parquet (تمام جفت‌ها + شاخص‌ها)
        ↓
[R3-مرحله۲] trend-classification.parquet (+ تجمیع به فصل)
        ↓
[R3-مرحله۳] market-candidates-ranked.parquet (Top N با نمره ۶ وزنی)
```

## ۲. شاخص‌های محاسبه‌شده (هر جفت: کالا × جریان)

| شاخص | فرمول | دقت |
|------|-------|-----|
| `value_2021 … value_2025_ytd` | sum سالانه (میلیون USD) | Decimal |
| `value_2025_annualized` | `ytd × 12 / months_available` | Decimal |
| `cagr` | `(v_end / v_start)^(1/N) − 1` (سال کامل) | Decimal |
| `pct_change` / `growth_multiplier` | تغییر کل / ضریب | Decimal |
| `slope`, `r_squared` | OLS روی نقاط سالانه | float→Decimal |
| `mk_p_value` | Mann-Kendall با tie correction | float→Decimal |
| `cv` | `std / mean` | float→Decimal |
| `trend_consistency` | سال‌های متوالی رشد مثبت | int |
| `mean_recent_3y` | میانگین ۳ سال اخیر کامل | Decimal |

## ۳. Mann-Kendall (میراث مرجع — برای سری ۵ نقطه‌ای)

الگوریتم کامل با tie correction در recipe-09 مرجع موجود است؛ تفسیر: `p<0.05` معنادار، `p<0.10` متوسط، `p≥0.10` بدون روند. پیاده‌سازی یا از `pymannkendall` یا کد مرجع — خروجی پس از محاسبه به Decimal.

## ۴. طبقه‌بندی — ترتیب اولویت (دقیقاً مثل مرجع)

1. `emerging`: value_start ≈ 0 و value_end > threshold (پیش‌فرض 100k USD — مصوبه R1)
2. `disappearing`: value_start > threshold و value_end < threshold/10
3. CAGR قابل محاسبه نیست → `insufficient_data`
4. `strong_growth`: CAGR > 10٪ و mk_p < 0.05 و slope > 0
5. `moderate_growth`: 0 < CAGR ≤ 10٪ و mk_p < 0.10
6. `declining`: CAGR < 0 و mk_p < 0.10
7. `volatile`: cv > 0.5 و r_squared < 0.3
8. `stable`: |CAGR| ≤ 2٪ و r_squared < 0.3
9. غیر آن: `weak_growth` / `weak_decline` / `stable`

## ۵. نمره‌دهی — تطبیق روسیه (تفاوت اصلی با مرجع)

```
market_score = w1*norm(size) + w2*norm(growth) + w3*norm(competition_gap)
             + w4*norm(access) + w5*norm(stability) − w6*norm(sanctions_friction)
```

- وزن‌ها مصوب Decision-004 (نقطه شروع مثل مرجع: 0.30/0.20/0.20/0.10/0.10/0.10؛ قید Σw=1؛ نرمال‌سازی min-max کل دیتاست).
- `sanctions_friction`: امتیاز ریسک تحریمی هر کالا/جریان (همپوشانی با فهرست‌های OFAC/EU، پیچیدگی پرداخت، ریسک حمل) — متد ساخت در R1 مستند می‌شود.
- توصیه‌ها: `select` (>0.7) / `monitor` (0.4–0.7) / `investigate` (<0.4).
- پرچم‌های ریسک: `volatile` (cv>0.7)، `concentrated` (سهم بزرگ‌ترین شریک>70٪)، `declining_recent`، `partial_data`، `sanctions_exposed`.

## ۶. مدیریت داده sparse (میراث مرجع)

NaN/صفر → Decimal(0)؛ همه سال‌ها صفر → حذف از خروجی؛ سال پایانی partial → annualized؛ شکاف وسط سری → `insufficient_data`.

## ۷. تست‌های الزامی (گیت QA در R5)

1. Sum consistency با Parquet ورودی < 0.0001٪.
2. پوشش کامل جفت‌ها در classification؛ بدون NULL در `trend_category`.
3. `market_score ∈ [0,1]`؛ rank یکتا بدون شکاف.
4. شکست هر تست → `issues.md` + برگشت به مرحله مربوطه R3.

## مراجع

- [[conventions]] بخش ۵-۶ · [[R3-analyze-market]] · [[lessons]]
- مرجع: `Market-Research/03-Recipes/recipe-09-trend-classification.md`
