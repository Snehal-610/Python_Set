# 15. Get the first date and last date of the current month.
import datetime

TodayDate = datetime.datetime.now()
FirstDay = datetime.datetime(TodayDate.year, TodayDate.month, TodayDate.day - (TodayDate.day - 1),
                             TodayDate.hour, TodayDate.minute, TodayDate.second)

# NextMonth = FirstDay.replace(day=28) + datetime.timedelta(days=TodayDate.day)

import calendar  # LAst DAy

L = calendar.monthrange(TodayDate.year, TodayDate.month)[1]
LastDay = datetime.datetime(TodayDate.year, TodayDate.month, L)
# LastDay = NextMonth - datetime.timedelta(days=NextMonth.day)
print(f"First Day: {FirstDay}\nLast Day: {LastDay}")

# 16.Get me the 1st and last date of the current month in the format as following. '14th
# June 2016 Tuesday 10:00:00 AM'
print(f"{FirstDay.strftime('%d %B %Y %A %I:%M:%S %p')}\n{LastDay.strftime('%d %B %Y %A %I:%M:%S %p')}")





