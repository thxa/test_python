# https://docs.python.org/3/library/inspect.html
# https://github.com/python/cpython/blob/3.7/Lib/inspect.py source code
import inspect
from sorted_set import SortedSet

# https://docs.python.org/3/library/reprlib.html
# https://github.com/python/cpython/blob/3.7/Lib/reprlib.py
import reprlib

# https://docs.python.org/3/library/itertools.html 
import itertools

def full_sig(method):
	try:
		return "%s%s" %(method.__name__, inspect.signature(method))
	except ValueError:
		return method.__name__ + "(...)"

def brief_doc(obj):
	doc = obj.__doc__
	if doc is not None:
		lines = doc.splitlines()
		if len(lines) > 0:
			return lines[0]
	return ''

def print_table(rows_of_columns, *headers):
	num_columns = len(rows_of_columns[0])
	num_headers = len(headers)

	if num_headers != num_columns:
		raise TypeError("Exected {} header arguments, "
						"got {}".format(num_columns, num_headers))
	
	rows_of_columns_with_header = itertools.chain([headers], rows_of_columns)
	columns_of_rows = list(zip(*rows_of_columns_with_header))
	column_widths = [max(map(len, column)) for column in columns_of_rows]
	column_specs = ("{{:{w}}}".format(w=width) for width in column_widths)
	format_spec = ' '.join(column_specs)
	print(format_spec.format(*headers))
	rules = ('-' * width for width in column_widths)
	print(format_spec.format(*rules))
	for row in rows_of_columns:
		print(format_spec.format(*row))

def dump(obj):
	print("Type")
	print('=' * 4)
	print(type(obj))
	print()

	print("Documentation")
	print('=' * 13)
	print(inspect.getdoc(obj))
	print()

	print("Attributes")
	print('=' * 10)
	all_attr_names = SortedSet(dir(obj))
	method_names = SortedSet(
		filter(lambda attr_name: callable(getattr(obj, attr_name)),
			   all_attr_names))
	assert method_names <= all_attr_names
	attr_names = all_attr_names - method_names
	attr_names_and_values = [(name, reprlib.repr(getattr(obj, name)))
							 for name in attr_names]
	print_table(attr_names_and_values, "Name", "Value")
	print()

	print("Methods")
	print('=' * 7)
	# print(method_names)
	methods = (getattr(obj, method_name) for method_name in method_names)
	# print(list(methods)[0].__name__)
	method_names_and_doc = [(full_sig(method), brief_doc(method)) for method in methods]
	print_table(method_names_and_doc, "Name", "Description")
	print()