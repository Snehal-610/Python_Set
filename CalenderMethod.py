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


# MonthDate = calendar.Calendar()
# for dates in MonthDate.itermonthdates(2021, 9):
#     if dates.month == 9:
#         print(dates)

MonthDate = calendar.Calendar(firstweekday=0)
# for dates in MonthDate.itermonthdates(2021, 9):
#     if dates.month == 9:
#         print(dates)

# for dates in MonthDate.itermonthdays(2021, 9):
    # if dates != 0:
    #    print(dates)

for dates in MonthDate.itermonthdays2(2021, 9):
    if dates[0] != 0:
       print(dates)