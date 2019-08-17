class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "{}({!r}, {!r})".format(
			self.__class__.__name__, self.x, self.y)


def main():

	v = Vector(4, 2)

	print(dir(v))
	print(v)
	print(v.x)
	print(v.y)
	
	print(v.__dict__)
	print(type(v.__dict__))
	print(v.__dict__['x'])
	print(v.__dict__['y'])
	
	# Change value x from v object
	v.__dict__['x'] = 6
	print(v.__dict__['x'])
	
	# Delete element x from v object
	del v.__dict__['x']
	print(v.__dict__)

	# Change value y from v object
	setattr(v, 'y', 4)

	print(getattr(v, 'y'))
	
	# Delete element y from v object
	delattr(v, 'y')

	print(v.__dict__)
	

if __name__ == '__main__':
	main()