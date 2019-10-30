import time
import hashlib
import requests
import json
import random

timestamp = str(time.time())
private_key = "9af8c7d1960b0397198b103770d88bbcecf330f3"
public_key = "0dc72be1960f79199db0cf50e7d980d8"

hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())
url = "http://gateway.marvel.com:80/v1/public/characters"
# comic = 'Age of Ultron (2013)'
connection_url = url+"?ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest
# print(connection_url)
response = requests.get(connection_url)
jsontext = json.loads(response.text)

payloadObject = jsontext['data']
supperlist = payloadObject['results']


#def monopolyworp():
#    x= (random.choice(supperlijst))
#    return x
# while True:
#     if not supper['description']:
#         monopolyworp()
#     break
# def rasuper():
#     while True:
#         if not supper['description']:
#             return monopolyworp()
#         break
# rasuper()

# def rasuper():
#     held = supper['description']
#     if False:
#         if supper['description'] != "":
#             return held
#         else:
#             return monopolyworp()
#     else:
#         return held

#def rasuper():
#  while True:
#        #print(supper)
#        if len(supper['description']) != 0:
#            return monopolyworp()

def rasuper():
    while True:
        randomhero = random.choice(supperlist)
        if randomhero['description'] != '':
            return randomhero['name']
# print(rasuper())
