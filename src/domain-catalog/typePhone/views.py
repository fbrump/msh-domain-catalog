# domain-catalog/typePhone/views.py

from flask_restful import Resource, fields, marshal_with
from flask import json, jsonify, Response
from .models import TypePhone
from .serializers import TypePhoneMessageResponse, GetAllTypePhoneMessageResponse

resource_fields = {
	'code': fields.String,
	'description': fields.String
}

LIST_TYPES_PHONE = [
	TypePhone(code= '1', description='Mobile Phone'),
	TypePhone(code= '2', description='Landline'),
]

class TypePhoneView(Resource):
	@marshal_with(resource_fields)
	def get(self, **kwargs):
		return LIST_TYPES_PHONE

## Example 2 - BaseMessage
"""

class TypePhoneView(Resource):
	#@marshal_with(resource_fields)
	def get(self, **kwargs):
		_model = TypePhone(1, 'mobile')
		return jsonify(
			protocol='asdf;lkjqwerpoiuqwer;lkajsdfpoqiwuer',
			result=json.dumps(_model.__dict__),
			message='Success'
		)
"""

## Exemple 1 - BaseModel
"""

class TypePhoneView(Resource):
	#@marshal_with(resource_fields)
	def get(self, **kwargs):
		_model = TypePhone(1, 'mobile')
		print(_model)
		message = TypePhoneMessageResponse(model=_model)
		return message.toJson()

"""