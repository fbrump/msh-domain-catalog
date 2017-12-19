from flask_restful import Resource, fields, marshal_with
from .models import DayOfWeek

resource_fields = {
    'code': fields.String,
    'abbr': fields.String,
    'description': fields.String,
}

def getListData():
	_list = list()
		
	_list.append(DayOfWeek(1, 'MON', 'Monday'))
	_list.append(DayOfWeek(1, 'MON', 'Monday'))
	_list.append(DayOfWeek(1, 'MON', 'Monday'))
	_list.append(DayOfWeek(1, 'MON', 'Monday'))
	_list.append(DayOfWeek(1, 'MON', 'Monday'))
	_list.append(DayOfWeek(1, 'MON', 'Monday'))
	_list.append(DayOfWeek(1, 'MON', 'Monday'))

	return _list

class DaysOfWeekView(Resource):
	def get(self, **kwargs):
		#return getListData()
		return { 'data': 'oi'}