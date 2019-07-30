# https://docs.python.org/3/library/functions.html#complex
print(2j)

print(3 + 4j)
print(type(3 + 4j))

print(complex(3))
print(complex(-2, 3))
print(complex('(-2+3j)'))
print(complex('-2+3j'))
# print(complex('-2 + 3j'))
c = 3 + 5j
print(c)
print(c.real)
print(c.imag)
print(c.conjugate())

# https://docs.python.org/3/library/math.html
import math
# print(math.sqrt(-1))


# https://docs.python.org/3/library/cmath.html
import cmath
print(cmath.sqrt(-1))

print(cmath.phase(1+1j))

# https://docs.python.org/3/library/functions.html#abs
print(abs(1+1j))

print(cmath.polar(1+1j))

modulus, phase = cmath.polar(1+1j)
print(modulus)
print(phase)

print(cmath.rect(modulus, phase))

def inductive(ohms):
	return complex(0.0, ohms)

def capacitive(ohms):
	return complex(0.0, -ohms)

def resistive(ohms):
	return complex(ohms)

def impedance(components):
	z = sum(components)
	return z

complex_impedance_plane =  impedance([inductive(10), resistive(10), capacitive(5)])
print(complex_impedance_plane)

phase = cmath.phase(complex_impedance_plane)
print(phase)
print(math.degrees(phase))