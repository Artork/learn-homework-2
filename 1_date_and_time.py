"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    from datetime import  date, timedelta

    dt_today = date.today()
    one_day = timedelta(days=1)
    one_month = timedelta(days=30)
    print(dt_today-one_day)
    print(dt_today)
    print(dt_today-one_month)
    


def str_2_datetime(date_string):
    from datetime import datetime
    date_format = "%d/%m/%y %H:%M:%S.%f"
    date_str = datetime.strptime(date_string, date_format)
    print(date_str)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
