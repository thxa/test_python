from abc import ABCMeta


class Text(metaclass=ABCMeta):
	pass


def main():
	print(Text.register(str))

	print(issubclass(str, Text))
	print(isinstance("Is this text?", Text))


	@Text.register
	class Prose:
		pass

	print(issubclass(Prose, Text))

if __name__ == '__main__':
	main()