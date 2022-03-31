class Car:

	def __init__(self,brand, model, engine, capacity, year, version, isdamaged, isfailure):
		self.brand = brand
		self.model = model
		self.engine = engine
		self.capacity = capacity
		self.year = year
		self.version = version
		self.isdamaged = isdamaged
		self.isfailure = isfailure


	def isdamaged(self):
		return not(self.isdamaged and self.isfailure)


car_01 = Car('VW', 'Passat', 'diesel', '1896', ' 2001','Variant', True, False)
car_02 = Car('Toyota', 'Paseo', 'petrol', '1497', '1997', 'Convertible', False, False)
car_03 = Car('Audi', 'A3', 'petrol','1598', '2001', 'hatchback', False, False)

print(car_01.brand,car_01.model,car_01.engine,car_01.capacity,car_01.year,car_01.version)
print(car_02.brand,car_02.model,car_02.engine,car_02.capacity,car_02.year,car_02.version)

print(car_01)
print(car_02)

