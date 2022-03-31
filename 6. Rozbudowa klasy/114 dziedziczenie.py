brandOnSale = "Toyota"

class Car:

	numberOfCars = 0
	listOfCars = []


	def __init__(self,brand, model, engine, capacity, year, version, isOK, isOnSale):
		self.brand = brand
		self.model = model
		self.engine = engine
		self.capacity = capacity
		self.year = year
		self.version = version
		self.isOK = isOK
		self.__isOnSale = isOnSale
		Car.numberOfCars +=1
		Car.listOfCars.append(self)

	def GetInfo(self):
		print("{} {}".format(self.brand, self.model).upper())
		print("Is OK - OK - {}".format(self.isOK))
		#print("Accessories   {}".format(self.accessories))
		print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


	def __GetIsOnSale(self):
		return self.__isOnSale

	def __SetIsOnSale(self, newIsOnSaleStatus):
		if self.brand == brandOnSale:
			self.__isOnSale = newIsOnSaleStatus

	IsOnSale = property(__GetIsOnSale,__SetIsOnSale, None)

car_01 = Car('VW', 'Passat', 'diesel', '1896', ' r2001','Variant', False, False)
car_02 = Car('Toyota', 'Paseo', 'petrol', '1497', 'r1997', 'Convertible', False, False)
car_03 = Car('Audi', 'A3', 'petrol','1598', 'r2001', 'hatchback', False, True)


class Truck(Car):
	def __init__(self,brand, model, engine, capacity, year, version, isOK, isOnSale, capacityKg):
		super().__init__(brand, model, engine, capacity, year, version, isOK, isOnSale)
		self.capacityKg = capacityKg

	def GetInfo(self):
		super().GetInfo()
		print('Capacity Kg - -  - {}'.format(self.capacityKg))
truck_01 = Truck('Ford', 'Transit','diesel','2197','2019','Truck',True,True,'2300')

truck_01.GetInfo()