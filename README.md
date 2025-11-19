# Persian Date Today (Jalali Calendar)

A simple and lightweight Python application that displays the **current Persian (Shamshi/Jalali) date and day of the week** in a beautiful, readable Persian format — both in the terminal and in a small graphical window using Tkinter.

Perfect for adding a touch of Persian culture to your desktop or integrating into larger Persian-language projects.

![Screenshot](screenshot.png)

## Features
- Shows today's date in Jalali (Persian) calendar
- Displays Persian day name (شنبه، یک‌شنبه، etc.)
- Fully formatted and human-readable output
- Terminal output + minimal GUI using Tkinter
- Uses the popular `jdatetime` library
- Supports Persian fonts (Vazir font included in display)

 Example Output

تاریخ شمسی امروز: 1404/08/28 (سه‌شنبه، ۲۸ آبان ۱۴۰۴)

And a small window showing the same date in Persian script.

 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/persian-date-today.git
cd persian-date-today

(Recommended) Create a virtual environment:

bash

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

Install dependencies:

bash

pip install jdatetime

(Optional but recommended) Install the Vazir font for perfect Persian rendering:Download from: https://github.com/rastikerdar/vazir-font
Install on your system (double-click TTF files)

 Runbash

python persian_date.py

The script will print the current Persian date in the terminal and open a small window showing the same. RequirementsPython 3.6+
jdatetime library
(For GUI) Tkinter (comes with standard Python)
Vazir font (for best visual experience)

