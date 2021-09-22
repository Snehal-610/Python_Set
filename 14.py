# 14.Get the dates of current month starting from Monday to Sunday in a list.
import datetime

TodayDate = datetime.date.today()
FirstDay = datetime.date(TodayDate.year, TodayDate.month, TodayDate.day - (TodayDate.day - 1))
F = int(FirstDay.strftime('%w'))

counter = 0
if F == 0:
    counter += 1
else:
    for i in range(F, 8):
        counter += 1
    print(counter)
FirstMonday = datetime.date(FirstDay.year,FirstDay.month,FirstDay.day+counter)

l = []
for i in range(0,7):
    result = str(datetime.date(FirstDay.year,FirstDay.month,FirstMonday.day+i))
    l.append(result)
print(l)