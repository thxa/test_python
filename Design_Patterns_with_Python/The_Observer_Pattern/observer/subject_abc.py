from abc import ABCMeta, abstractmethod
from .observer_abc import AbsObserver

class AbsSubject(object, metaclass=ABCMeta):

	_observers = set()

	def attach(self, observer):
		if not isinstance(observer, AbsObserver):
			raise TypeError("Observer not derived from AbsObserver")
		self._observers |= {observer}
	
	def detach(self, observer):
		self._observers -= {observer}

	def notify(self, value=None):
		for observer in self._observers:
			if value is None:
				observer.update()
			else:
				observer.update(value)