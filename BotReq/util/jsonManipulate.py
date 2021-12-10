def changeKeyValuePair(json,key,value):
    if(json[key]):
        json[key]=value

def addKeyValuePair(json,key,value):
    if(not(json.get(key))):
        json.update({key:value})