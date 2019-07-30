import inspect
import sorted_set

# from sorted_set is import itertools.chain
from sorted_set import chain

# This is like chain
def chains(*iterables):
	# result = (element for it in iterables for element in it)
	# return result
	for it in iterables:
		for element in it:
			yield element


def main():
	# Is sorted_set Moudule
	print(inspect.ismodule(sorted_set))
	
	# Get all in sorted_set Moudule
	print(inspect.getmembers(sorted_set))
	
	# Get all in inspect 
	print(dir(inspect))

	# getmember only class
	print(inspect.getmembers(sorted_set, inspect.isclass))
	
	# getmember only function of SortedSet
	print(inspect.getmembers(sorted_set.SortedSet, inspect.isfunction))
	
	# from sorted_set is import itertools.chain
	print(list(chain([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])))

	# chains like chain
	print(list(chains([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])))
	print(chains([0, 1, 2, 3, 4], [5, 6, 7, 8, 9]))

	init_sig = inspect.signature(sorted_set.SortedSet.__init__)
	print(init_sig)
	print(init_sig.parameters)
	print(repr(init_sig.parameters['items'].default))
	print(str(init_sig))
	print(inspect.signature(abs))

if __name__ == '__main__':
	main()