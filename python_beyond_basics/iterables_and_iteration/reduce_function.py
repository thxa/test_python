from functools import reduce
import operator

print(reduce(operator.add, [1, 2, 3, 4, 5]))

numbers = [1, 2, 3, 4, 5]
accumuator = operator.add(numbers[0], numbers[1])

for item in numbers[2:]:
	accumuator = operator.add(accumuator, item)

print(accumuator)

def mul(x, y):
	print("mul {} {}".format(x, y))
	return x * y

print(reduce(mul, range(1, 10)))

# print(reduce(mul, [])) Error this is empty
# print(reduce(mul, [1]))

values = [1, 2, 3]
print(reduce(operator.add, values, 0))

values = []
print(reduce(operator.add, values, 0))

values = [1, 2, 3]
print(reduce(operator.mul, values, 1))
print(reduce(operator.add, values, 0))

