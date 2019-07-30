class SimpleList(object):
	def __init__(self, items):
		self._items = list(items)

	def add(self, item):
		self._items.append(item)

	def __getitem__(self, index):
		return self._items[index]

	def sort(self):
		self._items.sort()

	def __len__(self):
		return len(self._items)

	def __repr__(self):
		return "SimpleList({!r})".format(self._items)


# inheritance single from SimpleList
class SortedList(SimpleList):
	def __init__(self, items=()):
		super().__init__(items)
		self.sort()

	def add(self, item):
		super().add(item)
		self.sort()

	def __repr__(self):
		return "SortedList({!r})".format(list(self))


# inheritance single from SimpleList
class IntList(SimpleList):
	def __init__(self, items=()):
		for x in items:
			self._validate(x)
		super().__init__(items)

	@staticmethod
	def _validate(x):
		if not isinstance(x, int):
			raise TypeError("IntList only supports integer values.")

	def add(self, item):
		self._validate(item)
		super().add(item)

	def __repr__(self):
		return "IntList({!r})".format(list(self))


# Multiple inheritance from SimpleList AND IntSimple
class SortedIntList(IntList, SortedList):
	def __repr__(self):
		return "SortedIntList({!r})".format(list(self))

# test SortedList
sl = SortedList([0, 5, 60, 3, 7, 8])
print(sl)
sl.add(-5)
print(sl)
sl.add(20)
print(sl)


# isinstance(value, type) Funcion
print(isinstance(sl, SimpleList))
print(isinstance(sl, SortedList))
# print(isinstance(sl, object))

# test IntList
il = IntList([1, 2, 5, 2, 50, 3])
print(il)
il.add(-4)
print(il)
# il.add("1")

# issubclass Function
print(issubclass(SortedList, SimpleList))
print(issubclass(IntList, SimpleList))
print(issubclass(SimpleList, IntList))

# test class SortedIntList
sil = SortedIntList([1, 3, 5, 20 , 45, 0, 2])
print(sil)
sil.add(-22)
print(sil)

# bases of class
print(SortedIntList.__bases__)
print(IntList.__bases__)
print(SortedList.__bases__)
print(SimpleList.__bases__)
print(object.__bases__)

# mro
print(SortedIntList.mro())
print(SortedIntList.__mro__)

# test super 
print(super(SortedList, SortedIntList).add)

print()
print(super(SortedList, sil))
print(sil)
super(SortedList, sil).add(1)
print(sil)
super(SortedList, sil).add("Hello I am n't number, I'm string")
print(sil)
