# https://docs.python.org/3/library/datetime.html#datetime-objects
# from datetime import datetime
# print(datetime.time)
# from datetime import datetime as Datetime
# import datetime as dt

import datetime

print(datetime.datetime(2019, 1, 1, 10, 50, 10, 452321))
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
print(datetime.datetime.fromordinal(5))
print(datetime.datetime.fromtimestamp(237782))
print(datetime.datetime.utcfromtimestamp(237782))

d = datetime.date.today()
t = datetime.time(8, 15)
print(datetime.datetime.combine(d, t))

dt = datetime.datetime.strptime("Monday 6 January 2019, 12:42:31",
								"%A %d %B %Y, %H:%M:%S")
print(dt)
print(dt.date())
print(dt.time())
print(dt.day)
print(dt.isoformat())
