# Russia-market — تحلیل بازار روسیه (Bootstrap)

> **مخزن Obsidian Vault** برای پروژه تحقیقاتی «بازار روسیه». این مخزن با الگوبرداری کامل از پروژه مرجع [`Market-Research`](https://github.com/amirreza-torbat/Market-Research) (تحلیل صادرات ایران) ساخته شده است.
>
> ✅ **وضعیت فعلی: R1-DONE → READY-FOR-R2** (۱۴۰۵-۰۶-۲۵) — قراردادها نهایی شد (Decision-005: HS6، وزن‌ها 0.30/0.20/0.20/0.10/0.10/0.10، آستانه‌ها، κ=4.5٪، BACI V202601 لنگر، کالیبراسیون سالانه mirror، IRICA محوری برای سمت ایران). **داده پایه دانلود و فیلتر شد**: واردات آینه‌ای روسیه 2021–2024 (284.6G→201.8G$)، صادرات ایران، نرخ‌های CBR (۱٬۳۲۴ روز)، `countries.csv` (۲۳۸ کشور)، `hs6-codes.csv` (۵٬۰۲۲ کد)، ورک‌بوک [`07-Exports/01-raw-consolidated.xlsx`](07-Exports/01-raw-consolidated.xlsx). راستی‌آزمایی‌های حقوقی ثبت شد: FTS №312، FTA ایران–اوراسیا لازم‌الاجرا ۲۰۲۵-۰۵-۱۵، واردات موازی №506/№1532/№2701/№135، surcharge №1721. گام بعدی: `R2` (ETL + reconciliation + کالیبراسیون + IRICA).

---

## 🗺️ نقشه سریع Vault

| پوشه | محتوا | مخاطب |
|------|-------|-------|
| [`00-Overview/`](00-Overview/) | معرفی، قراردادها، منابع داده، واژه‌نامه، درس‌آموخته‌های مرجع | همه |
| [`01-Tasks/`](01-Tasks/) | تسک‌های placeholder با Task ID (`R#-task-slug`) و وابستگی‌ها | مدیر + Agentهای اجرایی |
| [`02-Prompts/`](02-Prompts/) | پرامپت‌های نقش‌محور agent (اسکلت) | فراخوانی agent |
| [`03-Recipes/`](03-Recipes/) | دستورالعمل‌های گام‌به‌گام (SOP) | همه agentها |
| [`04-State/`](04-State/) | STATUS، progress، issues، decisions، closure، QA | همه |
| [`05-Data/`](05-Data/) | داده خام / interim / processed (raw در .gitignore) | Data/Analyst |
| [`_templates/`](_templates/) | قالب تسک و یادداشت | همه |
| [`07-Exports/`](07-Exports/) | برنامه و خروجی ۵ ورک‌بوک Excel (Scope v2) | همه |
| `project-flow.canvas` (ریشه) | نقشه گرافیکی پروژه (Canvas داخلی Obsidian) | همه |
| [`scripts/`](scripts/) | اسکریپت‌های پایتون تکرارپذیر | Data/Analyst |

پوشه `06-Analysis/` در زمان اجرا (R3) ساخته می‌شود؛ `07-Exports/` برای برنامه ۵ ورک‌بوک Excel (Scope v2 — Decision-004) هم‌اکنون موجود است.

---

## 🎯 هدف پروژه (نهایی‌شدنی در R1)

1. تحلیل جنبه‌ای از **بازار روسیه** که کاربر در مرحله bootstrap انتخاب می‌کند (کاندیدهای پیشنهادی: جستجوی فرصت صادرات ایران→روسیه، خلأهای وارداتی پس از ۲۰۲۲، ورود شرکت‌های ایرانی، مطالعه کلان).
2. اعمال کامل متدولوژی پروژه مرجع: حلقه کامل تحلیل روند، طبقه‌بندی ۷+۳ دسته‌ای، رتبه‌بندی با نمره ترکیبی ۶ وزنی.
3. تطبیق با واقعیت داده‌ای روسیه: **توقف انتشار آمار گمرکی از آوریل ۲۰۲۲** → راهبرد داده آینه‌ای (mirror data) + منابع ایرانی + منابع ثانویه روسی.
4. دقت عددی: خطای کل **کمتر از 0.0001٪** با `decimal.Decimal` (میراث مرجع).

---

## ⚙️ گردش کار پیشنهادی (placeholder — پس از تأیید موضوع در R1 بازطراحی می‌شود)

```
Bootstrap(این کامیت) → R1: scan + نهایی‌سازی conventions
  → R2: validate داده (mirror/official، CIF→FOB)
  → R3: analyze (روند + طبقه‌بندی + رتبه‌بندی)
  → R4: compile (گزارش‌ها + خروجی‌ها)
  → R5: review + publish (QA نهایی + closure + release)
```

---

## 🤝 قراردادهای همکاری agentها (میراث مرجع)

1. هر agent قبل از شروع باید `04-State/STATUS.md` و `00-Overview/conventions.md` را بخواند.
2. هر agent بعد از پایان، یک سطر به `04-State/progress.md` اضافه و در صورت نیاز `STATUS.md` را به‌روز کند.
3. هیچ agentی فایل خارج از ساختار تعریف‌شده نسازد.
4. نام‌گذاری: `kebab-case`؛ تسک‌ها با فرمت `R#-task-slug.md`.
5. زبان: فارسی برای توضیحات، انگلیسی برای اصطلاحات فنی و نام فیلدها.
6. محاسبات فقط با `decimal.Decimal` — خطای نهایی < 0.0001٪.

---

## 🚀 شروع سریع

```bash
git clone https://github.com/amirreza-torbat/Russia-market.git
cd Russia-market
cat 04-State/STATUS.md          # کجای مسیر هستیم؟
cat 00-Overview/conventions.md  # قراردادها
cat 01-Tasks/_MOC.md            # تسک بعدی
```

---

## 🔐 نکته امنیتی

- توکن GitHub **هرگز** در فایل‌ها commit نمی‌شود (`.env` و `*.local.md` در `.gitignore`).
- در کامیت bootstrap توکن در هیچ فایلی قرار نگرفته است؛ پس از اتمام کار، کاربر باید توکن صادرشده برای این مأموریت را revoke کند.
- [`04-State/issues.md`](04-State/issues.md) — Issue-001 این ریسک را مستند می‌کند.

---

## 📞 مالکیت

- مالک مخزن: [@amirreza-torbat](https://github.com/amirreza-torbat)
- تاریخ bootstrap: ۲۰۲۶-۰۹-۱۵ (۱۴۰۵-۰۶-۲۴)
- الگوی ساختار: [`Market-Research`](https://github.com/amirreza-torbat/Market-Research)
