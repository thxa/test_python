
def modulus_three(n):
	r = n % 3
	if r == 0:
		print("Multiple of 3")
	elif r == 1:
		print("Remainder 1")
	else: # r == 2
		assert r == 2, "Remainder is not 2"
		print("Remainder 2")


def modulus_four(n):
	r = n % 4
	if r == 0:
		print("Multiple of 4")
	
	elif r == 1:
		print("Remainder 1")

	elif r == 2:
		print("Remainder 2")

	elif r == 3:
		print("Remainder 3")

	else: # r == 2
		assert False, "This should never happen"
		print("Remainder 2")


def main():
	modulus_three(1)
	modulus_three(2)
	modulus_three(3)

	modulus_four(1)
	modulus_four(2)
	modulus_four(3)
	modulus_four(4)


if __name__ == '__main__':
	main()