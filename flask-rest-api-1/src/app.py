from flask import Flask, jsonify, request, render_template
# jsonify serializes data to JavaScript Object Notation (JSON) format
# request

app = Flask(__name__) 

stores = [ # JSON uses ""!! not ''
    {'name': 'My Wonderful Store',
    'items': [
        {
            'name' : 'My Item',
            'price' : 15.99
        }
    ]},
]

@app.route('/')
def home():
    return render_template('index.html')

# Post - used to receive data
# Get - used to send data back only


# POST /store data: {name:} # create a new store with a given name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json() # this request is made in the endpoint # name of the store
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name> # get the stored name
@app.route('/store/<string:name>', methods=['GET']) # <string:name>' is a flask syntax
def get_store(name):
    # Iterate over stores
    # if the store name matches, return it
    # if none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store['name'])
    return jsonify({"message": 'store not found'})


# GET /store # return a list of all stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) # convert stored variables into json

# POST /store/<string:name>/item {name:, price} # create an item in the specific store with given name
@app.route('/store/<string:name>/item', methods=['POST'])
def create_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item # get all the items in a specific stores with name 
@app.route('/store/<string:name>/item')
def get_items_in_store(name):

    for store in stores:
        if store['items']:
            if store['name'] == name:
                return jsonify({'items' : store["items"]})
        else:
            return jsonify({'message': 'store is empty'})
    else:
        return jsonify({'message': 'store not found'})


if __name__ == '__main__':
    app.debug = True # 디버깅모드 활성화
    app.run()


'''
from flask import Flask

app = Flask(__name__) # '__main__' # if we run directly

@app.route('/') # www.mysite.com/api/ # endpoint '/'
def home():
    return "Hello, World!"

app.run(port=5000)
'''



'''
from flask import Flask
# define an app
app = Flask(__name__) # '__main__' # if we run directly


@app.route('/') # www.mysite.com/api/ # endpoint '/'
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()
    #app.run(port=4995)
'''
