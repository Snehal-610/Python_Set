# Calender Methods
import calendar

year = 2012
month = 11
# print(calendar.month(year, month))

# print(calendar.calendar(2021,0.5,1,6))

# weekdays = calendar.Calendar(firstweekday = 2)
#
# for day in obj.iterweekdays():
#     print(day)


MonthDate1 = calendar.Calendar()
# for dates in MonthDate1.itermonthdates(2021, 9):
#     if dates.month == 9:
#         print(dates)

MonthDate = calendar.Calendar(firstweekday=0)
# for dates in MonthDate.itermonthdates(2021, 9):
#     if dates.month == 9:
#         print(dates)

# for dates in MonthDate.itermonthdays(2021, 9):
# if dates != 0:
#    print(dates)

# for dates in MonthDate.itermonthdays2(2021, 9):
#     if dates[0] != 0:
#         print(dates)

# for day in MonthDate1.yeardatescalendar(2021,1):
    # print(day)

Specificday = MonthDate1.yeardatescalendar(2021,1)[0][0][0][:5]
print(Specificday)
