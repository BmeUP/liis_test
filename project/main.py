from flask import Flask
from flask_restful import Resource, Api
from resources.urls import urls

app = Flask(__name__)
api = Api(app)
urls(api)


if __name__ == '__main__':
    app.run(debug=True)