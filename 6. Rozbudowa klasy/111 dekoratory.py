class Car:
	def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, accessories):
		self.brand = brand
		self.model = model
		self.isAirBagOK = isAirBagOK
		self.isPaintingOK = isPaintingOK
		self.isMechanicOK = isMechanicOK
		self.accessories = accessories

	def GetInfo(self):
		print("{} {}".format(self.brand, self.model).upper())
		print("Is Air Bag - OK - {}".format(self.isAirBagOK))
		print("Is Painting OK - {}".format(self.isPaintingOK))
		print("Is Mechanic OK - {}".format(self.isMechanicOK))
		print("Accessories   {}".format(self.accessories))
		print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")


def __iadd__(self, other):
	accessories = self.accessories
	accessories.extend(other)
	return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK, self.isMechanicOK, accessories)

car_01 = Car('Toyota', 'Paseo', True, True, True, ['zimnuju sziny'])
car_01.GetInfo()


car_02 = Car("Toyota", "Altezza", True, True, False, [])

car_02.GetInfo()


car_01 += [' choinka o zapachu kokosowym do malucha', 'Naklejka z rybką']
car_01.GetInfo()
