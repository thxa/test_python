import datetime

print(datetime.timedelta(milliseconds=1, microseconds=1000))

td = datetime.timedelta(weeks=1, minutes=2, milliseconds=5500)
print(td)
print(td.days)
print(td.seconds)
print(td.microseconds)
print(str(td))
print(repr(td))
