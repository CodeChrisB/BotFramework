import re as re
import requests
import concurrent.futures as cf
from time import sleep
import string, random

#
#VARIABLES
#
class BotReq:
    body={}
    bulkNumber=1
    url=""
    output=-1
    #
    #METHODS
    #
    def __init__(self, body,url):
        self.body = body
        self.url = url


    

    def setBody(self,newBody):
        self.body = newBody

    def getBody(self): 
        return self.body

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        return self.url

    def runRequest(self):
        r = requests.post(self.url,data=self.body)
        print(r.text)
    
    def runNTimes(self,n):
        with cf.ThreadPoolExecutor() as executor:
            for i in range(262,16500): 
                r = requests.post(self.url, data=self.body)
                if(val):
                    print(r.text)

#
# OPTIONS
#

    def PrintOutPut(self,val):
        self.output = val
