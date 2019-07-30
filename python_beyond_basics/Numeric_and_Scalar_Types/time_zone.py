import datetime

cet = datetime.timezone(datetime.timedelta(hours=1), "CET")
print(cet)

departure = datetime.datetime(year=2019, month=5, day=10,
							  hour=11, minute=30, tzinfo=cet)

arrival = datetime.datetime(year=2019, month=5, day=10,
							hour=13, minute=5, tzinfo=datetime.timezone.utc)
print(departure)
print(arrival)

print(arrival - departure)