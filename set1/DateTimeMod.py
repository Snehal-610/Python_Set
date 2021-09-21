import datetime

DayToday = datetime.datetime.now()
print("Date and Time for Today: ", DayToday)
print("Date for Today: ", DayToday.date())
print("Current Time: ", DayToday.time())
# ItrateDetail = DayToday.timetuple()
# print("All Information in tuple format: ", ItrateDetail)
# print("Year: ", ItrateDetail[0])

# ----------------------- Using strftime -----------------------
# print(DayToday.strftime(f"%d / %m / %y, %I:%M:%S %p"))
# print(DayToday.strftime(f"%d / %m / %y, %I:%M:%S %p"))
# print(DayToday.strftime(f"%d / %m / %y, %I:%M:%S %p"))
# print(DayToday.strftime(f"%A - %B - %Y, %I:%M:%S %p"))

# -----------------------Creating Date Object ------------------------
DateObj = datetime.datetime(2021, 11, 22, 17, 55, 6)
DateObj2 = datetime.datetime(2020, 1, 28, 1, 55, 58)
print("Date for Today: ", DateObj.year)
print("Current Time: ", DateObj.month)
# print("Date and Time for Specific date: ", DateObj)
# print("Difference of two date: ", DateObj - DateObj2)
# print("Difference of two date: ", DayToday - DateObj2)
# print("TimeStamp: ", DayToday.timestamp())


# -------------------------------- TimeDelta --------------------------
FutureDate = DayToday + datetime.timedelta(days=15)
print("15 Day After Today: ", FutureDate)
Birthday = datetime.datetime(2021, 10, 6)

print("How many days Remaining: ", Birthday - DayToday)
