#imports
from flask import Flask, jsonify, request
from flask_cors import CORS 
import pymongo 

#connection credentials (uri and database_name)
connection_url = 'mongodb://devp_user:1234567890@greendeck-task-1-shard-00-00.bomos.mongodb.net:27017,greendeck-task-1-shard-00-01.bomos.mongodb.net:27017,greendeck-task-1-shard-00-02.bomos.mongodb.net:27017/ecommerce_products?ssl=true&replicaSet=atlas-rnhhmw-shard-0&authSource=admin&retryWrites=true&w=majority'
databse_name = 'ecommerce_products'

#setting connection
client = pymongo.MongoClient(connection_url)
db = client.get_database(databse_name)
records=db.Task_1  #Task_1 is the collection name

app = Flask(__name__) 

# READ

#read the first entry that matches the query object using find_one()
@app.route('/read_one/<key>/<value>/', methods=['GET']) 
def read_one(key, value): 
    queryObject = {key: value} 
    query = records.find_one(queryObject) 
    query.pop('_id') #removing the _id attribute
    return jsonify(query) #returning the matching entry
#read all the entries in a document using find()
@app.route('/read_all', methods=['GET']) 
def read_all(): 
    query = records.find() 
    output = {} # initializing a dict
    i = 0
    for cur_quer in query: 
        output[i] = cur_quer #appending 1 entry to the dict at a time
        output[i].pop('_id') #removing the _id attribute from each entry
        i += 1
    return jsonify(output) #returning all the entries

# CREATE
#create/insert one entry into the database using insert_one()
@app.route('/create/<name>/<brand_name>/<regular_price_value>/<offer_price_value>/<currency>/<classification_l1>/<classification_l2>/<classification_l3>/<classification_l4>/<image_url>/', methods=['POST']) 
def create(name, brand_name, regular_price_value, offer_price_value, currency, classification_l1, classification_l2, classification_l3, classification_l4, image_url): 
    queryObject = { 
        'name' :name,
        'brand_name' :brand_name,
        'regular_price_value' : regular_price_value,
        'offer_price_value' : offer_price_value,
        'currency' : currency, 
        'classification_l1' : classification_l1,
        'classification_l2' : classification_l2, 
        'classification_l3' : classification_l3,
        'classification_l4' : classification_l4, 
        'image_url' : image_url
    } 
    query = records.insert_one(queryObject) 
    return "Query inserted successfully...!!!" #confirming the creation 
                                               #of new entry

#UPDATE
# updating a particular entry using update_one()
@app.route('/update/<key>/<value>/<element>/<updateValue>/', methods=['PUT']) 
def update(key, value, element, updateValue): 
    queryObject = {key: value} # the key-value pair/entry to be updated
    updateObject = {element: updateValue} #the updated key-value pair
    query = records.update_one(queryObject, {'$set': updateObject}) 
    if query.acknowledged:   #confirming if record updated or not
        return "Record Updated Successfully" 
    else: 
        return "Update Operation Unsuccessful" 

# DELETE
# deleting one record that matches the condition using deleteOne
@app.route('/delete_one/<key>/<value>', methods=['DELETE'])
def delete_one(key, value):
    queryObject={key:value} #condition to be matched
    query = records.delete_one(queryObject)
    if query.acknowledged: #confirming if record deleted or not
        return "One matching record deleted"
    else: 
        return "Delete Operation Unsuccessful"
#deleting all the records containing the matching condition using delelteMany
@app.route('/delete_many_match/<key>/<value>', methods=['DELETE'])
def delete_many_match(key, value):
    queryObject={key: value} #condition to be matched
    query = records.delete_many(queryObject)
    if query.acknowledged:   #confirming if records deleted or not
        return "All matching records deleted"
    else: 
        return "Delete Operation Unsuccessful"
#deleting all the records present in the document using deleteMany
@app.route('/delete_all_records/', methods=['DELETE'])
def delete_all():
    query = records.delete_many({})
    if query.acknowledged:    #confirming if records deleted or not
        return "All records deleted Successfully"
    else: 
        return "Delete Operation Unsuccessful"

if __name__ == '__main__': 
    app.run(host='0.0.0.0') 
