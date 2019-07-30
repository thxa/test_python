class Trace:
	def __init__(self):
		self.enabled = True

	def __call__(self, f):
		def warp(*args, **kwargs):
			if self.enabled:
				print("Calling {}".format(f))
			return f(*args, **kwargs)
		return warp

n = map(ord, "The quick brown fox")

result = map(Trace()(ord), "The quick brown fox")

for item in result:
	print(item)
# print(next(result))
# print(next(result))
# print(next(result))

# map versus comprehensions
i = [str(i) for i in range(5)]
print(i)
i = map(str, range(5))
print(list(i))
