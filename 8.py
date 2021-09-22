import datetime
from dateutil.relativedelta import relativedelta
DateToday = datetime.datetime.now()
Birthday = datetime.datetime(1994,10,6)
Age = relativedelta(DateToday, Birthday)
print(f"Your Age is:{Age.years} Years, {Age.months} Months, {Age.days} Days")