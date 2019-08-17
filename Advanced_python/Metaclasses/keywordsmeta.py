# from duplicatesmeta import ProhibitDuplicatesMeta


class KeyWordsOnlyMeta(type):

	def __call__(cls, *args, **kwargs):
		if args:
			raise TypeError("Constructor for class {!r} does not accept positional arguments.".format(cls))
		return super().__call__(cls, **kwargs)




class ConstrainedToKeywords(metaclass=KeyWordsOnlyMeta):

	def __init__(self, *args, **kwargs):
		print("args = ", args)
		print("kwargs = ", kwargs)


def main():
	c = ConstrainedToKeywords(color="white")
	# c = ConstrainedToKeywords(23, 44, 44, color="white")

if __name__ == "__main__":
	main()