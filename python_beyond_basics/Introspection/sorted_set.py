# https://docs.python.org/3/library/collections.abc.html#module-collections.abc
# https://docs.python.org/3/library/unittest.html
from collections.abc import Sequence, Set
from bisect import bisect_left
from itertools import chain


class SortedSet(Sequence, Set):

	def __init__(self, items=None):
		# Construction
		self._items = sorted(set(items)) if items is not None else []
	
	# ContainerProtocol
	def __contains__(self, item):
		try:
			self.index(item)
			return True
		except ValueError:
			return False

	# SizedProtocol
	def __len__(self):
		return len(self._items)

	# IterableProtocol
	def __iter__(self):
		# genretes faster then iter
		# for item in self._items:
		# 	yield item
		return iter(self._items)

	# SequenceProtocol indexing
	def __getitem__(self, index):
		# print(index)
		# print(type(index))
		result = self._items[index]
		return SortedSet(result) if isinstance(index, slice) else result

	# ReprProtocol
	def __repr__(self):
		return "SortedSet({})".format(
			repr(self._items) if self._items else ''
			)

	# EqualityProtocol
	# https://docs.python.org/3/reference/datamodel.html#object.__eq__
	# self == other
	def __eq__(self, other):
		if not isinstance(other, SortedSet):
			return NotImplemented
		return self._items == other._items

	# InequalityProtocol
	# https://docs.python.org/3/reference/datamodel.html#object.__ne__
	# self != other
	def __ne__(self, other):
		if not isinstance(other, SortedSet):
			return NotImplemented
		return self._items != other._items

	# Get item of index
	def index(self, item):
		index = bisect_left(self._items, item)
		if (index != len(self._items)) and (self._items[index] == item):
			return index
		raise ValueError("{} not found".format(repr(item)))

	# Counting how many repeting the item
	def count(self, item):
		return int(item in self)

	# self + other
	def __add__(self, other):
		return SortedSet(chain(self._items, other._items))

	# self * other
	def __mul__(self, other):
		return self if other > 0 else SortedSet()

	# other * self 
	def __rmul__(self, other):
		return self * other

	# Set Protocol ###
	def issubset(self, iterable):
		return self <= SortedSet(iterable)

	def issuperset(self, iterable):
		return self >= SortedSet(iterable)

	def intersection(self, iterable):
		return self & SortedSet(iterable)

	def union(self, iterable):
		return self | SortedSet(iterable)

	def symmetric_difference(self, iterable):
		return self ^ SortedSet(iterable)

	def difference(self, iterable):
		return self - SortedSet(iterable)
	# Set Protocol ###