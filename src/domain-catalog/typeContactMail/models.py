# domain-catalog/typeContactMail/models.py

import uuid

class TypeContactMail(object):
	"""
		Model that mapping object Type Contact Mail on domain
		Param:
			Code	- public identification that will used on other domains
			name 	- Description about what it is
			uid		- internal identification used for implementations
			status	- set type is activate or inactivate
	"""
	def __init__(self, code, name):
		self.name = name
		self.code = code
		
		# This field will not be sent in the response
		self.status = True
		self.uid = str(uuid.uuid4())
		def SetStatus(self, status):
			self.status = status

