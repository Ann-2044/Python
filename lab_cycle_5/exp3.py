import calendar
from datetime import date,timedelta
today=date.today()
yesterday=today-timedelta(days=1)
tommorow=today+timedelta(days=1)
print("Yesterday=",calendar.day_name[yesterday.weekday()])
print("Today=",calendar.day_name[today.weekday()])
print("Tommorow=",calendar.day_name[tommorow.weekday()])
