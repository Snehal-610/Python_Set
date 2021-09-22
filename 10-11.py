# 10.Get the date which is 1 year from today's date.
import datetime

TodayDate = datetime.date.today()
NextYear = datetime.date(TodayDate.year + 1, TodayDate.month, TodayDate.day)
print(f"Present Date: {TodayDate}\nNext Year Date: {NextYear}\n")

# 11.Get the date which is 1 month from today's date.
TodayDate = datetime.date.today()
NextMonth = datetime.date(TodayDate.year, TodayDate.month + 1, TodayDate.day)
print(f"Present Date: {TodayDate}\nNext Year Date: {NextMonth}")
