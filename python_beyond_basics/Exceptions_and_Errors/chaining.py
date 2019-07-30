import math

# https://docs.python.org/3/library/traceback.html
import traceback


class inclinationError(Exception):
	pass


def inclination(dx, dy):
	try:
		return math.degrees(math.atan(dy / dx))
	except ZeroDivisionError as e:
		raise inclinationError("Slop cannot be vertical") from e


def main():
	try:
		inclination(3, 5)
		inclination(0, 5)
	except inclinationError as e:
		print(e)
		# print(e.__context__)
		print(e.__cause__)
		print(e.__traceback__)
		traceback.print_tb(e.__traceback__)
		s = traceback.format_tb(e.__traceback__)
		print(s)



if __name__ == '__main__':
	main()
	print("Finished")