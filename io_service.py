
from pymongo import MongoClient
import datetime
import time
import re

client = MongoClient('localhost', 27017)

db = client.test_database

collection = db.sensors



def get_cursor(collection, topic_re, last_id=-1, await_data=True):
    options = { 'tailable': True }
    spec = { 
        'ts': { '$gt': last_id }, # only new messages
        'k': topic_re }
    if await_data:
        options['await_data'] = True
    cur = collection.find(spec, **options)
    cur = cur.hint([('$natural', 1)]) # ensure we don't use any indexes
    return cur
    

while True:
    cur = get_cursor(
        db.sensors, 
        re.compile('^foo'), 
        await_data=True)
    for msg in cur:
        last_id = msg['ts']
        print(msg)
    time.sleep(0.1)




