# https://docs.python.org/3/library/abc.html
# from abc import ABCMeta
from abc import ABC, abstractmethod

# class SwordMeta(type):

# 	def __instancecheck__(cls, instance):
# 		return cls.__subclasscheck__(type(instance))

# 	def __subclasscheck__(cls, sub):
# 		return (hasattr(sub, "swipe") and callable(sub.swipe)
# 				and
# 				hasattr(sub, "sharpen") and callable(sub.sharpen))


# class Sword(metaclass=SwordMeta):
# class Sword(metaclass=ABCMeta):
class Sword(ABC):
	@classmethod
	def __subclasshook__(self, sub):
		return (hasattr(sub, "swipe") and callable(sub.swipe)
				and
				hasattr(sub, "sharpen") and callable(sub.sharpen)
				and
				hasattr(sub, "thrust") and callable(sub.thrust)
				and
				hasattr(sub, "parry") and callable(sub.parry)		
				or NotImplemented)

	@abstractmethod
	def swipe(self):
		raise NotImplementedError

	@abstractmethod
	def thrust(self):
		print("Thrusting...")

	@abstractmethod
	def parry(self):
		raise NotImplementedError


class BroadSword(Sword):

	def swipe(self):
		print("Swoosh!")

	def sharpen(self):
		print("Shink!")

	def thrust(self):
		super().thrust()

	def parry(self):
		print("parry")


@Sword.register
class LightSaber:

	def swipe(self):
		print("Ffffkrrrrshhzzzwooooom..woom..wooom..")


class SamuraiSword:

	def swipe(self):
		print("Slice!")

	def sharpen(self):
		print("Shink!")
		

class Rifle:

	def fire(self):
		print("Bang!")


def main():

	print(issubclass(BroadSword, Sword))
	print(issubclass(SamuraiSword, Sword))
	print(issubclass(Rifle, Sword))
	print(issubclass(LightSaber, Sword))
	print()

	broadsword = BroadSword()
	print(isinstance(broadsword, Sword))

	broadsword.swipe()
	broadsword.sharpen()
	broadsword.thrust()
	broadsword.parry()
	# broadsword.thrust()
	print(BroadSword.__mro__)

if __name__ == '__main__':
	main()