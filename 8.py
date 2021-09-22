import datetime
from dateutil.relativedelta import relativedelta
DateToday = datetime.datetime.now()

birth_year = int(input("Enter birth year : "))
birth_month = int(input("Enter birth month : "))
birth_day = int(input("Enter birth day : "))

Birthday = datetime.datetime(birth_year,birth_month,birth_day)
Age = relativedelta(DateToday, Birthday)
print(f"Your Age is:{Age.years} Years, {Age.months} Months, {Age.days} Days")

