from vector_2 import *


class LoggingProxy():
	def __init__(self, target):
		super().__setattr__("target", target)

	# https://docs.python.org/3/reference/datamodel.html#object.__getattribute__
	def __getattribute__(self, name):
		target = super().__getattribute__("target")

		try:
			value = getattr(target, name)
		except AttributeError as e:
			raise AttributeError("{} could not forward request {} to {}".format(
				super().__getattribute__("__class__").__name__,
				name,
				target)) from e
		print("Retrieved attribute {!r} = {!r} from {!r}".format(name, value, target))
		return value

	def __setattr__(self, name, value):
		target = super().__getattribute__("target")

		try:
			setattr(target, name, value)
		except AttributeError as e:
			raise AttributeError("{} could not forward request {} to {}".format(
				super().__getattribute__("__class__").__name__,
				name,
				target)) from e
		else:
			print("Set attribute {!r} = {!r} from {!r}".format(name, value, target))

	def __repr__(self):
		target = super().__getattribute__("target")
		repr_callable = getattr(target, "__repr__")
		return repr_callable()


def main():
	cv = ColoredVector(red=23, green=44, blue=238, p=9, q=14)
	cw = LoggingProxy(cv)

	print(cv)

	print(vars(cw))
	print(cw.p)
	print(cw.red)
	# cw.p = 15
	# cw.red = 20
	# print(cw.p)
	# print(cw.red)
	print(cw.__repr__())
	print(repr(cw))


if __name__ == '__main__':
	main()
		