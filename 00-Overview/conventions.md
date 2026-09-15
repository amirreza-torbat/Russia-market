---
folder: 00-Overview
type: convention
created: 2026-09-15
last_updated: 1405-06-24
status: draft
---

# 📐 قراردادها و استانداردها (Conventions)

این سند **منبع حقیقت** قراردادهای Vault است (الگوی [[Market-Research]] با تطبیق روسیه). هر agent **باید** قبل از ایجاد هر فایلی این سند را رعایت کند. موارد `TBD در R1` پس از تأیید موضوع توسط کاربر نهایی می‌شوند.

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
- **همه کلیدهای سال در CSV/Parquet میلادی هستند** (2021–2025) — منابع بین‌المللی میلادی‌اند و هر تبدیل = ریسک خطا.
- سال پایانی (2025) ممکن است partial باشد؛ روش‌های YTD / annualized (`value * 12 / months_available`) مطابق مرجع، با ثبت انتخاب در `decisions.md`.
- نگاشت شمسی ۱۴۰۰–۱۴۰۴ فقط در گزارش‌های فارسی ذکر می‌شود، هرگز در کلید داده.

### ۴.۲ کدهای کشور
- استاندارد اصلی: **ISO 3166-1 alpha-3** (`IRN`, `RUS`) — سازگار با BAC/CEPII.
- Comtrade/M49: ایران = `364`، روسیه = `643` — در فیلد جداگانه نگهداری شود.
- جدول مرجع: `05-Data/processed/countries.csv` (ساخته‌شده در R1) با ستون‌های `iso3, m49, iso2, name_fa, name_en`.

### ۴.۳ واحد پول و ارقام
- داده تجاری: **USD (native از منبع)** — تبدیل نکن.
- داده روبلی: تبدیل به USD فقط با **نرخ میانگین سالانه رسمی CBR**؛ نرخ‌ها در `05-Data/processed/cbr-rates-annual.csv` ذخیره و در گزارش‌ها نرخ هم ذکر می‌شود.
- داده Rosstat: در **واحد فیزیکی native** (kg, unit, m³) بماند؛ دلاری‌سازی فقط برای مقایسه بین‌المللی و با نرخ CBR.
- **دقت**: همه محاسبات با `decimal.Decimal` (نه float)؛ خروجی scipy/stats در صورت نیاز فقط پس از محاسبه به Decimal برگردد. تلورانس کل QA: **< 0.0001٪** (`|calc − ref| / ref < 0.000001`). اعشار گزارش: حداکثر ۴ رقم.

### ۴.۴ کد محصول
- استاندارد اصلی: **HS6 / ТН ВЭД ۶ رقمی** به‌صورت string (پیش‌صفرها حفظ شود) — `TBD در R1` (در صورت انتخاب تحلیل کلان: ۲۱ بخش HS یا ۹۶+ فصل).
- همیشه ستون‌های `hs6`, `hs4`, `hs2` (فصل) کنار هم نگه داشته شود.

### ۴.۵ داده آینه‌ای (Mirror Data) — تطبیق کلیدی روسیه
- روسیه از آوریل ۲۰۲۲ آمار گمرکی تفصیلی منتشر نمی‌کند (طبقه‌بندی طبق مصوبه دولتی مارس ۲۰۲۲ — شماره دقیق مصوبه در R1 راستی‌آزمایی می‌شود). بنابراین:
  1. **دوره 2021 تا Q1-2022**: گزارش رسمی FTS/Rosstat در دسترس است.
  2. **پس از Q2-2022**: واردات روسیه ≈ مجموع صادرات گزارش‌شده شرکا به روسیه (mirror) از BAC/Comtrade.
- **تنظیم CIF→FOB**: mirror (واردات شرکا از دید روسیه) CIF است؛ `FOB = CIF × (1 − κ)` با `κ ≈ 4–5%` (بازه عدم قطعیت 3–6%) — حساسیت‌سنجی در R2. مقدار نهایی κ در `decisions.md` ثبت می‌شود.
- **اعتبارسنجی متقابل**: در دوره هم‌پوشان (2021–Q1-2022) mirror را با داده رسمی FTS مقایسه و bias factor محاسبه کن (گیت QA در R2).

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
- آستانه‌های اولیه (مثل مرجع): `threshold_emerging_disappearing = 100,000 USD`، `cagr_strong = 10٪`، `cagr_stable = 2٪`، `cv_volatile = 0.5`، `r_squared_clear = 0.3` — نهایی در R1 با توجه به مقیاس بازار روسیه.

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
- مقادیر وزن‌ها `TBD در R1` (نقطه شروع پیشنهادی مثل مرجع: 0.30/0.20/0.20/0.10/0.10/0.10) و پس از مصوبه در `decisions.md` ثبت می‌شود.
- توصیه‌ها: `select` (>0.7)، `monitor` (0.4–0.7)، `investigate` (<0.4) + پرچم‌های ریسک (`volatile`, `concentrated`, `declining_recent`, `partial_data`, `sanctions_exposed`).

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
