# domain-catalog/typeContactMail/views.py

from flask_restful import Resource, fields, marshal_with
from .models import TypeContactMail
from .serializers import TypeContactMailSerializer

resource_fields = {
	'code': fields.String,
	'name': fields.String
}

LIST_TYPES_CONTACT_MAIL = [
	TypeContactMail(code= '3', name='Personal'),
	TypeContactMail(code= '2', name='Professional'),
	TypeContactMail(code= '1', name='Mobile'),
]

class TypeContactMailView(Resource):
	@marshal_with(resource_fields)
	def get(self, **kwargs):
		return LIST_TYPES_CONTACT_MAIL