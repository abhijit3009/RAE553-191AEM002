from flask import Flask, request # Flask is imported from module

from flask_restful import Resource, Api, abort, reqparse # all file classes are imported from flask_restful


from flask_jwt import JWT, jwt_required, current_identity#import JWT,jwt_required, current_identity from flask_jwt module

#import authenticate and identity from securty.py previously created.
from security import authenticate, identity
from user import UserRegister
from item import Item

# Flask application is created
app = Flask(__name__)

# Adding a secreate line
app.secret_key = 'abhi'

#Api application instance is created 
api = Api(app)

#create a JWT object. 
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/<name>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
