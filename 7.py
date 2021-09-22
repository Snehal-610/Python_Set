import datetime
from dateutil.relativedelta import relativedelta
DateToday = datetime.datetime.now()
Birthday = datetime.datetime(2025, 10, 6)
Difference = Birthday - DateToday
print("Difference of Two date is: ",Difference)


# or ----------- or
if Birthday > DateToday:
    Diff = relativedelta(Birthday,DateToday)
    print(f"Difference is:{Diff.years} Years, {Diff.months} Months, {Diff.days} Days")
else:
    Diff = relativedelta(DateToday, Birthday)
    print(f"Difference is:{Diff.years} Years, {Diff.months} Months, {Diff.days} Days")
