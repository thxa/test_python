# Decorator
def escape_unicode(f):
	def warp(*args, **kwargs):
		x = f(*args, **kwargs)
		return ascii(x)
	return warp

@escape_unicode # Decorator
def nother_test():
	return "hello"

# What Can Be a Decorator
class CallCount:
	def __init__(self, f):
		self.f = f
		self.count = 0

	def __call__(self, *args, **kwargs):
		self.count += 1
		return self.f(*args, *kwargs)

@CallCount
def hello(name):
	return f"hello {name}"

# Instances as Decorators
class Trace:
	def __init__(self):
		self.enabled = True

	def __call__(self, f):
		def warp(*args, **kwargs):
			if self.enabled:
				print("Calling {}".format(f))
			return f(*args, **kwargs)
		return warp

tracer = Trace()

@tracer
def rotate_list(l):
	return l[1:] + [l[0]]

# Multiple Decorators
@tracer
@escape_unicode
def make_char_emoji_like(name):
	return name + "👌"

#Decorator method
class IslandMaker:
	def __init__(self, suffix):
		self.suffix = suffix

	@tracer
	def make_island(self, name):
		return name + self.suffix

# functools.wraps()
import functools

def noop(f):
	@functools.wraps(f)	
	def noop_warapper(*args, **kwargs):
		return f(*args, **kwargs)
	# noop_warapper.__name__ = f.__name__
	# noop_warapper.__doc__ = f.__doc__
	return noop_warapper

@noop
def hello(name):
	"Print a well-known message."
	print(f"hello {name}")

print(hello.__name__)
print(hello.__doc__)

# validatoring Arguments
def check_non_negative(index):
	def validator(f):
		def wrap(*args):
			if args[index] < 0:
				raise ValueError(
					f"Argument {index} must be non-negative.")
			return f(*args)
		return wrap
	return validator

@tracer
@check_non_negative(1)
def create_list(value, size):
	return [value] * size

print(create_list("hello", 1))