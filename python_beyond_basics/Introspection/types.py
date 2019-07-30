
def main():
	i = 7
	print(type(i))
	
	print(int)
	print(repr(int))
	print(type(i) is int)

	print(type(type("")(78)))
	print(type("")(78))

	print(type(type(i)(78)))
	print(type(i)(78))

	print(type(type(i)))

	print(i.__class__)
	print(i.__class__.__class__)
	print(i.__class__.__class__.__class__)

	print(issubclass(type, object))
	print(type(object))

	print(isinstance(i, int))


if __name__ == '__main__':
	main()