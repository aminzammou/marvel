import time
import hashlib
import requests
import json
from marvel import *

timestamp = str(time.time())
private_key = "9af8c7d1960b0397198b103770d88bbcecf330f3"
public_key = "0dc72be1960f79199db0cf50e7d980d8"

hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())
naam = rasuper()
url = "http://gateway.marvel.com:80/v1/public/characters"
connection_url = url+"?ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest+"&name="+naam
print(connection_url)

response = requests.get(connection_url)
jsontext = json.loads(response.text)

payloadObject = jsontext['data']
supperlist = payloadObject['results']

# for supper in supperlist:
#     print(supper['description'])

for supper in supperlist:
    hint = supper['description'].replace(supper['name'],'***').split(',')
    print(hint)
