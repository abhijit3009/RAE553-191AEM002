from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
app.secret_key='abhi'
api = Api(app)

items = {}

parser = reqparse.RequestParser()
parser.add_argument('price')

class item(Resource):
    def get(self, name):
        return items[name]

    def delete(self, name):
        del items[name]
        return ''

    def put(self, name):
        args = parser.parse_args()
        task = {'price': args['price']} # task = { price : 5555 }
        items[name] = task          #items[pen] = { "price" : "5555" }
        return task # prints { "price" : "5555"}

    def post(self, name):
        if name not in items:
            args = parser.parse_args()
            task = {'price': args['price']}
            items[name] = task
            return task
        else:
            abort(404)



# ItemList

class itemList(Resource):
    def get(self):
        return items


##
## Actually setup the Api resource routing here
##
api.add_resource(itemList, '/items')
api.add_resource(item, '/items/<name>')


if __name__ == '__main__':
    app.run()
