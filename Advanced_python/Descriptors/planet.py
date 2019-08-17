

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

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		if not value:
			raise ValueError("Cannot set empty Planet.name")
		self._name = value

	@property
	def radius_metres(self):
		return self._radius_metres

	@radius_metres.setter
	def radius_metres(self, value):
		if value <= 0:
			raise ValueError("radius_metres value {} is not positive.".format(value))
		self._radius_metres = value

	@property
	def mass_kilograms(self):
		return self._mass_kilograms

	@mass_kilograms.setter
	def mass_kilograms(self, value):
		if value <= 0:
			raise ValueError("mass_kilograms value {} is not positive.".format(value))
		self._mass_kilograms = value

	@property
	def orbital_period_seconds(self):
		return self._orbital_period_seconds

	@orbital_period_seconds.setter
	def orbital_period_seconds(self, value):
		if value <= 0:
			raise ValueError("orbital_period_seconds value {} is not positive.".format(value))
		self._orbital_period_seconds = value

	@property
	def surface_temperature_kelvin(self):
		return self._surface_temperature_kelvin

	@surface_temperature_kelvin.setter
	def surface_temperature_kelvin(self, value):
		if value <= 0:
			raise ValueError("surface_temperature_kelvin value {} is not positive.".format(value))
		self._surface_temperature_kelvin = value


def main():
	pluto = Planet(name="pluto", radius_metres=1184e3, mass_kilograms=1.305e22, orbital_period_seconds=7816012992, surface_temperature_kelvin=55)
	print(pluto.radius_metres)
	pluto.radius_metres = -1000

	planet_x = Planet(name="X", radius_metres=10e3, mass_kilograms=0, orbital_period_seconds=-7293234, surface_temperature_kelvin=-5)



if __name__ == '__main__':
	main()