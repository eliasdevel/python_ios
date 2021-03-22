
from pymongo import MongoClient
import datetime
import time
import re

client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.sensors



def get_cursor(collection, id, valor):
    options = { 'tailable': True }
    spec = { 
        'valor_atual': { '$ne': valor }, # valor diferente do anterior
        '_id': id }

    options['await_data'] = True
    cur = collection.find(spec, **options)
    return cur

values = {}
for x in collection.find():
    values[x['_id']] =  0 

while True:
    #percorre dados da collection
    for item in collection.find():
        #quando muda valor      
        if(item['valor_atual'] != values[item['_id']]):
            print(item);
            values[item['_id']] = item['valor_atual']
time.sleep(0.1)




