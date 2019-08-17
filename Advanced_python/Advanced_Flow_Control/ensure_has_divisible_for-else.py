# https://docs.python.org/3/tutorial/controlflow.html
# with for-else
def for_else(item, divisor):
	for item in items:
		if item % divisor == 0:
			found = item
			break
	else: # No break
		items.append(divisor)
		found = divisor
	return found

# without for-else
def ensure_has_divisible(items, divisor):
	for item in items:
		if item % divisor == 0:
			return item

	items.append(divisor)
	return divisor 

def main():
	items = [2, 36, 25, 9]
	divisor = 12

	# found = for_else(items, divisor)
	found = ensure_has_divisible(items, divisor)
	print("{items} contains {found} which is a multiple of {divisor}".format(**locals()))


if __name__ == '__main__':
	main()