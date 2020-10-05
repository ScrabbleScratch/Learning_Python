from datetime import date
import datetime

todays_date = date.today()
currentTime = datetime.datetime.now()

print(todays_date.year, todays_date.month, todays_date.day, sep='/')
print(currentTime.hour, currentTime.minute, currentTime.second, sep=':')
