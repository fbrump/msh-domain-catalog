from flask import Flask, jsonify
from flask_restful import Api
from dayOfWeek.views import DaysOfWeekView, DaysOfWeekItemView, TestView

app = Flask(__name__, instance_relative_config=True)
api = Api(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')

api.add_resource(DaysOfWeekView, '/api/days-of-weeks/', endpoint = 'dayOfWeek')
api.add_resource(DaysOfWeekItemView, '/api/days-of-weeks/<int:id>/', endpoint = 'dayOfWeekItem')
api.add_resource(TestView, '/api/tests/')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5050)