brandOnSale = "Toyota"

class Car:

	def __init__(self,brand, model, engine, capacity, year, version, isOnSale):
		self.brand = brand
		self.model = model
		self.engine = engine
		self.capacity = capacity
		self.year = year
		self.version = version
		self.__isOnSale = isOnSale

	def show_info(self):
		print(f"{self.brand.upper}")
		print(f"{self.model}")
		print(self.engine)

	def show_fuel(self,engine):
		self.engine = engine

	def add_year(self,year):
		self.year.extend(year)

	def __GetIsOnSale(self):
		return self.__isOnSale

	def __SetIsOnSale(self, newIsOnSaleStatus):
		if self.brand == brandOnSale:
			self.__isOnSale = newIsOnSaleStatus

	IsOnSale = property(__GetIsOnSale,__SetIsOnSale, None)


car_01 = Car('VW', 'Passat', 'diesel', '1896', ' r2001','Variant', False)
car_02 = Car('Toyota', 'Paseo', 'petrol', '1497', 'r1997', 'Convertible', False)
car_03 = Car('Audi', 'A3', 'petrol','1598', 'r2001', 'hatchback', False)

car_offer = []
car_offer.append(car_01)
car_offer.append(car_02)
car_offer.append(car_03)
print("Today in our offer:")
for c in car_offer:
	print("{} - {} - {} - {} - {}ccm - {}".format(c.brand, c.model,c.version, c.engine,c.capacity, c.year))
	print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')

car_01.GetIsOnSale(True)