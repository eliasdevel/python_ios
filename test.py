from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.sensors

print(collection.find_one({'_id':1 }))



