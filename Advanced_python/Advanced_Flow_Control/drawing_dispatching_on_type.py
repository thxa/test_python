# https://docs.python.org/3/library/functools.html#functools.singledispatch
from functools import singledispatch

class Shape:

	def __init__(self, solid):
		self.solid = solid


class Circle(Shape):

	def __init__(self, center, radius, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.center = center
		self.radius = radius

	
	def intersects(self, shape):
		# Delegate to the generic function, swapping arguments
		return intersects_with_circle(shape, self)	


class Parallelogram(Shape):

	def __init__(self, pa, pb, pc, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.pa = pa
		self.pb = pb
		self.pc = pc


class Triangle(Shape):

	def __init__(self, pa, pb, pc, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.pa = pa
		self.pb = pb
		self.pc = pc
		


# Double Dispatch with Methods
@singledispatch
def intersects_with_circle(shape, circle):
	TypeError("I don't know to compute intersection of {!r} with {!r}".format(circle, shape))


@intersects_with_circle.register(Circle)
def _(shape, circle):
	return circle_intersects_circle(circle, shape)


@intersects_with_circle.register(Parallelogram)
def _(shape, circle):
	return circle_intersects_parallelogram(circle, shape)


@intersects_with_circle.register(Triangle)
def _(shape, circle):
	return circle_intersects_triangle(circle, shape)



# Singledispatch on Type
@singledispatch
def draw(shape):
	raise TypeError("I Can't draw shape {!r}".format(shape))


@draw.register(Circle)
def _(shape):
	print("\u25CF" if shape.solid else "\u25A1")


@draw.register(Parallelogram)
def _(shape):
	print("\u2580" if shape.solid else "\u2581")


@draw.register(Triangle)
def _(shape):
	print("\u25B2" if shape.solid else "\u25B3")


def main():
	shapes = [Circle(center=(0, 0), radius=5, solid=False),
			  Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
			  Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True)]

	for shape in shapes:
		draw(shape)

if __name__ == '__main__':
	main()