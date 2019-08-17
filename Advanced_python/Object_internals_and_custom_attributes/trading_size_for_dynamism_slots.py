import sys

class Resistor:
	# https://docs.python.org/3/reference/datamodel.html#notes-on-using-slots
	__slots__ = ["resistance_ohms", "tolerance_percent", "power_watts"]

	def __init__(self, resistance_ohms, tolerance_percent, power_watts):
		self.resistance_ohms = resistance_ohms
		self.tolerance_percent = tolerance_percent
		self.power_watts = power_watts


def main():
	r10 = Resistor(10, 5, 0.25)
	
	print(sys.getsizeof(r10))

	# print(sys.getsizeof(r10) + sys.getsizeof(r10.__dict__))

	# r10.cost_dollars = 0.02
	# print(sys.getsizeof(r10) + sys.getsizeof(r10.__dict__))

	d = {}
	print(sys.getsizeof(d))


if __name__ == '__main__':
	main()
