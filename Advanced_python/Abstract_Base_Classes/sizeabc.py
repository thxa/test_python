from collections.abc import Sized


class SizeCollection:
	def __init__(self, size):
		self._size = size

	def __len__(self):
		return self._size


class SizeMeta(type):
	def __instancecheck__(cls, instance):
		return cls.__subclasscheck__(type(instance))
	
	def __subclasscheck__(cls, sub):
		return (hasattr(sub, "__len__") and callable(sub.__len__))

class Size(metaclass=SizeMeta):
	pass

def main():
	print(issubclass(SizeCollection, Sized))
	print(issubclass(SizeCollection, Size))


if __name__ == '__main__':
	main()