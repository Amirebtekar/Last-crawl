# last crawl checker

با این ابزار میتونید آخرین زمان کرول شدن ادرس سایتتون رو برسی کنید. و بعد از اجرا ادرس هایی که بیشتر از 30 روز از اخرین کرول آنها گذشته رو پیدا کنید و برسیشون کنید.
همچنین میتونید روی سرور اجرا کنیدش و به صورت ماهانه این کار رو انجام بده و بعد از انجام کار با پیامک بهتون اطلاع بده که فایل مورد نظر رو چک کنید

## آماده سازی در 10 مرحله آسان

1. ابتدا اقدام به نصب پایتون کنید. برای این کار به [https://www.python.org/downloads/] مراجعه کنید.
2. در مرحله دوم فایل [https://github.com/Amirebtekar/Last-crawl/archive/refs/heads/main.zip] دانلود کنید
3. فایل بالا اکسترکت کنید و در پوشه یک ترمینال باز کنید.
4. دستور زیر را در ترمینال اجرا کنید `pip install -r requirements.txt`
5. در این مرحله باید service account بسازید. [آموزش ساخت service account](https://amirebtekar.ir/google-indexing-api/)
6. نام فایل در یافتی را به `service_account` تغییر بدید. و جایگزین فایل داخل پوشه کنید
7. فایل `app.py` را با استفاده از ادیتور باز کنید.
8. خط های 9,10,21,38,39,40 را کامل کنید
9. اگر پنل پیامک ندارید خط 21,38,39,40 تغییر ندین
10. فایل رو سیو کنید

## اجرای ابزار
1. یک ترمینال باز کنید و دستور `python app.py` رو اجرا کنید.
2. به بقیه کارهاتون برسید و منتظر پیامک باشید :)
3. اگر هم پیامک ست نکردید در ترمینال خود منتظر `++++ The End ++++` باشید
4. همچنین 3 فایل check_Me ,result , sitemap در پوشه برای شما ایجاد میشه که فایل check me ادرس url هایی هست که بیشتر از 30 روزه کرول نشدن 

لیمیت روزانه 2000 تا url رو داره اما میشه با کمی تغییر این لیمیت رو افزایش داد

سعی میکنم ویدیو آموزشش رو هم توی لینکدینم https://www.linkedin.com/in/amir-ebtekar/ بزارم
