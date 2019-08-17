import functools

def invariant(predicate):
	"""Create a class decorator which checks a class invariant.
	
	Args:
		predicate: A callable to which, after every method invocation,
			the object on which the method was called will be passed.
			The predicate should evaluate to True if the class invariant
			has been maintained, or False if it has been violated.

	Returns:
		A class decorator for checking the class invariant tested by
		the supplied predicate function.

	"""

	def invariant_checking_class_decorator(cls):
		"""A class decorator for checking invariants."""

		method_names = [name for name, attr in vars(cls).items() if callable(attr)]
		for name in method_names:
			_warp_method_with_invariant_checking_proxy(cls, name, predicate)

		property_names = [name for name, attr in vars(cls).items() if isinstance(attr, property)]
		for name in property_names:
			_warp_property_with_invariant_checking_proxy(cls, name, predicate)
		return cls
	return invariant_checking_class_decorator

def _warp_method_with_invariant_checking_proxy(cls, name, predicate):
	method = getattr(cls, name)
	assert callable(method)

	@functools.wraps(method)
	def invariant_checking_method_decorator(self, *args, **kwargs):
		result = method(self, *args, **kwargs)
		if not predicate(self):
			raise RuntimeError("Class invariant {!r} violated for {!r}".format(predicate.__doc__, self))	
		return result

	setattr(cls, name, invariant_checking_method_decorator)


class InvariantCheckingPropertyProxy:
	def __init__(self, referent, predicate):
		self._referent = referent
		self._predicate = predicate

	def __get__(self, instance, owner):
		if instance is None:
			return self
		result = self._referent.__get__(instance, owner)
		
		if not self._predicate(instance):
			raise RuntimeError("Class invariant {!r} violated for {!r}".format(
				self._predicate.__doc__, instance))	
		
		return result

	def __set__(self, instance, value):

		if instance is None:
			return self._referent
		result = self._referent.__set__(instance, value)
		
		if not self._predicate(instance):
			raise RuntimeError("Class invariant {!r} violated for {!r}".format(
				self._predicate.__doc__, instance))	
		
		return result

	def __delete__(self, instance):
		result = self._referent.__delete__(instance)

		if not self._predicate(instance):
			raise RuntimeError("Class invariant {!r} violated for {!r}".format(
				self._predicate.__doc__, instance))	
		
		return result


def _warp_property_with_invariant_checking_proxy(cls, name, predicate):
	prop = getattr(cls, name)
	invariant_checking_property = InvariantCheckingPropertyProxy(prop, predicate)

	setattr(cls, name, invariant_checking_property)

# def my_class_decorators(cls):
# 	for name, attr in vars(cls).items():
# 		print(name)
# 	return cls

def not_below_absolute_zero(temperature):
	"""Temperature not below absolute zero"""
	return temperature._kelvin >= 0 


def below_absolute_hot(temperature):
	"""Temperature below absolute hot"""
	return temperature._kelvin <= 1.416785e32 

@invariant(below_absolute_hot)
@invariant(not_below_absolute_zero)
class Temperature:

	def __init__(self, kelvin):
		self._kelvin = kelvin

	def get_kelvin(self):
		return self._kelvin

	def set_kelvin(self, value):
		self._kelvin = value

	@property
	def celsius(self):
		return self._kelvin - 273.15
	
	@celsius.setter
	def celsius(self, value):
		self._kelvin = value + 273.15

	@property
	def fahrenheit(self):
		return self._kelvin * 9/5 - 459.67

	@fahrenheit.setter
	def fahrenheit(self, value):
		self._kelvin = (value + 459.67) * 5/9


def main():
	temperature = Temperature(5.0)
	print(temperature.get_kelvin())

	temperature.set_kelvin(75)
	print(temperature.celsius)


	print(temperature.celsius)
	print(temperature.fahrenheit)
	# temperature.celsius = -100
	# print(temperature.celsius)
	# print(temperature.get_kelvin())

	temperature.set_kelvin(14e31)
	print(temperature.fahrenheit)
	print(temperature.celsius)
	# temperature.celsius = -300
	# print(temperature.get_kelvin())

if __name__ == '__main__':
	main()