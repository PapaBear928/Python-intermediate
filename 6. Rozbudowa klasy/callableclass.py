class Memory:
	def __init__(self, list):
		self.list_of_items = list

	def __call__(self, item):
		self.list_of_items.append(item)

mem = Memory([])
print("List of items in mem", mem.list_of_items)


mem.list_of_items.append('buy milk')
print("List of items in mem", mem.list_of_items)

mem('buy butter')
mem('buy bread')
mem('buy beer')
print(mem.list_of_items)