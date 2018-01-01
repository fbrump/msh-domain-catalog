# domain-catalog/app.py

from flask import Flask, jsonify
from flask_restful import Api
from dayOfWeek.views import DaysOfWeekView, DaysOfWeekItemView
from typeContactMail.views import TypeContactMailView
from typePhone.views import TypePhoneView

app = Flask(__name__, instance_relative_config=True)
api = Api(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')

api.add_resource(DaysOfWeekView, '/api/days-of-weeks/', endpoint = 'dayOfWeek')
api.add_resource(DaysOfWeekItemView, '/api/days-of-weeks/<int:id>/', endpoint = 'dayOfWeekItem')
api.add_resource(TypeContactMailView, '/api/type/mail/', endpoint = 'typeContactMail')
api.add_resource(TypePhoneView, '/api/type/phone/', endpoint = 'typePhone')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)