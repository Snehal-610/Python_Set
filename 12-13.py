# 12.Get the 1st day of the current month from today's dat
import datetime

TodayDate = datetime.date.today()
FirstDay = datetime.date(TodayDate.year, TodayDate.month, TodayDate.day - (TodayDate.day - 1))
print(f"First day of {TodayDate.strftime('%B')} month of {TodayDate.strftime('%Y')} is {FirstDay.strftime('%A')}\n")

# 13.Get the 1st month of the current year from today's date.
FirstDay = datetime.date(TodayDate.year, TodayDate.month - (TodayDate.month - 1), TodayDate.day)
print(f"\nFirst day of {TodayDate.strftime('%Y')} is {FirstDay.strftime('%B')}")