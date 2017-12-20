# BASE MESSAGES (Serializers)
import flask
import uuid
import json

class BaseMessage(object):
	"""docstring for BaseMessage"""
	def __init__(self, protocol=None):
		super(BaseMessage, self).__init__()
		self.statusCode = 200
		self.setProtocol(protocol)
	def getProtocol(self):
		return self._protocol
	def setProtocol(self, protocol):
		self._protocol = protocol if protocol else str(uuid.uuid4())
	def setModel(self, model):
		self.model
	def setStatusCode(self, code):
		self.statusCode = code
	def getMessage(self):
		if self.statusCode == 200:
			return 'Success'
		elif self.statusCode == 300:
			return 'Validation'
		else:
			return 'Internal Error'
	def getJson(self):
		return { 
			'Return':  self.model.toJson() if self.model else None,
			'Protocol': str(uuid.uuid4()),
			'Message': self.getMessage()
		}

class BaseModel(object):
	"""docstring for BaseModel"""
	def __init__(self):
		super(BaseModel, self).__init__()
	def toJson(self):
		return json.dumps(self.__dict__, indent=4, separators=(',', ': '))

class PersonModel(BaseModel):
	"""docstring for PersonModel"""
	def __init__(self, name, age):
		super(PersonModel, self).__init__()
		self.name = name
		self.age = age