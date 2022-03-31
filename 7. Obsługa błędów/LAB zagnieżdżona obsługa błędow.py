import datetime as dt


class Trip:
	def __init__(self, symbol, title, start, end):
		self.symbol = symbol
		self.title = title
		self.start = start
		self.end = end

	def check_data(self):
		if len(self.title) == 0:
			raise Exception("Title is empty!")
		if self.start > self.end:
			raise ValueError("Start date is later than end date!")


	@classmethod
	def publish_offer(cls,trips):
		list_of_errors = []

trips = [
	Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
	Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
	Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
	]