import datetime

past_time = datetime.datetime.today() - datetime.timedelta(days=5)
print(past_time)

from datetime import date, timedelta
past_time = date.today() - timedelta(days=5)
print(past_time)