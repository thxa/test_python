# def sign(x):
# 	if x < 0:
# 		return -1
# 	elif x > 0:
# 		return 1
# 	return 0

# print(sign(5))
# print(sign(-5))
# print(sign(0))

# print(False - False)
# print(False - True)
# print(True - False)
# print(True - True)
from fractions import Fraction
import bmp

def sign(x):
	return (x > 0) - (x < 0)

# print(sign(5))
# print(sign(-5))
# print(sign(0))

def orientation(p, q, r):
	p = (Fraction(p[0]), Fraction(p[1]))
	q = (Fraction(q[0]), Fraction(q[1]))
	r = (Fraction(r[0]), Fraction(r[1]))

	d = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
	return sign(d)

a = (0, 0)
b = (4, 0)
c = (4, 3)
d = (8, 6)
e = (0.5, 0.5)
f = (12.0, 12.0)
g = (24.0, 24.0)

print(orientation(a, b, c))
print(orientation(a, c, b))
print(orientation(a, c, d))
print(orientation(e, f, g))

# e = (0.5, 0.5000000000000018)
# print(orientation(e, f, g))
# e = (0.5, 0.5000000000000019)
# print(orientation(e, f, g))
# e = (0.5, 0.5000000000000044)
# print(orientation(e, f, g))
# e = (0.5, 0.5000000000000046)
# print(orientation(e, f, g))

def main():
	px = 0.5

	pys = [	0.4999999999999999,
			0.4999999999999999006,
			0.499999999999999901,
			0.499999999999999902,
			0.4999999999999999023,
			0.499999999999999903,
			0.4999999999999999034,
			0.499999999999999904,
			0.4999999999999999045,
			0.499999999999999905,
			0.4999999999999999056,
			0.499999999999999906,
			0.499999999999999907,
			0.499999999999999908,
			0.499999999999999909,
			0.499999999999999910,
			0.499999999999999911,
			0.499999999999999912,
			0.499999999999999913,
			0.499999999999999914,
			0.499999999999999915,
			0.499999999999999916,
			0.499999999999999917,
			0.499999999999999918,
			0.499999999999999919,
			0.499999999999999920,
			0.499999999999999921,
			0.499999999999999922,
			0.499999999999999923,
			0.499999999999999924,
			0.499999999999999925,
			0.499999999999999926,
			0.499999999999999927,
			0.499999999999999928,
			0.499999999999999929,
			0.499999999999999930,
			0.499999999999999931,
			0.499999999999999932,
			0.499999999999999933,
			0.499999999999999934,
			0.499999999999999935,
			0.499999999999999936,
			0.499999999999999937,
			0.499999999999999938,
			0.499999999999999939,
			0.49999999999999994,
			0.499999999999999950,
			0.499999999999999951,
			0.499999999999999952,
			0.499999999999999953,
			0.499999999999999954,
			0.499999999999999955,
			0.499999999999999956,
			0.499999999999999957,
			0.499999999999999958,
			0.499999999999999959,
			0.499999999999999960,
			0.499999999999999961,
			0.499999999999999962,
			0.499999999999999963,
			0.499999999999999964,
			0.499999999999999965,
			0.499999999999999966,
			0.499999999999999967,
			0.499999999999999968,
			0.499999999999999969,
			0.499999999999999970,
			0.499999999999999971,
			0.499999999999999972,
			0.499999999999999973,
			0.499999999999999974,
			0.499999999999999975,
			0.499999999999999976,
			0.499999999999999977,
			0.499999999999999978,
			0.499999999999999979,
			0.499999999999999980,
			0.499999999999999981,
			0.499999999999999982,
			0.499999999999999983,
			0.499999999999999984,
			0.499999999999999985,
			0.499999999999999986,
			0.499999999999999987,
			0.499999999999999988,
			0.499999999999999989,
			0.499999999999999990,
			0.499999999999999991,
			0.499999999999999992,
			0.499999999999999993,
			0.499999999999999994,
			0.499999999999999995,
			0.499999999999999996,
			0.499999999999999997,
			0.499999999999999998,
			0.499999999999999999,
			0.500000000000000000,
			0.500000000000000001,
			0.500000000000000002,
			0.500000000000000003,
			0.500000000000000004,
			0.500000000000000005,
			0.500000000000000006,
			0.500000000000000007,
			0.500000000000000008,
			0.500000000000000009,
			0.500000000000000010,
			0.500000000000000011,
			0.500000000000000012,
			0.500000000000000013,
			0.500000000000000014,
			0.500000000000000015,
			0.500000000000000016,
			0.500000000000000017,
			0.500000000000000018,
			0.500000000000000019,
			0.500000000000000020,
			0.500000000000000021,
			0.500000000000000022,
			0.500000000000000023,
			0.500000000000000024,
			0.500000000000000025,
			0.500000000000000026,
			0.500000000000000027,
			0.500000000000000028,
			0.500000000000000029,
			0.500000000000000030,
			0.500000000000000031,
			0.500000000000000032,
			0.500000000000000033,
			0.500000000000000034,
			0.500000000000000035,
			0.500000000000000036,
			0.500000000000000037,
			0.500000000000000038,
			0.500000000000000039,
			0.500000000000000040,
			0.500000000000000041,
			0.500000000000000042,
			0.500000000000000043,
			0.500000000000000044,
			0.500000000000000045,
			0.500000000000000046,
			0.500000000000000047,
			0.500000000000000048,
			0.500000000000000049,
			0.500000000000000050,
			0.500000000000000051,
			0.500000000000000052,
			0.500000000000000053,
			0.500000000000000054,
			0.500000000000000055,
			0.500000000000000056,
			0.500000000000000057,
			0.500000000000000058,
			0.500000000000000059,
			0.500000000000000060,
			0.500000000000000061,
			0.500000000000000062,
			0.500000000000000063,
			0.500000000000000064,
			0.500000000000000065,
			0.500000000000000066,
			0.500000000000000067,
			0.500000000000000068,
			0.500000000000000069,
			0.500000000000000070,
			0.500000000000000071,
			0.500000000000000072,
			0.500000000000000073,
			0.500000000000000074,
			0.500000000000000075,
			0.500000000000000076,
			0.500000000000000077,
			0.500000000000000078,
			0.500000000000000079,
			0.500000000000000080,
			0.500000000000000081,
			0.500000000000000082,
			0.500000000000000083,
			0.500000000000000084,
			0.500000000000000085,
			0.500000000000000086,
			0.500000000000000087,
			0.500000000000000088,
			0.500000000000000089,
			0.500000000000000090,
			0.500000000000000091,
			0.500000000000000092,
			0.500000000000000093,
			0.500000000000000094,
			0.500000000000000095,
			0.500000000000000096,
			0.500000000000000097,
			0.500000000000000098,
			0.500000000000000099,
			0.500000000000000100,
			0.500000000000000101,
			0.500000000000000102,
			0.500000000000000103,
			0.500000000000000104,
			0.500000000000000105]

	q = (12.0, 12.0)
	r = (24.0, 24.0)

	# for py in pys:
	# 	p = (px, py)
	# 	o =  orientation(p, q, r)
	# 	print("orientation({p[0]:>3}, {p[1]:<19} q, r) -> {o:>2}".format(p=p, o=o))

	color = {-1: 0, 0: 127, +1: 255}

	pixels = [[color[orientation((px, py), q, r)] for px in pys] for py in reversed(pys)]
	bmp.write_grayscale('above_below_float.bmp', pixels)
	
if __name__ == '__main__':
	main()