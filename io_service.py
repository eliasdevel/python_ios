from pymongo import MongoClient
import datetime
import time
import re

import RPi.GPIO as gpio

client = MongoClient('localhost', 27017)

db = client.sensors_database

collection = db.sensors

values = {}
for x in collection.find():
    #seta zerado para passar pela primeira verificacao
    values[x['_id']] =  0 


def setup():
    gpio.setmode(gpio.BOARD)
    gpio.setup(1, gpio.OUT)
    gpio.setup(2, gpio.OUT)
    gpio.setup(3, gpio.OUT)
    gpio.setup(4, gpio.OUT)
    gpio.setup(5, gpio.OUT)
    gpio.setup(6, gpio.OUT)


setup()

while True:
    #percorre dados da collection
    for item in collection.find():
        #quando muda valor      
        if(item['valor_atual'] != values[item['_id']]):
            print('Mudanca de valor detectada')
            print(item);
            values[item['_id']] = item['valor_atual'];
            
            #TODO colocar chamada de mudanca de valor
            if(item['valor_ideal'] < item['valor_acionamento']):
                print('\n\nresfirar\n\n')
                #resfriar
                
            if(item['valor_ideal'] > item['valor_acionamento']):
                print('\n\naquecer\n\n')
                #aquecer
                values['s'] =''
time.sleep(1)






