class NoDuplicates:
	def __init__(self, list):
		self.list_of_items= list

	def __call__(self, item):
		self.list_of_items.append(item)

		for a in item:
			if not a in self.list:
				self.list.append(a)

Nodup = NoDuplicates([])
print(Nodup.list_of_items)
Nodup.list_of_items.append('keyboard')
print(Nodup.list_of_items)
Nodup.list_of_items.append('keyboard','mouse', 'pendrive')
print(Nodup.list_of_items)
Nodup.list_of_items.append('charger', 'pendrive')
print(Nodup.list_of_items)