from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.sensors



data = [{
        "_id": 1,
        "nome": "Sensor de temperatura da cozinha",
        "id_485": "A",
        "valor_atual": 22,
        "aciona_saida": 1,
        "valor_acionamento":12,
        "temperatura_ideal":22,
        "dt_update": datetime.datetime.now()
        }, 
        {
        "_id": 2,
        "nome": "Sensor de temperatura da cozinha",
        "id_485": "A",
        "valor_atual": 20,
        "aciona_saida": 1,
        "valor_acionamento":118,
        "temperatura_ideal":22,
        "dt_update": datetime.datetime.now()
        }]

# for insert new or update old values
for d in data:
    collection.update({'_id':d['_id']}, d)