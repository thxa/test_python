
from fractions import Fraction

# def mixed_numeral(vulgar):
# 	if not (hasattr(vulgar, "numerator") and hasattr(vulgar, "denominator")):
# 		raise TypeError("{} is not a rational number".format(vulgar))

# 	integer = vulgar.numerator // vulgar.denominator
# 	fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
# 						vulgar.denominator)
# 	return integer, fraction


def mixed_numeral(vulgar):
	try:
		integer = vulgar.numerator // vulgar.denominator
		fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
							vulgar.denominator)
		return integer, fraction
	except AttributeError as e:
		raise TypeError("{} is not a rational number".format(vulgar)) from e


def main():
	print(mixed_numeral(Fraction("11/10")))
	print(mixed_numeral(1.7))

if __name__ == '__main__':
	main()