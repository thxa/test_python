# https://docs.python.org/3/tutorial/classes.html#scopes-and-namespaces-example

def report_scope(arg):
	from pprint import pprint as pp
	x = 11

	# all varbales in loacl
	# https://docs.python.org/3/library/functions.html#locals
	pp(locals(), width=10)
	
def main():
	# all varbales in global
	# https://docs.python.org/3/library/functions.html#globals
	print(globals())
	globals()["n"] = 1
	print(n)
	report_scope(24)

	name = "Test"
	age = 0
	country = None

	print("{name} is {age} years old and is from {country}".format(**locals()))


if __name__ == '__main__':
	main()
	print(n)