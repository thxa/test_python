# https://docs.python.org/3/reference/datamodel.html#basic-customization


class ChessCoordinate:

	# https://docs.python.org/3/reference/datamodel.html#object.__new__
	def __new__(cls, *args, **kwargs):
		print("args =", repr(args))
		print("kwargs =", repr(kwargs))
		obj = super().__new__(cls)
		print("id(obj)  =", id(obj))
		return obj # like self
	
	# https://docs.python.org/3/reference/datamodel.html#basic-customization
	def __init__(self, file, rank):

		print("id(self) =", id(self))
		print("self.__dict__ = ", self.__dict__)

		if len(file) != 1:
			raise ValueError("{} component file {!r} does not have a length of one."
							 .format(self.__class__.__name__, file))

		if file not in "abcdefgh":
			raise ValueError("{} component file {!r} is out of range."
							 .format(self.__class__.__name__, file))

		if rank not in range(1, 9):
			raise ValueError("{} component rank {!r} is out of range."
							 .format(self.__class__.__name__, rank))

		self._file = file # Like self.__dict__["_file"] = file
		print("self.__dict__ = ", self.__dict__)

		self._rank = rank # Like self.__dict__["_rank"] = rank
		print("self.__dict__ = ", self.__dict__)

	@property
	def file(self):
		return self._file
	
	@property
	def rank(self):
		return self._rank
	
	def __repr__(self):
		return "{}(file={}, rank={})".format(self.__class__.__name__, self.file, self.rank)

	def __str__(self):
		return "{}{}".format(self.file, self.rank)


def main():
	# print(dir(ChessCoordinate))
	# print(ChessCoordinate)
	white_queen = ChessCoordinate("d", 4)
	print(white_queen)
	# print(ChessCoordinate.__getattribute__)
	# print(ChessCoordinate.__new__)

if __name__ == '__main__':
	main()