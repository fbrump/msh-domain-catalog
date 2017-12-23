# domain-catalog/typePhone/serializers.py

from dayOfWeek.serializers import BaseMessage, BaseModel
from .models import TypePhone
import uuid

class TypePhoneMessageResponse(BaseModel):
	"""
		Message serializer for api type contact phone.
	"""
	def __init__(self, model):
		#super(TypePhone, self).__init__()
		self.description = model.description
		self.code = model.code

class GetAllTypePhoneMessageResponse(BaseMessage):
	"""docstring for GetAllTypePhoneMessageResponse"""
	def __init__(self, arg):
		super(GetAllTypePhoneMessageResponse, self).__init__()
		self.arg = arg
		