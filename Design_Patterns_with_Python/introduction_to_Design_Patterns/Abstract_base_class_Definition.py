# https://app.pluralsight.com/course-player?clipId=ab170999-5ab7-4036-a8fe-7bd1bfc5297c
import abc

class MyABC(object, metaclass=abc.ABCMeta):
	# __metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def do_something(self, value):
		"""Required method"""


	@abc.abstractproperty
	def some_property(self):
		"""Required property"""



class MyClass(MyABC):
	"""Implementaion of MyABC"""

	def __init__(self, value=None):
		self._myprop = value

	def do_something(self, value):
		"""Implementaion of abstract method"""
		self._myprop *= 2 + value

	@property
	def some_property(self):
		"""Implementaion of abstract property"""
		return self._myprop


class BadClass(MyABC):
	pass


if __name__ == '__main__':
	myclass = MyClass(1)
	print(myclass.some_property)
	
	myclass.do_something(1)
	print(myclass.some_property)

	bad = BadClass()
