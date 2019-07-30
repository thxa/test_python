import contextlib

@contextlib.contextmanager
def nest_test(name):
	print("Entering:", name)
	yield name
	print("Exiting", name)


def main():
	# Multiple Context Manager
	with nest_test('outer'), nest_test('inner'):
		print("BODY")

	# Multiple Context Manager
	with nest_test('outer'):
		with nest_test('inner'):
			print("BODY")

	# Multiple Context Manager
	with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
			print("BODY")

	# Don't Pass a List! 
	# with [nest_test('a'), nest_test('b')]:
	# 	pass

	# 
	with nest_test('a'), nest_test('b'):
		pass
	
	# 
	with nest_test('a'),\
	 	 nest_test('b'),\
	 	 nest_test('c'): pass


if __name__ == '__main__':
	main()