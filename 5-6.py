# 5.Print the current date using datetime and date libraries.
print("------------- 5")
import datetime
DayToday = datetime.datetime.now()
print(f"Date Time without strftime Function: {DayToday}")

# 6.Convert a datetime to a string.
print("------------- 6")
print(f'''Year: {DayToday.strftime('%Y')}\nMonth: {DayToday.month} - {DayToday.strftime('%B')}\nDay: {DayToday.strftime('%d')} - {DayToday.strftime('%A')}
Hours: {DayToday.strftime('%I')}\nMinutes: {DayToday.strftime('%M')}\nSeconds:{DayToday.strftime('%S')}''')

