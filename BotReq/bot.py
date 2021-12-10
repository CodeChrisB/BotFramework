import re
import requests
import concurrent.futures as cf
from time import sleep
import string, random

import BotReq.util.generate as gen
import BotReq.util.jsonManipulate as manipulate
import BotReq.session as sessionObj
from requests.api import options

#
#VARIABLES
#

class BotReq:

    #
    #METHODS
    #
    def __init__(self, body,url):
        self.body = body
        self.url = url
        self.session = None

    #region Getter & Setter
    def setBody(self,newBody):
        self.body = newBody

    def getBody(self): 
        return self.body

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        return self.url

    def getSession(self):
        return self.session
    #endregion

    #region Session
    def createSession(self,url):
        self.session = sessionObj.Session(url)
    
    def Session(self):
        return self.session


    #endregion
    def runRequest(self):
        r = requests.post(self.url,data=self.body)
        if(self.options["output"]):
            print(r.text)
    
    def runNTimes(self,n):
        with cf.ThreadPoolExecutor() as executor:
            for i in range(n): 
                if(self.options["permutGmail"]):
                    self.body[self.options["emailField"]] = self.options["permutations"][i]
                self.runRequest()
    
    def runPermutationTimes(self):
        if(self.options["permutations"]==[]):
            raise ValueError("Either the method PermutGmail(string) was not called or there does not exist any permutations for the given value")
        self.runNTimes(len(self.options["permutations"].l))

#
# OPTIONS
#
    options={
        "output":False,
        "permutGmail":-False,
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
