# -*- coding: utf-8 -*-



import jdatetime

def gregorian_to_jalali():
    # گرفتن تاریخ و زمان جاری به‌صورت شمسی
    jalali_date = jdatetime.datetime.now()
    
    # تنظیم روز هفته با شروع از شنبه
    days = {
        0: "شنبه",
        1: "یک‌شنبه",
        2: "دوشنبه",
        3: "سه‌شنبه",
        4: "چهارشنبه",
        5: "پنج‌شنبه",
        6: "جمعه"
    }
    day_of_week = jalali_date.weekday()
    day_name = days[day_of_week]
    
    # تنظیم نام ماه‌های شمسی
    months = {
        1: "فروردین",
        2: "اردیبهشت",
        3: "خرداد",
        4: "تیر",
        5: "مرداد",
        6: "شهریور",
        7: "مهر",
        8: "آبان",
        9: "آذر",
        10: "دی",
        11: "بهمن",
        12: "اسفند"
    }
    month_number = jalali_date.month
    month_name = months[month_number]
    
    # فرمت تاریخ شمسی
    day = jalali_date.day
    year = jalali_date.year
    return f"{year}/{month_number:02d}/{day:02d} ({day_name}، {day} {month_name} {year})"

# اجرای برنامه
if __name__ == "__main__":
    result = gregorian_to_jalali()
    print(f"تاریخ شمسی امروز: {result}")




import tkinter as tk
from tkinter import font

root = tk.Tk()
root.option_add("*Font", "Vazir 12")  # فونت Vazir
label = tk.Label(root, text=result, justify="right")
label.pack()
root.mainloop()


input()
