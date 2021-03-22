
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
    
valor_atual = 20
id = 1
while True:
    cur = get_cursor(
        db.sensors, 
        id,
        valor_atual 
        )
    for data in cur:
        valor_atual = data['valor_atual']
        id = data['_id']
        print(data)
    time.sleep(0.1)




