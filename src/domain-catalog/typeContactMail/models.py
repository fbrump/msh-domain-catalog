# domain-catalog/typeContactMail/models.py

from flask_restful import fields, marshal_with

resource_fields = {
	'code': fields.String,
	'name': fields.String
}

class TypeContactMailDao(object):
	def __init__(self, code, name):
		self.code = code
		self.name = name

		# This field will not be sent in the response
		self.status = 'active'

class TypeContactMail(Resource):
	@marshal_with(resource_fields)
	def get(self, **kwargs):
		return TypeContactMailDao(code=1, name='Personal')
