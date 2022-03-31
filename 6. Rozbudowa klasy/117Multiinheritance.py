class Car:
	def __init__(self, brand, model, isOK,):
		print('>> Class Car - init - start <<')
		self.brand = brand
		self.model = model
		self.isOK = isOK
		self.name = "{} {}".format(brand,model)
		print('>> Class Car - init - finishing <<')


	def GetInfo(self):
		print('>> Class Car - GetInfo- finishing <<')
		super().GetInfo()
		print("{} {}".format(self.brand, self.model).upper())
		print("Is OK - OK - {}".format(self.isOK))
		print('>> Class Car - GetInfo- end <<')


class Specialist :

	def __init__(self, firstname, surname, brand):
		print('>> Class SPECIALIST - INIT- start <<')
		self.firstname = firstname
		self.surname = surname
		self.name = "{} {}".format(firstname, surname)
		self.brand = brand
		print('>> Class SPECIALIST - init - finishing <<')



	def GetInfo(self):
		print('>> Class SPECIALIST - GetInfo- start <<')

		print("{} {} - ({})".format(self.firstname, self.surname, self.brand))

		print('>> Class SPECIALIST - GetInfo- end <<')


class CarSpecialist(Car, Specialist):


	def __init__(self,brand,model,IsOK,firstname,surname):
		print('>>Class CarSpecialist - INIT - Start')
		Car.__init__(self, brand, model, IsOK)
		Specialist.__init__(self,firstname,surname,brand.upper())
		print('>>Class CarSpecialist - INIT - ĘD')


	def GetInfo(self):
		print('>>Class CarSpecialist - GETINFĄ - Start')
		super().GetInfo()
		print('>>Class CarSpecialist - GETINFĄ - Stop')

tom = CarSpecialist('Toyota', 'Paseo', True, 'Zdenek', 'Pierdzikwiat')
#print(vars(tom))


tom.GetInfo()