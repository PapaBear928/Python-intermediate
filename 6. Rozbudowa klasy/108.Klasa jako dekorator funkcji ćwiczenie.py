class NoDuplicates:


	def __init__(self,funct):
		print("This is init of NoDuplicates Class")
		self.funct = funct

	def __call__(self, cake,additives):

		#no_duplicate_list = [ i for i in list if i not in Cake.additives]
		#items = self.funct(no_duplicate_list)
		#Cake.additives.append(items)
		#return items
		no_duplicate_list = []
		for a in additives:
			if not a in cake.additives:
				no_duplicate_list.append(a)
		self.funct(cake, no_duplicate_list)





class Cake:
	bakery_offer = []

	def __init__(self, name, kind, taste, additives, filling):

		self.name = name
		self.kind = kind
		self.taste = taste
		self.additives = additives.copy()
		self.filling = filling
		self.bakery_offer.append(self)

	def show_info(self):
		print("{}".format(self.name.upper()))
		print("Kind:        {}".format(self.kind))
		print("Taste:       {}".format(self.taste))
		if len(self.additives) > 0:
			print("Additives:")
			for a in self.additives:
				print("\t\t{}".format(a))
		if len(self.filling) > 0:
			print("Filling:     {}".format(self.filling))
		print('-' * 20)




cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')


@NoDuplicates
def add_additives(self, additives):
	self.additives.extend(additives)


add_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()