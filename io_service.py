
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
    

while True:
    #percorre dados da collection
    for x in collection.find():
        valor_atual = x['valor_atual']
        print(x['_id'])
        #pega cursor e espera mudanca de valor_atual
        cur = get_cursor(
            db.sensors, 
            x['_id'],
            valor_atual 
            )
        for data in cur:
            valor_atual = data['valor_atual']
            
            #quando mudou
            print(data)
    time.sleep(0.1)




