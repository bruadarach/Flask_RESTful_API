
from flask import Flask, request # ADDED !
from flask_restful import Resource, Api # Resource : api represents

app=Flask(__name__)
api = Api(app)

items = [] 

class Item(Resource): # OOP inheritance
    
    def get(self, name): # name of the student
        for item in items:
            if item['name'] == name:
                return item # flask restful doesn't need jsonify 
            
        return {'item': None}, 404

    def post(self, name):
        data = request.get_json(force=True) # Added! # this part will have an error if Header and body settings are not right in Postman.
        # force=True means you don't need the content type Header
        # silent=True  means you don't get error, just returns None.
        item = {'name': name, 'price': data['price']} # Added!
        items.append(item)
        return item, 201 # 201 is to be created! # 202 is to be accepted after the delay of creation

class ItemList(Resource): # ADDED!
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/"student name"
api.add_resource(ItemList, '/items') # ADDED! 

app.run(port=5000, debug=True)



'''
from flask import Flask
from flask_restful import Resource, Api # Resource : api represents

app=Flask(__name__)
api = Api(app)

items = [] 

class Item(Resource): # OOP inheritance
    
    def get(self, name): # name of the student
        for item in items:
            if item['name'] == name:
                return item # flask restful doesn't need jsonify 
            
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201 # 201 is to be created! # 202 is to be accepted after the delay of creation


api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/"student name"

app.run(port=5000)
'''



'''
from flask import Flask
from flask_restful import Resource, Api # Resource : api represents

app=Flask(__name__)
api = Api(app)

# define Resource
# with get methods we can access
class Student(Resource): # OOP inheritance
    
    # define method(get, post, etc.)
    # with get methods we can access
    def get(self, name): # name of the student
        return {'student': name}

api.add_resource(Student, '/student/<string:name>') # http://127.0.0.1:5000/student/"student name"
# tell api this Student resource is now accessible, 
# but we didn't have a endpoint/ so how we access? 
# @app.route('/student') is NOT neccessary => api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)
'''