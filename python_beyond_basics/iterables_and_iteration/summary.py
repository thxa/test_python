# from pprint import pprint as pp

# for loop short list
items = [(x, y) for y in range(10) for x in range(y)]
print(items)
# pp(items)

# for loop normal list
items = []
for y in range(10):
	for x in range(y):
		items.append((x, y))
print()
print(items)
# pp(items)

print()
# for loop short  double list
items = [[(x, y) for x in range(y + 1)] for y in range(10)]
print(items)

# for loop normal double list
items = []
for y in range(10):
	values = []
	for x in range(y + 1):
		values.append((x, y))
	items.append(values)
print()
print(items)


print()
# for loop short list and if 
items = [x / (x - y) 
		for x in range(52) 
		if x > 50
		for y in range(x)
		if x - y != 0]
print(items)
# for loop normal and if
items = []
for x in range(52):
	if x > 50:
		for y in range(x):
			if x - y != 0:
				items.append(x / (x - y))
print()
print(items)

# map(item_transforming_funcion, iterable1, iterable2) function
print()

i = [str(i) for i in range(5)]
print(i)
i = map(str, range(5))
print(list(i))

print()
print(list(map(chr, range(100))))

print()
list_number_of_char = list(map(ord, "Hello World"))
print(list_number_of_char)

print()
print(list(map(chr, list_number_of_char)))

# filter(predicate_function, iterable) function
print()
print(list(filter(lambda n: n > 0, [1, -2, 4, -5, 6, -3, -2, 0])))

print()

import functools

def add(n1, n2):
	return n1 + n2

# reduce(function, iterable, initializer)
print(functools.reduce(add, [1, 2, 3, 4, 5]))

print()
# iterable Protocol
numbers = iter(range(10))
numbers = range(10).__iter__()

# iterator Protocol
print(next(numbers))
print(numbers.__next__())

