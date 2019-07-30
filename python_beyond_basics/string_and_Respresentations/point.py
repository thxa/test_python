class Point2D(object):
	"""docstring for Point2D"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "({}, {})".format(self.x, self.y)

	def __repr__(self):
		return "Point2D(x={}, y={})".format(self.x, self.y)

	def __format__(self, f):
		if f == "r":
			return '{}, {}'.format(self.y, self.x, f)
		else:
			return '{}, {}'.format(self.x, self.y)


class Point3D(Point2D):
	"""docstring for Point3D"""
	def __init__(self, x, y, z):
		super().__init__(x, y)
		self.z = z

	def __str__(self):
		return "({}, {}, {})".format(self.x, self.y, self.z)

	def __repr__(self):
		return "Point3D(x={}, y={}, z={})".format(self.x, self.y, self.z)

	def __format__(self, f):
		if f == "r":
			return '{}, {}, {}'.format(self.z, self.y, self.x, f)
		else:
			return '{}, {}, {}'.format(self.x, self.y, self.z)


# Test str, repr, format
# https://app.pluralsight.com/player?course=python-beyond-basics&author=austin-bingham&name=python-beyond-basics-m05&clip=4&mode=live
# print(help(str))
# print(help(repr))
# print(help(format))

p2 = Point2D(5, 4)
p3 = Point3D(5, 4, 3)

marge = [p2, p3]

for p in marge:
	print()
	print("This is str:", str(p)) # str
	print("This is repr", repr(p)) # repr
	print("This is format", "{}".format(p)) # str
	print("This is format r", "{:r}".format(p)) # str
	print("This is format not r", "{!r}".format(p)) # repr
	print("This is format not s", "{!s}".format(p)) # str

# import reprlib
# points = [Point2D(x, y) for x in range(1000) for y in range(1000)]
# print(len(points))
# # print(points) # print all points
# print(reprlib.repr(points)) # print something in points

print(ascii("ثامر"))
print(ord('ث'))
print(chr(ord('ث')))