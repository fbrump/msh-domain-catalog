# domain-catalog/typeContactMail/serializers.py

from dayOfWeek.serializers import BaseMessage, BaseModel
from .models import TypeContactMail
import uuid

class TypeContactMailSerializer(BaseMessage):
    def __init__(self, *args, **kwargs):
        super(TypeContactMailSerializer, self).__init__(*args, **kwargs)
        pass

class TypeContactMailMessageResponse(BaseModel):
	"""docstring for TypeContactMailMessag"""
	def __init__(self, model):
		super(TypeContactMailMessag, self).__init__()
		self.name = model.name
		self.code = model.code
		