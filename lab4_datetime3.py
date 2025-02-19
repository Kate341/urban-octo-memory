import datetime

created_date = datetime.datetime.today()
created_date = created_date.strftime("%m/%d/%Y %I:%M:%S %p")
print(created_date)
#With PM and AM
created_date = datetime.datetime.today()
created_date = created_date.strftime("%m/%d/%Y %I:%M:%S.%f %p")
print(created_date)
#With microseconds and PM, AM
created_date = datetime.datetime.today()
created_date = created_date.strftime("%m/%d/%Y %I:%M:%S")
print(created_date)
#Without microseconds and PM, AM

