class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "{}({}, {})".format(self.__class__.__name__, self.x, self.y)

	def __len__(self):
		return len(self.__dict__)


v = Vector(11, 55)

print(v)

# Indirect pythonic
print(vars(v))
print(len(v))


# Direct unpythonic ?
print(v.__dict__)
print(v.__len__())
