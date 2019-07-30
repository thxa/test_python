# https://docs.python.org/3/library/functions.html
from decimal import Decimal
from fractions import Fraction


print(abs(-5))
print(abs(-5.0))

print(abs(Decimal(5)))

print(abs(Fraction(-5, 1)))

# https://docs.python.org/3/library/functions.html#abs
print(abs(complex(0, -5)))

# https://docs.python.org/3/library/functions.html#round
print(round(0.23123, 3))
print(round(0.23123, 1))
print(round(1.5))
print(round(2.5))

print(round(Decimal('3.25')))
print(round(Fraction(57, 100), 2))
print(round(Fraction(57, 100), 1))
print(round(Fraction(57, 100), 0))