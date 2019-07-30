# https://docs.python.org/2/library/fractions.html
# https://docs.python.org/3.1/library/fractions.html

from fractions import Fraction

"""
class fractions.Fraction(numerator=0, denominator=1)
class fractions.Fraction(other_fraction)
class fractions.Fraction(string)
"""

two_thirds = Fraction(2, 3)
four_fifths = Fraction(4, 5)

print(two_thirds)
print(four_fifths)

# print(Fraction(5, 0))
print(Fraction(23232132312323213))
print(Fraction(0.5))
print(Fraction(0.1))

from decimal import Decimal

print(Fraction(Decimal('0.1')))
print(Fraction('22/7'))

print(two_thirds + four_fifths)
print(two_thirds - four_fifths)
print(two_thirds * four_fifths)
print(two_thirds / four_fifths)
print(two_thirds // four_fifths)
print(two_thirds % four_fifths)

from math import floor
print(floor(Fraction('4/3')))

print(two_thirds ** four_fifths)