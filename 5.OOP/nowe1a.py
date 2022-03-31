class Car:

	def __init__(self, brand, model, engine, capacity, year, version, isMechanicOK, isPaintOK):
		self.brand = brand
		self.model = model
		self.engine = engine
		self.capacity = capacity
		self.year = year
		self.version = version
		self.isMechanicOK = isMechanicOK
		self.isPaintOK = isPaintOK

	def IsDamaged(self):
		return not(self.isMechanicOK and self.isPaintOK )


	def show_info(self):
		print(f"{self.brand.upper}")
		print(f"{self.model}")
		print(self.engine)

#car_01 = Car('VW', 'Passat', 'diesel', '1896', ' 2001', 'Variant', 'True', 'False')

car_01 = Car('VW', 'Passat', 'diesel', '1896', ' 2001','Variant', 'True', 'False')
car_02 = Car('Toyota', 'Paseo', 'petrol', '1497', '1997', 'Convertible', 'True', 'True')
car_03 = Car('Audi', 'A3', 'petrol','1598', '2001', 'hatchback', 'True', 'True')

car_offer = []
car_offer.append(car_01)
car_offer.append(car_02)
car_offer.append(car_03)
print("Today in our offer:")
for c in car_offer:
	print("{} - {} - {} - {} - {}ccm - {}".format(c.brand, c.model,c.version, c.engine,c.capacity, c.year))

	print('----------------------------------------------------------')

	print(car_01.brand,'X', car_01.IsDamaged(),'X', car_01.show_info())