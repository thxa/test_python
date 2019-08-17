# https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary
from weakref import WeakKeyDictionary

# https://app.pluralsight.com/player?course=advanced-python&author=robert-smallshire&name=advanced-python-m4&clip=2&mode=live
class Postive:
	def __init__(self):
		self._instance_data = WeakKeyDictionary()
	
	# Descriptor Protocol
	def __get__(self, instance, owner):
		if instance is None:
			return self
		return self._instance_data[instance]

	def __set__(self, instance, value):
		if value <= 0:
			raise ValueError("Value {} is not positive.".format(value))
		self._instance_data[instance] = value

	def __delete__(self, instance):
		raise AttributeError("Cannot delete attribute")


class Planet:

	def __init__(self, 
				 name,
				 radius_metres,
				 mass_kilograms,
				 orbital_period_seconds,
				 surface_temperature_kelvin):
		self.name = name
		self.radius_metres = radius_metres
		self.mass_kilograms = mass_kilograms
		self.orbital_period_seconds = orbital_period_seconds
		self.surface_temperature_kelvin = surface_temperature_kelvin

	
	def _get_name(self):
		return self._name


	def _set_name(self, value):
		if not value:
			raise ValueError("Cannot set empty Planet.name")
		self._name = value

	name = property(fget=_get_name, fset=_set_name)

	radius_metres = Postive()
	mass_kilograms = Postive()
	orbital_period_seconds = Postive()
	surface_temperature_kelvin = Postive()


def main():
	pluto = Planet(name="pluto",
				   radius_metres=1184e3, 
				   mass_kilograms=1.305e22, 
				   orbital_period_seconds=7816012992, 
				   surface_temperature_kelvin=55)

	mercury = Planet(name="Mercury",
				   radius_metres=2439e3, 
				   mass_kilograms=3.3022e23, 
				   orbital_period_seconds=7.60052e6, 
				   surface_temperature_kelvin=340)

	venus = Planet(name="Venus",
				   radius_metres=6051.8e3, 
				   mass_kilograms=4.8676e24, 
				   orbital_period_seconds=1.94142e7, 
				   surface_temperature_kelvin=737)

	earth = Planet(name="Earth",
				   radius_metres=6371.0e3, 
				   mass_kilograms=5.972e24, 
				   orbital_period_seconds=3.15581e7, 
				   surface_temperature_kelvin=288)


	mars = Planet(name="Mars",
				   radius_metres=3389.0e3, 
				   mass_kilograms=6.4185e23, 
				   orbital_period_seconds=5.93543e7, 
				   surface_temperature_kelvin=210)

	print(Planet.radius_metres)
	# return pluto, mercury, venus, earth, mars
	print(pluto.radius_metres)
	m = pluto.mass_kilograms
	print(m)
	# m = Postive.__get__(Postive, pluto, Planet)
	# pluto.radius_metres = -1000

	# planet_x = Planet(name="X", radius_metres=10e3, mass_kilograms=0, orbital_period_seconds=-7293234, surface_temperature_kelvin=-5)



if __name__ == '__main__':
	main()