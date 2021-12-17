import json
def getValue(str,key):
    return json.loads(str)[key]

def changeKeyValuePair(json,key,value):
    if(json.get(key)!=None):
        json[key]=value

def addKeyValuePair(json,key,value):
    if(not(json.get(key))):
        json.update({key:value})

