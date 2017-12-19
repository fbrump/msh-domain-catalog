from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__, instance_relative_config=True)
api = Api(app)

app.config.from_object('config')
app.config.from_pyfile('config.py')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)