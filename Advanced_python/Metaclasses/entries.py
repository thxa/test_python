

class EntriesMeta(type):

	def __new__(mcs, name, bases, namespace, **kwargs):
		print("EntriesMeta.__new__(mcs, name, bases, namespace, **kwargs)")
		print("  kwargs = ", kwargs)
		num_entries = kwargs["num_entries"]
		print("  num_entries = ", num_entries)
		namespace.update({chr(i): i for i in range(ord('a'), ord('a') + num_entries)})
		cls = super().__new__(mcs, name, bases, namespace)
		return cls

	def __init__(cls, name, bases, namespace, **kwargs):
		super().__init__(name, bases, namespace)


class AtoZ(metaclass=EntriesMeta, num_entries=26):
	pass


print(dir(AtoZ))
print(AtoZ.a)
print(AtoZ.z)


class EntriesMeta(type):

	def __new__(mcs, name, bases, namespace, num_entries, **kwargs):
		print("EntriesMeta.__new__(mcs, name, bases, namespace, **kwargs)")
		print("  kwargs = ", kwargs)
		# num_entries = kwargs["num_entries"]
		print("  num_entries = ", num_entries)
		namespace.update({chr(i): i for i in range(ord('a'), ord('a') + num_entries)})
		cls = super().__new__(mcs, name, bases, namespace)
		return cls

	def __init__(cls, name, bases, namespace, num_entries, **kwargs):
		super().__init__(name, bases, namespace)


class AtoJ(metaclass=EntriesMeta, num_entries=10):
	pass


print(dir(AtoJ))
print(AtoJ.a)
print(AtoJ.j)

