from flask import Flask
from flask_restful import Api

from dayOfWeek.views import DaysOfWeekView

app = Flask(__name__, instance_relative_config=True)
api = Api(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')

api.add_resource(DaysOfWeekView, '/api/days-of-weeks/<int:code>', endpoint = 'dayOfWeek')

if __name__ == '__main__':
    app.run(debug=True)