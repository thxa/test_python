from abc import ABCMeta, abstractmethod


class AbsObserver(object, metaclass=ABCMeta):

	@abstractmethod
	def update(self, value):
		""" Upadte State """
		pass