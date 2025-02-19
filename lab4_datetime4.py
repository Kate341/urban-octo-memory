import datetime
import math

years = int(input())
months = int(input())
days = int(input())
hours = int(input())
minutes = int(input())
seconds = int(input())

years1 = int(input())
months1 = int(input())
days1 = int(input())
hours1 = int(input())
minutes1 = int(input())
seconds1 = int(input())

first_date = datetime.datetime(years, months, days, hours, minutes, seconds)
second_date = datetime.datetime(years1, months1, days1, hours1, minutes1, seconds1)
delta = second_date - first_date
print(delta)

delta_seconds = delta.total_seconds()
print(int(delta_seconds))