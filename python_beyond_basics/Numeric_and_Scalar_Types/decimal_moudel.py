# https://docs.python.org/3/library/decimal.html
import decimal

print(decimal.getcontext())

print(decimal.Decimal(5))

from decimal import Decimal

print(Decimal(7))
print(Decimal('0.8'))
print(Decimal('0.8') - Decimal('0.7'))
print(Decimal(0.8) - Decimal(0.7))

decimal.getcontext().traps[decimal.FloatOperation] = True
# print(Decimal(0.8))
# print(Decimal('0.8') > 0.7)
# if float become False but if int or string float become True
a = Decimal(3)
b = Decimal('3.0')
c = Decimal('3.00')

print(a)
print(b)
print(c)

print(a * 2)
print(b * 2)
print(c * 2)

decimal.getcontext().prec = 6
d = Decimal('1.234567')
print(d)
print(d + Decimal(1))

print(Decimal('Infinity'))
print(Decimal('-Infinity'))
print(Decimal('NaN'))

print(Decimal('NaN') + Decimal('1.414'))

# print(Decimal('1.4') + 0.6)

# IEEE Standard for Radix-Independent Floating-Point Arthmetic
print((-7) % 3)
print(Decimal(-7) % Decimal(3))


def is_old(n):
	return n % 2 == 1

print(is_old(2))
print(is_old(3))

print(is_old(-2))
print(is_old(-3))

print(is_old(2.0))
print(is_old(3.0))

print(is_old(-2.0))
print(is_old(-3.0))


print(is_old(Decimal(2)))
print(is_old(Decimal(3)))

print(is_old(Decimal(-2)))
print(is_old(Decimal(-3)))

print(Decimal(-3) % 2)

def is_old(n):
	return n % 2 != 0

print(is_old(Decimal(-3)))

print(-7 // 3)
print(Decimal(-7) // Decimal(3))
print(Decimal('0.81').sqrt())
