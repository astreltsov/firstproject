import datetime
today = datetime.date.today()
print(f"Today's date is {today}.")
holiday = datetime.date(2020,12,31)
delta = holiday - today
print(f"Just {delta.days} days until the holiday")