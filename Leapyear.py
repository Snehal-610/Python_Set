import datetime

TodayDate = datetime.date(2000,1,1)
year = TodayDate.year


def IsLeap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


Lyear = IsLeap(year)
print(Lyear)