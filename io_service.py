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
    gpio.setup(10, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(12, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    

setup()

while True:
    #percorre dados da collection
    for item in collection.find():
        #quando muda valor      
        if(item['valor_atual'] != values[item['_id']]):
            if(len(item['valor_atual']) == 0):
                item['valor_atual'] = '0';
             
            print('Mudanca de valor detectada')
            print(item);
            values[item['_id']] = item['valor_atual'];
            
            
            if(float(item['valor_ideal']) > float(item['valor_acionamento']) ):
                print('\n\nAquecedor\n\n')
                if(float(item['valor_atual']) <= float(item['valor_acionamento'])):
                    print('acionando o sensor %d', item['aciona_saida'])
                    gpio.output(int(item['aciona_saida']), gpio.HIGH)
                else:
                    if(float(item['valor_atual']) >= float(item['valor_ideal'])):
                        print('desligando sensor %d', item['aciona_saida'])
                        gpio.output(int(item['aciona_saida']), gpio.LOW)   
             
            if(item['valor_ideal'] < item['valor_acionamento']):
                print('\n\nRefrigerador\n\n')
                if(item['valor_atual'] >= item['valor_acionamento']  ):
                    print('acionando o sensor %d', item['aciona_saida'])
                    gpio.output(int(item['aciona_saida']), gpio.HIGH)
                else:
                    if(item['valor_atual'] <= item['valor_ideal']):
                        print('desligando sensor %d', item['aciona_saida'])
                        gpio.output(int(item['aciona_saida']), gpio.LOW)
                        

    time.sleep(1)






