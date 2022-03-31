import datetime as dt

class MD:
	'''def __init__(self, year, month, day, max):
		self.date = dt.datetime(year, month, day)
		self.max = max

	def __getitem__(self, item):
		if item <= self.max:
			return self.date + dt.timedelta(days=item)
		else:
			raise StopIteration()

md = MD(2000, 1, 1, 2500000)

print(md[0], md[1, md[2]], md[2444444])'''

	def __init__(self, year,month,day, maxdays):
		self.date = dt.datetime(year,month,day)
		self.maxdays = maxdays

	def __getitem__(self, item):
		if item <= self.maxdays:
			return self.date + dt.timedelta(days=item)
		else:
			raise StopIteration()

md = MD(2000,1,1,2500000)

it = iter(md)

print(next(it))
print(next(it))
print(next(it))
print(next(it))