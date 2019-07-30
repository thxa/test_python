# https://docs.python.org/3/library/datetime.html
import datetime

print(datetime.date(year=2019, month=1, day=6))
print(datetime.date.today())
print(datetime.date.fromtimestamp(1000000000))
print(datetime.date.fromordinal(720669))

d = datetime.date.today()
print(d.year)
print(d.month)
print(d.day)
print(d.weekday())
print(d.isoweekday())
print(d.isoformat())
print(d.strftime('%A %d %B %Y'))

print("The date is {:%A %d %B %Y}".format(d))

e = datetime.date(2019, 3, 2)

print("{date:%A} {date.day} {date:%B}  {date.year}".format(date=e))

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)