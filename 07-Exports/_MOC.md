---
folder: 07-Exports
type: moc
title: MOC خروجی‌ها — برنامه ورک‌بوک‌های Excel
created: 2026-09-15
last_updated: 1405-06-24
status: review
tags: [MOC, excel, exports, scope-v2]
related: ["[[mental-model]]", "[[conventions]]"]
---

# 📤 MOC خروجی‌ها — برنامه ۵ ورک‌بوک Excel (Scope v2)

> طبق Decision-004، خروجی‌های عددی پروژه در **۵ ورک‌بوک Excel** تحویل می‌شود (درخواست کارفرما). فایل‌ها در همین پوشه ساخته می‌شوند و هر یک با یادداشت‌های مرتبط در Vault لینک می‌شود. نام‌گذاری: `NN-slug-YYYYMMDD.xlsx` (قرارداد kebab-case + snapshot تاریخ). همه اعداد: Decimal، حداکثر ۴ رقم اعشار، منبع‌دار.

## فهرست ورک‌بوک‌ها (پیش‌نویس — نهایی‌سازی شیت‌ها در R1)

### `01-raw-consolidated.xlsx` — داده پایه یکپارچه (خروجی R1)
| شیت | محتوا | منبع |
|-----|-------|------|
| `README` | راهنما، تاریخ snapshot، قراردادها | — |
| `mirror_imports` | واردات روسیه HS6 از همه شرکا (2021–2025 + YTD-2026) با `est_flag` | BAC/CEPII (+ Comtrade) |
| `iran_exports_ru` | صادرات رسمی ایران به روسیه (۱۴۰۰–۱۴۰۴ میلادی‌شده) | IRICA |
| `cbr_rates` | RUB/USD میانگین سالانه | CBR |
| `countries` | iso3, m49, iso2, name_fa, name_en | — |
| `qa_flags` | پرچم کیفیت هر رکورد | — |

### `02-demand-russia.xlsx` — تقاضای روسیه (خروجی R3)
| شیت | محتوا |
|-----|-------|
| `trend_metrics` | شاخص‌های روند همه جفت‌ها (CAGR، MK، OLS، CV، …) |
| `classification_73` | طبقه‌بندی ۷+۳ به تفکیک HS6 |
| `war_opportunity` | کالاهای دارای شکاف عرضه پس از ۲۰۲۲ + سهم شرکای غیردوست قبل/بعد |
| `top300_demand` | فهرست کوتاه تقاضا |

### `03-iran-capacity-competition.xlsx` — ظرفیت ایران و رقابت (خروجی R3)
| شیت | محتوا |
|-----|-------|
| `iran_capacity` | ماتریس ظرفیت صادراتی ایران (تجارتی/تکنیکال، پرچم انباشت) |
| `competitor_shares` | سهم CHN/TUR/IND/BLR به تفکیک HS6 + روند سهم |
| `market_score` | امتیاز ۶ وزنی + توصیه select/monitor/investigate |
| `top100_candidates` | رتبه‌بندی نهایی (یادداشت کامل Top 50 در Vault) |

### `04-access-matrix.xlsx` — ماتریس دسترسی به بازار (خروجی R4)
| شیت | محتوا |
|-----|-------|
| `channels` | لایه‌های ورود: عمده/ریتیل زنجیره‌ای/مارکت‌پلیس/مستقیم — الزامات و بازیگران |
| `marketplaces` | WB/Ozon/Yandex Market/Мегамаркет: کمیسیون، FBO/FBS، شرایط فروشنده غیرروس |
| `certification` | EAC/GOST/SGR/Chestny Znak/دامپزشکی به تفکیک HS6 |
| `payments` | کانال‌های تسویه، کارمزد، زمان، ریسک |
| `logistics` | مسیرها (خزر/ریل/جاده)، هزینه و زمان به تفکیک نوع کالا |

### `05-margin-roadmap.xlsx` — حاشیه سود و نقشه راه (خروجی R5)
| شیت | محتوا |
|-----|-------|
| `landed_cost` | ماشین‌حساب پارامتری: FOB تا قیمت مقصد به تفکیک مسیر/کانال |
| `margin_results` | باندهای حاشیه سود خالص کاندیدهای منتخب (با `est_flag`) |
| `roadmap_12m` | نقشه راه ورود ۱۰–۲۰ کالای منتخب: کانال، شریک، سرمایه، تقویم، ریسک |
| `assumptions` | فرضیات و ضریب‌های به‌کاررفته (قابل تغییر توسط کارفرما) |

## اتصال به Vault

- هر ورک‌بوک پس از تولید: یادداشت `type: excel-output` در همین پوشه + backlink از [[dashboard]] و یادداشت‌های تحلیلی `06-Analysis/`.
- اعداد کلیدی هر ورک‌بوک در یادداشت تحلیلی خودش ارجاع می‌شوند (قرارداد ۸ conventions: هر یادداشت تحلیلی backlink به تسک و منبع).

## مراجع

[[mental-model]] (بخش ۷) · [[conventions]] (بخش ۴) · `04-State/decisions.md` (Decision-004)
