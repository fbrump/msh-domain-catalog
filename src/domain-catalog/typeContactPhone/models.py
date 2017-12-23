# domain-catalog/typeContactPhone/models.py

class TypeContactPhone(object):
	"""
		This class mapping Type Contact Phone model with your properties.

		Field:
			Code 		- Code identify model
			Description - Description about type
			Active 		- Defined if this object is activate or not

	"""
	def __init__(self, code, description, active):
		super(TypeContactPhone, self).__init__()
		self.code = code
		self.active = active
		