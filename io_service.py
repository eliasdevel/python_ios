from pymongo import MongoClient
import datetime
import time
import re

client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.sensors

values = {}
for x in collection.find():
    #seta zerado para passar pela primeira verificacao
    values[x['_id']] =  0 

while True:
    #percorre dados da collection
    for item in collection.find():
        #quando muda valor      
        if(item['valor_atual'] != values[item['_id']]):
            print(item);
            values[item['_id']] = item['valor_atual']
            #TODO colocar chamada de mudanca de valor

time.sleep(1)




