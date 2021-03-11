#!/bin/bash

apt-get install python

apt-get install python-pip

pip install pymongo

apt-get install mongodb

mkdir /data
cd /data
mkdir db

chmod 777 -R /data

# TODO criar serviço que inicie o mongodb automático
mongod
