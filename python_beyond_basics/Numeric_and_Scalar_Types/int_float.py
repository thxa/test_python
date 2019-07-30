from math import factorial as fac
import sys

# print(fac(1000))

print(sys.float_info)
most_negtive_float = -sys.float_info.max
greatest_negtive_float = -sys.float_info.min

print(most_negtive_float)
print(greatest_negtive_float)

print(float(10))

print(float(2**53))
print(float(2**53 + 1)) # False
print(float(2**53 + 2)) # True
print(float(2**53 + 3)) # False
print(float(2**53 + 4)) # True

print(0.8 - 0.7)
print(2 / 3)

# What Every Computer Scientist Should Know About FLoating-Point Arithmetic