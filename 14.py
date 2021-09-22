# 14.Get the dates of current month starting from Monday to Sunday in a list.
import datetime, calendar

TodayDate = datetime.date.today()
DayRange = calendar.monthrange(TodayDate.year, TodayDate.month)

FirstDay = datetime.date(TodayDate.year, TodayDate.month, TodayDate.day - (TodayDate.day - 1))
FirstMonday_date = datetime.date(TodayDate.year, TodayDate.month, FirstDay.day + (7 - DayRange[0]))
# F = int(FirstDay.strftime('%w'))
# counter = 0
# if F == 0:
#     counter += 1
# else:
#     for i in range(F, 8):
#         counter += 1
#     print(counter)
# FirstMonday = datetime.date(FirstDay.year,FirstDay.month,FirstDay.day+counter)

Last = (DayRange[0] + DayRange[1]) % 7
LastDate = datetime.date(TodayDate.year, TodayDate.month, DayRange[1])
print(LastDate)
LastSunday = datetime.date(TodayDate.year, TodayDate.month, LastDate.day - 4)

InnerList = []
for i in range(FirstMonday_date.day - 1, LastSunday.day):
    result = datetime.date(TodayDate.year, TodayDate.month, FirstDay.day + i)
    InnerList.append(result)


def divide_chunks(List, n):
    for i in range(0, len(List), n):
        yield List[i:i + n]


s = list(divide_chunks(InnerList, 7))
print(s)
