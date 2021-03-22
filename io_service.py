
from pymongo import MongoClient
import datetime
import time


client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.sensors



cursor = collection.find(tailable=True,await_data=True)
while cursor.alive:
    try:
        doc = cursor.next()
        print doc
    except StopIteration:
        time.sleep(1)



