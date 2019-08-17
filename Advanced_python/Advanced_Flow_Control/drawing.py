

class Shape:

	def __init__(self, solid):
		self.solid = solid


class Circle(Shape):

	def __init__(self, center, radius, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.center = center
		self.radius = radius

	def draw(self):
		print("\u25CF" if self.solid else "\u25A1")


class Parallelogram(Shape):

	def __init__(self, pa, pb, pc, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.pa = pa
		self.pb = pb
		self.pc = pc

	def draw(self):
		print("\u2580" if self.solid else "\u2581")



class Triangle(Shape):

	def __init__(self, pa, pb, pc, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.pa = pa
		self.pb = pb
		self.pc = pc
		
	def draw(self):
		print("\u25B2" if self.solid else "\u25B3")



def draw_circle(shape):
	print("\u25CF" if shape.solid else "\u25A1")

def draw_parallelogram(shape):
	print("\u2580" if shape.solid else "\u2581")

def draw_triangle(shape):
	print("\u25B2" if shape.solid else "\u25B3")

# def draw(shape):
# 	if isinstance(shape, Circle):
# 		draw_circle(shape)
	
# 	elif isinstance(shape, Parallelogram):
# 		draw_parallelogram(shape)

# 	elif isinstance(shape, Triangle):
# 		draw_triangle(shape)

# 	else:
# 		raise TypeError("I Can't draw shape {!r}".format(shape))

def draw(shape):
	drawers = {
		Circle: draw_circle,
		Parallelogram: draw_parallelogram,
		Triangle: draw_triangle,
	}

	try:
		drawer = drawers[type(shape)]
	except KeyError as e:
		raise TypeError("I Can't draw shape") from e
	else:
		drawer(shape)

def main():
	shapes = [Circle(center=(0, 0), radius=5, solid=False),
			  Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
			  Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True)]

	for shape in shapes:
		shape.draw()
		draw(shape)

if __name__ == '__main__':
	main()