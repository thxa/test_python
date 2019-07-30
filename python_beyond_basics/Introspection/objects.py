def main():
	i = 7

	print(dir(i))

	print(getattr(i, 'denominator'))
	print(i.denominator)

	print(getattr(i, 'conjugate'))
	print(callable(getattr(i, 'conjugate')))
	print(i.conjugate.__class__.__name__)

	print(hasattr(i, 'index'))

	print(hasattr(i, 'bit_length'))
	print(getattr(i, 'bit_length'))

	# print(getattr(i, 'numerator'))
	# print(getattr(i, 'imag'))

if __name__ == '__main__':
	main()