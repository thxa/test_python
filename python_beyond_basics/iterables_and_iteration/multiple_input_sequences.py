sizes = ["small", "medium", "large"]
colors = ["lavender", "teal", "burnt orange"]
animals = ["cat", "dog", "cmale"]

def combine(size, color, animal):
	return "{} {} {}".format(size, color, animal)

print(list(map(combine, sizes, colors, animals)))


import itertools
def combine(quantity, size, color, animal):
	return "{} x {} {} {}".format(quantity, size, color, animal)

print(list(map(combine, itertools.count(), sizes, colors, animals)))
