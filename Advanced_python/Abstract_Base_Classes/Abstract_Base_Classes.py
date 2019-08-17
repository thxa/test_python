# https://docs.python.org/3/library/collections.abc.html
# https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence
from collections.abc import MutableSequence

def main():
	print(issubclass(list, MutableSequence))

	print(list.__mro__)

	print(MutableSequence.__mro__)

	#def issubclass():
		# if hasattr(type(MutableSequence), "__subclasscheck__"):
		# 	return type(MutableSequence).__subclasscheck__(list)


if __name__ == '__main__':
	main()