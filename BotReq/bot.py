import re as re
import requests
import concurrent.futures as cf
from time import sleep
import string, random
import BotReq.util.generate as gen
import BotReq.util.jsonManipulate as manipulate

from requests.api import options

#
#VARIABLES
#
class BotReq:
    body={}
    bulkNumber=1
    url=""
    
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
        if(self.options["output"]):
            print(r.text)
    
    def runNTimes(self,n):
        with cf.ThreadPoolExecutor() as executor:
            for i in range(n): 
                if(self.options["premutGmail"]):
                    self.body[self.options["emailField"]] = self.options["permutations"][i]
                self.runRequest()

#
# OPTIONS
#
    options={
        "output":False,
        "premutGmail":-False,
        "emailField":"email",
        "permutations":[]
    }

    def PremutGmail(self,emailField):
        manipulate.changeKeyValuePair(self.options,"permutGmail",1)
        manipulate.changeKeyValuePair(self.options,"emailField",emailField)
        manipulate.changeKeyValuePair(
            self.options,
            "permutations",
            gen.permuations((self.body[self.options["emailField"]]))
        )

    def PrintOutPut(self,val):
        manipulate.changeKeyValuePair(self.options,"output",val)
    
    def ChangeBodyValue(self,key,value):
        manipulate.changeKeyValuePair(self.body,key,value)

    def AddBodyValue(self,key,value):
        manipulate.addKeyValuePair(self.body,key,value)