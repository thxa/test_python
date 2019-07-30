# https://docs.python.org/3/library/exceptions.html
def lookups():
	l = [1, 4, 6]
	try:
		item = l[5]
	except LookupError:
		print("Handler IndexError")
		# print(IndexError.mro())

	d = dict(a=1, b=2, c=3)
	try:
		value = d['x']
	except LookupError:
		print("Handler KeyError")
		# print(KeyError.mro())


if __name__ == '__main__':
	lookups()