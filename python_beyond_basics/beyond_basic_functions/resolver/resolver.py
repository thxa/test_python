import socket

class Resolver:
	def __init__(self):
		self._cache = {}
	# Callable instances
	def __call__(self, host):
		if host not in self._cache:
			self._cache[host] = socket.gethostbyname(host)
		return self._cache[host]
	
	def clear(self):
		self._cache.clear()

	def has_host(self, host):
		return host in self._cache


def sequence_class(immutable):
	cls = tuple if immutable else list
	return cls

# Classes Are Callable
print(callable(Resolver))

# seq_t = sequence_class(immutable=True)
# seq_l = sequence_class(immutable=False)
# print(seq_t("hello"))
# print(seq_l("hello"))

# Lambdas
firestname = lambda x: x.split()[-1]
sorted(arg1, key=, reverse=False)
sequer = lambda x: x ** x
print(sequer(2))

# Extended Formal Argument Syntax 
def print_args(arg1, *args, **kwargs):
	print(arg1)
	print(args)
	print(kwargs)

a = (1, 2, 3, 4, 5)
k = {"red": 54, "green": 55, "blue": 231}

# Extended Call Syntax 
print_args(*a, **k)

print("-" * 35)
def color(red, green, blue, **kwargs):
	print("red = %s" % red)
	print("green = %s" % green)
	print("blue = %s" % blue)

color(**k)
print(dict(k))

# Forwarding Arguments
def trace(f, *args, **kwargs):
	print("args = %s" %args)
	print("kwargs = %s" %kwargs)
	result = f(*args, **kwargs)
	print("result = %s" %result)
	return result

print(int('ff', base=16))

trace(int, 'ff', base=16)


# Transposing Tables
sunday 	= [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday 	= [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

daily = [sunday, monday, tuesday]
for item in zip(*daily):
	print(item)

# tersported
transposed = list(zip(*daily))
print(transposed)