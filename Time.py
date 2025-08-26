from datetime import datetime, date

birth_str = input("Enter your birthday (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()

today = date.today()

if today.month == birth_date.month and today.day == birth_date.day:
    print("HBD")
else:
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    days_left = (next_birthday - today).days
    print(f"{days_left}left.")

#  2003-12-10