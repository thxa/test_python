class ExampleIterator(object):

	def __init__(self, data):
		self.index = 0
		self.data = data

	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.data):
			raise StopIteration()

		rslt = self.data[self.index]
		self.index += 1
		return rslt

# items = ExampleIterator()
# print(next(items))
# print(next(items))
# print(next(items))

# for item in ExampleIterator():
# 	print(item)


class ExampleIterable(object):
	def __init__(self):
		self.data = [1, 2, 3]

	def  __iter__(self):
		return ExampleIterator(self.data)


for item in ExampleIterable():
	print(item)

print([i * 3 for i in ExampleIterable()])