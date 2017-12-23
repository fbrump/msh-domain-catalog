# domain-catalog/typePhone/views.py

from flask_restful import Resource, fields, marshal_with
from .models import TypePhone
from .serializers import TypePhoneMessageResponse

resource_fields = {
	'code': fields.String,
	'description': fields.String
}

LIST_TYPES_PHONE = [
	TypePhone(code= '1', description='Mobile Phone'),
	TypePhone(code= '2', description='Landline'),
]

class TypePhoneView(Resource):
	#@marshal_with(resource_fields)
	def get(self, **kwargs):
		model = TypePhone(1, 'mobile')
		message = TypePhoneMessageResponse(model)
		return message