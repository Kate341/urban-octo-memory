import datetime

yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
today = datetime.datetime.today()
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)

from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
today = date.today()
tomorrow = date.today() + timedelta(days=1)

print(yesterday)
print(today)
print(tomorrow)