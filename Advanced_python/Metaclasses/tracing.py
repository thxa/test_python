
# https://docs.python.org/3/reference/datamodel.html#metaclasses

class TracingMeta(type):

	# https://docs.python.org/3/reference/datamodel.html#preparing-the-class-namespace
	@classmethod
	def __prepare__(mcs, name, bases, **kwargs):
		print("TracingMeta.__prepare__(name, bases, **kwargs)")
		print("  mcs = ", mcs)
		print("  name = ", name)
		print("  bases = ", bases)
		print("  kwargs = ", kwargs)
		namespace = super().__prepare__(name, bases)
		print("<-- namespace = ", namespace)
		print()
		return namespace

	def __new__(mcs, name, bases, namespace, **kwargs):
		print("TracingMeta.__new__(name, bases, namespace, **kwargs)")
		print("  mcs = ", mcs)
		print("  name = ", name)
		print("  bases = ", bases)
		print("  namespace = ", namespace)
		print("  kwargs = ", kwargs)
		cls = super().__new__(mcs, name, bases, namespace)
		print("<-- cls = ", cls)
		print()
		return cls

	def __init__(cls, name, bases, namespace, **kwargs):
		print("TracingMeta.__init__(cls, name, bases, namespace, **kwargs)")
		print("  cls = ", cls)
		print("  name = ", name)
		print("  bases = ", bases)
		print("  namespace = ", namespace)
		print("  kwargs = ", kwargs)
		super().__init__(name, bases, namespace)
		print()

	def metamethod(cls):
		print("TracingMeta.metamethod(cls)")
		print("  cls = ", cls)
		print()

	def __call__(cls, *args, **kwargs):
		print("TracingMeta.__call__(cls, *args, **kwargs)")
		print("  cls = ", cls)
		print("  args = ", args)
		print("  kwargs = ", kwargs)
		print("  About to call type.__call__()")
		obj = super().__call__(*args, **kwargs)
		print("  Returned from type.__call__()")
		print("<-- obj = ", obj)
		print()
		return obj



# class TracingClass(metaclass=TracingMeta):

# 	def __new__(cls, *args, **kwargs):
# 		print("TracingClass.__new__(cls, *args, **kwargs)")
# 		print("  cls = ", cls)
# 		print("  args = ", args)
# 		print("  kwargs = ", kwargs)
# 		obj = super().__new__(cls)
# 		print("<-- cls = ", cls)
# 		print()
# 		return obj

# 	def __init__(self, *args, **kwargs):
# 		print("TracingClass.__init__(self, *args, **kwargs)")
# 		print("  self = ", self)
# 		print("  args = ", args)
# 		print("  kwargs = ", kwargs)
# 		print()


# t = TracingClass(42, keyword="clef")

# class Widget(metaclass=TracingMeta):
# 	def action(message):
# 		print(message)
# 	the_answer = 42


# print("Has Widget metamethod?", hasattr(Widget, "metamethod"))
# Widget.metamethod()

# w = Widget()
# print("Has Widget metamethod?", hasattr(w, "metamethod"))


# class Reticulate(metaclass=TracingMeta, tension=496):

# 	def reticulate(self, spline):
# 		print(spline)
# 	cubic = True