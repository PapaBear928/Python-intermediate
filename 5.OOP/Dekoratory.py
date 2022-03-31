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



	def __GetIsOnSale(self):
		return self.__isOnSale


	@property
	def IsOnSale(self):
		return  self.__isOnSale


	@IsOnSale.setter
	def IsOnSale(self, newIsOnSaleStatus):
		if self.brand == brandOnSale:
			self.__isOnSale = newIsOnSaleStatus


	@IsOnSale.deleter
	def IsOnSale(self):
		self.__isOnSale == None


	@property
	def CarTitle(self):
		return "Brand: () , Model:()".format(self.brand,self.model).title()

car_01 = Car('Audi', 'A3', 'petrol','1598', 'r2001', 'hatchback', False)



print(car_01.IsOnSale)