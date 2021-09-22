# 9.Get the date which is 1 week from today's date.
import datetime

DateToday = datetime.date.today()
NextWeekDate = DateToday + datetime.timedelta(days=7)
print(f"Next Week Date is: {NextWeekDate}")
