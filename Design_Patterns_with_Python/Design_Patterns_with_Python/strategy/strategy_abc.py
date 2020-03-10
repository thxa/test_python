from abc import ABCMeta, abstractmethod

class ABCStrategy(metaclass=ABCMeta):
	# __metaclass__ = ABCMeta

	@abstractmethod
	def calculate(self, order):
		""" Calculate shipping cost """
