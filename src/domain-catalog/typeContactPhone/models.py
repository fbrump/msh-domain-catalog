# domain-catalog/typeContactPhone/models.py

import uuid

class TypeContactPhone(object):
	"""
		This class mapping Type Contact Phone model with your properties.

		Field:
			Code 		- Code identify model
			Description - Description about type
			Status 		- Defined if this object is activate or not
			UID 		- Other code internal

	"""
	def __init__(self, code, description):
		super(TypeContactPhone, self).__init__()
		self.code = code
		self.description = description
		self.status = True
		self.uid = str(uuid.uuid4())
	def setStatus(self, isActive):
		set.status = isActive
		