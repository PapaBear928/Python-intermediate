import random

class Memory:
	list_of_already_selcted_cars = []

	def __init__(self,funct):
		print("This is init of Memory Class")
		self.funct = funct


	def __call__(self, list):
		print("This is CALL of Memory Class Instance")
		cars_not_selected = [i for i in list if i not in Memory.list_of_already_selcted_cars]
		print('+-- selecting only from a list of', cars_not_selected)
		items = self.funct(cars_not_selected)
		Memory.list_of_already_selcted_cars.append(items)
		return items

cars = ['Opel', 'VW','Suzuki', 'Mazda', 'Fiat','Peugeot', 'Renault', 'Toyota', 'Honda', 'BMW', 'Mercedes', 'Dodge']

@Memory
def SelectPromoToday(list_of_cars):
	return random.choice(list_of_cars)


@Memory
def SelectShowToday(list_of_cars):
	return random.choice(list_of_cars)


@Memory
def SelectFreeAccesories(list_of_cars):
	return random.choice(list_of_cars)

print("Promo:", SelectPromoToday(cars))
print("Show:", SelectShowToday(cars))
print("Free Adds:", SelectFreeAccesories(cars))
