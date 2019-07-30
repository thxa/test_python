def median(iterable):
	"""Obtain the central value of a series

	Sorts the iterable and returns the middle value if there is an even
	number of elements, or the arithmetic mean of the middle two elements
	if there is an even number of elements.

	Args:
		iterable: A series of orderable items.
	
	Returns:
		The median value.
	"""
	
	items = sorted(iterable)
	median_index = ((len(items) - 1 ) // 2)
	if len(items) == 0:
		raise ValueError("median() arg is empty sequence")
	if len(items) %	2 != 0:
		return items[median_index]
	return (items[median_index] + items[median_index + 1]) / 2.0


def main():
	try:
		print(median([5, 2, 1, 4, 3]))
		print(median([5, 2, 1, 4, 3, 6]))
		print(median([]))
	
	except ValueError as e:
		print("Payload:", e.args)
		print(str(e))

	
if __name__ == '__main__':
	main()