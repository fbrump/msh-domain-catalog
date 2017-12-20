from your_orm import Model, Column, Integer, String, DateTime

class DayOfWeek(object):
	"""docstring for DayOfWeek"""
	code = Column(String)
	abbr = Column(String)
	description = Column(String)
	date_created = Column(DateTime, auto_now_add=True)
	def __init__(self, code, abbr, description):
		super(DayOfWeek, self).__init__()
		self.code = code
		self.abbr = abbr
		self.description = description

class User(Model):
	email = Column(String)
	password = Column(String)
	date_created = Column(DateTime, auto_now_add=True)