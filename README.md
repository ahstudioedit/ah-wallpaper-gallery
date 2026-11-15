# AH Wallpaper Gallery

تصاميم تفاعلية لبرنامج AH Wallpaper. يقرأ البرنامج `index.json` من هذا المستودع ويعرض التصاميم في تبويبة «اكتشف».

## إضافة تصميم
1. أنشئ مجلدًا داخل `designs/` باسم قصير بالإنجليزية بلا مسافات، مثل `neon-city`.
2. ضع فيه:
   - `design.ahwp` — من زر «مشاركة» في البرنامج.
   - `thumb.jpg` — صورة 640×360 تقريبًا، أقل من 150KB.
   - `meta.json` — انسخه من `designs/example/` وعدّل الاسم والمصمم.
3. شغّل `python tools/make_index.py`.
4. ارفع التعديلات (commit + push).

## الحدود
- حجم `design.ahwp` حتى 20MB. التصاميم الأكبر تُرفع في GitHub Releases.
- راجع كل تصميم قبل إضافته.
