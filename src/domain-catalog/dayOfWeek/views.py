from flask import jsonify
from flask_restful import Resource, fields, marshal_with
from .models import DayOfWeek
from .serializers import PersonModel
import uuid

LIST_DAYS_OF_WEEKS = [
	{ 'code': 1, 'name':'Sunday'},
	{ 'code': 2, 'name':'Monday'},
	{ 'code': 3, 'name':'Tuesday'},
	{ 'code': 4, 'name':'Wednesday'},
	{ 'code': 5, 'name':'Thursday'},
	{ 'code': 6, 'name':'Friday'},
	{ 'code': 7, 'name':'Saturday'},
]

class TestView(Resource):
	def get(self, **kwargs):
		person = PersonModel(name='Brum', age=17)
		return person.toJson()
		

class DaysOfWeekView(Resource):
	def get(self, **kwargs):
		return { 
			'Return':  LIST_DAYS_OF_WEEKS,
			'Protocol': str(uuid.uuid4()),
			'Message': 'Success'
		}

class DaysOfWeekItemView(Resource):
	def get(self, id, **kwargs):
		return { 
			'Return':  self.getDay(id),
			'Protocol': str(uuid.uuid4()),
			'Message': 'Success'
		}
	def getDay(self, id):
		for day in LIST_DAYS_OF_WEEKS:
			if day['code'] == id:
				return day
		return None