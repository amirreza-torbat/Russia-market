---
folder: 01-Tasks
type: moc
created: 2026-09-15
last_updated: 1405-06-24
status: draft
---

# 🗺️ MOC تسک‌ها (Tasks Map of Content)

> ⚠️ **این تسک‌ها placeholder هستند (status: draft)** — پس از پاسخ کاربر به سؤالات bootstrap، در `R1` با موضوع مصوب نهایی/بازطراحی می‌شوند و در `04-State/decisions.md` ثبت خواهند شد. قرارداد شناسه: `R#-task-slug.md`؛ انواع: `scan / validate / analyze / compile / review`.
>
> 🆕 **نگاشت Scope v2 (Decision-004 — [[mental-model]] بخش ۸)**: `R1` = آماده‌سازی همه ماژول‌ها + داده پایه · `R2` = M1/M2 (اعتبارسنجی + YTD-2026) · `R3` = M1/M2/M3/M7 (تقاضا + ظرفیت ایران + رقابت + امتیاز) · `R4` = M4/M5 (ماتریس دسترسی) + تدوین · `R5` = M6/M8 (حاشیه سود + نقشه راه) + QA/closure. خروجی‌های Excel: [/07-Exports/_MOC](../07-Exports/_MOC.md).

## نمودار وابستگی (پیش‌نویس)

```
[bootstrap: این کامیت] ✅
        ↓
[R1: initial-scan — نهایی‌سازی conventions + دانلود داده پایه] ⬜
        ↓
[R2: validate-data — mirror/official reconciliation + CIF→FOB] ⬜
        ↓
[R3: analyze-market — روند + طبقه‌بندی ۷+۳ + رتبه‌بندی ۶ وزنی] ⬜
        ↓
[R4: compile-report — یادداشت‌های Obsidian + 06-Analysis + 07-Exports] ⬜
        ↓
[R5: review-publish — QA نهایی + closure + release] ⬜
```

## فهرست تسک‌ها

| Task ID | عنوان | نوع | وضعیت | فایل | وابسته به |
|---------|-------|-----|-------|------|-----------|
| `R1` | اسکن اولیه: نهایی‌سازی قراردادها + دانلود داده پایه | scan | ⬜ draft | [R1-initial-scan.md](R1-initial-scan.md) | bootstrap |
| `R2` | اعتبارسنجی داده و reconciliation آینه‌ای | validate | ⬜ draft | [R2-validate-data.md](R2-validate-data.md) | R1 |
| `R3` | تحلیل روند، طبقه‌بندی و رتبه‌بندی | analyze | ⬜ draft | [R3-analyze-market.md](R3-analyze-market.md) | R2 |
| `R4` | تدوین گزارش‌ها و خروجی‌ها | compile | ⬜ draft | [R4-compile-report.md](R4-compile-report.md) | R3 |
| `R5` | بازبینی نهایی، QA و انتشار | review | ⬜ draft | [R5-review-publish.md](R5-review-publish.md) | R4 |

**راهنمای وضعیت**: `draft` → `pending` → `in-progress` → `review` → `done` | `blocked`

## توالی اجرا

پنج تسک بالا **سری** اجرا می‌شوند (هر یک به قبلی وابسته است). در R1، بسته به موضوع مصوب ممکن است تسک‌های موازی (مثل تحلیل به تفکیک کشور و به تفکیک کالا) از الگوی task-04/task-05 مرجع اضافه شوند.

## چگونه یک تسک را شروع/تمام کنیم؟ (الگوی مرجع)

1. فایل تسک را باز کن؛ بخش «معیار پذیرش» را بخوان.
2. `04-State/STATUS.md` را به‌روز کن (in-progress + نام agent)؛ شاخه `feature/R#-slug` بساز.
3. هر مایل‌ستون را در `04-State/progress.md` ثبت کن.
4. پایان: معیارهای پذیرش ✓، سطر final در progress، وضعیت در همین MOC و STATUS به `done`، سپس merge به `main`.

## مراجع

- [/00-Overview/conventions](../00-Overview/conventions.md) · [/00-Overview/lessons](../00-Overview/lessons.md)
- [/03-Recipes/_MOC](../03-Recipes/_MOC.md) · [/04-State/STATUS](../04-State/STATUS.md)
