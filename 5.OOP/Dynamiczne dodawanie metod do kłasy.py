import csv
import types

def exportToFile_Static(path,header,data):
	with open (path, mode="w") as file:
		writer = csv.writer(file,delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(header)
		writer.writerow(data)
	print("TO JEST STATYCZNE EXPORTOWANIE")

def exportToFile_Class(cls,path):
	with open (path, mode="w") as file:
		writer = csv.writer(file,delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['brand', 'model', 'engine', 'capacity', 'year'])
		for c in cls.listOfCars:
			writer.writerow([c.brand, c.model, c.engine, c.capacity, c.year])
	print("TO JEST EXPORTOWANIE na poziomie klasy")

def exportToFile_Instance(self,path):
	with open (path, mode="w") as file:
		writer = csv.writer(file,delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['brand', 'model', 'engine', 'capacity', 'year'])
		writer.writerow([self.brand,self.model,self.engine,self.capacity,self.year])
	print("TO JEST EXPORTOWANIE na poziomie Instancyji")

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

	def __SetIsOnSale(self, newIsOnSaleStatus):
		if self.brand == brandOnSale:
			self.__isOnSale = newIsOnSaleStatus

	IsOnSale = property(__GetIsOnSale,__SetIsOnSale, None)


car_01 = Car('VW', 'Passat', 'diesel', '1896', ' r2001','Variant', False)
car_02 = Car('Toyota', 'Paseo', 'petrol', '1497', 'r1997', 'Convertible', False)
car_03 = Car('Audi', 'A3', 'petrol','1598', 'r2001', 'hatchback', False)


#exportToFile_Static(r'C:\desktop\export_static.csv', ['brand', 'model','engine'],[car_01.brand,car_01.model,car_01.engine])

Car.exportToFile_Class = types.MethodType(exportToFile_Class,Car)
Car.exportToFile_Class(path= r'C:\desktop\export_class.csv')