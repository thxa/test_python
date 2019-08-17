

class DataDescriptor:
	# https://docs.python.org/3/reference/datamodel.html#object.__get__
	def __get__(self, instance, owner):
		print("DataDescriptor.__get__({!r}, {!r}, {!r})"
			  .format(self.__dict__, instance.__dict__, owner.__name__))
			  # .format(self.__class__.__dict__, instance.__dict__, owner.__name__))

	# https://docs.python.org/3/reference/datamodel.html#object.__set__
	def __set__(self, instance, value):
		print("DataDescriptor.__set__({!r}, {!r}, {!r})"
		  	  .format(self, instance, value))


class NonDataDescriptor:

	def __get__(self, instance, owner):
		print("NonDataDescriptor.__get__({!r}, {!r}, {!r})"
			  .format(self.__dict__, instance.__dict__, owner.__name__))
			  # .format(self.__class__.__dict__, instance.__dict__, owner.__name__))


class Owner:
	a = DataDescriptor()
	b = NonDataDescriptor()


def main():
	obj = Owner()
	obj.a
	obj.__dict__['a'] = 196883
	print()
	obj.a

	print()
	obj.b
	obj.__dict__['b'] = 744
	print()
	print(obj.b)


if __name__ == '__main__':
	main()