---
folder: 00-Overview
type: convention
created: 2026-09-15
last_updated: 1405-06-25
status: done
---

# 📐 قراردادها و استانداردها (Conventions)

این سند **منبع حقیقت** قراردادهای Vault است (الگوی [[Market-Research]] با تطبیق روسیه). همه موارد `TBD در R1` در جریان اجرای R1 (۱۴۰۵-۰۶-۲۵) مصوب و ثبت شدند (Decision-005) — این سند اکنون نهایی است.

---

## ۱. زبان و فونت

- **زبان اصلی**: فارسی برای توضیحات و تحلیل‌ها؛ اصطلاحات فنی انگلیسی (`HS Code`, `mirror data`, `schema`).
- **نام فیلدهای داده**: انگلیسی و `snake_case` (مثل `export_value_usd`, `partner_iso3`).
- **اعداد**: ارقام فارسی در متن فارسی؛ ارقام لاتین در داده ساختاریافته.
- **تاریخ**: در نام فایل `YYYY-MM-DD` میلادی؛ در متن فارسی می‌توان پسوند شمسی افزود مثل `2025-12-31 (1404-10-10)`.

## ۲. نام‌گذاری فایل‌ها

| نوع | فرمت | مثال |
|-----|------|------|
| یادداشت عمومی | `kebab-case` | `russia-imports-overview.md` |
| تسک | `R#-task-slug.md` | `R1-initial-scan.md` |
| پرامپت | `prompt-role-name.md` | `prompt-analyst.md` |
| دستورالعمل | `recipe-NN-short-slug.md` | `recipe-09-trend-classification.md` |
| داده خام | `raw/<source>/<dataset>__<params>__YYYYMMDD.csv` | `raw/bac/bac__mirror_643__h6__2021-2025__20260915.csv` |
| داده پردازش‌شده | `processed/<name>.parquet` | `processed/mirror-russia-imports-2021-2025.parquet` |

- نام پوشه/فایل فقط ASCII، بدون فاصله و بدون حروف اکسن‌دار (مثل `Synthese` نه `Synthèse`).

## ۳. ساختار یادداشت‌های Obsidian

هر یادداشت این frontmatter را دارد:

```yaml
---
folder: 00-Overview
type: analysis|task|recipe|prompt|state|overview|data|glossary|convention
title: عنوان فارسی
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft|in-progress|review|done|blocked
tags: []
related: ["[[R1-initial-scan]]"]
---
```

## ۴. قراردادهای داده

### ۴.۱ تقویم و بازه زمانی
- **همه کلیدهای سال در CSV/Parquet میلادی هستند** (2021–2025 + YTD-2026) — منابع بین‌المللی میلادی‌اند و هر تبدیل = ریسک خطا.
- **پوشش واقعی منابع (راستی‌آزمایی‌شده R1)**: BACI V202601 فقط تا **2024** دارد → 2025 و YTD-2026 (تا ماه ۹) از IRICA (سمت ایران) و انتشارهای ماهانه/فصلی شرکا با پرچم `partial_year` + annualization (`value × 12 / months_available`) — مصوب Decision-005.
- نگاشت شمسی ۱۴۰۰–۱۴۰۴ فقط در گزارش‌های فارسی ذکر می‌شود، هرگز در کلید داده.

### ۴.۲ کدهای کشور
- استاندارد اصلی: **ISO 3166-1 alpha-3** (`IRN`, `RUS`) — سازگار با BAC/CEPII.
- Comtrade/M49: ایران = `364`، روسیه = `643` — در فیلد جداگانه نگهداری شود.
- جدول مرجع: `05-Data/processed/countries.csv` (ساخته‌شده در R1 ✅ — ۲۳۸ ردیف از `country_codes_V202601.csv`) با ستون‌های `iso3, m49, iso2, name_en, name_fa, role` (ستون `role`: `core`/`comparator`/`other` — افزوده Scope v2). کدهای خاص BAC (مثل `S19` = Areas nes) با همان کد در ستون m49 نگهداری و در R2 مدیریت می‌شوند.

### ۴.۳ واحد پول و ارقام
- داده تجاری: **USD (native از منبع)** — تبدیل نکن.
- داده روبلی: تبدیل به USD فقط با **نرخ میانگین سالانه رسمی CBR**؛ نرخ‌ها در `05-Data/processed/cbr-rates-annual.csv` ذخیره و در گزارش‌ها نرخ هم ذکر می‌شود.
- داده Rosstat: در **واحد فیزیکی native** (kg, unit, m³) بماند؛ دلاری‌سازی فقط برای مقایسه بین‌المللی و با نرخ CBR.
- **دقت**: همه محاسبات با `decimal.Decimal` (نه float)؛ خروجی scipy/stats در صورت نیاز فقط پس از محاسبه به Decimal برگردد. تلورانس کل QA: **< 0.0001٪** (`|calc − ref| / ref < 0.000001`). اعشار گزارش: حداکثر ۴ رقم.

### ۴.۴ کد محصول
- استاندارد اصلی: **HS6 / ТН ВЭД ۶ رقمی** به‌صورت string (پیش‌صفرها حفظ شود) — **مصوب R1** (Decision-003 بند ۲). تحلیل کلان فقط به‌عنوان *نمایش تجمیعی* در سطح فصل (hs2؛ ۹۷ فصل / ۲۱ بخش) ارائه می‌شود و دانه‌بندی تحلیل جداگانه نیست.
- همیشه ستون‌های `hs6`, `hs4`, `hs2` (فصل) کنار هم نگه داشته شود.
- فهرست مرجع کدها: `05-Data/processed/hs6-codes.csv` (۵٬۰۲۲ کد HS92 از BACI V202601 — ✅ R1).

### ۴.۵ داده آینه‌ای (Mirror Data) — تطبیق کلیدی روسیه
- روسیه از آوریل ۲۰۲۲ آمار گمرکی تفصیلی منتشر نمی‌کند (**راستی‌آزمایی‌شده R1**: مصوبه **Постановление Правительства РФ от 09.03.2022 № 312** — اصلاح ماده ۲۷۸ قانون ۲۸۹-ФЗ؛ از مارس ۲۰۲۳ فقط جمع‌های کلان صادرات/واردات دوباره منتشر می‌شود). بنابراین:
  1. **دوره 2021 تا Q1-2022**: گزارش رسمی FTS/Rosstat در دسترس است.
  2. **پس از Q2-2022**: واردات روسیه ≈ مجموع صادرات گزارش‌شده شرکا به روسیه (mirror) از BAC/Comtrade.
  3. **کالیبراسیون سالانه (افزوده R1 — Issue-006)**: پوشش mirror پس از ۲۰۲۲ افت می‌کند (2024: ≈۷۱٪ واردات رسمی برآوردی) → مجموع سالانه mirror با جمع‌های کلان رسمی FTS (منتشرشده از 2023-03) به‌صورت **ضریب کالیبراسیون به تفکیک سال** مقیاس می‌شود؛ ترکیب HS6 دست‌نخورده می‌ماند.
- **تنظیم CIF→FOB**: mirror (واردات شرکا از دید روسیه) CIF است؛ `FOB = CIF × (1 − κ)` با **κ = 4.5٪** (نقطه مرکزی مصوب R1 — Decision-005؛ بازه عدم قطعیت 3–6%) — حساسیت‌سنجی در R2.
- **اعتبارسنجی متقابل**: در دوره هم‌پوشان (2021–Q1-2022) mirror را با داده رسمی FTS مقایسه و bias factor محاسبه کن (گیت QA در R2). **لنگر R1**: mirror 2021 = 284.59 میلیارد دلار CIF ≈ ۰٫۹۶۱× واردات رسمی 2021 (≈296.1 میلیارد = 789.4 چرخش − 493.3 صادرات)؛ چین 2021: mirror 73.17 در برابر رسمی 72.0 (CIF) → +1.6٪.

## ۵. تاکسونومی روند (میراث مرجع — ۷ دسته اصلی + ۳ فرعی)

| دسته | کد | معیار |
|------|----|-------|
| رشد قوی | `strong_growth` | CAGR > 10٪، Mann-Kendall p < 0.05، slope > 0 |
| رشد متوسط | `moderate_growth` | 0 < CAGR ≤ 10٪، MK p < 0.10 |
| پایدار | `stable` | \|CAGR\| ≤ 2٪، R² < 0.3 |
| نوسانی | `volatile` | CV > 0.5، R² < 0.3 |
| کاهشی | `declining` | CAGR < 0، MK p < 0.10 |
| نوظهور | `emerging` | value_start ≈ 0، value_end > threshold |
| محوشده | `disappearing` | value_start > threshold، value_end ≈ 0 |
| (فرعی) | `weak_growth` / `weak_decline` / `insufficient_data` | بدون معناداری / داده ناکافی |

- ترتیب اعمال اولویت‌ها و آستانه‌ها دقیقاً مطابق `03-Recipes/` (port از recipe-09 مرجع).
- آستانه‌های **مصوب R1** (تنظیم برای مقیاس بازار روسیه — Decision-005): `threshold_emerging_disappearing = 500,000 USD`، `cagr_strong = 10٪`، `cagr_stable = 2٪`، `cv_volatile = 0.5`، `r_squared_clear = 0.3`.

### شاخص‌های هر جفت (کالا × جریان)
`cagr`, `pct_change`, `growth_multiplier`, `slope (OLS)`, `r_squared`, `mk_p_value`, `cv`, `trend_consistency`, `mean_value`, `mean_recent_3y`, `value_end_ytd`, `value_end_annualized` — فرمول‌ها مطابق recipe-09 مرجع.

## ۶. نمره‌دهی ترکیبی (فرمول ۶ وزنی — تطبیق روسیه)

ساختار میراث مرجع حفظ می‌شود؛ وزن ششم برای بازار روسیه به **ضریب اصطکاک تحریمی** بازتعریف شده است:

```
market_score = w1 * norm(size)          # اندازه بازار (mirror imports یا مصرف)
             + w2 * norm(growth)        # CAGR / slope روند واردات
             + w3 * norm(competition)   # شدت رقابت (یا شکاف عرضه — برعکس)
             + w4 * norm(access)        # دسترسی تعرفه‌ای (FTA ایران-اوراسیا) و لجستیک
             + w5 * norm(stability)     # ثبات روند (trend_consistency)
             - w6 * norm(sanctions_friction)  # ضریب اصطکاک تحریمی (پرداخت، حمل، ریسک انطباق)
```

- قید: `Σw = 1`، نرمال‌سازی min-max روی کل دیتاست، `market_score ∈ [0,1]`.
- وزن‌های **مصوب** (Decision-003 بند ۵ + Decision-005): `w1=0.30 (size)، w2=0.20 (growth)، w3=0.20 (competition)، w4=0.10 (access)، w5=0.10 (stability)، w6=0.10 (sanctions_friction)`.
- **قاعده حاشیه سود (افزوده Scope v2 — مصوب پیش‌فرض R1، Decision-005)**: فیلتر سخت اعمال نمی‌شود؛ برای هر کاندید باندهای حاشیه (M6) گزارش و حاشیه خالص برآوردی < 10٪ با پرچم هشدار `low_margin` درج می‌شود — کارفرما می‌تواند آستانه عددی متفاوت مصوب کند.
- توصیه‌ها: `select` (>0.7)، `monitor` (0.4–0.7)، `investigate` (<0.4) + پرچم‌های ریسک: `volatile`, `concentrated`, `declining_recent`, `partial_data`, `sanctions_exposed` + **پرچم‌های جدید Scope v2 (Decision-004)**: `war_opportunity` (شکاف عرضه پس از ۲۰۲۲)، `unfriendly_surcharge_advantage` (مزیت تعرفه‌ای ایران مقابل کشورهای «غیردوست» — مصوبه ۲۱٫۱۰٫۲۰۲۳ № 1721)، `import_dependence` (وابستگی ساختاری به واردات)، `ir_coverage_gap` (شکاف پوشش BACI سمت ایران — Issue-007).

## ۷. قراردادهای Git

- پیام commit: `type(scope): subject` — types: `feat, fix, docs, refactor, data, analysis, chore`.
- شاخه‌ها: `main` پایدار؛ `feature/R#-slug` برای اجرا؛ push مستقیم فقط برای فایل‌های State.
- **امنیت**: هیچ توکن/محرمانه‌ای در فایل‌ها؛ `.env` و `*.local.md` در `.gitignore`؛ داده‌های بزرگ raw هرگز commit نمی‌شوند (دانلود تکرارپذیر با `scripts/`).

## ۸. قراردادهای Vault و State

- هر پوشه `_MOC.md` دارد (به‌جز 00-Overview که README ریشه نقشه است — الگوی مرجع).
- هر یادداشت تحلیلی حداقل یک backlink به تسک و یک backlink به منبع داده دارد.
- state چهارگانه در `04-State/`: `STATUS.md` (نقطه شروع هر agent)، `progress.md`، `issues.md`، `decisions.md` — فقط اضافه‌کردن، هرگز حذف نکردن سطر.
- یادداشت `draft` در گزارش نهایی قابل استناد نیست؛ فقط `done`.

## ۹. مدیریت خطا

- هر خطای داده/محاسبه → ثبت در `issues.md`؛ blocker داده‌ای → تسک مربوطه `blocked` و درج در `STATUS.md`.
- اگر تلورانس < 0.0001٪ حاصل نشد → کار متوقف، ریشه‌یابی در `issues.md`، وضعیت پروژه `blocked`.

## مراجع

- [[project-overview]] · [[data-sources]] · [[glossary]] · [[lessons]]
- [/03-Recipes/_MOC](../03-Recipes/_MOC.md) · [/04-State/decisions](../04-State/decisions.md)
