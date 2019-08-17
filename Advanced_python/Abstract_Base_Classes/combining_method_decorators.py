from abc import ABC, abstractmethod

class AbstractBaseClass(ABC):

	@property
	@abstractmethod
	def abstract_property(self):
		raise NotImplementedError

	@property
	def concrete_property(self):
		return "send, cement, water"



def main():
	print(AbstractBaseClass.abstract_property.__isabstractmethod__)
	print(AbstractBaseClass.concrete_property.__isabstractmethod__)

if __name__ == '__main__':
	main()