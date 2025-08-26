from datetime import datetime, date
import re

# import time
year_pattern = re.compile(r"^[0-9]{4}-[01-12]{2}-[01-31]{2}$")
year_pattern2 = re.compile(r"^\d{4}-(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012])$")
year_patter3 = re.compile(
    r"^(((0[1-9]|[12][0-9]|30)[-/]?(0[13-9]|1[012])|31[-/]?(0[13578]|1[02])|(0[1-9]|1[0-9]|2[0-8])[-/]?02)[-/]?[0-9]{4}|29[-/]?02[-/]?([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00))$"
)


birth_str = input("Enter your birthday (YYYY-MM-DD): ")


def date_format(date=birth_str):
    if year_pattern.match(date):
        birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
        return birth_date
    elif year_pattern2.match(date):
        birth_date = datetime.strptime(birth_str, "%Y-%d-%m").date()
        return birth_date
    elif year_patter3.match(date):
        birth_date = datetime.strptime(birth_str, "%d-%m-%Y").date()
        return birth_date


today = date.today()

if today.month == date_format().month and today.day == date_format().day:
    print("HBD")
else:
    next_birthday = date_format().replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_left = (next_birthday - today).days
    print(f"{days_left}left.")

#  2003-12-10
# print(time.time())
# 24-12-2003
# 2003-24-12