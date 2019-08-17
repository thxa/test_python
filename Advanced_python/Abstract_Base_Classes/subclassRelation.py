from collections.abc import Hashable

def main():
	print(issubclass(object, Hashable))
	print(issubclass(list, object))
	print(issubclass(list, Hashable))

	print(object.__hash__)
	print(list.__hash__)



if __name__ == '__main__':
	main()