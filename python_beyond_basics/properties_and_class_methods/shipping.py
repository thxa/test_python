import iso6346
class ShippingContainer(object):
	
	HEIGHT_FT = 8.5
	WIDTH_FT = 8.0

	next_serial = 1337 # class Attributes
	
	# @staticmethod
	# def _get_next_serial():
	# 	result =  ShippingContainer.next_serial # or self.next_serial
	# 	ShippingContainer.next_serial += 1
	# 	return result
	@staticmethod
	def _make_bic_code(owner_code, serial):
		return iso6346.create(owner_code=owner_code,
							  serial=str(serial).zfill(6))
	
	@classmethod
	def _get_next_serial(cls):
		result = cls.next_serial # or self.next_serial
		cls.next_serial += 1
		return result

	@classmethod
	def create_empty(cls, owner_code, length_ft, *args, **kwargs):
		return cls(owner_code, length_ft, contents=None, *args, **kwargs)

	@classmethod
	def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
		return cls(owner_code, length_ft, contents=list(items), *args, **kwargs)

	def __init__(self, owner_code, length_ft, contents):
		self.owner_code = owner_code
		self.length_ft = length_ft
		self.contents = contents
		self.bic = self._make_bic_code(owner_code=owner_code,
									   serial=ShippingContainer._get_next_serial())

	def _calc_volume(self):
		return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


	@property
	def volume_ft3(self):
		self._calc_volume()

class RefrigeratedShippingContainer(ShippingContainer):
	
	MAX_CELSIUS = 4.0
	FRIDGE_VOLUME_FT3 = 100

	@staticmethod
	def _make_bic_code(owner_code, serial):
		return iso6346.create(owner_code=owner_code,
							  serial=str(serial).zfill(6),
							  category="R")

	@staticmethod
	def  _c_to_f(celsius):
		return celsius * 9 / 5 + 32

	@staticmethod
	def  _f_to_c(fahrenheit):
		return (fahrenheit - 32) * 5 / 9
		
	def __init__(self, owner_code, length_ft, contents, celsius):
		super().__init__(owner_code, length_ft, contents)
		self.celsius = celsius

	@property
	def celsius(self):
		return self._celsius

	def _set_celsius(self, value):
		if value > RefrigeratedShippingContainer.MAX_CELSIUS:
			raise ValueError("Temperature too hot!")
		self._celsius = value
	
	@celsius.setter
	def celsius(self, value):
		self._set_celsius(value)

	@property
	def fahrenheit(self):
		return RefrigeratedShippingContainer._c_to_f(self.celsius)

	@fahrenheit.setter
	def fahrenheit(self, value):
		self.celsius = RefrigeratedShippingContainer._f_to_c(value)

	def _calc_volume(self):
		return super()._calc_volume - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3

	# @property
	# def volume_ft3(self):
	# 	return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

	MIN_CELSIUS = -20.0

	# @RefrigeratedShippingContainer.celsius.setter
	def celsius(self, value):
		if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
			raise ValueError("Temperature too cold!")
		super()._set_celsius(value)
		# super().celsius = value <- Error
		# RefrigeratedShippingContainer.celsius.fset(self, value)

"""
@property 
	property.fget(self): getting the atterbute
	property.fset(self, value): set atterbute
	@<nameattr>.setter
"""